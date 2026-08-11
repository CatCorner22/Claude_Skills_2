# Evals — finance-skills:capital-budgeting

## 1. Positive trigger (should load the skill)
> "We can buy a new machine for 500k. It adds 180k of pre-tax operating cash a year for 5 years,
> depreciates straight-line, salvages for 50k, and needs 40k of working capital. Tax is 25%, hurdle
> rate 9%. Is it worth it, and how does it stack up against a cheaper alternative with a higher IRR?"

Expected: skill loads; builds incremental after-tax cash flows across the three phases (outlay + ΔNWC,
annual OCF with the depreciation tax shield, terminal after-tax salvage + NWC recovery); computes NPV,
IRR, payback, and PI; and — facing the "higher IRR alternative" — ranks on **NPV**, explaining IRR's
scale/timing blind spot. Excludes any sunk cost and does not put financing cost in the cash flows.

## 2. Near-miss (should NOT load this skill)
> "Just remind me of the present-value formula and how to pick a discount rate for a single future
> cash flow."

Expected: this is the underlying time-value mechanics with no project or incremental cash-flow build —
`finance-skills:time-value-of-money` should handle it. If capital-budgeting loads as primary, tighten
the "Not for" cross-link.

## 3. Quality rubric
A good response:
- **Does the task:** constructs incremental after-tax free cash flows (including the depreciation tax
  shield, ΔNWC, and after-tax salvage), computes NPV/IRR/payback/PI, and gives a clear accept/rank.
- **Teaches:** explains that NPV measures value created and is the governing rule, while IRR, payback,
  and PI are supplements with specific blind spots (scale/timing, time value, rationing).
- **Safe:** excludes sunk costs, keeps financing costs out of the cash flows (they are in the rate),
  ranks mutually exclusive projects by NPV rather than IRR, and reports sensitivity, not a single point.
