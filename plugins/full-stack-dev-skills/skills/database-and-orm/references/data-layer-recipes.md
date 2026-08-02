# Data-layer recipes (reference)

## Contents
- Session/transaction setup
- Migration workflow
- N+1 diagnosis
- SQLite → Postgres checklist

## Session/transaction setup
```python
# db.py — the one place engines and sessions exist
engine = create_engine(settings.db_url,
                       connect_args={"check_same_thread": False} if "sqlite" in settings.db_url else {})
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def get_db():                      # FastAPI dependency = transaction boundary
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
```
SQLite in production-ish use: enable WAL once (`PRAGMA journal_mode=WAL`) for readers-don't-
block-writers. Service functions receive the session; none of them commit.

## Migration workflow
1. Change models → `alembic revision --autogenerate -m "add invoices.due_date"`
2. **Read the generated migration.** Autogenerate cannot see renames (drop+add = data loss);
   fix by hand with `op.alter_column`.
3. One migration per PR; merged migrations are immutable — fix forward with a new one.
4. Deploy-safe pattern for tightening: add nullable → backfill (data migration or script) →
   add NOT NULL in a later migration once code writes it always.
5. `alembic upgrade head` runs in CI against a scratch DB — a migration that can't apply
   cleanly fails the build, not the deploy.

## N+1 diagnosis
Symptom: page slow, DB fine; log shows the same query with different IDs, dozens of times.
```python
# dev: see the SQL
engine = create_engine(url, echo=True)          # or log slow queries in prod middleware
# fix: declare the access pattern
select(Invoice).options(selectinload(Invoice.lines), joinedload(Invoice.customer))
# or: stop loading graphs for read views
select(Invoice.id, Invoice.amount, Customer.name).join(Customer)
```
Rule of thumb: `selectinload` for one-to-many (second query with IN), `joinedload` for
many-to-one (single JOIN); raw column selects for list screens.

## SQLite → Postgres checklist
- [ ] All schema changes already via Alembic (no drifted dev DB)
- [ ] No engine-specific SQL in feature code (search for `sqlite_`, string-concat SQL)
- [ ] Types portable: Decimal, DateTime(timezone=True), JSON via ORM types
- [ ] `db_url` is config; test suite runs against Postgres in CI before the switch
- [ ] Data move: dump/load script or `pgloader`; verify row counts + spot checksums
- [ ] Concurrency assumptions revisited: Postgres gives real concurrent writers, but also
      real lock behavior — retest the hot write paths
- [ ] Backups configured on day one of Postgres (the ops cost you deferred, now due)
