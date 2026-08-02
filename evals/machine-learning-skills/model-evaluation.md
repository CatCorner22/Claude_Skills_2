# Evals — machine-learning-skills:model-evaluation

## 1. Positive trigger (should load the skill)
> "My fraud classifier gets 98.5% accuracy but the reviewers say it barely catches anything. What metric
> should I actually use, how do I pick a threshold, and how do I cross-validate this properly?"

Expected: skill loads; explains accuracy is the wrong proxy under imbalance; switches to precision/recall/F1
and PR AUC; builds the confusion matrix and sets a threshold from FP/FN cost or an alert budget; recommends
stratified (or grouped/time-series) cross-validation; insists on comparing to a baseline; and checks for
leakage given the suspiciously high accuracy.

## 2. Near-miss (should NOT load this skill)
> "What business decision does this model actually support, and what should the target even be?"

Expected: this is problem framing, upstream of evaluation. The `machine-learning-skills:ml-project-framing`
skill should handle it. If this evaluation skill loads, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** chooses a metric matched to the decision and class balance, picks a validation scheme
  suited to the data shape, reads the confusion matrix, sets a cost-based threshold, and compares to a baseline.
- **Teaches:** explains *why* the metric must match the decision (accuracy fails under imbalance; ROC AUC is
  optimistic vs PR AUC) and *why* leakage silently inflates offline results — not just which number to report.
- **Safe:** never uses a random split on temporal/grouped data, never fits preprocessing on the full dataset,
  never tunes on the test set, and never reports a metric without its baseline.
