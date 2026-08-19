# Cleaning recipes (reference)

Practical decisions and diagnostics; tool-agnostic, with SQL / pandas equivalents noted.
Method lineage: the structure rules are Wickham's ("Tidy Data", Journal of Statistical
Software, 2014); the missing-data mechanism vocabulary (MCAR/MAR/MNAR) is Rubin's, standard
across the missing-data literature.

## Contents
- [Tidy-data rules](#tidy-data-rules)
- [Type/format normalization](#typeformat-normalization)
- [Category standardization via mapping tables](#category-standardization-via-mapping-tables)
- [Missing-value strategies and their bias](#missing-value-strategies-and-their-bias)
- [Deduplication](#deduplication)
- [Join hygiene and fan-out diagnosis](#join-hygiene-and-fan-out-diagnosis)
- [Validation checklist](#validation-checklist)
- [Pipeline shape: reproducible and non-destructive](#pipeline-shape-reproducible-and-non-destructive)
- [Worked example — merging two request logs](#worked-example--merging-two-request-logs)
- [Sources and attribution notes](#sources-and-attribution-notes)

## Tidy-data rules
1. Each **variable** is a column.
2. Each **observation** is a row.
3. Each **value** is one cell (no `"12, 15"` or `"NY/NJ"` packed into one cell).

Common fixes, named as Wickham names the messes:
- **Column headers are values, not variable names** ("one column per month/region") →
  unpivot into `period, value` (pandas `melt`; SQL `UNPIVOT` or a `UNION ALL` per column).
- **Multiple variables stored in one column** (`"2024-Q1-East"`) → split into their parts.
- **Variables in both rows and columns** (a metric column whose values are metric *names*)
  → pivot the metric names back out to columns.
- **Multiple observational units in one table** (order fields repeated on every line item)
  → separate tables per unit, joined by key.
If a `GROUP BY`, pivot, or join feels awkward, the structure is usually the problem, not the
query.

## Type/format normalization
- Dates: parse to a real date type; state the input format; watch `MM/DD` vs. `DD/MM`; store/compare in one time zone.
- Numbers from text: strip `$ , % ( )`; treat parentheses/`CR` as negatives; watch European `1.234,56`.
- Strings: `TRIM` whitespace, collapse internal doubles, unify case for keys; normalize Unicode/accents if matching.
- Booleans: map `Y/Yes/1/true` → one representation.
- Keys: make join keys the **same type** on both sides (`'007'` ≠ `7` in a join).
- Coerce loudly, not silently: prefer a parse that errors or flags unparseable values
  (pandas `pd.to_numeric(errors='coerce')` + a count of new NaNs) over one that guesses.
- If values were mangled before you ever saw them — leading zeros lost, encoding artifacts,
  columns shifted — the fix belongs at ingest: `data-tools-skills:csv-and-flat-file-wrangling`.

## Category standardization via mapping tables
- Build one **mapping table**: `variant → canonical` (`N.Y.` → `NY`), kept as data (a CSV, a
  lookup sheet, a dbt seed) — reviewable, reusable, versionable.
- Populate it from the data: list distinct values with counts, map the head of the
  distribution explicitly, and route unmapped stragglers to a visible `UNMAPPED` bucket that
  fails validation if it grows.
- Apply by join (SQL `LEFT JOIN mapping`) or pandas `.map()`/`merge` — never by a chain of
  in-place replaces scattered through a script.
- Case- and whitespace-normalize *before* mapping so the table stays small.
- Keep the mapping under review: a new source system means new variants; the `UNMAPPED`
  bucket is the tripwire.

## Missing-value strategies and their bias
| Strategy | When reasonable | Bias / cost |
|---|---|---|
| Drop rows (listwise) | Few missing, missing completely at random (MCAR) | Shrinks sample; skews summaries once missingness is non-random |
| Drop column | Column mostly empty or not usable | Loses a variable |
| Mean/median impute | Numeric, roughly central, low missingness | Shrinks variance; weakens correlations; median safer on skew |
| Mode impute | Categorical | Over-weights the majority class |
| Forward/back fill | Ordered time series | Wrong across regime changes/gaps |
| Model/kNN/regression impute | Missing depends on other columns (MAR) | More work; can leak if done before train/test split |
| Explicit "Unknown" category | Categorical where absence is meaningful | Keeps rows; treat as a real level |

Always add a `was_missing_<col>` flag when imputing, so the fabrication is visible. Classify
the mechanism first (Rubin's taxonomy):
- **MCAR** — missingness unrelated to anything: dropping rows costs sample size and nothing
  else, whatever you go on to compute.
- **MAR** — missingness depends on other *observed* columns (small accounts skip a field):
  model-based imputation using those columns is defensible. Dropping rows is not ruled out here
  either — a model of `y` on those columns, fit on complete cases, stays unbiased as long as the
  missingness does not also depend on `y` itself — but any marginal figure (a mean, a total, a
  rate) read off the survivors is biased, so say which of the two you are doing.
- **MNAR** — missingness depends on the missing value itself (large values withheld): no
  in-data fix is unbiased; say so in the caveats rather than pretending.
For *model* pipelines, imputation must be fit on training data only —
`machine-learning-skills:feature-engineering` owns that discipline.

## Deduplication
- Define the duplicate key first (exact business key, or fuzzy on name+date+amount).
- Decide the survivor rule: latest timestamp, most-complete record, or a priority source.
- Exact: `SELECT DISTINCT` / group by key; keep-one via `ROW_NUMBER() … = 1` (pandas
  `drop_duplicates(subset=…, keep=…)`).
- Fuzzy: block on a cheap key (zip, first letter), then compare within blocks; review before deleting.
- Re-assert key uniqueness after, and count what was removed — "deduped 3,120 rows" is a
  validation fact, not a footnote.

## Join hygiene and fan-out diagnosis
- Establish each side's cardinality: is the join key unique on the left, the right, both, neither?
- **1:1** → row count unchanged. **1:many** → left rows repeat (often intended). **many:many** →
  explosion; almost always a grain error.
- Symptom of fan-out: a `SUM` roughly doubles after adding a join. Diagnose by counting distinct keys
  vs. rows on each side; aggregate the finer table to the target grain in a CTE *before* joining, or
  use `COUNT(DISTINCT …)` — idioms in `data-analytics-bi-skills:sql-for-analysts`.
- `LEFT JOIN` keeps unmatched left rows (nulls on the right); an `INNER` join silently drops them —
  confirm which you want by checking the dropped count.
- Quick assertion before any join: `SELECT key, COUNT(*) FROM side GROUP BY key HAVING COUNT(*) > 1`
  on whichever side you believe is unique (pandas: `df[key].is_unique`).

## Validation checklist
- Row count in vs. out is explainable (you know why it changed, step by step).
- Intended key is unique.
- Control totals (row count, sum of amount) tie to a trusted source.
- Value ranges/domains hold (no impossible negatives, categories all canonical, `UNMAPPED` empty).
- Imputation flags exist for every imputed column; imputed share per column is recorded.
- Steps are scripted and re-runnable; raw source untouched.

## Pipeline shape: reproducible and non-destructive
- **Raw is read-only.** Raw extract lands in one place and is never edited; cleaning writes
  to a new file/table. Raw/processed/output separation and naming conventions:
  `data-tools-skills:data-file-hygiene`.
- **Script, don't click.** SQL, pandas, or Power Query steps that re-run identically on next
  month's extract; script structure and environment pinning:
  `coding-agent-skills:python-for-analysts`.
- **Log the decisions.** Each step prints/records what it changed (rows dropped and why,
  values imputed, duplicates removed) so the run leaves an audit trail.
- **Fail loudly.** Validation checks at the end of the pipeline stop the run rather than
  shipping a silently wrong output.

## Worked example — merging two request logs

Domain-neutral on purpose: the "requests" below are any tracked work items — support
tickets, legal intake, invoice approvals, access requests. **All values are illustrative.**
Goal: one clean table, one row per request, from two systems' exports.

**Profile first** (`data-analytics-bi-skills:exploratory-data-analysis`): System A exports
12,400 rows, one per request, with `req_id` unique; System B exports 9,800 rows covering
8,150 distinct requests — `req_id` duplicates because its grain turns out to be one row per
*status change*. Column `opened` is text
in A (`03/07/2025`) and a real date in B; `priority` holds `H, High, high, P1`; `owner` is
blank in 14% of A's rows.

1. **Tidy structure.** B is collapsed to one row per request (latest status change wins) —
   its grain, not its formatting, was the real problem. A's packed column
   `region_channel` (`"East/Web"`) is split into `region` and `channel`.
2. **Types.** A's `opened` parsed with an explicit format; both systems' timestamps
   normalized to one time zone; `req_id` cast to string on both sides (B zero-pads to 8
   digits — `'00012345'` vs. `12345` would join to nothing).
3. **Categories.** A mapping table for `priority`: `H`→`High`, `high`→`High`, `P1`→`High`,
   `P2`→`Medium`, … Distinct-value counts showed 11 variants for 3 real levels; two
   stragglers land in `UNMAPPED` and get mapped after checking with the source team.
4. **Missing values.** `owner` blank in 14% of A: investigation shows blanks are
   auto-closed requests (MAR — missingness depends on an observed column, `close_type`).
   Decision: impute `owner = 'auto'` as an explicit category, flag `was_missing_owner`,
   and record that owner-level workload stats exclude auto-closed items.
5. **Dedup.** After the union of A and B, 210 requests appear in both systems. Key:
   `req_id`. Survivor rule: the row from the system of record (A), keeping B's extra
   `resolution_code` column via a join instead of a second row.
6. **Join hygiene.** Joining requests to the owner roster: roster has one row per owner per
   *fiscal year* — a 1:many trap. Rosters are filtered to the current year first (making it
   1:1), verified by row counts before/after: 20,340 in, 20,340 out.
7. **Validate.** Final: 20,340 rows — 12,400 from A + 8,150 distinct requests from B − 210
   in both = 20,340; the reconciliation uses B's collapsed request count, never its 9,800
   raw status-change rows. Also verified: `req_id` unique, sum of A's amounts ties to A's
   own export footer total, `UNMAPPED` empty, imputation flags present. The script re-runs
   top to bottom on next month's exports; both raw files sit untouched in `raw/`.

The two decisions that changed downstream numbers — collapsing B's grain and the `owner`
imputation policy — head the **decisions log** delivered with the cleaned file, because a
reader who disagrees with either must be able to see and reverse them.

## Sources and attribution notes
- Wickham, H., "Tidy Data", *Journal of Statistical Software* 59(10), 2014 — the three
  structure rules and the catalogue of common messes.
- Rubin, D. B. — the MCAR/MAR/MNAR missing-data mechanism taxonomy (standard since Rubin
  1976; expositions in Little & Rubin, *Statistical Analysis with Missing Data*).
- Attribution note: the "analysts spend 80% of their time cleaning data" figure circulates
  widely (often via surveys of self-reported time) but has weak provenance as a research
  finding — argue from your own pipeline's history instead of quoting it as established fact.
