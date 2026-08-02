---
name: exploratory-data-analysis
description: >-
  Profiles a dataset before any modeling or reporting — its shape, column types, grain, distributions,
  missingness, outliers, and relationships — so you understand and can trust the data before drawing
  conclusions from it. Use when first inspecting a new dataset, sizing up data quality, or deciding
  what needs fixing before analysis. Triggers: EDA, exploratory data analysis, data profiling, profile
  the data, first look at data, distribution, summary statistics, central tendency, spread, outliers,
  correlation, cross-tab, missing data, data quality check, get to know the data.
---

# Exploratory data analysis (EDA)

## When to use
- First contact with a new dataset — understanding its structure, quality, and what it can answer.
- Sizing up data quality (missingness, outliers, inconsistent categories) before you build anything on it.
- Deciding what to clean or transform, or checking whether a metric is even measurable in the data.
- Not for: actually fixing the issues you find (imputing, dedup, reshaping) → see
  `data-analytics-bi-skills:data-cleaning`. For the formal definitions and formulas behind these
  summary statistics → see `data-analytics-bi-skills:descriptive-statistics`.

## Do it
1. **Start from the question.** Write the decision or metric the data must support. EDA is directed
   exploration, not aimless plotting — the question tells you which columns and relationships matter.
2. **Profile shape and grain.** Row count, column count, and — critically — what *one row represents*.
   Test the assumed key for uniqueness (duplicate keys mean the grain isn't what you think). Confirm
   each column's data type matches its meaning (dates stored as text, IDs stored as numbers).
3. **Check completeness and validity.** Compute missingness per column (count and %). Range-check
   numerics (negatives where impossible, absurd maxima), and list the distinct levels of each
   categorical to catch typos and stray codes (`Y/N/y/Yes/1`).
4. **Go univariate first.** For each variable on its own: central tendency (**mean and median** —
   compare them to sense skew), spread (**SD, IQR, min/max**), and shape. Plot a histogram or boxplot
   for numerics and a frequency bar for categoricals. One variable at a time before any pair.
5. **Flag outliers, don't reflexively delete them.** Mark points beyond `1.5×IQR` from the quartiles
   or `|z| > 3`, then *investigate*: a genuine extreme value, a unit error, and a data-entry typo all
   look alike and are handled differently.
6. **Then go bivariate.** Correlation for numeric pairs (Pearson for linear, Spearman for monotonic),
   cross-tabs for categorical pairs, and group-by summaries for numeric-by-category. Scatter plots for
   the pairs your question cares about.
7. **Visualize before you trust a summary number.** A mean, an SD, and a correlation can be identical
   across wildly different shapes (Anscombe's quartet). Look at the picture; let it correct the
   statistic.
8. **Write a short data-quality memo.** Capture the grain, key issues (missingness, outliers, bad
   categories), notable relationships, and an explicit list of what must be cleaned before analysis —
   which is the handoff to cleaning and modeling. See `references/profiling-checklist.md`.

## Why / learn
EDA exists to answer one prior question before any analysis: *can I trust the numbers this data will
produce?* Every downstream metric, chart, and model inherits the data's structure and flaws, so an
hour spent understanding shape, grain, missingness, and distributions saves days of debugging a result
that was wrong from the start. The discipline is **structure → one variable → pairs**: you can't
interpret a relationship between two columns until you understand each column alone, and you can't
understand a column until you know the grain it lives at. The mean-vs-median comparison, the
missingness scan, and the outlier check are cheap early-warning signals — a mean far above the median
tells you the distribution is skewed and that averages will mislead; a column that's 40% missing may
not be usable at all. And you visualize *first* because summary statistics compress away exactly the
patterns (clusters, nonlinearity, a lone leverage point) that change the conclusion. The goal isn't a
pile of plots; it's a defensible statement of what the data is, what it can answer, and where it will
bite you.

## Common mistakes
- Jumping to modeling/charts before profiling → you build on unknown grain and hidden nulls. Profile first.
- Reporting the mean on a skewed distribution → misleading "typical" value. Compare mean vs. median; report both.
- Deleting outliers on sight → you may erase the real signal or a fixable error. Investigate the cause first.
- Trusting a correlation without a scatter plot → identical stats hide very different shapes. Plot it.
- Ignoring the categorical levels → `NY`, `N.Y.`, and `New York` split one group into three. List distinct values.
- Treating missingness as random → if it's not, dropping those rows biases every later number. Ask *why* it's missing.

## Tailor to your environment
Record your setup in `references/your-environment.md` (keep any real data — actual column names,
sample rows, thresholds tied to a client — in `your-environment.private.md`, which is git-ignored).
Capture your typical data sources and formats, the tools you profile with (SQL, pandas, Excel, a BI
tool's data panel), the grain of your common tables, and any domain validity rules (e.g. an amount
must be ≥ 0, a status is one of a known set). This skill then targets its generic checks at your real
columns. To then *fix* what you find, hand off to `data-analytics-bi-skills:data-cleaning`.

## References
- references/profiling-checklist.md — the concrete profiling checklist and what to compute per column type
- references/your-environment.md — your sources, tools, grain, and validity rules (add when supplied)
