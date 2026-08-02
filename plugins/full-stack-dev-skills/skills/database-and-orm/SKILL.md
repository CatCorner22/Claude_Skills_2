---
name: database-and-orm
description: >-
  Designs and operates the application data layer the lean way — schema design with real
  constraints, SQLAlchemy/SQLModel models, Alembic migrations as the only schema-change path,
  query patterns that avoid N+1 and load only what's needed, transactions at the service
  boundary, and the SQLite-first-Postgres-ready growth path. Use when designing tables,
  writing or reviewing ORM queries, setting up or fixing migrations, debugging slow or
  N+1-ridden endpoints, or moving dev SQLite to production Postgres. Triggers: database
  schema, SQLAlchemy, SQLModel, alembic migration, N+1 query, ORM slow, design tables,
  foreign key, sqlite to postgres, transaction handling, database indexes app.
---

# Database and ORM for applications

## When to use
- Designing or changing an app's schema; writing/reviewing ORM models and queries;
  managing migrations; fixing slow data access.
- Not for: analytical SQL over exports/warehouses → see
  `data-analytics-bi-skills:sql-for-analysts` and `data-tools-skills:duckdb-local-analytics`.
  Enterprise COA/ledger design → the accounting plugins.

## Do it
1. **Put the rules in the schema, not in prose.** `NOT NULL` by default, foreign keys always,
   `UNIQUE` where business says unique, `CHECK` for simple invariants (`amount > 0`). The
   database enforcing a rule beats every code path remembering to — application validation
   (Pydantic) is the friendly error; the constraint is the guarantee.
2. **Model tables 1:1 and resist cleverness:**

```python
class Invoice(Base):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    amount: Mapped[Decimal]
    status: Mapped[str] = mapped_column(default="draft")   # plain str + CHECK beats enum churn
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    customer: Mapped["Customer"] = relationship()
```

   Integer (or UUID, pick once) PKs, money as `Decimal`/integer-cents never float, UTC
   timestamps, soft-delete only when the domain truly needs undelete (it usually doesn't).
3. **Alembic is the only way schemas change** — including in dev. `alembic revision
   --autogenerate` then *read the diff* (autogenerate misses renames — it sees drop+add),
   one migration per PR, never edit a merged migration, and keep migrations
   data-compatible with the code deployed either side of them (add column nullable →
   backfill → tighten).
4. **Kill N+1 at the query, not the loop.** The pattern — one query for parents, one query
   *per* parent for children — is invisible in dev (10 rows) and fatal in prod (10k rows):

```python
stmt = select(Invoice).options(selectinload(Invoice.customer)).where(Invoice.status == "open")
```

   `selectinload` for collections, `joinedload` for to-one; and when a screen needs three
   columns from three tables, a plain `select(cols).join(...)` beats loading object graphs.
   Turn on SQL echo in dev occasionally — the query log is the truth.
5. **Draw the transaction at the service function.** One request/use-case = one session =
   one transaction: the `get_db` dependency opens/commits/rolls back; service code never
   commits mid-flow (partial writes are how "impossible" states happen). Retries wrap the
   whole transaction, never a half.
6. **Index what you filter and join on** — FKs, columns in frequent `WHERE`/`ORDER BY` — and
   nothing else until a slow query says so (each index taxes every write). `EXPLAIN` the one
   slow query rather than guessing at ten.
7. **Ride SQLite until it objects, then move.** SQLite (WAL mode) serves dev and single-node
   production shockingly far — zero ops, one file. Move to Postgres when you need concurrent
   writers at scale, a hosted/replicated DB, or Postgres-only features. Keep the code
   portable: types via the ORM, no engine-specific SQL in features, config-only switch —
   `references/data-layer-recipes.md` has the checklist plus migration and transaction
   recipes.

## Why / learn
The database is the only layer whose mistakes are *permanent* — bad code ships and gets
patched, bad data ships and gets archaeologically excavated — which is why constraints go in
the schema: a `NOT NULL` is a rule that holds even when a bug, a manual fix, or next year's
second app writes the table. The migration discipline is version control extended to state:
code can roll back by deploying the old build, but the schema can't "roll back" data it
already dropped, so migrations are one-way doors and get the read-the-diff respect one-way
doors deserve. N+1 is the classic ORM trap because the ORM's core convenience — objects with
traversable relationships — quietly converts a join into a loop of queries; the fix isn't
abandoning the ORM but telling it your access pattern (`selectinload`) so it can be the SQL
it was hiding. Transactions-at-the-service-edge is the atomicity version of thin routes: a
use case either happened or didn't, and mid-function commits create the third state nobody
designs for. And SQLite-first is lean-code economics applied to infrastructure: the fewest
moving parts that serve today's requirement, with the Postgres door deliberately kept open —
paying the ops cost when the requirement arrives, not when the architecture diagram imagines
it.

## Common mistakes
- Rules only in application code → the DB outlives the code paths; constraints in the schema.
- Float for money → rounding drift; `Decimal` or integer cents.
- Schema changed by hand in dev → dev and prod diverge; Alembic everywhere.
- Trusting autogenerate blind → renames become drop+add (data loss); read every migration.
- N+1 discovered in production → `selectinload`/`joinedload`; peek at the SQL log in dev.
- Loading full object graphs to render three columns → select the columns; ORM ≠ obligation.
- Commits sprinkled inside services → partial states; one transaction per use case at the edge.
- Indexing everything preemptively → write tax with no read payoff; index from evidence.
- Premature Postgres (ops burden) or terminal SQLite (concurrency wall) → SQLite-first, portable code, config-switch when it objects.

## Tailor to your environment
Record your data-layer decisions in `references/your-environment.md`: engine per environment,
PK/timestamp/money conventions, migration workflow, and the known hot queries with their
indexes — so new tables and queries match the house shape.

## References
- references/data-layer-recipes.md — migration workflow, transaction/session setup, N+1 diagnosis, SQLite→Postgres checklist
- references/your-environment.md — your engines, conventions, hot paths (fill in)
