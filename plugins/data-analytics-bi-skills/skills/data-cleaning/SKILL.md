---
name: data-cleaning
description: >-
  Cleans and reshapes messy data into an analysis-ready, tidy form — handling missing values, type
  and format coercion, deduplication, category standardization, and join hygiene — with validation
  at each step and a reproducible, non-destructive workflow. Use when preparing, wrangling, or fixing
  data before analysis or reporting. Triggers: data cleaning, data wrangling, data prep, data
  preparation, missing values, impute, deduplicate, remove duplicates, standardize, normalize
  categories, tidy data, reshape, pivot, join hygiene, fan-out, data quality fix.
---

# Data cleaning

## When to use
- Preparing a raw extract for analysis: fixing types, missing values, duplicates, and inconsistent categories.
- Reshaping data into a tidy structure, or diagnosing why a join is multiplying or dropping rows.
- Making messy data reproducibly analysis-ready without destroying the source.
- Not for: the first-look profiling that tells you *what* is wrong (distributions, missingness scan,
  outlier detection) → see `data-analytics-bi-skills:exploratory-data-analysis`. Run that first; this
  skill fixes what it finds.

## Do it
1. **Profile before you touch anything.** Know the grain, the intended key, column types, and where
   the nulls and bad categories are — reuse the EDA output if you have it
   (`data-analytics-bi-skills:exploratory-data-analysis`). Cleaning blind creates new errors.
2. **Get to tidy structure.** One variable per column, one observation per row, one value per cell.
   Split combined fields, unpivot wide "one column per month" layouts into long form, and give every
   column a single, consistent meaning. Most downstream pain is really a structure problem.
3. **Coerce types and formats.** Parse real dates from text, pull numbers out of `"$1,200"` strings,
   trim whitespace, unify case, and make units consistent (cents vs. dollars, %, kg vs. lb). Do this
   before comparisons and joins, which silently fail on mismatched types.
4. **Standardize categories via a lookup, not ad-hoc replaces.** Map every variant (`NY`, `N.Y.`,
   `New York`) to one canonical value through an explicit mapping table you can review and reuse —
   scattered find-and-replace is unauditable and misses cases.
5. **Handle missing values with a stated strategy.** Choose per column: drop rows, drop the column,
   or impute (mean/median/mode, forward-fill for time series, or model-based) — and know the bias each
   introduces. When you impute, **add a `was_missing` flag** so the fabrication stays visible
   downstream. See `references/cleaning-recipes.md`.
6. **Deduplicate on the real key.** Define what makes two rows the same (exact key vs. fuzzy match on
   name/date), decide which record wins (latest, most complete), and remove the rest. Confirm the key
   is unique afterward.
7. **Practice join hygiene.** Before joining, know each side's cardinality (1:1, 1:many, many:many).
   A many-to-many or an unexpected 1:many **fans out** and multiplies rows, inflating every later sum.
   Compare row counts before and after; aggregate the finer side to the target grain first if needed.
8. **Validate and keep it reproducible.** Re-check row counts, key uniqueness, control totals, and
   value ranges against expectations. Script the steps (SQL/pandas/Power Query) so they re-run on the
   next extract, and **never overwrite the raw source** — clean into a copy.

## Why / learn
"Garbage in, garbage out" is the whole reason this skill exists, but the sharper point is that
**cleaning is analysis**: every decision — which rows to drop, how to fill a gap, which duplicate
wins, how to bucket a category — changes the numbers your conclusion rests on. That's why the
decisions must be *explicit and recorded*, not buried in a one-off edit. **Tidy structure** is the
foundation because analysis tools assume it: one variable per column and one observation per row is
what lets a `GROUP BY`, a pivot, or a join behave predictably; when a join misbehaves, the cause is
almost always a grain or cardinality surprise, not the join itself. **Missing-value handling is where
bias sneaks in** — dropping rows quietly deletes whoever tends to be missing, and mean-imputation
shrinks variance and weakens every correlation, so the honest move is to pick a method that fits *why*
the data is missing and to flag what you fabricated. And you keep the pipeline **reproducible and
non-destructive** because the raw source is your only ground truth; the moment you overwrite it, you
can't check whether a surprising result is real or a cleaning artifact.

## Common mistakes
- Cleaning before profiling → you fix the wrong things and miss the real ones. Profile first (EDA).
- Overwriting the raw file → you lose ground truth and can't audit. Clean into a copy; keep the source.
- Mean-imputing skewed or not-random missing data → biases results toward the middle. Match the method to the mechanism; flag imputed cells.
- Dropping all rows with any null → silently biases the sample and shrinks it. Decide per column, per mechanism.
- Deduping on the wrong key → deletes legitimate rows or keeps true dupes. Define the key explicitly.
- Joining without checking cardinality → fan-out double-counts. Verify 1:1 vs. 1:many; compare row counts.
- One-off find-and-replace for categories → unauditable and incomplete. Use a reusable mapping table.
- Type mismatch on join keys (`'007'` vs. `7`) → rows silently don't match. Coerce types first.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep real data — actual category mappings,
client keys, sample rows — in `your-environment.private.md`, which is git-ignored). Capture your
common source formats and their quirks, your canonical category lookups (states, product codes, entity
names), your tools (SQL, pandas, Power Query, dbt), your key definitions per table, and your standard
validation totals. This skill then applies its generic recipes to your real messes. Use
`data-analytics-bi-skills:exploratory-data-analysis` to decide *what* needs cleaning before you start.

## References
- references/cleaning-recipes.md — tidy-data rules, missing-value strategies and their bias, dedup, and join-fan-out diagnostics
- references/your-environment.md — your sources, category lookups, keys, and validation totals (add when supplied)
