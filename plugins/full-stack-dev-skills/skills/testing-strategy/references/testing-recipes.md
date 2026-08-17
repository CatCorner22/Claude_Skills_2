# Testing recipes (reference)

## Contents
- conftest spine
- Prove the spine: the isolation canary
- What each line of the spine is holding up
- Choosing the test engine
- Factory helpers
- Level-decision table
- Playwright skeleton
- External-boundary mocks
- Async apps: what changes

The spine below was run against SQLAlchemy 2.0 + FastAPI (0.141) — eleven tests covering a
committing endpoint, FK/UNIQUE/CHECK violations mapped to `409`, and cross-test isolation. All
eleven pass as written; re-run with the two SQLite settings removed, seven fail. The failure
notes in this file are those observed failures, not cautions in principle.

## conftest spine
```python
# conftest.py
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from app.db import Base, get_db
from app.main import app

TEST_DB_URL = os.environ.get("TEST_DATABASE_URL", "sqlite:///./test.db")


def _make_sqlite_behave(eng):
    """Two pysqlite defaults break things this suite depends on."""
    @event.listens_for(eng, "connect")
    def _on_connect(dbapi_conn, _record):
        dbapi_conn.isolation_level = None          # (2) we will drive BEGIN ourselves
        cur = dbapi_conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")      # (1) or FK constraints are ignored
        cur.close()

    @event.listens_for(eng, "begin")
    def _on_begin(conn):
        conn.exec_driver_sql("BEGIN")              # (2) makes SAVEPOINTs reliable


@pytest.fixture(scope="session")
def engine():
    is_sqlite = TEST_DB_URL.startswith("sqlite")
    eng = create_engine(TEST_DB_URL,
                        connect_args={"check_same_thread": False} if is_sqlite else {})
    if is_sqlite:
        _make_sqlite_behave(eng)
    Base.metadata.create_all(eng)
    yield eng
    Base.metadata.drop_all(eng)
    eng.dispose()


@pytest.fixture
def db(engine):
    conn = engine.connect()
    tx = conn.begin()                                       # outer transaction
    session = Session(bind=conn, join_transaction_mode="create_savepoint")
    try:
        yield session
    finally:
        session.close()
        tx.rollback()          # undoes everything — including the app's own commits
        conn.close()


@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = lambda: db           # app shares the test session
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()
```

## Prove the spine: the isolation canary
Two tests, permanently in the suite. They cost nothing and they fail the moment the fixture
stops isolating — which is otherwise invisible, because broken isolation shows up as green.
```python
def test_canary_1_endpoint_commits(client):
    assert client.post("/invoices", json={...}).status_code == 201

def test_canary_2_next_test_sees_clean_db(db):
    assert db.scalar(select(func.count()).select_from(Invoice)) == 0
    assert db.scalar(select(func.count()).select_from(Customer)) == 0
```
Add the engine's own canary next to it — one deliberate constraint violation, so a test engine
that silently drops constraints cannot pass:
```python
def test_canary_3_fk_is_enforced(db):
    db.add(Invoice(customer_id=10 ** 9, number="ORPHAN", amount_cents=1))
    with pytest.raises(IntegrityError):
        db.flush()
```

## What each line of the spine is holding up
- **`join_transaction_mode="create_savepoint"`** — the session's `commit()` releases a SAVEPOINT
  and immediately opens a new one, so the endpoint under test can commit for real while the
  fixture's outer `tx.rollback()` still undoes everything. It also keeps the app's
  `session.rollback()` meaning what it means in production (revert to the last savepoint).
  Without the argument you get SQLAlchemy 2.0's default, `conditional_savepoint`, which on a
  plain outer transaction degrades to `rollback_only`: isolation still holds (this is not the
  1.x leak), but the app's `commit()` is quietly demoted to a flush and the app's `rollback()`
  discards the *whole* outer transaction — after which the rest of that test sees an empty
  database and the fixture's own rollback warns `transaction already deassociated from
  connection`. Either mode isolates; only `create_savepoint` behaves like production.
- **The `BEGIN` workaround (SQLite only)** — pysqlite manages `BEGIN` itself and does not open a
  transaction before a `SAVEPOINT`, so `create_savepoint` on default pysqlite **leaks**: rows
  committed by the endpoint survive `tx.rollback()`, and you get exactly the order-dependent
  flake the fixture exists to prevent (observed: 1 row leaking into the next test, 3 by the
  test after). Setting `isolation_level = None` and emitting `BEGIN` on the engine's `begin`
  event fixes it. On Postgres, savepoints work natively and this block is unnecessary.
- **`PRAGMA foreign_keys=ON`** — per *connection*, not per database. Without it SQLite writes the
  FK into the DDL and ignores it, so a constraint test passes without testing anything (observed:
  a POST with `customer_id=4242` returning `201`).
- **`connect_args={"check_same_thread": False}`** — `TestClient` runs the app off the calling
  thread. On SQLAlchemy 2.0 the pysqlite dialect already defaults this to `False` for **file**
  databases, so it is belt-and-braces there; it is required for **in-memory** databases, which
  default to `check_same_thread=True` on a `SingletonThreadPool` — one connection per thread, so
  another thread silently gets a *different, empty* database. In-memory also needs
  `poolclass=StaticPool` for the same reason.
- **`try/finally` in both fixtures** — a failing assert must not leave a dangling connection or a
  permanent `dependency_overrides` entry that poisons every later test.
- **`client` depending on `db`** — the override is what makes the app use the test's session. Code
  that opens its own session (`SessionLocal()` inside a service, a background task) escapes the
  fixture entirely: its writes are committed for real and outlive the test, or on SQLite may
  block against the fixture's write lock. Session-per-request in, session created ad hoc out.

## Choosing the test engine
One flag, two answers, chosen per behavior:
```bash
pytest                                             # fast: SQLite file, own-logic tests
TEST_DATABASE_URL=postgresql+psycopg://…/test pytest   # truthful: the engine you deploy
```
- **SQLite is fine** for endpoint contracts, business rules in your own code, serialization
  shapes, auth wiring — anything where your code, not the database, decides the answer.
- **The production engine is required** for FK/UNIQUE/CHECK/deferred-constraint behavior,
  migrations (`alembic upgrade head` on a scratch DB), anything touching `NUMERIC`
  precision/scale, `VARCHAR` length, `LIKE`/collation case sensitivity, Postgres-only types and
  operators (arrays, `jsonb`, `ILIKE`), upsert clauses, or any concurrency scenario. Row locking
  is the sharpest of these: `select(...).with_for_update()` compiles to a plain `SELECT` on
  SQLite — the clause is silently dropped — so a test of your pessimistic-locking path passes
  while locking nothing.
- **Get it in CI either way.** A Postgres service container in the CI job, or testcontainers so
  the same fixture spins one up locally. The full suite against the production engine at least
  once per pipeline is what stops "passes on SQLite" from becoming a deploy story.

## Factory helpers
```python
def make_customer(db, **kw) -> Customer:
    c = Customer(name=kw.get("name", "Acme"), email=kw.get("email", "a@x.co"))
    db.add(c)
    db.commit()          # commit setup rows, don't just flush() them
    return c
```
Plain functions with keyword overrides beat factory frameworks until relationships get deep.
Why `commit()` and not `flush()`: if the endpoint under test hits an error and calls
`session.rollback()`, everything un-committed in that session goes with it — including the rows
this helper created, so the test then fails on its own setup. Committed setup rows survive the
app's rollback, and the fixture's outer `tx.rollback()` still removes them at the end. (Observed
both ways: with `flush()`, a test asserting one customer after a rolled-back request saw zero.)

## Level-decision table
| Behavior | Level | Why |
|---|---|---|
| Endpoint contract (status, shape, auth, validation) | API test | The contract is the value |
| Business rule reachable via API | API test | Covers rule + wiring at once |
| Tricky pure logic (math, parsing, dates) | Unit (no mocks) | Fast, precise failure location |
| Cross-page user flow (login → create → verify) | Playwright E2E | Only level that sees the whole |
| Third-party API interaction | API test + respx mock | Determinism at the real boundary |
| DB constraint behavior (FK, UNIQUE, CHECK, deferred) | API or db-fixture test **on the production engine** | Default SQLite ignores FKs and scale, so a SQLite pass proves nothing |
| Migration applies and is reversible | CI job on a scratch DB of the **production engine** | Migrations are dialect-specific; SQLite rebuilds tables where Postgres alters them |
| Framework internals, trivial pass-throughs, styling | Don't test | No rentable regression risk |

## Playwright skeleton
```ts
test("create invoice money path", async ({ page }) => {
  await page.goto("/login");
  await page.getByLabel("Email").fill(user.email);
  await page.getByLabel("Password").fill(user.password);
  await page.getByRole("button", { name: "Log in" }).click();
  await page.getByRole("link", { name: "Invoices" }).click();
  await page.getByRole("button", { name: "New invoice" }).click();
  await page.getByLabel("Amount").fill("99.50");
  await page.getByRole("button", { name: "Save" }).click();
  await expect(page.getByText("Invoice created")).toBeVisible();
});
```
Rules: role/label selectors (not CSS classes), seeded test user per run, retry-on-CI once
(flaky twice = fix or delete), cap the whole E2E stage at a few minutes.

## External-boundary mocks
```python
@pytest.fixture
def bank_api(respx_mock):
    respx_mock.get("https://bank.example/balances").respond(json={"available": "1000.00"})
    return respx_mock

def test_position_uses_bank_balance(client, bank_api):
    assert client.get("/cash/position").json()["available"] == "1000.00"
```
Clock: inject `now()` as a dependency/parameter; freeze in tests. Randomness: seed or
inject. Email/SMS: capture via a fake sender fixture, assert on the captured payload.

## Async apps: what changes
An `AsyncSession`/asyncpg app keeps every decision in `SKILL.md` and replaces the plumbing.
`TestClient` runs the app on its own event loop in a worker thread, so it cannot share an
`AsyncSession` or an async transaction fixture with the test that created it. Instead:
- client: `httpx.AsyncClient(transport=ASGITransport(app=app), base_url="http://test")`, with
  `pytest-asyncio` (or anyio mode) and async fixtures.
- fixtures: `create_async_engine`, `await conn.begin()`, `AsyncSession(bind=conn,
  join_transaction_mode="create_savepoint")`, `await tx.rollback()`; schema creation goes through
  `await conn.run_sync(Base.metadata.create_all)`.
- the same two canaries still apply, and matter more: async fixtures have more ways to be
  silently mis-scoped. Port the canary first, then the tests.
