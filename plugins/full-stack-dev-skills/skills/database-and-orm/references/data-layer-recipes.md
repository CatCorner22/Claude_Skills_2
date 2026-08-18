# Data-layer recipes (reference)

## Contents
- Engine + session setup (with the SQLite pragmas)
- Transaction boundary: where `commit()` goes
- Money that survives both engines
- Connection pooling
- Migration workflow
- N+1 diagnosis
- SQLite → Postgres checklist
- Three probes (run these once per project)

Every snippet here was exercised against SQLAlchemy 2.0 + FastAPI (0.141) before being written
down. The numbers in "Connection pooling" are the library defaults at that version — re-read
them from your own install (`print(engine.pool.status())`) rather than trusting this page.

## Engine + session setup (with the SQLite pragmas)
```python
# db.py — the one place engines and sessions exist
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

IS_SQLITE = settings.db_url.startswith("sqlite")

engine = create_engine(
    settings.db_url,
    connect_args={"check_same_thread": False} if IS_SQLITE else {},
    pool_pre_ping=not IS_SQLITE,          # see "Connection pooling"
)

if IS_SQLITE:
    @event.listens_for(engine, "connect")
    def _sqlite_on_connect(dbapi_conn, connection_record):
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")    # per CONNECTION — not a property of the file
        cur.execute("PRAGMA journal_mode=WAL")   # readers don't block the writer
        cur.execute("PRAGMA busy_timeout=5000")  # wait 5s instead of "database is locked"
        cur.close()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
```
Why the listener rather than one `PRAGMA` at startup: `foreign_keys` is per-connection state, and
a pooled engine opens connections lazily, on new threads, and again after `dispose()` or a
`pool_recycle`. Anything short of the `connect` event leaves some connections unguarded, and the
unguarded ones fail silently — they accept orphan rows. `journal_mode` *is* persistent in the
file, so re-issuing it is a cheap no-op (and harmless on `:memory:`, where it stays `memory`).

`check_same_thread`: on SQLAlchemy 2.0 the pysqlite dialect already defaults it to `False` for
**file** databases (they use `QueuePool`), so passing it is belt-and-braces there. It is load
bearing for **in-memory** databases, which default to `check_same_thread=True` on a
`SingletonThreadPool` — one connection *per thread*, so a second thread silently gets a
different, empty database (`no such table: invoices`). An in-memory DB shared across threads
needs both:
```python
create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
```

## Transaction boundary: where `commit()` goes
```python
def get_db():
    """Session LIFECYCLE only. No commit here — see SKILL.md step 5."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()        # close() rolls back anything still uncommitted
```
```python
# routers/invoices.py — the use case owns the transaction
@router.post("/invoices", status_code=201, response_model=InvoiceOut)
def post_invoice(payload: InvoiceIn, db: Session = Depends(get_db)):
    try:
        invoice = services.create_invoice(db, payload)   # add() + flush(), never commit()
        db.commit()                                      # inside the request
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="violates a database constraint")
    return invoice
```
**Why not `db.commit()` after the `yield`.** A FastAPI yield-dependency's post-`yield` block runs
in the *request-scoped* exit stack, which closes after the response has been sent. Verified on
FastAPI 0.141 with a dependency that raises exactly where the commit would be: the client got
`201` and the success body; the exception surfaced afterwards, as a server-side error the client
never sees. A deferred-constraint violation, serialization failure, deadlock, or dropped
connection there therefore rolls back a request you already reported as successful — and no
`except IntegrityError` in your code can reach it, so `409`/retry handling is impossible.
Newer FastAPI exposes a per-dependency scope for teardown-before-response; treat that as a
second belt, not the boundary. The version-dependence is the point: keep the commit somewhere
your own code controls.

`with db.begin():` inside the handler is the other correct form, with one sharp edge — it raises
`InvalidRequestError: A transaction is already begun on this Session.` if anything already used
the session, which an auth or tenant-lookup dependency sharing `get_db` usually has
(`Session.autobegin` is `True` by default). Verified both ways: fresh session → fine; after one
`SELECT` → raises. An explicit `db.commit()` at the end of the use case has no such
precondition, which is why it is the default recommendation here.

Retries (serialization failures, deadlocks) wrap the **whole** use case — re-run the service
call from the top after a `rollback()`, never retry a half-applied transaction.

## Money that survives both engines
```python
from decimal import Decimal, ROUND_HALF_UP

amount_cents: Mapped[int] = mapped_column(BigInteger)       # default while SQLite is in the path
balance:      Mapped[Decimal] = mapped_column(Numeric(12, 2))   # Postgres-only path

def to_minor(d: Decimal, scale: int = 2) -> int:
    return int((d * (10 ** scale)).to_integral_value(rounding=ROUND_HALF_UP))

def from_minor(units: int, scale: int = 2) -> Decimal:
    return (Decimal(units) / (10 ** scale)).quantize(Decimal(1).scaleb(-scale))
```
Pick the scale once (2 for most currencies, 3 for fils, 4 if unit prices need mills) and put it
in the column name. `BigInteger`, not the bare `Mapped[int]`: 4-byte `INTEGER` caps a cents
column at $21,474,836.47. Integers are exact on both engines and exact under `SUM`; a `Decimal` column
on SQLite is not — pysqlite has no decimal type, so SQLAlchemy binds a double and rebuilds the
`Decimal` from it. Measured on SQLite through `Numeric(12, 2)`: `1.005 → 1.00`, `8.475 → 8.47`,
`99999999999999.99 → 99999999999999.98`. Current SQLAlchemy does this without a warning.
A bare `Mapped[Decimal]` also emits plain `NUMERIC` on Postgres — unconstrained precision and
scale — so write `Numeric(p, s)` explicitly even on the Postgres-only path.

## Connection pooling
This and the two engine differences above are what actually break on switch day.
```python
create_engine(
    settings.db_url,
    pool_size=5,          # persistent connections per PROCESS
    max_overflow=5,       # extra, transient, closed when returned
    pool_timeout=30,      # seconds a request waits for a connection before erroring
    pool_pre_ping=True,   # one cheap round trip per checkout; kills stale-connection 500s
    pool_recycle=1800,    # recycle below any proxy/server idle timeout
)
```
Defaults to know: `QueuePool` with `pool_size=5`, `max_overflow=10` (so **15 connections per
process**), `pool_timeout=30`, `pool_pre_ping=False`, `pool_recycle=-1` (never). SQLAlchemy 2.0
uses `QueuePool` for SQLite **file** databases too.

Size it against the server, not the app:
```
ceiling = (pool_size + max_overflow) x processes        # gunicorn/uvicorn workers, plus
                                                       # every other service on that DB
 4 workers x 15 = 60    fits a default Postgres max_connections = 100
 8 workers x 15 = 120   exceeds it -> "FATAL: sorry, too many clients already"
 8 workers x (5+5) = 80 fits, leaving room for migrations, psql and monitoring
```
Symptom map:
- `FATAL: sorry, too many clients already` / `too many connections` → the ceiling above.
- `QueuePool limit of size N overflow M reached, connection timed out` → app-side starvation:
  a leaked session, a long transaction, or too small a pool for the concurrency.
- `server closed the connection unexpectedly` / `SSL connection has been closed` on the first
  query after an idle period → stale pooled connection. `pool_pre_ping=True` plus a
  `pool_recycle` under the server's or proxy's idle timeout.

Use `NullPool` (no app-side pooling) when:
- an **external pooler** owns it — PgBouncer/pgpool in transaction mode. Don't stack two pools.
  (With asyncpg behind transaction-mode pooling, prepared-statement caching must also be off.)
- **serverless / short-lived processes**, where a pool is created and thrown away per invocation.
- Forking: never let a child process inherit live connections. `NullPool`, or call
  `engine.dispose(close=False)` in the post-fork hook so the child opens its own.

## Migration workflow
1. Change models → `alembic revision --autogenerate -m "add invoices.due_date"`
2. **Read the generated migration.** Autogenerate cannot see renames (drop+add = data loss);
   fix by hand with `op.alter_column`.
3. One migration per PR; merged migrations are immutable — fix forward with a new one.
4. Deploy-safe pattern for tightening: add nullable → backfill (data migration or script) →
   add NOT NULL in a later migration once code writes it always.
5. `alembic upgrade head` runs in CI against a scratch DB — a migration that can't apply
   cleanly fails the build, not the deploy.
6. SQLite caveat: it cannot `ALTER` a column's type or constraints, so Alembic emulates those
   changes by rebuilding the table (`with op.batch_alter_table(...)`). A rebuild is where an
   unenforced FK finally matters, and a batch migration written for SQLite may not be what you
   want on Postgres — run migrations in CI against the engine you deploy.

## N+1 diagnosis
Symptom: page slow, DB fine; log shows the same query with different IDs, dozens of times.
```python
# dev: see the SQL
engine = create_engine(url, echo=True)          # or log slow queries in prod middleware
# fix: declare the access pattern
select(Invoice).options(selectinload(Invoice.lines), joinedload(Invoice.customer))
# or: stop loading graphs for read views
select(Invoice.id, Invoice.amount_cents, Customer.name).join(Customer)
```
Rule of thumb: `selectinload` for one-to-many (second query with IN), `joinedload` for
many-to-one (single JOIN); raw column selects for list screens.

## SQLite → Postgres checklist
- [ ] All schema changes already via Alembic (no drifted dev DB)
- [ ] `PRAGMA foreign_keys=ON` was on in dev — otherwise assume orphan rows exist and go find
      them *before* the load: one `LEFT JOIN ... WHERE parent.id IS NULL` per FK
- [ ] Money columns are integer minor units, or `Numeric(p, s)` with precision and scale written
      out; a bare `Mapped[Decimal]` gets a `NUMERIC` with neither
- [ ] Pool sized: `(pool_size + max_overflow) x workers` under `max_connections`, with headroom
- [ ] `pool_pre_ping=True` and a `pool_recycle` below the server/proxy idle timeout
- [ ] `NullPool` if PgBouncer, pgpool, or serverless is in the path
- [ ] No engine-specific SQL in feature code (search for `sqlite_`, string-concat SQL)
- [ ] Types portable: DateTime(timezone=True), JSON via ORM types
- [ ] `db_url` is config; the test suite runs against Postgres in CI **before** the switch
- [ ] Data move: dump/load script or `pgloader`; verify row counts + spot checksums
- [ ] Concurrency assumptions revisited: Postgres gives real concurrent writers, but also
      real lock behavior — retest the hot write paths
- [ ] Case sensitivity and collation checked: SQLite's `LIKE` is ASCII-case-insensitive by
      default, Postgres's is not; any uniqueness that relied on that changes meaning
- [ ] Backups configured on day one of Postgres (the ops cost you deferred, now due)

## Three probes (run these once per project)
Keep them as tests. Each takes minutes and each answers a question the schema cannot.
```python
def test_fk_is_actually_enforced(db):
    db.add(Invoice(customer_id=10 ** 9, amount_cents=1))   # a customer id that cannot exist
    with pytest.raises(IntegrityError):
        db.flush()          # passes only if the engine enforces the FK

def test_money_roundtrip_is_exact(db):
    row = Ledger(balance=Decimal("1.005"))      # or amount_cents=1005
    db.add(row); db.flush(); db.expire_all()
    assert db.get(Ledger, row.id).balance == Decimal("1.005")

# probe 3: on YOUR framework version, can a failure where get_db would commit fail the request?
def _dep():
    yield "session"
    raise RuntimeError("pretend the commit failed")

app.post("/probe", status_code=201)(lambda s=Depends(_dep): {"ok": True})
status = TestClient(app, raise_server_exceptions=False).post("/probe").status_code
# 201 -> the teardown runs AFTER the response: a failed commit there cannot fail the request.
#        (This is what FastAPI 0.141 does by default.)
# 500 -> the teardown runs before the response on your version.
```
Either answer leaves the commit belonging in the handler — `201` because the teardown can't
report failure, `500` because it can only report a generic one. Re-run probe 3 after a framework
upgrade: this answer has changed across FastAPI versions, and silently.
