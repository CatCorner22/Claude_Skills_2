# Metrics, thresholds, and leakage (reference)

## Contents
- Regression metrics
- Classification metrics
- ROC AUC vs PR AUC
- Calibration
- Confusion matrix and threshold selection
- Cross-validation schemes
- Leakage checklist

## Regression metrics
- **MAE** — mean absolute error, same units as the target, robust to outliers.
- **RMSE** — root mean squared error; penalizes large errors more; use when big misses cost disproportionately.
- **R²** — fraction of variance explained; easy to flatter (rises as you add features; can be negative out of
  sample). Report alongside an error metric, never alone.
- **MAPE / MASE** — percentage and scaled errors; see `machine-learning-skills:time-series-forecasting` for their traps.

## Classification metrics
For a chosen threshold, from the confusion matrix (TP, FP, TN, FN):
- **Precision** = TP / (TP + FP) — of what you flagged, how much was right (controls false alarms).
- **Recall (sensitivity)** = TP / (TP + FN) — of the real positives, how many you caught (controls misses).
- **F1** — harmonic mean of precision and recall; a single number when both matter.
- **Accuracy** = (TP + TN) / all — misleading under imbalance; a 99%-negative problem scores 99% by predicting "no."

## ROC AUC vs PR AUC
- **ROC AUC** — probability the model ranks a random positive above a random negative; threshold-independent.
  **Optimistic under heavy imbalance** because the large negative class inflates the true-negative rate.
- **PR AUC (average precision)** — precision-vs-recall area; focuses on the rare positive class. **Prefer it
  when positives are scarce** (fraud, anomalies, defaults). Its baseline is the positive rate, not 0.5.

## Calibration
Ranking (AUC) says who is riskier; **calibration** says whether a predicted 0.10 really means a 10% chance.
When you make expected-cost decisions from the probability (not just rank), check a **reliability curve** and
consider **Platt scaling** or **isotonic regression** to recalibrate. Boosted trees are often mis-calibrated.

## Confusion matrix and threshold selection
The model outputs a score; the **decision** is a threshold on it.
1. For candidate thresholds, build the confusion matrix (TP/FP/TN/FN).
2. Attach the business cost of a false positive and a false negative.
3. Pick the threshold that minimizes total expected cost (or hits a required recall / an alert budget).
The optimum is almost never 0.5. Document the threshold and the cost assumptions behind it.

## Cross-validation schemes
| Data shape | Scheme | Why |
|---|---|---|
| Large, IID | Single holdout | Cheap; enough data for a stable estimate |
| Small / precious | k-fold (stratified for classification) | Uses every row; gives a variance estimate |
| Temporal | Time-series CV (rolling/expanding origin) | Never train on the future |
| Grouped (repeats per entity) | Grouped k-fold | Same entity never in both train and test |

## Leakage checklist
- **Target leakage** — a feature is a proxy for, or derived from, the outcome (e.g. `days_to_payment` when
  predicting late payment). Drop it.
- **Train/test contamination** — the same row, or near-duplicate, in both splits; or tuning on the test set.
- **Temporal leakage** — using future information, or a random split on time-ordered data.
- **Group leakage** — the same customer/account in train and test inflates scores.
- **Preprocessing leakage** — scalers, encoders, imputers, or feature selection fit on the full dataset
  instead of inside each training fold. Fit on train only; apply to validation/test.
- **Red flag:** a metric far better than the baseline or than domain intuition — trace every feature back to
  the prediction time before believing it.
