# ML framing spec (reference)

A framed problem is a one-page contract. Fill every field before modeling; a blank field is an open risk.

## The one-page template
- **Decision:** who acts, what action changes with the prediction, when, and the cost of a wrong call.
- **Target (label):** exactly what is predicted; type (number / category / event-in-window); observation
  window; how it is measured or labeled.
- **Task type:** regression | binary classification | multiclass | ranking | forecasting | anomaly.
- **Unit of prediction (grain):** what one row is (e.g. one invoice, one account-day, one customer-month).
- **Prediction time:** the exact moment the prediction is made, relative to which features must be known.
- **Features (known at prediction time):** list each with its source system and when it becomes available.
- **Evaluation metric:** the metric tied to the decision, plus the error-cost asymmetry it encodes.
- **Baseline:** the naive rule to beat (last value, seasonal-naive, current heuristic, majority class).
- **Data availability:** rows of labeled history; time span; refresh cadence; known gaps.
- **Risks / assumptions:** leakage risks, distribution shift, label noise, sample size, stability.

## Worked treasury examples
- **Daily cash-flow forecast.** Decision: size tomorrow's short-term investment / funding. Target: net
  cash movement for account-day *d+1* (a number). Grain: account-day. Prediction time: end of day *d*,
  after the position is struck. Metric: MAE in currency (and asymmetric penalty if an overdraft costs
  more than idle cash). Baseline: seasonal-naive (same weekday last week). Hand to
  `machine-learning-skills:time-series-forecasting`.
- **Payment-anomaly flag.** Decision: hold a payment for review. Target: is this transaction anomalous
  (rare/label-scarce). Grain: one transaction. Prediction time: at authorization, before release.
  Metric: precision at the top-N alerts the team can review per day. Baseline: current rule set. Hand
  to `machine-learning-skills:anomaly-detection`.
- **Late-payment risk.** Decision: prioritize collections calls. Target: invoice paid > 30 days past
  due, judged 45 days after issue (binary). Grain: one invoice. Prediction time: issue date. Metric:
  PR AUC (positives are the minority). Baseline: "flag every customer who was late last quarter."

## Leakage checklist (run at framing time, on paper)
- Is any feature recorded *after* the prediction time? → drop it.
- Is any feature derived from the target, or from a field updated when the outcome is known? → drop it.
- Does an ID, timestamp, or "case status" encode the answer (e.g. `closed_reason`)? → drop it.
- For time series/panels, will you split by time so the model never trains on the future? → require it.
- Are aggregates (customer averages, encodings) computed over rows you won't have yet at prediction? → recompute per split.

## Is this even an ML problem? (fast filter)
- No decision changes on the output → not an ML problem; it's a report or a curiosity.
- A simple deterministic rule already solves it → use the rule; skip the model.
- No labeled history and no way to label → not supervised-learnable yet; consider unsupervised/anomaly.
- The relationship won't be stable over the horizon you care about → forecasting will disappoint; say so.
