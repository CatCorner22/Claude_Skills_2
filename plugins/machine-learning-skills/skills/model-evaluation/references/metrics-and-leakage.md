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

## Uncertainty on the reported metric
Every metric is a statistic on a finite sample, so it carries a standard error. Report an interval.

- **A rate (precision, recall, accuracy)** is a proportion: `SE ≈ √(p̂(1−p̂)/n)`, and the `n` is the
  denominator of *that* rate — recall's `n` is the number of **positives** in the test set, not the row count.
- **AUC, RMSE, F1, a composite** have no tidy closed form: **bootstrap** the test set (resample rows with
  replacement, recompute, take the 2.5th/97.5th percentiles of ~2,000+ replicates).
- **k-fold** gives you a spread for free: report the mean **and** the across-fold standard deviation.
- **Both formulas assume the test rows are independent, and a grouped or temporal test set is not.** When
  the same entity contributes many rows — several invoices per customer, several days per account — the
  effective sample is the number of *entities*, not the number of rows, and resampling rows collapses the
  interval. Simulated on 200 entities × 20 rows with strong within-entity correlation, a row-level
  bootstrap returned a "95%" band about **half** the honest width, covering the true value **61%** of the
  time; resampling whole entities restored the width and 94% coverage. The size of the gap tracks how
  strongly rows within an entity agree, but the direction never changes — row resampling is always too
  narrow, never too wide. So bootstrap the **cluster** (whole entities, or contiguous time blocks for a
  series), and quote the entity or block count as the `n` behind the interval.

Worked: a test set with **40 positives** and an observed recall of **0.80**.
- `SE ≈ √(0.80 × 0.20 / 40) = √0.004 = 0.063` → 95% normal-approximation interval `0.80 ± 1.96 × 0.063 =
  0.80 ± 0.124` → **[0.68, 0.92]**, i.e. ±12 points on your headline number.
- At small `n` the normal approximation is crude — it is symmetric around p̂ and can run past 1 (at a
  recall of 0.95 on 40 positives it returns an upper bound of **1.018**). Prefer **Wilson**, which is
  asymmetric and stays inside [0, 1]: **[0.65, 0.90]** here. Note Wilson is not *wider* — it is shifted
  down, and the correction that matters is to the **lower** bound, which the normal approximation put 3
  points too high. **Clopper–Pearson** (exact) is the conservative choice and is genuinely wider:
  **[0.64, 0.91]**. Use Wilson below a few hundred events, Clopper–Pearson when you must not overstate.
- With **200 positives** the same 0.80 gives `SE = √(0.16/200) = 0.028` → **[0.74, 0.86]** (±5.5 points).

So: "we improved recall from 78% to 81%" on 40 positives is not a finding. Sizing question to ask before the
experiment, not after: how many positives does the test set need for the band to be narrower than the
smallest improvement worth shipping? A useful anchor — halving the interval width takes **4×** the positives.

## Slice (subgroup) evaluation
The aggregate metric is a weighted average over segments, and averages hide their worst term.
1. List the slices the decision actually touches: region, channel, product line, customer size/tenure,
   language, device, new-vs-returning, time period (recent months especially), plus any protected or
   contractually sensitive group.
2. Report the metric **per slice with the slice's own n** and the slice's own baseline. A slice can be worse
   than the current rule while the aggregate looks better than the current rule.
3. Watch for the two failure shapes: a **small slice with a terrible score** (invisible in the average, very
   visible to the people in it) and a **large slice carrying the whole lift** (the model works for one
   segment and you are about to deploy it to five).
4. Guard against slice-hunting: many slices means many chances for noise, so treat per-slice gaps as
   hypotheses to confirm (bigger sample, next period), and pre-register the slices you will report.
5. Time is the slice people forget. Score the most recent period separately — a model that is fine on
   average and degrading over the last quarter is a model with an expiry date.

## Label quality — auditing the target
The leakage checklist audits features; this audits the **target**. A label is a measurement produced by some
process — a reviewer, a rule, a downstream system, a judge model — and every metric inherits its error.
- **Provenance:** who or what produced each label, from what evidence, and at what point in time? Labels
  created *after* the prediction moment (a later manual correction, a closed-case disposition) may encode
  information the model won't have — which is target leakage wearing a label's clothes.
- **Agreement:** if humans (or an LLM judge) assign labels, measure agreement before trusting scores —
  repeat judgments per rater, multiple raters on the same items, a reference set, and a kappa. A model
  cannot be scored more finely than its labels agree with themselves.
- **Error review:** pull a sample of the model's *confident* mistakes and re-adjudicate them. Some fraction
  will be label errors, and that fraction is a ceiling on the metric you can honestly claim.
- **Asymmetry:** noise in the positive labels usually hurts more than noise in the negatives when positives
  are rare, because each mislabelled positive is a large share of a small class.
- **Do the study properly:** `continuous-improvement-skills:measurement-systems-analysis` runs the
  attribute-agreement study for pass/fail judgments (including LLM-as-judge scoring) and the crossed Gage
  R&R that splits repeatability (the same rater re-judging) from reproducibility (rater-to-rater), judged on
  %GRR and distinct categories. That skill already describes itself as adding the inter-rater rigor on top
  of this one; this is the return link — send label-quality questions there and bring the agreement numbers
  back into the evaluation report.

## Leakage checklist
Run all of it on **every** evaluation, and record what each check found — a suspiciously good score raises
the priority of the hunt, it is not the trigger for starting it.
- **Target leakage** — a feature is a proxy for, or derived from, the outcome (e.g. `days_to_payment` when
  predicting late payment). Drop it.
- **Train/test contamination** — the same row, or near-duplicate, in both splits; or tuning on the test set.
- **Temporal leakage** — using future information, or a random split on time-ordered data.
- **Group leakage** — the same customer/account in train and test inflates scores.
- **Preprocessing leakage** — scalers, encoders, imputers, or feature selection fit on the full dataset
  instead of inside each training fold. Fit on train only; apply to validation/test.
- **Selection leakage** — any choice made by looking at the test set: the threshold, the model, the feature
  set, the early-stopping point, "we tried a few splits." Each one turns test into validation.
- **Label-side problems** are audited separately — see *Label quality* above; the checks above only cover
  features and splits.
- **Red flag:** a metric far better than the baseline or than domain intuition — trace every feature back to
  the prediction time before believing it. Absence of the red flag is not absence of leakage.
