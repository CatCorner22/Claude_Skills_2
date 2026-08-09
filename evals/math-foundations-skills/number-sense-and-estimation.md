# Evals — math-foundations-skills:number-sense-and-estimation

## 1. Positive trigger (should load the skill)
> "Before I trust this model output — it says our new support team will handle 148,000
> tickets a year — give me a ballpark of my own. Back-of-the-envelope is fine: does that
> number make sense for a 6-person team?"

Expected: the skill loads and does its own estimate *before* engaging with the given figure
(anchoring guard), decomposing (e.g., tickets per agent per day × agents × working days:
6 agents × ~30 tickets/day × ~250 days = 45,000), computing an optimistic and a pessimistic
bound and checking they bracket the central figure, then triangulating by a second route. It
concludes the 148,000 claim is roughly 3× above the plausible range, states the comparison as
order-of-magnitude rather than fake-precise, shows every multiplication, and suggests where
the model likely went wrong (a units/period slip or an unrealistic per-agent rate) rather
than just declaring it false.

## 2. Near-miss (should load the ADJACENT skill instead)
> "We have 30 past projects with estimated vs actual durations — the actuals keep coming in
> long. Anchor our next project's estimate on that history and tell me what uplift to apply."

Expected: `decision-science-skills:reference-class-forecasting` loads instead. A distribution
of comparable past outcomes used to discipline a material estimate is formal outside-view
work — reference class, percentiles, uplift at a certainty level — not back-of-the-envelope
figuring. If number-sense-and-estimation loads here, its description is over-triggering.

## 2b. Near-miss (closer — should also NOT load this skill)
> "Here's a CSV of 4,000 invoice amounts. What's the typical value and how spread out are
> they? Median or trimmed figures if there are outliers."

Expected: `data-analytics-bi-skills:descriptive-statistics` loads instead. The data exists
and the ask is to summarize it (center, spread, robustness) — no estimation of an unmeasured
quantity and no gut-check of a computed claim is requested.

## 3. Quality rubric
A good response:
- **Does the task:** produces its own rough figure before examining any given number; uses a
  multiplicative decomposition with each factor judged explicitly; computes optimistic and
  pessimistic bounds by pushing every factor (not just one) and verifies the bounds bracket
  the central figure; triangulates via a genuinely different decomposition; reports a range
  and one significant figure, never false precision; when checking a given number, runs the
  five-question protocol (sign, magnitude, units, independent re-derivation, edge behavior)
  and says which checks passed or failed.
- **Teaches:** explains why a wrong exact answer looks identical to a right one (estimation as
  the independent low-precision channel), why ranges beat points, why factor errors partially
  cancel in products, and why estimating before looking guards against anchoring.
- **Stays honest:** every shown multiplication is arithmetically correct and recomputable;
  disagreement between estimate and calculation is reported as "investigate both," not
  "the estimate wins"; a number that passes the checks is called plausible, not verified; and
  the answer routes units questions to `math-foundations-skills:units-and-dimensional-analysis`
  and dataset summaries to `data-analytics-bi-skills:descriptive-statistics` rather than
  absorbing them.
