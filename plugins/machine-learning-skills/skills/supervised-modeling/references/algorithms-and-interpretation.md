# Algorithms, defaults, and interpretation (reference)

## Contents
- Model-family cheat-sheet
- Sensible starting hyperparameters
- Class-imbalance tactics
- Interpretation — coefficients and feature importance (with caveats)

## Model-family cheat-sheet
| Family | Strengths | Watch out for | Reach for when |
|---|---|---|---|
| **Linear / logistic regression** | Fast, interpretable, hard to overfit, extrapolates | Assumes additive, monotone effects; needs encoding/scaling | Always — as the baseline; when explanation matters |
| **Regularized linear (ridge/lasso/elastic-net)** | Controls overfit; lasso selects features | Still linear in the features you give it | Many features, collinearity, want sparsity |
| **Random forest** | Robust, low tuning, captures interactions, little preprocessing | Larger models; biased default importances | A strong nonlinear baseline with minimal fuss |
| **Gradient boosting (XGBoost/LightGBM/CatBoost)** | Top tabular accuracy | Overfits without care; more tuning | You need the best accuracy on tabular data |

Trees split the feature space into boxes: they capture interactions for free and need little scaling, but
they **cannot extrapolate** beyond the training range — a forecast of a value larger than anything seen is
impossible. Linear models extrapolate but assume the straight-line (or log-odds-linear) relationship holds.

## Sensible starting hyperparameters
- **Logistic/linear:** standardize features; ridge (L2) by default; lasso (L1) if you want feature selection;
  tune the regularization strength by cross-validation.
- **Random forest:** a few hundred trees; `max_features` ≈ sqrt(#features) for classification; let trees grow
  fairly deep; more trees only help (never hurt) accuracy, just cost time.
- **Gradient boosting:** small **learning rate** (0.01–0.1) with **more trees**; shallow trees (depth 3–8);
  **subsample** rows and columns (0.7–0.9); **early-stop** on a validation metric. Lower learning rate +
  early stopping is the safest overfitting control.

## Class-imbalance tactics
- **Class weights** (`class_weight='balanced'` / `scale_pos_weight`) — cheapest first move; reweights the loss.
- **Threshold tuning** — move the decision threshold off 0.5 to the point that matches the cost of FP vs FN.
- **Resampling** — oversample the minority (e.g. SMOTE) or undersample the majority; fit resampling **inside**
  cross-validation folds, never before splitting, or you leak.
- Judge with **precision/recall/F1 and PR-AUC**, not accuracy. See `machine-learning-skills:model-evaluation`.

## Interpretation — coefficients and feature importance (with caveats)
- **Linear coefficients:** sign = direction; magnitude is comparable across features **only after
  standardizing** them. In logistic regression a coefficient is a change in **log-odds**; exponentiate for
  an **odds ratio**.
- **Impurity (Gini/gain) importance:** fast but **biased** toward high-cardinality and continuous features,
  and computed on training data. Don't trust it as the final word.
- **Permutation importance:** shuffle one feature and measure the drop in a validation metric — model-agnostic
  and honest about predictive contribution. Prefer it.
- **Partial dependence / ICE:** shows the shape of a feature's effect (holding others fixed). Good for
  communicating *how* a feature moves the prediction.
- **SHAP:** consistent per-prediction attributions; useful for local explanations, at extra compute cost.
- **The universal caveat:** all of these describe what the *model* uses, not what *causes* the outcome.
  Correlated features share/split their importance; importance is not causation. Keep claims proportionate.
