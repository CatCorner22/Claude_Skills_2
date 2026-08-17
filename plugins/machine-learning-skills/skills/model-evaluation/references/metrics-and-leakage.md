# Metrics, thresholds, and leakage (reference)

## Contents
- Regression metrics
- Classification metrics
- ROC AUC vs PR AUC
- Calibration
- Confusion matrix and threshold selection
- Cross-validation schemes
- Uncertainty on the reported metric
- Slice (subgroup) evaluation
- Label quality — auditing the target
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
- **ROC AUC** — probability the model ranks a random positive above a random negative; threshold-independent
  and **prevalence-invariant**. Both ROC axes are within-class rates — TPR = TP/(TP+FN) uses only positives,
  FPR = FP/(FP+TN) only negatives, and TNR = 1 − FPR only negatives — so changing the class ratio changes
  none of them. Duplicating or downsampling negatives leaves AUC alone (up to sampling noise). AUC is
  therefore not "inflated by the true-negative rate"; it simply **does not know** how rare the positives are.
- **PR AUC (average precision)** — precision-vs-recall area; prevalence-*aware*, so it moves with the class
  ratio. **Prefer it when positives are scarce** (fraud, anomalies, defaults). Its baseline is the positive
  rate, not 0.5 — a 1%-positive problem has PR-AUC baseline 0.01, so 0.15 can be a 15× lift.

**Why a high AUC still ships a useless alert queue** (the honest mechanism). Precision mixes the classes:
`precision = TPR·P / (TPR·P + FPR·N)`. Take 100,000 rows, 1% positive → P = 1,000, N = 99,000, at a
threshold with TPR = 0.80 and FPR = 0.05:

| | Predicted positive | Predicted negative |
|---|---|---|
| **Actual positive (1,000)** | TP = 800 | FN = 200 |
| **Actual negative (99,000)** | FP = 4,950 | TN = 94,050 |

- Recall = 800/1,000 = **80%**; TNR = 94,050/99,000 = **95%** = 1 − FPR.
- Precision = 800 / (800 + 4,950) = 800/5,750 = **13.9%** — reviewers work 5,750 alerts to find 800 cases.
- Now downsample negatives to 1,000 (a balanced test set, same model, same threshold): FP = 0.05 × 1,000 =
  50, precision = 800/850 = **94.1%**. AUC is identical in both tables; precision moved 13.9% → 94.1%.

The lesson to carry: resampling does not improve AUC, and the precision it "improves" is an artifact of the
new class ratio. Report PR AUC (and precision at your operating point) on the *real* prevalence. Standard
references for the comparison: Davis & Goadrich (ICML 2006); Saito & Rehmsmeier (2015) — cited as
attributions, no numbers taken from them.

## Calibration
Ranking (AUC) says who is riskier; **calibration** says whether a predicted 0.10 really means a 10% chance.
When you make expected-cost decisions from the probability (not just rank), check a **reliability curve** and
consider **Platt scaling** or **isotonic regression** to recalibrate. Boosted trees are often mis-calibrated.

## Confusion matrix and threshold selection
The model outputs a score; the **decision** is a threshold on it. The threshold is a **fitted parameter**, so
it is selected on validation data and never on test.
1. On the **validation set** (or inside each CV fold), build the confusion matrix at candidate thresholds
   (TP/FP/TN/FN).
2. Attach the business cost of a false positive and a false negative.
3. Pick the threshold that minimizes total expected cost (or hits a required recall / an alert budget).
4. **Freeze** it, then score the test set **once** at that threshold and report that number as the estimate.
The optimum is almost never 0.5. Document the threshold, the split it was chosen on, and the cost
assumptions behind it.

Two cautions:
- **The threshold has its own selection noise.** The cost curve near its minimum is usually flat, and with
  few positives the argmin jumps between validation samples. Prefer a threshold justified by an operating
  constraint (a required recall, an alert budget of N/day) or averaged across CV folds over the single
  argmin of one small validation set — and re-check it when the class balance or the cost changes.
- **Selecting the threshold on test contaminates the estimate** exactly as hyperparameter tuning on test
  does. If it already happened, say so and treat the test number as an upper bound.

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
