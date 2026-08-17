# Evals — decision-science-skills:reference-class-forecasting

## 1. Positive trigger (should load the skill)
> "Our tuition-receipts driver has 24 cycles of forecast-vs-actual history — MAPE around 6% and a
> persistent under-forecast bias of about +3.5%. Use the outside view to anchor next cycle's
> number on that base rate, and tell me what uplift or haircut to apply at our chosen certainty
> level."

Expected: skill loads and treats the variance history as the reference class. It proposes the
class definition (trailing cycles, stated exclusions) and asks the user to ratify it; builds the
ratio distribution with empirical percentiles (P20/P50/P80), not just the mean; writes down the
unadjusted P50 anchor before discussing specifics; distinguishes the run of same-signed misses
(special cause — a one-time driver correction for the model owner) from single-cycle noise
(common cause — leave the rule alone); picks the percentile in the direction the risk hurts
(haircut for receipts feeding a liquidity floor, uplift for disbursements); and logs the
prediction with a confidence level and a review date for later scoring. **Critically, it does not
both uplift the anchor for the +3.5% bias and hand the same bias to the model owner as a curve
correction** — it names the choice explicitly (one layer owns it, and the other party is told), and
if the curve is corrected it says the class must be reset from the break date, the bias uplift drops
to ×1.00, and the class is thin again until post-correction cycles accumulate.

## 1b. Positive trigger (aggregation — the P80 portfolio trap)
> "Our house policy is P80 on every cost line. I've applied it to all twelve programs in next
> year's plan and the total contingency comes out at nearly 20% of the budget. Finance says that's
> too much padding but the policy is the policy — who's right?"

Expected: skill loads and says **Finance is right and the policy is being misapplied**: P80 is a
promise about a *single* commitment, and summing item P80s double-counts risk because independent
overruns partially cancel — variances add, standard deviations don't, so the P80 of the *sum* sits
well below the sum of the P80s (for ten independent equal lines, √10 ≈ 3.2× less contingency, and
the summed figure is nearer a P99.6 than a P80). Prescribes the standard shape: **P50 per line plus
one contingency at the portfolio level sized on the portfolio's own P80**, held and released by a
named owner with a reported balance. States the correlation assumption explicitly rather than
reflexively dividing by √n — shared drivers push the required contingency back up, and at ρ = 1 the
sum of the P80s is exactly right, which is what summing implicitly assumes. Flags the exceptions:
lines that must each stand alone (per-entity covenants, hard caps, grant line limits) keep their own
P80, and schedule risk does not pool this way — parallel chains merging at a milestone make it
*worse*. Names the credibility cost of chronic underspend as the mirror image of the bias the method
exists to correct. Does **not** simply endorse "the policy is the policy."

## 2. Near-miss (should NOT load this skill)
> "Build me a rolling 13-week cash forecast model in Excel — input sheets for AR collections,
> AP runs, payroll, and debt service, with check cells and scenario toggles."

Expected: `data-analytics-bi-skills:spreadsheet-modeling` owns building the model workbook —
structure, formulas, checks, and scenarios. This skill only feeds such a model with base-rate
anchors and uplifts. If this skill loads on a model-building request, its description is
over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "Our daily transaction-volume series has trend and weekly seasonality — fit a SARIMA model,
> backtest it with rolling-origin splits, and report the error by horizon."

Expected: `machine-learning-skills:time-series-forecasting` owns statistical/ML series modeling
and temporal validation. Rolling-origin backtesting sounds adjacent to "score predictions later,"
but the ask is model construction and evaluation, not base-rate anchoring of a judgment estimate.

## 3. Quality rubric
A good response:
- **Does the task:** proposes 2–3 candidate reference classes with trade-offs and has the human
  ratify one, frozen before outcomes are computed; builds an empirical percentile distribution
  from the actual history (ratio or signed-error form, consistent with the library's variance %
  and signed-bias definitions); states the unadjusted base-rate anchor first; every departure
  from the anchor is either a written inside-vs-outside justification or a policy uplift at a
  stated certainty level chosen in the direction the risk hurts; **the certainty level is applied at
  the right level** — per item for a single commitment, P50-per-item-plus-one-portfolio-contingency
  when the sum is what is owned, with the exceptions (per-item covenants and caps; schedule merge
  bias) checked; the prediction is logged (journal entry with class, number, confidence, review
  date) and a scoring method named; single-period misses are tested common-cause vs. special-cause
  before any rule change is suggested; and a measured bias is corrected in **exactly one** layer,
  with the class reset from the break date if the model's curve is the layer chosen.
- **Teaches:** explains the planning fallacy (why inside-view stories are optimistic), strategic
  misrepresentation (why a base rate can't be argued down by a better story), why the mean of a
  skewed overrun distribution misleads, why summing tail percentiles across a portfolio
  over-budgets (independent risks partially cancel; distributed padding is also invisible and
  unreclaimable, and chronic underspend costs the same credibility overruns do), why adjusting after
  every miss is Deming funnel Rule 2 and adds variance, and the distinction that reconciles that
  guard with "update small and often" — the *belief* about a live question moves continuously on new
  information about that case, while the *estimating rule* changes rarely and only on diagnosed
  error from closed cases.
- **Stays honest:** reports a thin class as thin instead of manufacturing precise percentiles;
  never lets an unwritten adjustment move the anchor; keeps the class-ratification and
  certainty-level decisions with the human; routes model corrections to the owning forecasting
  skill rather than rebuilding the model itself; and marks external evidence it cannot verify
  (e.g., published overrun distributions) as such rather than citing figures from memory.
