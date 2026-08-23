# Evals — math-foundations-skills:exponential-growth-and-logs

## 1. Positive trigger (should load the skill)
> "Our revenue went from $2.0M to about $3.22M over the last 5 years. What's the
> growth rate per year, how long until we double at that pace, and does the rule of
> 72 agree?"

Expected: skill loads and works in growth factors. It computes the endpoint ratio
(≈ 3.22/2.0 = 1.61), takes the fifth root to get CAGR ≈ 10% per year (1.10⁵ =
1.61051), and *checks by recompounding to the endpoint*. Doubling time comes out
both ways: exact ln 2/ln(1.10) ≈ 7.27 years and rule of 72 → 72/10 = 7.2, with the
note that the rule sits within about ±2% of exact in the 4–12% band (±1% over 6–10%). It states the
constant-rate assumption explicitly (the projection holds only if ~10% persists)
and explains why the per-year figure is a geometric, not arithmetic, summary of the
path. Every number shown is reproducible from the arithmetic given.

## 2. Near-miss (should NOT load this skill)
> "We're being offered $50,000 payable five years from now. What discount rate
> should we use, and what is it worth today?"

Expected: should NOT trigger this skill — it is a present-value question about the
worth of money across dates and the choice of a discount rate (time-value-of-money
territory, whose former owner is archived from this library), even though the
machinery ((1+r)^n) looks identical. If this skill loads on a PV/discount-rate
request, its description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Here's 36 months of order volume with a clear seasonal cycle — fit a model and
> project the next 12 months."

Expected: `machine-learning-skills:time-series-forecasting` owns fitting trend and
seasonality models to a history with temporal validation. "Project growth" sounds
adjacent, but the ask is model construction from a series, not constant-rate
factor/log arithmetic between endpoints.

## 3. Quality rubric
A good response:
- **Does the task:** converts every percent change to a factor before chaining;
  computes CAGR as (end/start)^(1/n) − 1 with n = periods between endpoints (not
  data points); verifies each computed rate by recompounding to the stated endpoint;
  uses t = ln(target/current)/ln(1+r) for horizon questions and shows the
  arithmetic; where the rule of 72 is used, states its approximation band and gives
  the exact figure alongside; averages multi-period rates geometrically.
- **Teaches:** explains why successive percent changes multiply rather than add
  (each acts on the new base — hence +10% then −10% = ×0.99), the log as the
  "what exponent" tool that turns how-long-until into division, why linear intuition
  underestimates compounding (e.g., 1%/day is ×37.8/year, not ×4.65), and why the
  arithmetic average of varying returns always flatters the outcome.
- **Stays honest:** labels projections with their constant-rate assumption instead
  of presenting them as facts; runs the dimensional check on time formulas (answer
  in the rate's own periods); flags when a log-scale chart would change the visual
  story and says which axis answers the user's actual question; and routes valuation
  (PV/NPV/IRR) or model-fitting requests to the owning skills rather than absorbing
  them.
