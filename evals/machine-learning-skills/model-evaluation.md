# Evals — machine-learning-skills:model-evaluation

## 1. Positive trigger (should load the skill)
> "My fraud classifier gets 98.5% accuracy but the reviewers say it barely catches anything. What metric
> should I actually use, how do I pick a threshold, and how do I cross-validate this properly?"

Expected: skill loads; explains accuracy is the wrong proxy under imbalance; switches to precision/recall/F1
and PR AUC; builds the confusion matrix and sets a threshold from FP/FN cost or an alert budget **on the
validation set, then scores test once at that frozen threshold**; recommends stratified (or
grouped/time-series) cross-validation; insists on comparing to a baseline; runs the leakage checklist (the
suspicious accuracy raises the priority, but the checklist runs either way); puts a confidence interval on
the reported metric and asks how many *positives* the test set holds; breaks performance down by slice; and
asks where the fraud labels came from and how consistent they are.

## 2. Near-miss (should NOT load this skill)
> "What business decision does this model actually support, and what should the target even be?"

Expected: this is problem framing, upstream of evaluation. The `machine-learning-skills:ml-project-framing`
skill should handle it. If this evaluation skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** chooses a metric matched to the decision and class balance, picks a validation scheme
  suited to the data shape, reads the confusion matrix, sets a cost-based threshold *on validation*, compares
  to a baseline, quantifies the metric's uncertainty, and reports performance by slice.
- **Teaches:** explains *why* the metric must match the decision (accuracy fails under imbalance) and *why*
  leakage silently inflates offline results — not just which number to report.
- **Gets the ROC/PR mechanism right:** says ROC AUC is **prevalence-invariant** (TPR/FPR/TNR are all
  within-class rates, so class balance does not move AUC) and that what collapses under imbalance is
  **precision** — a small FPR on a huge negative class swamps the few true positives. A response that claims
  the negative class "inflates the true-negative rate" or that resampling will raise AUC has failed this
  item, even though its conclusion (prefer PR AUC when positives are scarce) is right.
- **Safe:** never uses a random split on temporal/grouped data, never fits preprocessing on the full dataset,
  never tunes hyperparameters *or the threshold* on the test set, never reports a metric without its
  baseline, and never treats labels as unquestioned ground truth.
- **Delivers the contract:** the output reads as an evaluation report — validation scheme with rationale,
  metric tied to the decision, baseline-vs-model scores with lift, cost-based threshold with the split it was
  chosen on, overfit/underfit diagnosis, the leakage checklist and its findings, a CI on the headline metric
  with the effective n (positives, not rows), the metric by slice with per-slice n, and the label provenance.
