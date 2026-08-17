# Evals — full-stack-dev-skills:testing-strategy

## 1. Positive trigger (should load the skill)
> "Our test suite has 400 mock-heavy unit tests, goes red on every refactor, and still
> missed last week's production bug. Redesign the testing approach."

Expected: skill loads; rebalances toward API-boundary tests with a real test DB (conftest
spine, per-test rollback); keeps no-mock unit tests for tricky pure logic; a few Playwright
money-path flows; mocks only at external boundaries; last week's bug becomes a reproducing
regression test; explicit don't-test list replaces the coverage target.

## 1b. Positive trigger (the isolation path)
> "Every test passes on its own but two of them fail when we run the whole file, and CI is
> flaky. It's something about our test database fixture."

Expected: skill loads; identifies that the endpoint's own `commit()` is what breaks the
transaction-rollback fixture and that state is leaking between tests; fixes the spine
(`join_transaction_mode="create_savepoint"`, plus the pysqlite `BEGIN` workaround if the test DB
is SQLite, since `create_savepoint` on default pysqlite leaks); adds the two-test canary so the
regression cannot return silently; checks whether setup rows are committed rather than flushed.

## 2. Near-miss (should NOT load this skill)
> "How do I measure whether my churn model is any good — AUC, precision, calibration?"

Expected: model evaluation — `machine-learning-skills:model-evaluation`. If this skill
loads, sharpen the software-testing framing.

## 3. Quality rubric
A good response:
- **Does the task:** concrete rebalanced suite (fixtures, API tests, minimal E2E),
  regression test for the missed bug, runtime budget, and a fixture spine whose isolation is
  demonstrated by a canary rather than asserted.
- **Teaches:** the two tripwire failure modes, why the API boundary fires on behavior and
  stays silent on refactors, mock-your-own-code as self-agreement, tests-pay-rent, and the third
  failure mode — a harness that quietly isn't working, which shows up as green.
- **Has a failure envelope:** says where the recipe stops working. Constraint tests need the
  production engine because default SQLite ignores foreign keys; the sync `TestClient` spine
  does not carry over to an `AsyncSession` app; `create_savepoint` needs the pysqlite `BEGIN`
  workaround on SQLite.
- **Safe:** doesn't mock own DB/services, doesn't chase coverage numbers, treats
  three-mock tests as design signals to extract pure logic.

## 4. Anti-pattern the skill must not reproduce
Handing over a conftest spine as a copy-paste spine with no way to tell whether its isolation
actually holds, or a level-decision table that sends constraint tests to a SQLite fixture that
does not enforce constraints, fails this eval — the suite it produces is green for the wrong
reason, which is the specific outcome the skill promises to prevent.
