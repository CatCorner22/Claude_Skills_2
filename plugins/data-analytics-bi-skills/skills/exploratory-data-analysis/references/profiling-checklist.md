# Data profiling checklist (reference)

Work top to bottom on any new dataset. Compute these regardless of tool (SQL, pandas, Excel, BI).

## Contents
- Dataset level
- Per-column: numeric
- Per-column: categorical / text
- Per-column: date/time
- Pairwise / relationships
- Outlier rules of thumb
- Missingness triage

## Dataset level
- Row count, column count.
- **Grain:** what one row represents; test the candidate key for uniqueness (duplicate keys = wrong grain).
- Column data types vs. meaning (dates-as-text, IDs-as-int, booleans-as-strings).
- Time span covered and any gaps (missing months/days).
- Duplicate whole-row check.

## Per-column: numeric
- Count non-null, count/percent missing.
- **Central tendency:** mean and median — compare them (mean ≫ median ⇒ right-skew).
- **Spread:** standard deviation, min, max, quartiles (Q1/Q2/Q3), IQR.
- Count of zeros and negatives (are negatives valid?).
- Histogram + boxplot to see shape and tails.

## Per-column: categorical / text
- Number of distinct values (cardinality); a huge cardinality on a supposed category is a red flag.
- Top-N value frequencies; size of the long tail.
- Inconsistent encodings of the same thing (`Y/Yes/1`, `NY/N.Y./New York`, trailing spaces, case).
- Unexpected levels, blank strings vs. true NULL.

## Per-column: date/time
- Min and max (any future dates? any epoch-zero / 1900 placeholders?).
- Granularity (day vs. timestamp), time zone, DST artifacts.
- Completeness across the expected calendar (missing periods).

## Pairwise / relationships
- Numeric–numeric: correlation matrix (Pearson for linear, Spearman for monotonic) + scatter for key pairs.
- Categorical–categorical: cross-tab (contingency table); watch for empty cells.
- Numeric–categorical: group-by summary (mean/median/count per level); boxplot by group.
- Sanity: do relationships match domain expectations, or is something surprising (and why)?

## Outlier rules of thumb
- **IQR fence:** below `Q1 − 1.5·IQR` or above `Q3 + 1.5·IQR`.
- **Z-score:** `|(x − mean)/SD| > 3` (only meaningful when roughly symmetric).
- Always investigate before acting: genuine extreme, unit error (cents vs. dollars), or typo?

## Missingness triage
- Quantify per column (%) and per row (rows with many nulls).
- Classify the mechanism: **MCAR** (random), **MAR** (depends on other observed columns),
  **MNAR** (depends on the missing value itself). MNAR/MAR bias naive row-dropping and mean-imputation.
- Decide and *record* the handling — this is the input to `data-analytics-bi-skills:data-cleaning`.
