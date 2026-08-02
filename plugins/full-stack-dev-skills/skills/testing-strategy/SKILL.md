---
name: testing-strategy
description: >-
  Designs minimal effective test suites for full-stack apps — testing behavior at the API
  boundary over mocking internals, pytest fixtures for real (test) databases, a handful of
  Playwright end-to-end tests for critical user flows only, regression tests for every fixed
  bug, and explicit judgment about what NOT to test — so the suite catches real breakage
  without taxing every refactor. Use when setting up testing for an app, deciding what to
  test at which level, reviewing a slow or brittle suite, or adding tests around a bug.
  Triggers: testing strategy, what to test, pytest setup, test the API, mock or not,
  brittle tests, slow test suite, playwright e2e, test coverage target, regression test,
  test pyramid, integration vs unit.
---

# Testing strategy: minimal and effective

## When to use
- Standing up the test approach for an app, or rebalancing a suite that is slow, brittle, or
  quietly useless.
- Deciding the level (unit / API / end-to-end) for a specific behavior, or writing tests
  around a bug fix.
- Not for: review process and CI gates → `coding-agent-skills:git-and-code-review` and
  `full-stack-dev-skills:deploy-and-operate`. Model evaluation →
  `machine-learning-skills:model-evaluation`.

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

2. **Build the fixture spine once.** In `conftest.py`: an app client (`TestClient`), a
   fresh-schema test DB per session with per-test transaction rollback (fast isolation),
   and small factory helpers for common rows. Real database (SQLite file or Postgres in
   CI), not mocked sessions — the SQL is exactly what you need tested.
3. **Unit-test the genuinely tricky pure logic** — pricing math, date arithmetic, parsers:
   plain functions, plain asserts, no mocks. If a "unit" test needs three mocks to run,
   the design is telling you the logic is welded to I/O — extract the pure part
   (`full-stack-dev-skills:lean-code-principles`) instead of mocking around it.
4. **Keep end-to-end tests few and critical.** A handful of Playwright flows for the paths
   that must never break (log in, create the core object, complete the core action —
   the "money paths"). E2E tests are slow and flaky-prone; each one must earn its place by
   guarding a flow whose breakage is an incident.
5. **Mock only at true external boundaries** — third-party APIs, clocks, randomness, email.
   Use `respx`/`responses` for HTTP, inject the clock. Never mock your own database, your
   own services, or the framework: every internal mock is a place the test agrees with the
   code instead of checking it.
6. **Turn every bug into a test.** Before fixing: write the failing test that reproduces
   it; fix; the test passes and pins the behavior forever. This is the highest-ROI test
   category that exists — the probability-of-breaking is proven, it already broke.
7. **Be explicit about what NOT to test:** framework behavior (FastAPI's routing works),
   trivial getters/pass-throughs, private helpers already covered through the API, styling,
   and generated code. Coverage is a flashlight, not a target — chasing a percentage
   produces assertion-free tests that add cost and no protection.
   `references/testing-recipes.md` has the conftest spine, factory pattern, Playwright
   skeleton, and the level-decision table.

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

## Common mistakes
- Mock-everything unit suites → refactors go red, real breaks go green; test at the API boundary with a real test DB.
- Mocking your own database/services → the test agrees with the code instead of checking it; mock only external boundaries.
- E2E tests for every screen → slow, flaky, unmaintained; a few money-path flows only.
- Chasing a coverage percentage → assertion-free tests; rank by breakage probability × cost instead.
- Fixing bugs without a reproducing test → the same bug returns; test first, then fix.
- Three mocks to unit-test one function → extract the pure logic; the test difficulty is a design signal.
- Testing framework behavior → FastAPI's router works; test *your* rules.
- One shared mutable test database state → order-dependent flakes; per-test transaction rollback.

## Tailor to your environment
Record your testing conventions in `references/your-environment.md`: the fixture spine
location, test DB engine per environment, your money-path E2E list, external boundaries and
their mocks, and the suite-runtime budget you enforce.

## References
- references/testing-recipes.md — conftest spine, factories, Playwright skeleton, level-decision table
- references/your-environment.md — your fixtures, money paths, budgets (fill in)
