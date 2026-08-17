# ML framing spec (reference)

A framed problem is a one-page contract. Fill every field before modeling; a blank field is an
open risk.

## Contents
- Where this discipline comes from
- The one-page template
- Fully worked example: late-payment risk (analyst setting)
- Worked sketches in three more settings (attorney, operations, developer)
- The baseline catalog
- Leakage checklist (run at framing time, on paper)
- Is this even an ML problem? (fast filter)
- Handoffs once the frame is set

## Where this discipline comes from

The insist-on-business-understanding-first discipline is the oldest stable result in applied
data mining: CRISP-DM (the Cross-Industry Standard Process for Data Mining), developed by an
industry consortium — NCR, DaimlerChrysler, SPSS, and the insurer OHRA — conceived in the
mid-1990s with its step-by-step guide published at the turn of the millennium, places
**Business Understanding** as the first of six phases, before Data Understanding, Data
Preparation, Modeling, Evaluation, and Deployment [snippet-only]. This skill is that first
phase made concrete: the framing spec below is a Business Understanding deliverable. The
lineage matters because it explains the ordering — the process was designed around observed
project failures, and the failures clustered at the front, not in the algorithms.

## The one-page template
- **Decision:** who acts, what action changes with the prediction, when, and the cost of a wrong call.
- **Target (label):** exactly what is predicted; type (number / category / event-in-window); observation
  window; how it is measured or labeled — and, for human-judged labels, evidence the judges agree.
- **Task type:** regression | binary classification | multiclass | ranking | forecasting | anomaly.
- **Unit of prediction (grain):** what one row is (e.g. one invoice, one account-day, one customer-month).
- **Prediction time:** the exact moment the prediction is made, relative to which features must be known.
- **Features (known at prediction time):** list each with its source system and when it becomes available.
- **Evaluation metric:** the metric tied to the decision, plus the error-cost asymmetry it encodes.
- **Baseline:** the naive rule to beat (last value, seasonal-naive, current heuristic, majority class).
- **Data availability:** rows of labeled history; time span; refresh cadence; known gaps.
- **Risks / assumptions:** leakage risks, distribution shift, label noise, sample size, stability.

## Fully worked example: late-payment risk (analyst setting)

Any organization that issues invoices has this problem; nothing below is industry-specific.

- **Decision:** the collections team works a daily call list of at most 40 accounts. The
  prediction reorders that list at invoice issue. A false positive wastes one call slot; a
  false negative means a late invoice nobody called — roughly ten times worse by the team's
  own accounting of write-off exposure.
- **Target:** will invoice *i* be paid more than 30 days past due. Terms are net-30, so the
  due date is issue + 30 and "late" means paid after issue + 60; judged at issue + 75, with
  a still-unpaid invoice counted late (at day 75 it is already 45 days past due) — so every
  label is final when read. Binary.
- **Task type:** binary classification.
- **Grain:** one invoice, with an account-level roll-up for the decision: an account's daily
  score is its riskiest open invoice, and the call list takes the top 40 *accounts*, one
  slot each — otherwise one account with six open invoices could hold six of the forty slots.
- **Prediction time:** the moment the invoice is issued.
- **Features (each checked "knowable at issue?"):** customer's past on-time rate (billing
  system, available at issue — computed over *prior* invoices only), invoice amount (at
  issue), customer tenure (at issue), days-since-last-order (at issue). **Rejected as
  leakage:** payment reminders sent (recorded after issue), "disputed" flag (set after the
  outcome is in motion), customer's *current-quarter* average days-to-pay (window overlaps
  the label's own period).
- **Evaluation metric:** precision in the top-40 daily ranking, measured over accounts —
  the list is capacity-bound,
  so quality of the *head* of the ranking is the decision-relevant quantity. PR AUC as the
  secondary, since late invoices are the minority class.
- **Baseline:** "rank by: was this customer late last quarter, then by amount descending" —
  the team's current heuristic, written down and scored on the same history.
- **Data availability:** ~26 months of issued invoices with final outcomes; labels complete
  (payment dates are recorded mechanically, no human judgment needed).
- **Risks:** a pricing policy change 8 months ago (distribution shift — test stability across
  the boundary); customer consolidation means duplicate customer IDs (fix keys first);
  seasonal year-end payment behavior (split by time, never randomly).

Two framing findings *before any model*: the current-quarter average-days-to-pay feature —
the one stakeholders were most excited about — is leakage; and the baseline heuristic is
free, so the model's pitch is "beats the heuristic's top-40 precision," not "has good AUC."

## Worked sketches in three more settings

- **Attorney — intake triage.** Decision: which incoming matters get a senior review this
  week (capacity: 10). Target: will this matter breach its first deadline or require rework,
  judged 60 days after intake. Grain: one matter at intake. Prediction time: intake
  completion. Leakage trap: "hours billed" — recorded after intake. Label caution: "required
  rework" is a human judgment — measure reviewer agreement before trusting the labels
  (`continuous-improvement-skills:measurement-systems-analysis`). Baseline: the intake
  coordinator's current urgency flag.
- **Operations — weekly volume forecast.** Decision: next week's staffing level, set every
  Thursday. Target: total request/order/call volume for the following week (a number).
  Grain: one site-week. Prediction time: Thursday 12:00 of the prior week. Metric: MAE in
  units of staff-hours, with an asymmetry if understaffing costs more than overstaffing
  (pinball loss at the chosen quantile). Baseline: same week last year adjusted by the
  trailing 4-week ratio — seasonal-naive, and hard to beat. Series work hands to
  `machine-learning-skills:time-series-forecasting`.
- **Developer — risky-change flagging.** Decision: which merges get a mandatory second
  review. Target: will this change be linked to an incident or revert within 14 days.
  Grain: one merged change. Prediction time: merge time. Leakage trap: post-merge alert
  counts. Scarce labels (few incidents) → consider framing as anomaly ranking instead of
  classification — `machine-learning-skills:anomaly-detection`. Baseline: "flag changes
  touching more than N files or any file in the incident-prone list."

## The baseline catalog

Write the naive rule down and *score it on the same history* — it is the model's opponent.

| Task shape | Free baseline |
|---|---|
| Forecasting a series | Last value (naive); same period last cycle (seasonal-naive) |
| Binary classification | Majority class; the current human heuristic or rule |
| Ranking a queue | Current triage order; sort by the single most predictive raw field |
| Regression | Grand mean; group mean (per customer/site/category) |
| Anomaly flagging | The existing rule set / threshold list |

If a stakeholder can't articulate the current heuristic, that *is* the heuristic — undocumented
judgment — and writing it down is the first deliverable of the project.

## Leakage checklist (run at framing time, on paper)
- Is any feature recorded *after* the prediction time? → drop it.
- Is any feature derived from the target, or from a field updated when the outcome is known? → drop it.
- Does an ID, timestamp, or "case status" encode the answer (e.g. `closed_reason`)? → drop it.
- Do any aggregate features (customer averages, encodings) use windows that overlap the label's
  observation window? → recompute over strictly-prior data.
- For time series/panels, will you split by time so the model never trains on the future? → require it.
- Are aggregates computed over rows you won't have yet at prediction? → rebuild them *as of*
  the prediction timestamp, over strictly-prior rows only. Recomputing per split is a
  different guard (it stops test rows leaking into training features) and does not fix this
  one: inside the training fold, a row's own future is still in its aggregate
  (mechanics live in `machine-learning-skills:feature-engineering`).

## Is this even an ML problem? (fast filter)
- No decision changes on the output → not an ML problem; it's a report or a curiosity.
- A simple deterministic rule already solves it → use the rule; skip the model.
- No labeled history and no way to label → not supervised-learnable yet; consider
  unsupervised/anomaly framing, or start recording labels now.
- The relationship won't be stable over the horizon you care about → forecasting will
  disappoint; say so in the spec instead of discovering it in production.
- The promised lift rests only on the project's own story → take the outside view on how
  similar efforts actually performed (`decision-science-skills:reference-class-forecasting`)
  before committing the roadmap.

## Handoffs once the frame is set
- Signal exploration and data-quality profiling → `data-analytics-bi-skills:exploratory-data-analysis`
- Feature encoding/scaling with fit-on-train discipline → `machine-learning-skills:feature-engineering`
- Regression/classification build → `machine-learning-skills:supervised-modeling`
- Series forecasting with temporal backtesting → `machine-learning-skills:time-series-forecasting`
- Scarce-label unusual-instance detection → `machine-learning-skills:anomaly-detection`
- Metric, validation scheme, and leakage verification → `machine-learning-skills:model-evaluation`
