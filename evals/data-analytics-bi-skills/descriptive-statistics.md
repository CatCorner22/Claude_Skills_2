# Evals — data-analytics-bi-skills:descriptive-statistics

## 1. Positive trigger (should load the skill)
> "Here's a column of 10,000 order values. A handful are huge. What summary statistics should I
> report so the 'typical' order isn't distorted — and should I use the mean or the median?"

Expected: skill loads; fixes population/grain and sample-vs-population; explains mean vs. median vs.
mode and why the median + IQR are the honest summary under right-skew/outliers; pairs each center with
its matching spread; reports the five-number summary, `n`, and the missing count; recommends showing a
histogram/boxplot; notes the percentile method.

## 2. Near-miss (should NOT load this skill)
> "I have two campaigns' conversion rates and want to know whether the difference is statistically
> significant or just noise."

Expected: this is inference (comparing groups, quantifying uncertainty), not describing one sample —
`data-analytics-bi-skills:statistical-inference` should handle it. If descriptive-statistics loads as
the primary skill, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** states grain and sample-vs-population, computes central tendency, dispersion,
  shape, and percentiles, and reports a matched center+spread pair with `n` and missingness.
- **Teaches:** explains *why* the mean misleads on skewed/outlier-laden data and why the median/IQR
  are resistant — describe honestly before inferring.
- **Safe:** does not report a bare mean on skewed data, does not mismatch center/spread, states the
  percentile method, and shows or recommends the distribution's picture.
