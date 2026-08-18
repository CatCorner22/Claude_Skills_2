---
name: model-evaluation
description: >-
  Chooses the right metric and validation scheme for a model, guards against data leakage and
  overfitting, and compares every result against a baseline. Covers train/validation/test discipline,
  k-fold and time-series cross-validation, regression metrics (RMSE/MAE/R²) versus classification
  metrics (precision/recall/F1, ROC AUC vs PR AUC, calibration), confusion-matrix reading and
  threshold choice made on validation and tied to error costs, a confidence interval on the reported
  metric, performance by slice, label-quality checks, and the common sources of leakage. Use when
  validating any model or picking a metric or decision threshold. Triggers: model evaluation, evaluate
  a model, cross-validation, k-fold, overfitting, underfitting, ROC AUC, precision recall, PR AUC,
  RMSE, R2, data leakage, train test split, confusion matrix, threshold, calibration, subgroup
  performance, slice evaluation, label quality.
metadata:
  version: "1.3.0"
---

# Model evaluation

## When to use
- Deciding how to validate a model (holdout vs k-fold vs time-series CV) and which metric to report.
- Diagnosing overfitting/underfitting, choosing a decision threshold, or reading a confusion matrix.
- Running the leakage checklist on any evaluation (routinely, not only when results look "too good"), putting an interval on the reported metric, breaking performance down by slice, or comparing a model to its baseline.
- Not for: framing the target and picking the decision metric conceptually up front → see `machine-learning-skills:ml-project-framing`. For time-series-specific backtesting mechanics → see `machine-learning-skills:time-series-forecasting`. For qualifying the label/judgment process the metric is scored against — inter-rater agreement, attribute-agreement studies, Gage R&R → see `continuous-improvement-skills:measurement-systems-analysis`.
- Not for: what happens after the model ships — serving it, versioning responses, and
  detecting training/serving skew or drift in production → see
  `full-stack-dev-skills:ml-in-production` (a separate plugin). Offline metrics say whether
  it *was* good; that skill says whether it still is.

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
4. **Set the threshold on validation, then freeze it.** A probability model doesn't decide at 0.5 by law —
   it decides at the threshold that minimizes *your* cost of false positives vs false negatives. Build the
   confusion matrix at candidate thresholds **on the validation set (or inside each CV fold)**, pick the
   one that matches the business cost, then score the test set **once** at that frozen threshold. The
   threshold is a fitted parameter like any other: choose it on test and the reported precision/recall is
   optimistic, which is the same mistake as tuning hyperparameters on test.
5. **Compare against the baseline — always.** Report the naive/seasonal-naive/majority-class/current-rule
   score next to the model. An R² of 0.6 or an AUC of 0.8 means nothing until you know the baseline; "skill"
   is the *lift over baseline*, not the raw number.
6. **Diagnose overfit vs underfit.** Compare train and validation scores: a big gap (great on train, poor on
   validation) is **overfitting** → regularize, simplify, get more data; both poor is **underfitting** → a
   richer model or better features. Learning curves make the diagnosis visual.
7. **Run the leakage checklist every time — not only when results look too good.** Walk the whole list on
   every evaluation and write down what each check found: target leakage, train/test contamination,
   temporal leakage, group leakage, preprocessing fit on the full dataset. Trace every feature and every
   preprocessing step back to the prediction time and the split. A "too good" score escalates the hunt;
   it is not what starts it, because leakage that lands on a *plausible* score is the leakage that ships.
   The checklist is in `references/metrics-and-leakage.md`.
8. **Put an uncertainty band on the headline number.** A single point estimate hides how much of it is
   test-set luck. Report a confidence interval: a binomial interval for a rate (precision, recall,
   accuracy), a bootstrap over test rows for AUC, RMSE, or any composite. Ask whether the test set is big
   enough — for a rare positive class the sample size that matters is the **count of positives**, not the
   row count, so 40 positives put roughly ±12 points on a recall of 80% (worked in the reference). If a
   claimed improvement is smaller than that band, you have not measured an improvement.
9. **Score the slices that matter, not just the average.** Break the metric down by the segments the
   decision touches — region, channel, product line, customer tenure, device, time period, and any
   protected or contractually sensitive group. Report the per-slice metric *with its own n*, and flag any
   slice whose score sits materially below the aggregate. An average is a weighted blend that can hide a
   segment where the model is worse than the baseline; that segment is where deployment fails first.
10. **Audit label quality before blaming the model.** Ask how the target was produced, by whom, and with
   what disagreement rate — a label is a measurement, not a fact. Human-reviewed or LLM-judged labels
   need agreement evidence (repeat judgments, a reference set, kappa) before their errors get charged to
   the model; a metric cannot resolve differences smaller than the noise in its own labels. Re-review a
   sample of the model's confident "errors": some of them are the labels being wrong. Run the study in
   `continuous-improvement-skills:measurement-systems-analysis` (attribute-agreement / Gage R&R).

**Deliverable — the evaluation report.** The finished output states: (1) the split/validation
scheme and why it fits the data (IID / temporal / grouped); (2) the metric and the decision it
proxies; (3) baseline vs model scores side by side, with the lift; (4) the chosen threshold, the
split it was chosen on, and the FP/FN costs behind it (classification); (5) the overfit/underfit
diagnosis from the train-vs-validation gap; (6) the leakage checklist with what each check found
(run every time, not only on suspicious results); (7) a confidence interval on the headline
metric plus the effective sample size behind it (positives, not rows); (8) the metric by slice
with per-slice n, and any slice below the aggregate called out; (9) where the labels came from
and what is known about their error rate. The assistant drafts the report; the human owns the
error costs and the ship/no-ship decision.

## Why / learn
Two ideas do the heavy lifting: **the metric must match the decision, and leakage is the silent killer of
"great" offline results.** A metric is a proxy for the cost of being wrong; pick the wrong proxy and you
will optimize hard in the wrong direction — a 99%-accurate fraud model that never catches fraud is the
canonical example, because accuracy is the wrong proxy when positives are 1% of the data (there, precision,
recall, and PR AUC are what track the decision).

**ROC AUC is prevalence-invariant, and that is exactly the problem.** It is worth getting the mechanism
right, because the wrong story leads to wrong predictions about your own experiments. TPR = TP/(TP+FN) is
computed entirely within the positives; FPR = FP/(FP+TN) entirely within the negatives; TNR = 1 − FPR
likewise. Class balance moves none of them, so AUC — the probability the model ranks a random positive
above a random negative — depends only on the two score distributions and *not* on their mixing
proportion. Duplicate every negative ten times and AUC is unchanged. What imbalance destroys is
**precision**, because precision mixes the classes: a small FPR multiplied by a huge negative count still
produces far more false positives than there are true positives. At 1% positives, a threshold with TPR
0.80 and FPR 0.05 yields 800 true positives against 4,950 false ones — precision 13.9%, so ~86% of the
alert queue is noise, while AUC sits comfortably high. Balance that same test set by downsampling
negatives and precision jumps to 94% with AUC untouched. So prefer **PR AUC** when positives are scarce
not because ROC AUC is "inflated by true negatives" — it isn't — but because PR AUC is prevalence-*aware*
and therefore tracks the operational reality you will live with. The corollary is the practically useful
one: resampling to "fix imbalance" will not move your AUC, and any precision you gain from it is an
artifact of the new class ratio, not of a better model. (The ROC-vs-PR comparison is usually attributed to
Davis & Goadrich 2006 and Saito & Rehmsmeier 2015 — pointers to check before quoting, not sources for any
number here; every figure above is computed from its own stated inputs.)

Threshold choice is where evaluation meets economics: the model outputs a score, but the *decision* is a
threshold, and the right threshold is wherever the marginal cost of a false positive equals the marginal
cost of a false negative — almost never 0.5. That threshold is *fitted*, so it belongs on validation; a
threshold read off the test set turns the test set into a tuning set and the reported operating point into
a best case. Leakage is insidious precisely because it makes everything look wonderful: the model "knows"
the answer through a feature or a split that won't exist in production, so offline metrics soar and live
performance collapses. The habit that protects you is mechanical — split first, fit every transform on
train only, anchor every feature to the prediction time, and never let the test set influence a single
decision until the end. And always, always compare to a baseline, because a number without a reference
point is not evidence of anything.

Three things finish an honest report. **Uncertainty:** every metric is a statistic computed on a finite
sample, so it has a standard error; with a rare positive class the sample that matters is the positives,
and two models separated by less than that band are not distinguishable. **Slices:** the aggregate is a
weighted average, and averages conceal — the segment where your model is worse than the current rule is
invisible in the headline and obvious in production. **Labels:** the target is a measurement produced by
some process (a reviewer, a rule, a downstream system, a judge model), and no metric can be more accurate
than the labels it is scored against; when reviewers disagree with each other, part of every "error" you
are charging to the model is really disagreement in the ground truth.

## Common mistakes
- Random split on temporal or grouped data → future/entity leaks into training. Split by time or by group.
- Reporting accuracy on imbalanced data → hides a useless model. Use precision/recall/F1 and PR AUC.
- Deciding at the default 0.5 threshold → ignores error costs. Set the threshold from the FP/FN cost trade-off.
- No baseline → the metric is uninterpretable. Always show the naive/majority-class score alongside.
- Fitting scalers/encoders/imputers on the whole dataset → preprocessing leakage. Fit inside the train fold only.
- Tuning hyperparameters on the test set → optimistic, non-reproducible. Tune on validation/CV; touch test once.
- Picking the decision threshold on the test set → the threshold is a fitted parameter; the reported operating point is a best case. Choose it on validation, freeze it, score test once.
- Trusting a suspiciously high score → usually leakage. Trace features back to the prediction time before celebrating.
- Hunting leakage only when the score looks too good → leakage that lands on a plausible number ships. Run the checklist every time and record what it found.
- Explaining ROC AUC's imbalance problem as "the negative class inflates the true-negative rate" → false; TPR/FPR/TNR are within-class rates and AUC is prevalence-invariant. It is *precision* that collapses.
- Reporting a bare point estimate → give a CI, and check the effective n (positives, not rows). A gain inside the band is not a gain.
- Reporting only the aggregate metric → an average hides the slice where the model underperforms its own baseline. Score by segment with per-slice n.
- Treating labels as ground truth → labels are measurements with an error rate. Get agreement evidence, and re-review a sample of confident "errors."

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real cost figures, label rates, and sample rows
in `your-environment.private.md`, which is git-ignored): whether your data is IID / temporal / grouped, your
class balance, the business cost of a false positive vs a false negative, the metric your decision actually
cares about, your baseline, the slices your decision touches, and where your labels come from. This skill
then maps its generic guidance onto your problem. For the conceptual choice of metric during problem
framing, start at `machine-learning-skills:ml-project-framing`; to qualify the labelling or judging process
itself, run `continuous-improvement-skills:measurement-systems-analysis`.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/model-evaluation.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/metrics-and-leakage.md — metric definitions, ROC-vs-PR with the prevalence arithmetic, calibration, threshold selection on validation, confidence intervals on a metric, slice evaluation, label quality, and the leakage checklist
- references/your-environment.md — your data type, class balance, error costs, metric, baseline, slices, and label source (add when supplied)
