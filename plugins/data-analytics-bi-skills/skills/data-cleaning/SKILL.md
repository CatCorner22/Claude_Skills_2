---
name: data-cleaning
description: >-
  Cleans and reshapes messy extracts into analysis-ready form on Wickham's tidy-data
  principles (variable per column, observation per row, value per cell): coerces types and
  formats (dates-as-text, currency strings, units), standardizes categories through a
  reusable mapping table, handles missing values per column by missingness mechanism
  (MCAR/MAR/MNAR) with a was_missing flag on anything imputed, deduplicates on a
  defined key with a survivor rule, checks join cardinality so fan-out can't multiply rows,
  and validates counts and control totals in a scripted pipeline that never overwrites the
  raw source. Use when preparing, wrangling, or fixing data before analysis
  or reporting. Triggers: data cleaning, data wrangling, data prep, data preparation,
  missing values, impute, deduplicate, remove duplicates, standardize values, normalize
  categories, tidy data, reshape, pivot, join hygiene, fan-out, data quality fix, dirty
  data, unpivot, inconsistent categories, analysis-ready.
metadata:
  version: "1.4.0"
  source: >-
    The tidy-data structure rules follow Wickham, "Tidy Data", Journal of Statistical
    Software (2014); the missing-data mechanism vocabulary (MCAR/MAR/MNAR) is Rubin's,
    standard in the missing-data literature.
---

# Data cleaning

## When to use
- Preparing a raw extract for analysis: fixing types, missing values, duplicates, and inconsistent categories.
- Reshaping data into a tidy structure, or diagnosing why a join is multiplying or dropping rows.
- Making messy data reproducibly analysis-ready without destroying the source.
- Not for: the first-look profiling that tells you *what* is wrong (distributions, missingness scan,
  outlier detection) → see `data-analytics-bi-skills:exploratory-data-analysis`. Run that first; this
  skill fixes what it finds.
- Not for: file-level ingest problems — encodings, delimiters, BOMs, trailing footers, files that
  parse into the wrong columns → `data-tools-skills:csv-and-flat-file-wrangling` gets the file read
  correctly; this skill starts once the data is loaded.
- Not for: preparing *model* features — encoding, scaling, and leakage-safe imputation fit on
  training data only → `machine-learning-skills:feature-engineering`. The seam: this skill produces
  a trustworthy dataset; that one turns it into model inputs without leaking the future.

## Do it
1. **Profile before you touch anything.** Know the grain, the intended key, column types, and where
   the nulls and bad categories are — reuse the EDA output if you have it
   (`data-analytics-bi-skills:exploratory-data-analysis`). Cleaning blind creates new errors.
2. **Get to tidy structure.** One variable per column, one observation per row, one value per cell
   (Wickham's tidy-data rules). Split combined fields, unpivot wide "one column per month" layouts
   into long form, and give every column a single, consistent meaning. Most downstream pain is really
   a structure problem.
3. **Coerce types and formats.** Parse real dates from text, pull numbers out of `"$1,200"` strings,
   trim whitespace, unify case, and make units consistent (cents vs. dollars, %, kg vs. lb). Do this
   before comparisons and joins, which silently fail on mismatched types. If the mangling happened at
   parse time (lost leading zeros, encoding artifacts), fix the ingest instead —
   `data-tools-skills:csv-and-flat-file-wrangling`.
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
   Compare row counts before and after; aggregate the finer side to the target grain first if needed —
   the SQL idioms (pre-aggregating CTEs, `COUNT(DISTINCT …)` diagnostics) are in
   `data-analytics-bi-skills:sql-for-analysts`.
8. **Validate and keep it reproducible.** Re-check row counts, key uniqueness, control totals, and
   value ranges against expectations. Script the steps so they re-run on the next extract — clean,
   rerunnable analysis code per `coding-agent-skills:python-for-analysts` — and **never overwrite the
   raw source**: clean into a copy, with raw/processed/output kept separate per
   `data-tools-skills:data-file-hygiene`.

**Deliverable — three artifacts, not just a file.** (1) The **cleaned dataset**, written beside an
untouched raw source. (2) The **script** that produced it, re-runnable top to bottom on next
period's extract. (3) A short **decisions log**: for each column touched, what was changed and on
what rule — the mapping table used, the imputation method and its `was_missing` flag, the dedup key
and survivor rule, rows in vs. rows out with the reason for every difference, and the control totals
that tied. The log exists because a reader who disagrees with a cleaning decision must be able to
find and reverse it; a clean file with no log is an assertion, not a result.

## Why / learn
"Garbage in, garbage out" is the whole reason this skill exists, but the sharper point is that
**cleaning is analysis**: every decision — which rows to drop, how to fill a gap, which duplicate
wins, how to bucket a category — changes the numbers your conclusion rests on. That's why the
decisions must be *explicit and recorded*, not buried in a one-off edit. **Tidy structure** is the
foundation because analysis tools assume it: Wickham's observation ("Tidy Data", Journal of
Statistical Software, 2014) is that one variable per column and one observation per row is the shape
every `GROUP BY`, pivot, and join is built to expect, which is why messy structure surfaces as
mysterious query pain; when a join misbehaves, the cause is almost always a grain or cardinality
surprise, not the join itself. **Missing-value handling is where bias sneaks in** — dropping rows
quietly deletes whoever tends to be missing, and mean-imputation shrinks variance and weakens every
correlation, so the honest move is to pick a method that fits *why* the data is missing (Rubin's
MCAR/MAR/MNAR distinction) and to flag what you fabricated. And you keep the pipeline **reproducible
and non-destructive** because the raw source is your only ground truth; the moment you overwrite it,
you can't check whether a surprising result is real or a cleaning artifact.

## Common mistakes
- Cleaning before profiling → you fix the wrong things and miss the real ones. Profile first (EDA).
- Overwriting the raw file → you lose ground truth and can't audit. Clean into a copy; keep the source.
- Mean-imputing skewed or not-random missing data → biases results toward the middle. Match the method to the mechanism; flag imputed cells.
- Dropping all rows with any null → silently biases the sample and shrinks it. Decide per column, per mechanism.
- Deduping on the wrong key → deletes legitimate rows or keeps true dupes. Define the key explicitly.
- Joining without checking cardinality → fan-out double-counts. Verify 1:1 vs. 1:many; compare row counts.
- One-off find-and-replace for categories → unauditable and incomplete. Use a reusable mapping table.
- Type mismatch on join keys (`'007'` vs. `7`) → rows silently don't match. Coerce types first.
- Citing "analysts spend 80% of their time cleaning data" as established research → it's a
  widely repeated figure with weak provenance. Make the case from your own pipeline's history.

## Tailor to your environment
Wire in your current role here — the recipes are deliberately domain-neutral, and the same moves
clean an analyst's revenue extract, an attorney's matter export, an ops manager's ticket dump, or a
developer's event log, wherever you work next. Record your setup in
`references/your-environment.md` (keep real data — actual category mappings, client keys, sample
rows — in `your-environment.private.md`, which is git-ignored). Capture your common source formats
and their quirks, your canonical category lookups, your tools (SQL, pandas, Power Query, dbt), your
key definitions per table, and your standard validation totals. Use
`data-analytics-bi-skills:exploratory-data-analysis` to decide *what* needs cleaning before you start.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/data-cleaning.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/cleaning-recipes.md — tidy-data rules, type coercion, mapping-table category
  standardization, missing-value strategies and their bias, dedup, join-fan-out diagnostics, the
  validation checklist, and a worked domain-neutral example (merging two messy request logs)
- references/your-environment.md — your sources, category lookups, keys, and validation totals
  (sanitized stub; live detail goes in the `.private.md` twin)
