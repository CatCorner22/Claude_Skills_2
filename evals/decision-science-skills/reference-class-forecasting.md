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
prediction with a confidence level and a review date for later scoring.

## 2. Near-miss (should NOT load this skill)
> "Build me a rolling 13-week direct-method cash forecast from AR collections, AP runs, payroll,
> and debt service."

Expected: `cash-management-skills:cash-forecasting` owns building the projection — drivers,
calendars, and the model itself. This skill only feeds such a model with base-rate anchors and
uplifts. If this skill loads on a model-building request, its description is over-triggering.

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
  stated certainty level chosen in the direction the risk hurts; the prediction is logged
  (journal entry with class, number, confidence, review date) and a scoring method named;
  single-period misses are tested common-cause vs. special-cause before any rule change is
  suggested.
- **Teaches:** explains the planning fallacy (why inside-view stories are optimistic), strategic
  misrepresentation (why a base rate can't be argued down by a better story), why the mean of a
  skewed overrun distribution misleads, and why adjusting after every miss is Deming funnel
  Rule 2 and adds variance.
- **Stays honest:** reports a thin class as thin instead of manufacturing precise percentiles;
  never lets an unwritten adjustment move the anchor; keeps the class-ratification and
  certainty-level decisions with the human; routes model corrections to the owning forecasting
  skill rather than rebuilding the model itself; and marks external evidence it cannot verify
  (e.g., published overrun distributions) as such rather than citing figures from memory.
