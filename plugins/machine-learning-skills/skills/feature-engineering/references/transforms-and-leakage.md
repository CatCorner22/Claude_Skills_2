# Transforms and leakage-safe pipelines (reference)

## Contents
- Encoding categoricals
- Scaling and transforming numerics
- Datetime, lag, and rolling features
- Missing values
- Feature selection
- The leakage-safe pipeline pattern

## Encoding categoricals
| Method | Best for | Leakage / caveat |
|---|---|---|
| **One-hot** | Low cardinality (≤ ~15 levels) | Column explosion at high cardinality |
| **Ordinal** | Genuinely ordered categories (ratings, tiers) | Don't impose order on nominal fields |
| **Frequency / count** | High cardinality | Ties value to how common a level is; usually leak-safe |
| **Target (mean) encoding** | High cardinality with signal (merchant, GL account) | **Leaks the label unless done out-of-fold / smoothed** |

Target encoding done right: compute the category's target mean **out-of-fold** (or with additive smoothing
toward the global mean, and add noise) so a row is never encoded using its own label. Fit the encoding map on
training folds only and apply it to validation/test; unseen categories fall back to the global mean.

## Scaling and transforming numerics
- **Standardize** (z-score) for linear/logistic, SVM, k-NN, PCA, and regularized models; **min-max** when you
  need a bounded range. **Trees/boosting are scale-invariant** — skip scaling for them.
- **Log or Box-Cox** for right-skewed monetary amounts (balances, invoice values) to tame heavy tails; keep
  the transform in the pipeline so it applies identically at predict time.
- Fit every scaler on the **training fold only**.

## Datetime, lag, and rolling features
- From a timestamp: year, month, day-of-week, day-of-month, quarter, is-month-end, is-business-day,
  is-holiday, days-to/from-payroll, week-of-year. Encode cyclical fields (month, weekday) as sin/cos if the
  model is linear.
- **Lags:** `y_{t-1}`, `y_{t-7}`, `y_{t-28}` — the value some fixed number of periods back.
- **Rolling stats:** trailing mean/std/min/max over a window ending **strictly before** the current row.
- **Temporal-leakage rule:** any window or lag may use only rows with timestamps **before** the row being
  featured. Compute rolling features in time order; never center a window on the current point or include future rows.

## Missing values
- Impute with a **train-fitted** rule: median (robust) for numerics, a constant/"missing" category for
  categoricals, or a model-based imputer.
- Add a **binary missingness indicator** per field that is missing-not-at-random — in finance a blank often
  means "no history" or "step skipped," which is signal.
- Avoid dropping rows with missing values wholesale; it discards data and can bias the sample.

## Feature selection
1. **Remove the obvious:** near-constant, duplicate, ID-like, and leaky columns (anything derived from or
   posterior to the target).
2. **Regularize:** lasso (L1) drives weak coefficients to zero and selects features.
3. **Rank honestly:** permutation importance on a validation set; prune correlated pairs (keep one).
4. Prefer a small, stable set — easier to validate, monitor, and explain than a wide noisy matrix.

## The leakage-safe pipeline pattern
- Put **all** learned transforms (impute → encode → scale → select) plus the model in **one pipeline**.
- **Split first**, then `fit` the pipeline on the training fold; `transform` validation/test with the fitted pipeline.
- In cross-validation, the whole pipeline is re-fit **inside each fold** — including target encoding,
  imputation, and selection — so no fold ever learns from another. See `machine-learning-skills:model-evaluation`.
