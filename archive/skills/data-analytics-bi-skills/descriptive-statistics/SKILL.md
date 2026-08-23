---
name: descriptive-statistics
description: >-
  Summarizes a variable or dataset with the right measures of central tendency, dispersion, shape,
  and percentiles — and switches to robust measures (median, IQR, MAD) when outliers or skew would
  make the mean and standard deviation mislead. Delivers a per-variable summary block: matched
  center and spread, five-number summary, n and missing count, percentile method, and a plot.
  Use when describing or summarizing data, computing a
  "typical" value or a spread, or choosing which summary statistic to report before drawing
  conclusions. Triggers: descriptive statistics, summary statistics, mean, median, mode, average,
  standard deviation, variance, range, percentile, quartile, IQR, coefficient of variation, skewness,
  kurtosis, distribution shape, central tendency, spread.
metadata:
  version: "1.2.1"
---

# Descriptive statistics

## When to use
- Summarizing a numeric variable — its typical value, spread, and shape — before you infer or model.
- Choosing which summary to report when a distribution is skewed or has outliers (mean/SD vs. median/IQR).
- Building a summary-statistics table or the "at a glance" numbers for a report or dashboard.
- Not for: first-look structural profiling (grain, types, missingness) → see
  `data-analytics-bi-skills:exploratory-data-analysis`. For generalizing from a sample to a
  population with intervals or tests → see `data-analytics-bi-skills:statistical-inference`.

## Do it
`references/measures-and-formulas.md` carries the formulas, the robust alternatives, and the
worked five-number summary — open it when you need the definition rather than the choice.

1. **Fix the population and the grain.** State exactly which set of values you are summarizing and
   what one value represents ("revenue per closed order, FY24"). A mean means nothing until you can
   say "mean of what, per what," and mixing grains (order lines vs. orders) silently corrupts every
   statistic.
2. **Decide sample vs. population.** It changes the variance/SD denominator: population variance
   divides by `N`, sample variance by `n − 1` (Bessel's correction, which offsets the downward bias
   from estimating the mean from the same sample). Analytics data is almost always a *sample* of a
   larger process → use the sample formulas.
3. **Central tendency — pick the center that fits the shape.**
   - **Mean** — the balance point; best for roughly symmetric data. Sensitive to every outlier.
   - **Median** (50th percentile) — the middle value; resistant to outliers and skew. The honest
     "typical" for income, prices, durations, and balances.
   - **Mode** — the most frequent value; the only center for nominal categories, and a flag for
     multimodality (two modes often means two mixed populations).
4. **Dispersion — always pair a center with a matching spread.**
   - **Range** (max − min): trivial to read, dominated by the two most extreme points.
   - **Variance / standard deviation:** average squared / root-average-squared distance from the
     mean; pair with the mean. SD is in the data's units, variance in squared units.
   - **IQR** (`Q3 − Q1`): the spread of the middle 50%; resistant; pair with the median.
   - **Coefficient of variation** (`SD / mean`): unitless relative spread for comparing series of
     different scales — valid only for ratio data with a positive mean, meaningless near zero.
5. **Shape — quantify skew and tails.** Compare mean to median as a fast skew check: mean ≫ median
   ⇒ right-skew (a long high tail, e.g. revenue); mean ≪ median ⇒ left-skew. **Skewness** puts a
   number on that asymmetry; **kurtosis** measures tail heaviness / outlier-proneness (report
   *excess* kurtosis, where a normal distribution is 0), not "peakedness."
6. **Percentiles / quartiles.** Report the five-number summary (min, Q1, median, Q3, max) and the
   tail percentiles your decision needs (p5/p95, or p99 for SLAs and risk). State the interpolation
   method — tools disagree at the edges (Excel `PERCENTILE.INC` vs `.EXC`, differing quartile
   definitions) — so a percentile is reproducible.
7. **Choose robust vs. classical.** If skew or outliers are present, lead with **median + IQR**
   (optionally MAD or a trimmed mean); reserve **mean + SD** for roughly symmetric data.
8. **Deliver the summary block, not loose numbers.** Per variable, the finished output is:

```
variable · n · missing/excluded
center: median 412.50          spread: IQR 118.00      (mean + SD if roughly symmetric)
five-number: min / Q1 / median / Q3 / max               tails: p95 (p99 for SLA/risk)
shape: right-skewed (mean 512.30 > median 412.50) · percentile method: PERCENTILE_CONT
plot: histogram when the question is shape or multimodality; boxplot when it is outliers
      or a comparison across groups; both when n is large and the shape is contested
```

   Render the plot when the medium allows it. When it does not, the line still names one — the
   plot type and the variable — so the reader can produce it; "a plot would help" is not the
   deliverable, "histogram of order value, 40 bins" is.

   The assistant computes and drafts the block; the human owns the population/grain definition and
   the decision the numbers feed.

## Why / learn
Descriptive statistics answer "what does this data look like?" honestly, *before* any inference — and
the core skill is refusing to let one number impersonate a whole distribution. The mean is a fragile
summary: it is the balance point, so a single large invoice or a data-entry typo drags it away from
where most of the data actually sits, and on a right-skewed quantity (revenue, wait time, account
balance) the mean lands above the typical case and quietly overstates it. That is why the **median
and IQR often tell the truer story** — they are *resistant*, defined by rank position rather than
magnitude, so extreme values move them little or not at all. The mean-vs-median gap is itself
information: when they diverge, the distribution is skewed and any "average" headline will mislead.
Pairing is non-negotiable — a center with no spread hides whether values cluster or scatter, and a
spread with no center is uninterpretable (SD belongs with the mean, IQR with the median). The deeper
point is that a descriptive summary is a *faithful compression*: you are choosing which features of
the shape to keep, so keep the ones that survive the outliers your data really has — and show the
picture so the reader can see what the summary threw away.

## Common mistakes
- Reporting the mean on skewed or outlier-laden data → misleading "typical." Lead with the median/IQR.
- A center with no spread (or a spread with no center) → hides clustering vs. scatter. Report the pair.
- Mismatched pair (median with SD, mean with IQR) → inconsistent story. Mean↔SD, median↔IQR.
- Dividing sample variance by `n` instead of `n − 1` → understated spread. Use the sample formula.
- Coefficient of variation on data with a near-zero or negative mean → unstable nonsense. Ratio data only.
- Averaging across mixed grains or pooling distinct populations → a mean of two peaks that describes neither.
- Not stating the percentile method → the same p95 differs across Excel/SQL/pandas. State it.

## Tailor to your environment
Record your setup in `references/your-environment.md`; keep anything sensitive (real column names,
client thresholds, sample rows) in `your-environment.private.md`, which is git-ignored — commit only
sanitized, structural examples. Capture the variables you routinely summarize and their expected
shape (which are skewed by nature), your house convention for percentile/quartile method and rounding,
whether you default to mean/SD or median/IQR, and the tool you compute in (SQL, pandas, Excel, BI).
The skill then applies its generic choices to your real measures.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/descriptive-statistics.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/measures-and-formulas.md — formulas, when each measure is appropriate, and tool/percentile caveats
- references/your-environment.md — your variables, conventions, and tools (add when supplied)
