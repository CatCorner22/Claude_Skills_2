# Evals — finance-skills:time-value-of-money

## 1. Positive trigger (should load the skill)
> "I'll receive 10,000 a year for 5 years starting next year. At a 7% discount rate, what's that
> stream worth today, and what discount rate would make its present value equal to 38,000?"

Expected: skill loads; recognizes a 5-year ordinary annuity; computes PV with
`C × [1 − (1 + r)^(−n)] / r` at 7%; solves the second part as an IRR/rate problem; states the answer
with its rate and valuation date; explains discounting as making dated cash flows comparable.

## 2. Near-miss (should NOT load this skill)
> "Should we buy the new packaging line? Here are the capex, the incremental sales, the depreciation
> schedule, and the salvage value — tell me if it's worth it."

Expected: this is a full project evaluation requiring incremental after-tax cash-flow construction
and competing decision rules — `finance-skills:capital-budgeting` should handle it. This skill may be
used by that one for the underlying PV/IRR math, but should not be the primary skill. If it loads as
primary, tighten the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** lays cash flows on a timeline, matches the rate to the period, applies the right
  closed form (annuity vs perpetuity vs single sum), and computes PV/FV/NPV/IRR correctly.
- **Teaches:** explains *why* a dollar today outweighs one tomorrow (it can earn a return) and why
  discounting makes flows comparable — not just the arithmetic.
- **Safe:** checks IRR for multiple/no-solution when signs change more than once, defers to NPV for
  ranking, and never quotes a PV without its discount rate and valuation date.
