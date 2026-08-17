---
name: testing-strategy
description: >-
  Designs minimal effective test suites for full-stack apps — testing behavior at the API
  boundary over mocking internals, a pytest fixture spine whose per-test isolation is proved
  rather than assumed, the production engine for anything constraint- or dialect-dependent, a
  handful of Playwright end-to-end tests for critical user flows only, regression tests for
  every fixed bug, and explicit judgment about what NOT to test — so the suite catches real
  breakage without taxing every refactor. Use when setting up testing for an app, deciding what
  to test at which level, reviewing a slow, brittle, or order-dependent suite, or adding tests
  around a bug. Triggers: testing strategy, what to test, pytest setup, test the API, mock or
  not, brittle tests, flaky test, test isolation, slow test suite, playwright e2e, test coverage
  target, regression test, test pyramid, integration vs unit, testcontainers.
metadata:
  version: "1.1.0"
---

# Testing strategy: minimal and effective

## When to use
- Standing up the test approach for an app, or rebalancing a suite that is slow, brittle, or
  quietly useless.
- Deciding the level (unit / API / end-to-end) for a specific behavior, or writing tests
  around a bug fix.
- Not for: review process and CI gates → `coding-agent-skills:git-and-code-review` and
  `full-stack-dev-skills:deploy-and-operate`. Model evaluation →
  `machine-learning-skills:model-evaluation`. Component-level frontend tests (the recipes here
  cover the API and the browser flow, not the component layer) → the component patterns in
  `full-stack-dev-skills:frontend-modern-ui`.
- Scope of the recipes: the sync `TestClient` shape. An app on `AsyncSession`/asyncpg keeps every
  principle below and changes the plumbing — `httpx.AsyncClient(transport=ASGITransport(app))`,
  an anyio/asyncio-mode pytest, async fixtures, and the async equivalents of the transaction
  fixture. Don't copy the sync spine into an async app and expect it to hold.

## Do it
1. **Aim the suite at one question: "does the app still do what users need?"** Rank test
   value = (probability the code breaks) × (cost when it does) ÷ (cost of the test). Most of
   that value concentrates in a mid-sized band of **API-boundary tests** — real HTTP against
   your FastAPI app with a real test database — because they exercise routing, validation,
   auth, logic, and SQL in one shot and survive refactors.

```python
def test_create_invoice(client, db):
    r = client.post("/invoices", json={"customer_id": 1, "amount": "99.50",
                                       "due_date": "2026-08-01"})
    assert r.status_code == 201
    assert db.scalar(select(func.count()).select_from(Invoice)) == 1

def test_rejects_negative_amount(client):
    r = client.post("/invoices", json={"customer_id": 1, "amount": "-5", "due_date": "2026-08-01"})
    assert r.status_code == 422
```

2. **Build the fixture spine once — then prove it.** In `conftest.py`: an app client
   (`TestClient`), a fresh-schema test DB per session, per-test transaction rollback for
   isolation, and small factory helpers for common rows. Real database, not mocked sessions —
   the SQL is exactly what you need tested. **The isolation fixture is the one fixture that
   fails silently.** Whether the outer transaction survives the endpoint's own `commit()` (and
   any POST commits) depends on your SQLAlchemy version, the `join_transaction_mode` you probably
   didn't pass, and whether your driver's savepoints actually work — and when it goes wrong the
   symptom is not an error. It is a suite that passes in order and fails when someone reorders,
   parallelises, or runs one test alone. So make the promise falsifiable with a two-test canary,
   which is cheaper than the afternoon it replaces:

```python
def test_canary_1_writes(client):
    assert client.post("/invoices", json={...}).status_code == 201

def test_canary_2_sees_a_clean_db(db):          # must be 0, not 1
    assert db.scalar(select(func.count()).select_from(Invoice)) == 0
```

   `references/testing-recipes.md` has a spine that holds when the endpoint commits, and the two
   SQLite-specific settings it needs to hold at all.
3. **Choose the test engine deliberately, per test.** SQLite is a fine stand-in for tests that
   only touch your own logic, and the wrong tool for anything the *database* decides. It ignores
   foreign keys unless `PRAGMA foreign_keys=ON` is set on every connection, has no decimal type,
   doesn't enforce `NUMERIC` scale or `VARCHAR` length, and differs on `LIKE` case sensitivity —
   so an FK/constraint test on default SQLite can pass by never testing anything, or fail on a
   dialect difference that production doesn't have. Constraint, migration, and SQL-dialect tests
   belong on the engine you deploy: a Postgres service container in CI, or testcontainers
   locally. Keep it one flag (`TEST_DATABASE_URL`) so the same suite runs both ways, and run the
   full suite against the production engine at least in CI (see
   `full-stack-dev-skills:database-and-orm` for what SQLite silently changes).
4. **Unit-test the genuinely tricky pure logic** — pricing math, date arithmetic, parsers:
   plain functions, plain asserts, no mocks. If a "unit" test needs three mocks to run,
   the design is telling you the logic is welded to I/O — extract the pure part
   (`full-stack-dev-skills:lean-code-principles`) instead of mocking around it.
5. **Keep end-to-end tests few and critical.** A handful of Playwright flows for the paths
   that must never break (log in, create the core object, complete the core action —
   the "money paths"). E2E tests are slow and flaky-prone; each one must earn its place by
   guarding a flow whose breakage is an incident.
6. **Mock only at true external boundaries** — third-party APIs, clocks, randomness, email.
   Use `respx`/`responses` for HTTP, inject the clock. Never mock your own database, your
   own services, or the framework: every internal mock is a place the test agrees with the
   code instead of checking it.
7. **Turn every bug into a test.** Before fixing: write the failing test that reproduces
   it; fix; the test passes and pins the behavior forever. This is the highest-ROI test
   category that exists — the probability-of-breaking is proven, it already broke.
8. **Be explicit about what NOT to test:** framework behavior (FastAPI's routing works),
   trivial getters/pass-throughs, private helpers already covered through the API, styling,
   and generated code. Coverage is a flashlight, not a target — chasing a percentage
   produces assertion-free tests that add cost and no protection.
   `references/testing-recipes.md` has the conftest spine, factory pattern, Playwright
   skeleton, and the level-decision table.

**Deliverable:** a conftest spine whose isolation is demonstrated by the canary, API tests for
each endpoint contract and business rule, no-mock unit tests for the tricky pure logic, a named
money-path E2E list, a regression test per past bug, a written don't-test list, and a stated
suite-runtime budget.

## Why / learn
A test suite is a tripwire system, and tripwires have two failure modes: not firing when a
burglar walks through (missed regressions) and firing every time the wind blows (brittle
tests that fail on refactors). The API boundary is the sweet spot because it's the
*contract* — tests written against it fire when behavior changes (what users experience)
and stay silent when implementation changes (what refactoring touches). Mock-heavy unit
suites invert this: they pin implementation details, so they fail on every refactor and
pass even when the integrated behavior is broken — worse than useless, they're negative
signal that trains people to ignore red. The mock-at-external-boundaries rule follows from
asking "what am I actually asserting?": mocking *your own* code asserts that the code calls
itself the way it calls itself; mocking the *outside world* removes nondeterminism you
don't control. The bug-becomes-test rule is empirical Bayesianism — past breakage is the
best predictor of future breakage — and the what-not-to-test list is the lean-code
principle applied to tests, because tests are code too: every test must pay rent in caught
regressions, and a test that can't fail meaningfully is pure carrying cost.

There is a third failure mode the tripwire metaphor hides, and it lives in the fixtures rather
than the tests: **the harness that quietly isn't doing its job**. A rollback that doesn't roll
back, or a test engine that drops the constraint under test, produces green — the one colour
nobody investigates. Test code gets no tests of its own, so the only defence is making each
harness promise falsifiable by something cheap: a canary test for isolation, one deliberate
constraint violation for the engine. Prove the instrument, then trust the measurements.

## Common mistakes
- Mock-everything unit suites → refactors go red, real breaks go green; test at the API boundary with a real test DB.
- Mocking your own database/services → the test agrees with the code instead of checking it; mock only external boundaries.
- E2E tests for every screen → slow, flaky, unmaintained; a few money-path flows only.
- Chasing a coverage percentage → assertion-free tests; rank by breakage probability × cost instead.
- Fixing bugs without a reproducing test → the same bug returns; test first, then fix.
- Three mocks to unit-test one function → extract the pure logic; the test difficulty is a design signal.
- Testing framework behavior → FastAPI's router works; test *your* rules.
- One shared mutable test database state → order-dependent flakes; per-test transaction rollback.
- Assuming the rollback fixture isolates → it can be released by the endpoint's own commit; prove it with the canary.
- Constraint tests on default SQLite → the constraint isn't enforced, so the test passes vacuously; use the production engine.
- Copying the sync `TestClient` spine into an `AsyncSession` app → async fixtures and an async client, same principles.

## Tailor to your environment
Record your testing conventions in `references/your-environment.md`: the fixture spine
location, test DB engine per environment (and which tests require the production engine), your
money-path E2E list, external boundaries and their mocks, and the suite-runtime budget you
enforce.

## References
- references/testing-recipes.md — conftest spine (with the isolation canary), engine choice, factories, Playwright skeleton, level-decision table
- references/your-environment.md — your fixtures, money paths, budgets (fill in)
