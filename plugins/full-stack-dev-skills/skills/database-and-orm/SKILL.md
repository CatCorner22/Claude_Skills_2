---
name: database-and-orm
description: >-
  Designs and operates the application data layer the lean way — schema design with real
  constraints, SQLAlchemy/SQLModel models, Alembic migrations as the only schema-change path,
  query patterns that avoid N+1 and load only what's needed, transactions committed inside the
  request, connection pooling sized for the server, and the SQLite-first-Postgres-ready growth
  path with its silent engine differences named. Use when designing tables, writing or
  reviewing ORM queries, setting up or fixing migrations, debugging slow or N+1-ridden
  endpoints, or moving dev SQLite to production Postgres. Triggers: database schema,
  SQLAlchemy, SQLModel, alembic migration, N+1 query, ORM slow, design tables, foreign key,
  sqlite foreign keys, sqlite to postgres, transaction handling, connection pool, pool_size,
  too many connections, pgbouncer, database indexes app.
metadata:
  version: "1.2.1"
---

# Database and ORM for applications

## When to use
- Designing or changing an app's schema; writing/reviewing ORM models and queries;
  managing migrations; fixing slow data access.
- Sizing the connection pool, or moving a dev SQLite app onto production Postgres.
- Not for: analytical SQL over exports/warehouses → see
  `data-analytics-bi-skills:sql-for-analysts` and `data-tools-skills:duckdb-local-analytics`.
  Enterprise COA/ledger design → the accounting plugins.

## Do it
1. **Put the rules in the schema, not in prose.** `NOT NULL` by default, foreign keys always,
   `UNIQUE` where business says unique, `CHECK` for simple invariants (`amount_cents > 0`). The
   database enforcing a rule beats every code path remembering to — application validation
   (Pydantic) is the friendly error; the constraint is the guarantee.
   **Where "foreign keys always" is false: SQLite.** SQLite parses `FOREIGN KEY`, writes it into
   the DDL, and then ignores it unless `PRAGMA foreign_keys=ON` is issued **on every
   connection** — it is per-connection state, not a property of the file. So orphan rows insert
   clean, the schema looks correct, and the bill arrives when the Postgres load rejects them.
   Wire the `connect`-event pragma from `references/data-layer-recipes.md` and prove it with one
   deliberate orphan insert; without that proof, an FK on SQLite is a comment.
2. **Model tables 1:1 and resist cleverness:**

```python
class Invoice(Base):
    __tablename__ = "invoices"
    __table_args__ = (CheckConstraint("amount_cents > 0", name="ck_invoice_amount_positive"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    amount_cents: Mapped[int] = mapped_column(BigInteger)   # money: exact on every engine
    status: Mapped[str] = mapped_column(default="draft")    # plain str + CHECK beats enum churn
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                server_default=func.now())
    customer: Mapped["Customer"] = relationship()
```

   Integer (or UUID, pick once) PKs, UTC timestamps, soft-delete only when the domain truly
   needs undelete (it usually doesn't). **Money is where the SQLite-first path (step 7) and
   "never float" collide.** SQLite has no decimal type, so SQLAlchemy's pysqlite driver binds a
   `Decimal` as a C double and rebuilds a `Decimal` from that float on the way out — no warning
   on current SQLAlchemy. Verified SQLite round-trips through a `Numeric(12, 2)` column:
   `1.005 → 1.00`, `8.475 → 8.47`, `99999999999999.99 → 99999999999999.98`. And a bare
   `Mapped[Decimal]` compiles to an *unconstrained* `NUMERIC`, so Postgres gets no precision or
   scale either. Resolve it once, by what survives both engines:
   - **Integer minor units** (`amount_cents`, or mills if you need 4 places — fix the scale
     once and name it in the column) — exact on SQLite and Postgres, exact under `SUM`, and the
     only option that needs no per-engine caveat. Default to this while SQLite is in the path.
     Use `BigInteger`: a bare `Mapped[int]` is a 4-byte `INTEGER` on Postgres, which caps a cents
     column at $21,474,836.47 — an amount some invoice will eventually exceed.
   - **`Numeric(12, 2)`** — correct once Postgres is the only engine (psycopg and asyncpg return
     real `Decimal`s, no float in the path) and worth writing explicitly even then, because it
     pins the scale the bare annotation leaves open. Under SQLite it is still the float path,
     and the two engines need not round `1.005` the same way — which is how dev and prod come to
     disagree by a cent.
   - **Never `float`.** That failure is louder but the same shape.
3. **Alembic is the only way schemas change** — including in dev. `alembic revision
   --autogenerate` then *read the diff* (autogenerate misses renames — it sees drop+add),
   one migration per PR, never edit a merged migration, and keep migrations
   data-compatible with the code deployed either side of them (add column nullable →
   backfill → tighten).
4. **Kill N+1 at the query, not the loop.** The pattern — one query for parents, one query
   *per* parent for children — is invisible in dev (10 rows) and fatal in prod (10k rows):

```python
stmt = (select(Invoice)
        .options(selectinload(Invoice.lines),      # collection -> second query with IN
                 joinedload(Invoice.customer))     # to-one     -> one JOIN
        .where(Invoice.status == "open"))
```

   `selectinload` for collections, `joinedload` for to-one; and when a screen needs three
   columns from three tables, a plain `select(cols).join(...)` beats loading object graphs.
   Turn on SQL echo in dev occasionally — the query log is the truth.
5. **Draw the transaction inside the request, not in the dependency's teardown.** One
   request/use-case = one session = one transaction — but the `commit()` belongs in the request
   handler or the service call it makes, and `get_db` owns *lifecycle only*: `yield` the
   session, `close()` it in `finally` (close rolls back anything uncommitted). Committing after
   the `yield` is the trap. A FastAPI yield-dependency's post-`yield` block runs in the
   **request-scoped** exit stack, which current FastAPI closes *after the response has been
   sent* (verified on FastAPI 0.141: raising where the commit would be still returned `201` to
   the client, with the exception surfacing afterwards as a server error nobody's client sees).
   So a deferred-constraint violation, serialization failure, deadlock, or dropped connection
   rolls the write back *after* you promised success — and there is nowhere to catch
   `IntegrityError` and answer `409`. Which side of the response that block runs on has changed
   across FastAPI versions, and newer versions let a dependency opt into function scope; that
   version-dependence is itself the argument for not putting a business-critical step there.
   Service code still never commits mid-flow — it `flush()`es; the use case commits once.
6. **Index what you filter and join on** — FKs, columns in frequent `WHERE`/`ORDER BY` — and
   nothing else until a slow query says so (each index taxes every write). `EXPLAIN` the one
   slow query rather than guessing at ten.
7. **Ride SQLite until it objects — knowing what it silently won't do.** SQLite in WAL mode
   serves dev and single-node production shockingly far: zero ops, one file. It is not a small
   Postgres, and four differences are silent rather than loud — FKs off per connection (step 1),
   no decimal type (step 2), one writer at a time, and savepoints that misbehave under the
   pysqlite driver until you take over `BEGIN` (this one breaks test isolation, not production —
   see `full-stack-dev-skills:testing-strategy`). Move to Postgres when you need concurrent
   writers at scale, a hosted/replicated DB, or Postgres-only features. Keep the code portable:
   types via the ORM, no engine-specific SQL in features, config-only switch. **Two things
   actually break on switch day, and pooling is the one nobody wrote down:** SQLAlchemy's
   default `QueuePool` is `pool_size=5` + `max_overflow=10`, i.e. up to 15 connections *per
   process*, multiplied by your worker count, against a server whose `max_connections` is
   commonly 100; `pool_pre_ping` is off and `pool_recycle` is unset, so idle connections killed
   by the server or a proxy come back as `server closed the connection unexpectedly` on a real
   request. `references/data-layer-recipes.md` has the arithmetic, the settings, and when
   `NullPool` is the right answer instead.
8. **Prove the silent three on your own engine before relying on them.** Ten lines each, once
   per project, ideally as tests: insert a deliberate orphan (is the FK enforced?); round-trip
   `1.005` through the money column (what comes back?); raise where your `get_db` would commit
   (does the client still see `201`?). All three are in the recipes file. Every one of them has
   shipped as a production surprise in an app whose schema and code looked right.

**Deliverable:** models with constraints, an Alembic revision per change, named access patterns
for the hot queries, one commit per use case inside the request, a pool sized against the
server's limit, and the three probes above answered for the engine you actually deploy.

## Why / learn
The database is the only layer whose mistakes are *permanent* — bad code ships and gets
patched, bad data ships and gets archaeologically excavated — which is why constraints go in
the schema: a `NOT NULL` is a rule that holds even when a bug, a manual fix, or next year's
second app writes the table. But a constraint is only a guarantee on an engine that enforces it,
and "the DDL contains it" is not that guarantee: SQLite's foreign keys are the standing example
of a rule that reads as enforced and isn't. The general form is worth more than the specific
gotcha — **a data-layer promise you have not watched fail is a promise you have not tested**,
and the cheapest version of every check in step 8 is one deliberate violation.
The migration discipline is version control extended to state:
code can roll back by deploying the old build, but the schema can't "roll back" data it
already dropped, so migrations are one-way doors and get the read-the-diff respect one-way
doors deserve. N+1 is the classic ORM trap because the ORM's core convenience — objects with
traversable relationships — quietly converts a join into a loop of queries; the fix isn't
abandoning the ORM but telling it your access pattern (`selectinload`) so it can be the SQL
it was hiding. Transactions-at-the-use-case is the atomicity version of thin routes: a
use case either happened or didn't, and mid-function commits create the third state nobody
designs for — with the corollary that the commit has to sit somewhere your error handling can
still reach, which a framework teardown running after the response is not. And SQLite-first is
lean-code economics applied to infrastructure: the fewest moving parts that serve today's
requirement, with the Postgres door deliberately kept open — paying the ops cost when the
requirement arrives, not when the architecture diagram imagines it. Pooling is the tax on
walking through that door: the file that never had a connection limit is replaced by a server
that does.

## Common mistakes
- Rules only in application code → the DB outlives the code paths; constraints in the schema.
- `FOREIGN KEY` in the DDL read as enforcement on SQLite → orphans insert silently; pragma on every connection, plus one orphan-insert test.
- Float for money → rounding drift; integer minor units, or `Numeric(p, s)` once Postgres is the only engine.
- `Mapped[Decimal]` on a SQLite-backed app → values round-trip through a C double, no warning; and Postgres inherits an unconstrained `NUMERIC`.
- Schema changed by hand in dev → dev and prod diverge; Alembic everywhere.
- Trusting autogenerate blind → renames become drop+add (data loss); read every migration.
- N+1 discovered in production → `selectinload`/`joinedload`; peek at the SQL log in dev.
- Loading full object graphs to render three columns → select the columns; ORM ≠ obligation.
- `commit()` after the `yield` in `get_db` → the response may already be sent, so a failed commit returns success; commit in the handler/service.
- Commits sprinkled mid-service → partial states; services `flush()`, the use case commits once.
- Indexing everything preemptively → write tax with no read payoff; index from evidence.
- Switching to Postgres on default pool settings → `too many connections`, or stale-connection 500s; size the pool against `max_connections` and turn on `pool_pre_ping`.
- Premature Postgres (ops burden) or terminal SQLite (concurrency wall) → SQLite-first, portable code, config-switch when it objects.

## Tailor to your environment
Record your data-layer decisions in `references/your-environment.md`: engine per environment,
PK/timestamp/money conventions (minor-unit scale, or the `Numeric` precision), migration
workflow, pool settings against your server's `max_connections`, and the known hot queries with
their indexes — so new tables and queries match the house shape.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/database-and-orm.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/data-layer-recipes.md — engine/session setup with the SQLite pragmas, transaction boundary, migration workflow, N+1 diagnosis, pooling numbers, SQLite→Postgres checklist, the three probes
- references/your-environment.md — your engines, conventions, hot paths (fill in)
