# Data profiling checklist (reference)

Work top to bottom on any new dataset; compute these regardless of tool (SQL, pandas,
Excel, BI). Method lineage: the exploratory stance is Tukey's (*Exploratory Data Analysis*,
1977 — exploration as a discipline prior to and distinct from confirmatory statistics); the
plot-before-trusting-summaries demonstration is Anscombe's quartet ("Graphs in Statistical
Analysis", *The American Statistician*, 1973).

## Contents
- [The stance: exploratory before confirmatory](#the-stance-exploratory-before-confirmatory)
- [Dataset level](#dataset-level)
- [Per-column: numeric](#per-column-numeric)
- [Per-column: categorical / text](#per-column-categorical--text)
- [Per-column: date/time](#per-column-datetime)
- [Pairwise / relationships](#pairwise--relationships)
- [Outlier rules of thumb](#outlier-rules-of-thumb)
- [Missingness triage](#missingness-triage)
- [The data-quality memo template](#the-data-quality-memo-template)
- [Worked example — first contact with an activity extract](#worked-example--first-contact-with-an-activity-extract)
- [Tool notes](#tool-notes)
- [Sources and attribution notes](#sources-and-attribution-notes)

## The stance: exploratory before confirmatory
Tukey's distinction, kept operational:
- **Exploration** looks for structure, surprises, and problems — it is allowed to chase
  anything, and its findings are *hypotheses and caveats*, not conclusions.
- **Confirmation** tests a stated hypothesis on its own terms —
  `data-analytics-bi-skills:statistical-inference` — and is weakened every time the same
  data that suggested a pattern is also used to certify it.
Practical consequences: record what you looked at (a pattern found after checking forty
pairs is weaker than one predicted in advance); let plots veto statistics (the quartet);
and write the memo even when "nothing interesting" appeared — grain, missingness, and
validity findings are the deliverable, not a by-product.

## Dataset level
- Row count, column count.
- **Grain:** what one row represents; test the candidate key for uniqueness (duplicate keys = wrong grain).
- Column data types vs. meaning (dates-as-text, IDs-as-int, booleans-as-strings).
- Time span covered and any gaps (missing months/days).
- Duplicate whole-row check.
- Provenance: who produced the extract, when, from what system, with what filters already
  applied — a "complete" file that was pre-filtered upstream lies silently.

## Per-column: numeric
- Count non-null, count/percent missing.
- **Central tendency:** mean and median — compare them (mean ≫ median ⇒ right-skew).
- **Spread:** standard deviation, min, max, quartiles (Q1/Q2/Q3), IQR.
- Count of zeros and negatives (are negatives valid?).
- Histogram + boxplot to see shape and tails.
- Suspicious spikes: a mass at exactly 0, 999, or a round cap often marks sentinel values
  or system limits, not data.
- Formal definitions and robust alternatives (median, IQR, MAD when outliers distort):
  `data-analytics-bi-skills:descriptive-statistics`.

## Per-column: categorical / text
- Number of distinct values (cardinality); a huge cardinality on a supposed category is a red flag.
- Top-N value frequencies; size of the long tail.
- Inconsistent encodings of the same thing (`Y/Yes/1`, `NY/N.Y./New York`, trailing spaces, case).
- Unexpected levels, blank strings vs. true NULL (they count differently everywhere).
- Free-text masquerading as a category (notes typed into a code field).

## Per-column: date/time
- Min and max (any future dates? any epoch-zero / 1900 placeholders?).
- Granularity (day vs. timestamp), time zone, DST artifacts.
- Completeness across the expected calendar (missing periods).
- Impossible orderings across columns (closed before opened; shipped before ordered).

## Pairwise / relationships
- Numeric–numeric: correlation matrix (Pearson for linear, Spearman for monotonic) + scatter for key pairs.
- Categorical–categorical: cross-tab (contingency table); watch for empty cells.
- Numeric–categorical: group-by summary (mean/median/count per level); boxplot by group.
- Sanity: do relationships match domain expectations, or is something surprising (and why)?
- A surprising relationship is a *lead*, not a result — testing it so it generalizes is
  confirmatory work (`data-analytics-bi-skills:statistical-inference`).

## Outlier rules of thumb
- **IQR fence:** below `Q1 − 1.5·IQR` or above `Q3 + 1.5·IQR`.
- **Z-score:** `|(x − mean)/SD| > 3` (only meaningful when roughly symmetric).
- Always investigate before acting: genuine extreme, unit error (cents vs. dollars), or typo?
  The three cases get three different treatments — keep, convert, correct.
- These are univariate screens. Points that are only anomalous in combination (a normal
  amount at an abnormal hour), or outlier detection as the deliverable itself, belong to
  `machine-learning-skills:anomaly-detection`.

## Missingness triage
- Quantify per column (%) and per row (rows with many nulls).
- Classify the mechanism: **MCAR** (random), **MAR** (depends on other observed columns),
  **MNAR** (depends on the missing value itself). MNAR/MAR bias naive row-dropping and mean-imputation.
- A quick MAR probe: compare the distributions of other columns for rows where X is missing
  vs. present — visible differences mean the missingness carries information.
- Decide and *record* the handling — this is the input to `data-analytics-bi-skills:data-cleaning`.

## The data-quality memo template
One page, written for the person who acts next (often future-you):
- **Dataset:** source, extract date, row/column counts.
- **Grain:** one row = <…>; key = <…> (unique: yes/no — if no, what duplicates mean).
- **Fit to the question:** can the driving metric/decision be computed from this data at
  all? What's missing?
- **Quality findings:** missingness per affected column (% and suspected mechanism),
  outliers flagged (rule used, count, suspected cause), category problems (variants,
  unmapped codes), type/format problems, calendar gaps.
- **Notable relationships:** the two or three patterns worth follow-up, each labeled
  hypothesis-not-finding.
- **Cleaning list:** the explicit, ordered handoff to `data-analytics-bi-skills:data-cleaning`.
- **Caveats that survive cleaning:** what no amount of fixing will make this data able to say.

## Worked example — first contact with an activity extract

Domain-neutral on purpose: the "items" below are any logged units of work — transactions,
tickets, matters, deployments, orders. **All numbers are illustrative.**

The question (step 1): "Which categories of item are slowest to complete, and is it getting
worse?" A 200k-row CSV arrives: `item_id, category, opened, closed, amount, owner, status`.

- **Shape and grain (step 2).** 200,412 rows; `item_id` has 3,911 duplicates — the grain is
  one row per *assignment*, not per item: items reassigned between owners appear once per
  owner. Every later count must first collapse to items, or reassigned items double-count.
  `opened` is text; `amount` parsed as text too (thousands separators).
- **Completeness and validity (step 3).** `closed` missing on 12% of rows — legitimate for
  open items, so missing-here-means-open, an informative non-null-mechanism to encode, not
  impute away. `category` has 23 distinct values for what should be 8 (case and punctuation
  variants). `amount` has 41 negatives — reversals, per the source team, i.e. real data.
- **Univariate (step 4).** Completion days: mean 11.2, median 4 — strong right skew; the
  "typical" completion is 4 days and any average-based SLA claim would mislead. Completion
  days exist only for closed items: 12% of items are still open, i.e. right-censored, and
  open items skew long, so every duration figure here is optimistic. Histogram
  shows a spike at exactly 90 days — an auto-close policy, not behavior.
- **Outliers (step 5).** IQR fence flags 2.1% of durations. Investigation of the top ten:
  seven genuine long-runners, two data errors (closed date year-typo 2035), one unit error.
  Three different fixes; zero blanket deletions.
- **Bivariate (step 6).** Median completion days by category (group-by, boxplots): two
  categories run 3× the rest — but both are also the categories with the auto-close spike,
  so the gap may be policy, not workload. Labeled a hypothesis for follow-up. The "is it
  getting worse" half of the question needs a like-for-like cohort comparison: group items
  by *opened* month and measure every cohort at the same age (e.g. share closed within 30
  days of opening) — a naive trend over closed items scores recent months only on their
  fast finishers, because their slow items are still open, and so looks deceptively good.
- **Plot check (step 7).** The duration-vs-amount correlation is r ≈ 0.02, "no
  relationship" — but the scatter shows two separate clouds (small routine items;
  large reviewed items), each with its own positive slope. Simpson's-pattern lead recorded.
- **Memo (step 8).** Grain warning (assignment vs. item), the auto-close artifact, the
  category variants → mapping table, the 2035 typos, and the two-clouds lead; cleaning list
  handed to `data-analytics-bi-skills:data-cleaning`; caveats recorded that durations are
  censored at 12% (open items appear in no completion figure) and that pre-2023 data
  lacks `owner` entirely.

## Tool notes
- **SQL:** `COUNT(*)`, `COUNT(DISTINCT key)`, `GROUP BY` frequency tables,
  `PERCENTILE_CONT` for quartiles; over raw files without a server —
  `data-tools-skills:duckdb-local-analytics`.
- **pandas:** `df.info()`, `df.describe()`, `value_counts()`, `df[key].is_unique`,
  `df.isna().mean()`, `df.hist()`; script structure per `coding-agent-skills:python-for-analysts`.
- **Spreadsheet:** pivot tables for frequencies, `COUNTBLANK`, min/max/quartile functions —
  workable to ~100k rows; beyond that, move to SQL or pandas.

## Sources and attribution notes
- Tukey, J. W., *Exploratory Data Analysis*, Addison-Wesley (1977) — the exploratory
  stance, boxplots, and the exploration/confirmation distinction.
- Anscombe, F. J., "Graphs in Statistical Analysis", *The American Statistician* 27(1)
  (1973) — the quartet: four datasets with matching summary statistics and different shapes.
- Attribution note: the quartet is **Anscombe's**, not Tukey's — they are frequently
  conflated because both argue for looking at the data. (Anscombe and Tukey were
  collaborators; the quartet paper is Anscombe's alone.)
