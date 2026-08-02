---
name: feature-engineering
description: >-
  Engineers, encodes, scales, and selects model features with transforms fit only on training data so
  nothing leaks from the future or the test set. Covers encoding categoricals (one-hot, target, frequency,
  ordinal), scaling and normalization, datetime and lag/rolling features, aggregations and interactions,
  missing-value handling as information, fit-on-train-only pipelines, and basic feature selection. Use
  when improving model inputs or preparing features for a model. Triggers: feature engineering, features,
  encoding, one-hot, target encoding, frequency encoding, scaling, normalization, standardize, datetime
  features, lag features, rolling features, feature selection, interactions, missing values.
---

# Feature engineering

## When to use
- Preparing raw columns into model-ready features, or improving an existing feature set to lift model quality.
- Encoding categoricals, scaling numerics, building datetime/lag/rolling features, or handling missing values.
- Selecting a smaller, more robust feature set and wiring transforms into a leakage-safe pipeline.
- Not for: choosing the model that consumes the features → see `machine-learning-skills:supervised-modeling`. For validating that features actually help and aren't leaking → see `machine-learning-skills:model-evaluation`.

## Do it
1. **Fit every transform on training data only.** Put encoders, scalers, imputers, and selectors in a
   **pipeline** that is `fit` on the training fold and merely `transform`s validation/test. This one habit
   prevents most leakage — the statistics a transform learns (means, categories, target rates) must come
   only from data the model is allowed to see.
2. **Encode categoricals to match cardinality.** **One-hot** for low-cardinality fields; **ordinal** for
   genuinely ordered categories; **frequency/count** or **target (mean) encoding** for high-cardinality
   fields (merchant, GL account, vendor). Target encoding must be computed **within cross-validation folds**
   (or with smoothing/out-of-fold) or it leaks the label straight into the feature. See `references/transforms-and-leakage.md`.
3. **Scale numerics when the model needs it.** **Standardize** (z-score) or **min-max** for linear, distance,
   and regularized models and anything gradient-based; tree ensembles are scale-invariant and don't need it.
   Fit the scaler on train only. Consider a **log/Box-Cox** transform for heavily skewed monetary values.
4. **Build datetime and lag/rolling features — carefully.** From a timestamp derive day-of-week, month,
   quarter-end, business-day, holiday, and payroll-cycle flags. For time series add **lags** (`y_{t-1}`,
   `y_{t-7}`) and **rolling** stats (trailing mean/std) — but each window may use **only past data relative
   to the row's timestamp**, or you leak the future. This is the most common leak in finance data.
5. **Add aggregations and interactions where the domain suggests them.** Group statistics (per-customer
   average, per-account volatility), ratios (amount ÷ typical amount), and interaction terms can encode real
   structure. Compute aggregates over training rows only, and be wary of stats that peek across the split.
6. **Treat missingness as information.** Impute with a train-fitted rule (median, or a model), and add a
   **"was missing" indicator** — in finance a blank field is often meaningful (no prior history, a skipped
   step), not random noise. Don't drop rows wholesale just to avoid imputing.
7. **Select a smaller, robust feature set.** Remove near-constant, duplicate, and obviously leaky columns
   first; then use **regularization (lasso)**, **permutation importance**, or correlation pruning to cut the
   rest. Fewer well-chosen features generalize better and are far easier to monitor than a wide, noisy matrix.

## Why / learn
Two truths sit under all of this. First, **good features often beat fancier algorithms**: a linear model on
well-constructed features (the right lags, a sensible encoding, a meaningful ratio) routinely outperforms a
heavily tuned boosting model fed raw columns, because you are injecting domain knowledge the algorithm would
otherwise have to discover from limited data. Feature engineering is where your understanding of the business
does its work. Second — the cardinal rule — **never let information from the future or from the test set leak
into a feature.** Leakage is subtle because it usually improves offline scores, which is exactly why it feels
like progress; it is only unmasked when the model meets reality and collapses. The mechanism that keeps you
honest is fitting transforms on the training data alone: a scaler's mean, a target encoder's category rates,
an imputer's fill value, a selector's chosen columns — every one of these is a *statistic learned from data*,
and if it learns from validation/test rows or from future timestamps, the model has effectively seen the
answer. Think of a feature as a question you could genuinely answer at prediction time with only past,
in-sample information; if you couldn't, it isn't a feature, it's a leak.

## Common mistakes
- Fitting a scaler/encoder/imputer on the whole dataset before splitting → leakage. Fit on train inside a pipeline.
- Naive target encoding on the full data → the label leaks into the feature. Encode out-of-fold or with smoothing.
- Rolling/lag features that include the current or future rows → temporal leakage. Use strictly past windows.
- One-hot encoding a 1,000-category field → an explosion of sparse columns. Use frequency/target encoding instead.
- Scaling features for a tree model → wasted effort (trees are scale-invariant); scale for linear/distance models.
- Dropping every row with a missing value → thrown-away signal and bias. Impute + add a missingness indicator.
- Keeping dozens of correlated/near-constant features → noise and instability. Prune and select.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real column names, category lists, and sample
rows in `your-environment.private.md`, which is git-ignored): your categorical fields and their cardinality,
which numerics are skewed, the timestamp columns and the calendar effects that matter (month-end, payroll,
holidays), how missingness arises and what it means, and your preferred pipeline tooling. This skill then maps
its generic transforms onto your columns, and hands the model choice to `machine-learning-skills:supervised-modeling`.

## References
- references/transforms-and-leakage.md — encoding/scaling/datetime/selection recipes and the leakage-safe pipeline pattern
- references/your-environment.md — your columns, cardinalities, calendar effects, and missingness meaning (add when supplied)
