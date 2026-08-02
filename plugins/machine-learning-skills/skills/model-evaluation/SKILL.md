---
name: model-evaluation
description: >-
  Chooses the right metric and validation scheme for a model, guards against data leakage and
  overfitting, and compares every result against a baseline. Covers train/validation/test discipline,
  k-fold and time-series cross-validation, regression metrics (RMSE/MAE/R²) versus classification
  metrics (precision/recall/F1, ROC AUC vs PR AUC, calibration), confusion-matrix and threshold choice
  tied to error costs, and the common sources of leakage. Use when validating any model or picking a
  metric or decision threshold. Triggers: model evaluation, evaluate a model, cross-validation, k-fold,
  overfitting, underfitting, ROC AUC, precision recall, PR AUC, RMSE, R2, data leakage, train test
  split, confusion matrix, threshold, calibration.
---

# Model evaluation

## When to use
- Deciding how to validate a model (holdout vs k-fold vs time-series CV) and which metric to report.
- Diagnosing overfitting/underfitting, choosing a decision threshold, or reading a confusion matrix.
- Hunting for data leakage when offline results look "too good," or comparing a model to its baseline.
- Not for: framing the target and picking the decision metric conceptually up front → see `machine-learning-skills:ml-project-framing`. For time-series-specific backtesting mechanics → see `machine-learning-skills:time-series-forecasting`.

## Do it
1. **Split before you look at anything.** Carve out a **test set** and don't touch it until the very end;
   tune on **train + validation** (or cross-validation). For temporal data, **split by time**, never
   randomly — a random split lets the future leak into training.
2. **Choose the validation scheme for your data.** Large, IID data → a single **holdout** is fine. Small
   or precious data → **k-fold cross-validation** (stratified for classification) to use every row and get
   a variance estimate. Temporal data → **time-series CV** (rolling/expanding origin) — see
   `machine-learning-skills:time-series-forecasting`. Grouped data (repeats per customer) → **grouped CV**
   so the same entity never sits in both train and test.
3. **Pick the metric from the decision, not habit.** Regression → **MAE** (robust), **RMSE** (punishes big
   misses), **R²** (variance explained, easily flattered). Classification → **precision/recall/F1**, and
   for ranking quality **ROC AUC** on balanced problems but **PR AUC** when positives are rare. If you need
   calibrated probabilities (expected-cost decisions), check **calibration**, not just ranking. Details in
   `references/metrics-and-leakage.md`.
4. **Read the confusion matrix and set the threshold by cost.** A probability model doesn't decide at 0.5
   by law — it decides at the threshold that minimizes *your* cost of false positives vs false negatives.
   Build the confusion matrix at candidate thresholds and pick the one that matches the business cost.
5. **Compare against the baseline — always.** Report the naive/seasonal-naive/majority-class/current-rule
   score next to the model. An R² of 0.6 or an AUC of 0.8 means nothing until you know the baseline; "skill"
   is the *lift over baseline*, not the raw number.
6. **Diagnose overfit vs underfit.** Compare train and validation scores: a big gap (great on train, poor on
   validation) is **overfitting** → regularize, simplify, get more data; both poor is **underfitting** → a
   richer model or better features. Learning curves make the diagnosis visual.
7. **Hunt leakage whenever results look too good.** Trace every feature and every preprocessing step back to
   the prediction time and the split. Target leakage, train/test contamination, temporal leakage, group
   leakage, and preprocessing fit on the full dataset are the usual culprits — the checklist is in
   `references/metrics-and-leakage.md`.

## Why / learn
Two ideas do the heavy lifting: **the metric must match the decision, and leakage is the silent killer of
"great" offline results.** A metric is a proxy for the cost of being wrong; pick the wrong proxy and you
will optimize hard in the wrong direction — a 99%-accurate fraud model that never catches fraud is the
canonical example, because accuracy is the wrong proxy when positives are 1% of the data (there, precision,
recall, and PR AUC are what track the decision). ROC AUC is popular but *optimistic under imbalance*
because the huge negative class inflates the true-negative rate; PR AUC focuses on the rare positives you
actually care about. Threshold choice is where evaluation meets economics: the model outputs a score, but
the *decision* is a threshold, and the right threshold is wherever the marginal cost of a false positive
equals the marginal cost of a false negative — almost never 0.5. Leakage is insidious precisely because it
makes everything look wonderful: the model "knows" the answer through a feature or a split that won't exist
in production, so offline metrics soar and live performance collapses. The habit that protects you is
mechanical — split first, fit every transform on train only, anchor every feature to the prediction time,
and never let the test set influence a single decision until the end. And always, always compare to a
baseline, because a number without a reference point is not evidence of anything.

## Common mistakes
- Random split on temporal or grouped data → future/entity leaks into training. Split by time or by group.
- Reporting accuracy on imbalanced data → hides a useless model. Use precision/recall/F1 and PR AUC.
- Deciding at the default 0.5 threshold → ignores error costs. Set the threshold from the FP/FN cost trade-off.
- No baseline → the metric is uninterpretable. Always show the naive/majority-class score alongside.
- Fitting scalers/encoders/imputers on the whole dataset → preprocessing leakage. Fit inside the train fold only.
- Tuning hyperparameters on the test set → optimistic, non-reproducible. Tune on validation/CV; touch test once.
- Trusting a suspiciously high score → usually leakage. Trace features back to the prediction time before celebrating.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real cost figures, label rates, and sample rows
in `your-environment.private.md`, which is git-ignored): whether your data is IID / temporal / grouped, your
class balance, the business cost of a false positive vs a false negative, the metric your decision actually
cares about, and your baseline. This skill then maps its generic guidance onto your problem. For the
conceptual choice of metric during problem framing, start at `machine-learning-skills:ml-project-framing`.

## References
- references/metrics-and-leakage.md — metric definitions, ROC-vs-PR, calibration, threshold selection, and the leakage checklist
- references/your-environment.md — your data type, class balance, error costs, metric, and baseline (add when supplied)
