# Cleaning recipes (reference)

Practical decisions and diagnostics. Tool-agnostic; examples note SQL / pandas equivalents.

## Contents
- Tidy-data rules
- Missing-value strategies and their bias
- Type/format normalization
- Deduplication
- Join hygiene and fan-out diagnosis
- Validation checklist

## Tidy-data rules
1. Each **variable** is a column.
2. Each **observation** is a row.
3. Each **value** is one cell (no `"12, 15"` or `"NY/NJ"` packed into one cell).
Common fixes: unpivot "one column per period" into `period, value` (melt/UNPIVOT); split composite
columns; combine multi-row headers into one. If a `GROUP BY`/pivot/join feels awkward, the structure
is usually the problem, not the query.

## Missing-value strategies and their bias
| Strategy | When reasonable | Bias / cost |
|---|---|---|
| Drop rows (listwise) | Few missing, missing completely at random (MCAR) | Shrinks sample; biases if not MCAR |
| Drop column | Column mostly empty or not usable | Loses a variable |
| Mean/median impute | Numeric, roughly central, low missingness | Shrinks variance; weakens correlations; median safer on skew |
| Mode impute | Categorical | Over-weights the majority class |
| Forward/back fill | Ordered time series | Wrong across regime changes/gaps |
| Model/kNN/regression impute | Missing depends on other columns (MAR) | More work; can leak if done before train/test split |
| Explicit "Unknown" category | Categorical where absence is meaningful | Keeps rows; treat as a real level |
Always add a `was_missing_<col>` flag when imputing, so the fabrication is visible. Classify the
mechanism (MCAR / MAR / MNAR) — it decides which methods are honest.

## Type/format normalization
- Dates: parse to a real date type; state the input format; watch `MM/DD` vs. `DD/MM`; store/compare in one time zone.
- Numbers from text: strip `$ , % ( )`; treat parentheses/`CR` as negatives; watch European `1.234,56`.
- Strings: `TRIM` whitespace, collapse internal doubles, unify case for keys; normalize Unicode/accents if matching.
- Booleans: map `Y/Yes/1/true` → one representation.
- Keys: make join keys the **same type** on both sides (`'007'` ≠ `7` in a join).

## Deduplication
- Define the duplicate key first (exact business key, or fuzzy on name+date+amount).
- Decide the survivor rule: latest timestamp, most-complete record, or a priority source.
- Exact: `SELECT DISTINCT` / group by key; keep-one via `ROW_NUMBER() … = 1` (pandas
  `drop_duplicates(subset=…, keep=…)`).
- Fuzzy: block on a cheap key (zip, first letter), then compare within blocks; review before deleting.
- Re-assert key uniqueness after.

## Join hygiene and fan-out diagnosis
- Establish each side's cardinality: is the join key unique on the left, the right, both, neither?
- **1:1** → row count unchanged. **1:many** → left rows repeat (often intended). **many:many** →
  explosion; almost always a grain error.
- Symptom of fan-out: a `SUM` roughly doubles after adding a join. Diagnose by counting distinct keys
  vs. rows on each side; aggregate the finer table to the target grain in a CTE *before* joining, or
  use `COUNT(DISTINCT …)`.
- `LEFT JOIN` keeps unmatched left rows (nulls on the right); an `INNER` join silently drops them —
  confirm which you want by checking the dropped count.

## Validation checklist
- Row count in vs. out is explainable (you know why it changed).
- Intended key is unique.
- Control totals (row count, sum of amount) tie to a trusted source.
- Value ranges/domains hold (no impossible negatives, categories all canonical).
- Steps are scripted and re-runnable; raw source untouched.
