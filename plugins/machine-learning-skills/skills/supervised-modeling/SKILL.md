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
---

# Supervised modeling

## When to use
- Predicting a numeric outcome (regression) or a category (classification) from a set of features.
- Choosing between an interpretable linear/logistic model and a tree ensemble, and tuning it sensibly.
- Interpreting a fitted model — reading coefficients or feature importance without over-claiming.
- Not for: framing the problem, target, and baseline in the first place → see `machine-learning-skills:ml-project-framing`. For choosing metrics, cross-validation, and guarding leakage → see `machine-learning-skills:model-evaluation`. For encoding/scaling the inputs → see `machine-learning-skills:feature-engineering`.

## Do it
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
5. **Move to trees/ensembles when linear underfits.** Use a **random forest** for a robust, low-tuning
   nonlinear model, or **gradient boosting (XGBoost/LightGBM)** for top accuracy on tabular data. They
   capture interactions and nonlinearity linear models miss, and need little scaling or encoding fuss.
6. **Regularize to control overfitting.** For linear/logistic use **L2 (ridge)** or **L1 (lasso, which
   also selects features)**. For boosting, limit tree **depth**, use a small **learning rate** with more
   trees, subsample rows/columns, and stop early on a validation metric. Watch the train-vs-validation gap.
7. **Handle class imbalance deliberately.** With rare positives, don't optimize accuracy. Use **class
   weights**, tune the **decision threshold** to the cost of errors, and consider resampling — then judge
   with precision/recall/PR-AUC, not accuracy. See `machine-learning-skills:model-evaluation`.
8. **Interpret honestly, then validate against the baseline.** Read **standardized coefficients** (sign
   and magnitude) for linear/logistic; for trees prefer **permutation importance** and **partial
   dependence** over default impurity importance. Treat all of these as *associations, not causes*, and
   confirm the model actually beats the baseline out of sample before shipping.

## Why / learn
The governing principle is **start with an interpretable baseline, and add complexity only when it earns
its keep.** A linear or logistic model is not a throwaway — it is a real model, it rarely overfits, and
its coefficients are a defensible explanation, which matters enormously in finance where a black box that
holds a payment or flags a customer has to be justifiable. You reach for trees and boosting when the
linear model demonstrably underfits (it can't capture the curve or the interaction), and the price you
pay is interpretability and a real risk of overfitting that only regularization and honest validation keep
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

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real feature names, sample rows, and target
distributions in `your-environment.private.md`, which is git-ignored): the target and task type, the
feature list and their types, class balance if classifying, your preferred libraries (scikit-learn,
XGBoost, LightGBM), and any interpretability requirement (e.g. a model you must explain to auditors or
risk). This skill then maps its generic steps onto your data and constraints, and defers metric and
validation choices to `machine-learning-skills:model-evaluation`.

## References
- references/algorithms-and-interpretation.md — model-family cheat-sheet, default hyperparameters, imbalance tactics, and interpretation caveats
- references/your-environment.md — your target, features, class balance, libraries, and interpretability needs (add when supplied)
