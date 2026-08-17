# Evals — data-analytics-bi-skills:data-cleaning

## 1. Positive trigger (should load the skill)
> "This customer export is a mess — dates are text, there are duplicate rows, the `state` column has
> `NY`, `N.Y.`, and `New York`, and about 10% of the revenue values are blank. Help me get it
> analysis-ready."

Expected: skill loads; profiles first, moves to tidy structure, coerces types, standardizes
categories via a reusable mapping table (not scattered replaces), chooses a documented
missing-value strategy matched to the mechanism (with a `was_missing` flag), dedupes on a
defined key with a survivor rule, checks join cardinality, and validates non-destructively.

## 2. Near-miss (should NOT load this skill)
> "I just received a dataset I've never seen. Before I change anything, how do I profile the data —
> what does one row represent, which columns are typed wrong, and where are the distributions and
> outliers that will bite me later?"

Expected: this is first-look profiling, not fixing — the
`data-analytics-bi-skills:exploratory-data-analysis` skill should handle it (it owns *profile the
data*, *what does one row represent*, *distribution*, and *outliers*). The prompt deliberately
dangles cleaning bait ("before I change anything", "typed wrong"); if this cleaning skill loads as
primary, tighten the description / cross-links. (Note the neighboring seam: had the ask been for
the summary itself — central tendency, spread, a five-number summary —
`data-analytics-bi-skills:descriptive-statistics` owns that, not EDA and not this skill. A file
that won't even *parse* — encodings, delimiters, BOMs — is likewise not this skill:
`data-tools-skills:csv-and-flat-file-wrangling` owns ingest.)

## 3. Quality rubric
A good response:
- **Does the task:** reaches tidy structure (Wickham's rules, applied to the actual mess),
  fixes types, standardizes categories with a reusable mapping table and an UNMAPPED
  tripwire, picks a missing-value strategy fit to the mechanism (MCAR/MAR/MNAR, flagging
  imputed cells), dedupes on an explicit key, and checks join cardinality/fan-out.
- **Teaches:** explains *why* cleaning decisions change conclusions (bias from row-dropping
  and mean-imputation, fan-out double-counting) and why every decision must be explicit and
  recorded; attributes tidy data to Wickham (JSS 2014) rather than vaguely to "best practice".
- **Honest:** does not quote the "80% of time is cleaning" folk statistic as research.
- **Safe:** keeps the raw source intact (raw/processed separation per
  `data-tools-skills:data-file-hygiene`), makes the steps reproducible/scripted, and
  validates row counts and control totals afterward; hands model-feature imputation to
  `machine-learning-skills:feature-engineering`.
