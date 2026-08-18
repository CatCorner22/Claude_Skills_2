---
name: supervised-modeling
description: >-
  Builds and interprets supervised regression and classification models — starting with an
  interpretable linear or logistic baseline, then tree ensembles (random forest, gradient boosting /
  XGBoost / LightGBM) — with sensible defaults, regularization, class-imbalance handling, a leakage-safe
  fit/predict pipeline, and honest interpretation of coefficients and feature importance. Use when
  predicting a numeric or categorical outcome from features. Triggers: regression, classification,
  logistic regression, linear regression, random forest, gradient boosting, XGBoost, LightGBM, predict
  a category, predict a number, classifier, feature importance, coefficients.
metadata:
  version: "1.2.0"
---

# Supervised modeling

## When to use
- Predicting a numeric outcome (regression) or a category (classification) from a set of features.
- Choosing between an interpretable linear/logistic model and a tree ensemble, and tuning it sensibly.
- Interpreting a fitted model — reading coefficients or feature importance without over-claiming.
- Not for: framing the problem, target, and baseline in the first place → see `machine-learning-skills:ml-project-framing`. For choosing metrics, cross-validation, and guarding leakage → see `machine-learning-skills:model-evaluation`. For encoding/scaling the inputs → see `machine-learning-skills:feature-engineering`.

## Do it
Algorithm selection by data shape, starting hyperparameters with the reasoning behind each number, a
worked baseline-to-ensemble ladder with the decision to stop, the imbalance thresholds, the failure
envelopes, and how to read coefficients and importances without over-claiming are all in
`references/algorithms-and-interpretation.md`.

1. **Confirm the task type.** Numeric target → **regression**; categorical target → **classification**
   (binary or multiclass). This decides the model family, the loss, and the metrics. If the problem isn't
   framed yet, do `machine-learning-skills:ml-project-framing` first.
2. **Split before you fit anything.** Hold out a test set (by time for temporal data) and keep it
   untouched. Every transform and model decision is made on train/validation only — see
   `machine-learning-skills:model-evaluation`.
3. **Start with an interpretable baseline model.** Fit **linear regression** or **logistic regression**.
   It's fast, hard to overfit, and its coefficients tell a story you can defend to stakeholders. This is
   your reference point; anything more complex must beat it.
4. **Build one clean fit/predict pipeline.** Chain preprocessing (impute → encode → scale) and the model
   in a single pipeline whose transforms are **fit on train only**, so the same steps apply identically
   at predict time and nothing leaks. Encoding/scaling detail lives in `machine-learning-skills:feature-engineering`.
5. **Move to trees/ensembles when linear underfits — one rung at a time, with a stop rule you wrote
   first.** Use a **random forest** for a robust, low-tuning nonlinear model, or **gradient boosting
   (XGBoost/LightGBM)** for top accuracy on tabular data. They capture interactions and nonlinearity linear
   models miss, and need little scaling or encoding fuss. Climb the ladder (baseline → linear → forest →
   boosting → tuned boosting → stack) and **keep a rung only when its validation gain over the best kept
   model exceeds the across-fold standard deviation** — a gain inside the fold noise is not a finding, and
   a rung you keep is a rung you maintain forever. Before judging a family, check its train-vs-validation
   gap: a memorized forest scoring badly is an untuned fit, not a verdict on forests. The reference works
   a six-rung ladder end to end, including the two rungs that get rejected and why.
6. **Regularize to control overfitting.** For linear/logistic use **L2 (ridge)** or **L1 (lasso, which
   also selects features)**. For boosting, limit tree **depth**, use a small **learning rate** with more
   trees, subsample rows/columns, and stop early on a validation metric. Watch the train-vs-validation gap.
7. **Handle class imbalance deliberately.** With rare positives, don't optimize accuracy. Use **class
   weights** first (one argument, no data change, cannot leak), tune the **decision threshold** to the cost
   of errors, and reach for resampling only for a specific symptom — then judge with precision/recall/PR-AUC,
   not accuracy. See `machine-learning-skills:model-evaluation`. The quantity that decides which tactic you
   need is the **absolute count of minority events, not the ratio**: above a few thousand positives only the
   threshold and the metric are broken; below roughly **50** the estimate is what's broken, not the model,
   and comparing models at that size is noise. The reference gives the full threshold table and the
   derivation of the 50.
8. **Interpret honestly, then validate against the baseline.** Read **standardized coefficients** (sign
   and magnitude) for linear/logistic; for trees prefer **permutation importance** and **partial
   dependence** over default impurity importance. Treat all of these as *associations, not causes*, and
   confirm the model actually beats the baseline out of sample before shipping. Each quantity also has a
   specific claim it does **not** support — permutation importance is not what a model retrained without
   the feature would lose, and an odds ratio is not a change in probability. The reference tabulates what
   each one licenses, what it does not, and the check to run before saying it aloud.

**Deliverable — the model summary.** The finished output contains: (1) the task type, target, and
split scheme; (2) the interpretable baseline's out-of-sample score next to the final model's;
(3) the pipeline (ordered steps, transforms fit on train only) and the final hyperparameters;
(4) how imbalance and the decision threshold were handled, if classifying; (5) an interpretation
section saying what the model relies on — worded as association, never cause. The assistant
builds and interprets the models; the human owns the framing, the error costs, and the decision
to ship. `references/algorithms-and-interpretation.md` expands this into the twelve-item contract
a finished summary has to satisfy, including the rungs you rejected and the model's own failure
envelope stated in its own terms.

## Why / learn
The governing principle is **start with an interpretable baseline, and add complexity only when it earns
its keep.** A linear or logistic model is not a throwaway — it is a real model, it rarely overfits, and
its coefficients are a defensible explanation, which matters wherever a prediction has to be defended to
someone who did not build it — an adverse-action notice, a triage rule a clinician overrides, a screening
model an auditor will ask about. You reach for trees and boosting when the linear model demonstrably
underfits (it can't capture the curve or the interaction), and the price you pay is interpretability and a real risk of overfitting that only regularization and honest validation keep
in check. Understanding *why* the families differ helps you choose: linear models assume an additive,
monotone relationship and extrapolate; trees carve the feature space into boxes, capture interactions for
free, but never extrapolate beyond the training range. Interpretation is where people most often fool
themselves — impurity-based feature importance is biased toward high-cardinality and continuous features,
and *every* importance measure describes what the model used, not what causes the outcome. Two correlated
features split their importance; a feature can look unimportant only because a collinear twin absorbed it.
Keep the claim as strong as the evidence: "the model relies on X," not "X drives the outcome."

## Common mistakes
- Reaching for XGBoost first → an unexplainable model you can't defend and can't debug. Start linear/logistic.
- Fitting transforms on all the data before splitting → leakage. Fit the pipeline on train only.
- Optimizing accuracy on imbalanced data → a model that predicts "never" and scores 98%. Use class weights + PR metrics.
- Reading impurity feature importance as truth → biased toward continuous/high-cardinality features. Prefer permutation importance.
- Calling a large coefficient "important" without scaling the features → magnitude reflects units, not effect. Standardize first.
- Interpreting importance/coefficients as causation → they're associations. Say "the model uses," not "X causes."
- Tuning on the test set → optimistic, non-reproducible results. Tune on validation/CV; touch test once.
- Declaring a winner on a gain smaller than the across-fold sd → you shipped noise and now maintain it.
- Comparing two models by whether their marginal confidence intervals overlap → they were scored on the
  same rows, so compare them **paired**; overlapping bands routinely hide a difference a paired test finds.
- Judging a model family from an untuned fit → "the forest didn't help" is usually a memorized forest.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real feature names, sample rows, and target
distributions in `your-environment.private.md`, which is git-ignored): the target and task type, the
feature list and their types, class balance if classifying, your preferred libraries (scikit-learn,
XGBoost, LightGBM), and any interpretability requirement (e.g. a model you must explain to auditors or
risk). This skill then maps its generic steps onto your data and constraints, and defers metric and
validation choices to `machine-learning-skills:model-evaluation`.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/supervised-modeling.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/algorithms-and-interpretation.md — model-family cheat-sheet, starting hyperparameters with the reasoning for each number, a worked six-rung baseline-to-ensemble ladder with the stop decision, when linear genuinely beats an ensemble, imbalance thresholds, interpretation licences and non-licences, failure envelopes, and the twelve-item deliverable contract
- references/your-environment.md — your target, features, class balance, libraries, and interpretability needs (add when supplied)
