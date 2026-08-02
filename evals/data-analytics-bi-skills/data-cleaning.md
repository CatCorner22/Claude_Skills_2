# Evals — data-analytics-bi-skills:data-cleaning

## 1. Positive trigger (should load the skill)
> "This customer export is a mess — dates are text, there are duplicate rows, the `state` column has
> `NY`, `N.Y.`, and `New York`, and about 10% of the revenue values are blank. Help me get it
> analysis-ready."

Expected: skill loads; profiles first, moves to tidy structure, coerces types, standardizes
categories via a lookup, chooses a documented missing-value strategy (with a flag), dedupes on a
defined key, checks join cardinality, and validates non-destructively.

## 2. Near-miss (should NOT load this skill)
> "I just received a dataset I've never seen. What summary statistics and plots should I run to
> understand its distributions and spot data-quality issues?"

Expected: this is first-look profiling, not fixing — the
`data-analytics-bi-skills:exploratory-data-analysis` skill should handle it. If this cleaning skill
loads as primary, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** reaches tidy structure, fixes types, standardizes categories with a reusable
  mapping, picks a missing-value strategy fit to the mechanism (and flags imputed cells), dedupes on
  an explicit key, and checks join cardinality/fan-out.
- **Teaches:** explains *why* cleaning decisions change conclusions (bias from row-dropping and
  mean-imputation, fan-out double-counting) and why the work must be explicit.
- **Safe:** keeps the raw source intact, makes the steps reproducible, and validates row counts /
  control totals afterward.
