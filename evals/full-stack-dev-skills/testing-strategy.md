# Evals — full-stack-dev-skills:testing-strategy

## 1. Positive trigger (should load the skill)
> "Our test suite has 400 mock-heavy unit tests, goes red on every refactor, and still
> missed last week's production bug. Redesign the testing approach."

Expected: skill loads; rebalances toward API-boundary tests with a real test DB (conftest
spine, per-test rollback); keeps no-mock unit tests for tricky pure logic; a few Playwright
money-path flows; mocks only at external boundaries; last week's bug becomes a reproducing
regression test; explicit don't-test list replaces the coverage target.

## 2. Near-miss (should NOT load this skill)
> "How do I measure whether my churn model is any good — AUC, precision, calibration?"

Expected: model evaluation — `machine-learning-skills:model-evaluation`. If this skill
loads, sharpen the software-testing framing.

## 3. Quality rubric
A good response:
- **Does the task:** concrete rebalanced suite (fixtures, API tests, minimal E2E),
  regression test for the missed bug, runtime budget.
- **Teaches:** the two tripwire failure modes, why the API boundary fires on behavior and
  stays silent on refactors, mock-your-own-code as self-agreement, tests-pay-rent.
- **Safe:** doesn't mock own DB/services, doesn't chase coverage numbers, treats
  three-mock tests as design signals to extract pure logic.
