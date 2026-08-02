# Evals — machine-learning-skills:supervised-modeling

## 1. Positive trigger (should load the skill)
> "I have a labeled dataset of customers with features like tenure, average balance, and product count,
> and a flag for who defaulted. I want to predict default. Should I use logistic regression or a random
> forest, and how do I read which features matter?"

Expected: skill loads; confirms it's binary classification; starts with a logistic-regression baseline;
builds a leakage-safe fit/predict pipeline; considers random forest / gradient boosting if linear
underfits; handles the likely class imbalance with weights and threshold tuning; interprets standardized
coefficients and permutation importance with the causation caveat; defers metrics to `model-evaluation`.

## 2. Near-miss (should NOT load this skill)
> "How should I one-hot vs target-encode a 400-category merchant field without leaking the target?"

Expected: this is a feature-encoding question, not model building. The
`machine-learning-skills:feature-engineering` skill should handle it. If this modeling skill loads,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** identifies task type, starts with an interpretable baseline, uses a train-only-fit
  pipeline, escalates to ensembles when justified, regularizes, addresses imbalance, and interprets the
  model with appropriate caveats.
- **Teaches:** explains *why* to start interpretable and add complexity only when it earns its keep, and
  why impurity importance and coefficients are associations, not causes — not just which function to call.
- **Safe:** never fits transforms before splitting, never optimizes accuracy on imbalanced data, and never
  claims feature importance proves causation.
