# Measures and formulas (reference)

Notation: `n` = count, `xᵢ` = each value, `x̄` = sample mean, `μ` = population mean. The "sample"
formulas (`n − 1`) are the default for analytics; use the "population" formulas (`N`) only when your
data is the entire population, not a sample of a process.

## Central tendency
- **Mean** `x̄ = (Σ xᵢ) / n` — balance point; symmetric data; not resistant to outliers.
- **Median** — sort the values; the middle one (average of the two middle if `n` is even); equals the
  50th percentile; resistant. Use for skewed/outlier-prone quantities (income, price, latency, balance).
- **Mode** — the most frequent value. Only center for nominal data; ≥ 2 modes ⇒ suspect mixed populations.
- **Trimmed mean** — the mean after dropping the top and bottom k% of values; a compromise between
  mean and median that tempers outliers without discarding shape entirely.
- **Weighted mean** `Σ wᵢxᵢ / Σ wᵢ` — when values represent different sizes (e.g. price weighted by volume).

## Dispersion
- **Range** = max − min. Uses only the two extremes; very fragile.
- **Sample variance** `s² = Σ(xᵢ − x̄)² / (n − 1)`. **Population variance** `σ² = Σ(xᵢ − μ)² / N`.
- **Standard deviation** `s = √s²` — same units as the data; pair with the mean.
- **IQR** = `Q3 − Q1` — the middle-50% spread; resistant; pair with the median.
- **MAD** (median absolute deviation) = `median(|xᵢ − median|)` — the most robust common spread.
- **Coefficient of variation** `CV = s / x̄` (often ×100%) — unitless; compares relative variability
  across differently-scaled series. Valid only for ratio data with a positive mean.

## Shape
- **Skewness** — signed asymmetry. Positive (right) skew: long high tail, mean > median. Negative
  (left) skew: long low tail, mean < median. Near 0: roughly symmetric.
- **Kurtosis** — tail heaviness / outlier-proneness. Report **excess kurtosis** = kurtosis − 3, so a
  normal distribution reads 0; positive ⇒ heavier tails than normal (more frequent extremes). It is
  about the tails, not "peakedness."

## Percentiles and quartiles
- **Percentile** `p` — the value below which p% of the data falls; the median is p50, Q1 = p25, Q3 = p75.
- **Five-number summary** — min, Q1, median, Q3, max; the basis of a boxplot.
- **Interpolation matters at the edges.** Different tools use different definitions:
  - Excel `PERCENTILE.INC` / `QUARTILE.INC` — inclusive linear interpolation (numpy default `linear`).
  - Excel `PERCENTILE.EXC` / `QUARTILE.EXC` — exclusive interpolation (drops the endpoints).
  - Tukey "hinges" (used by some boxplots) differ again on odd vs. even `n`.
  - SQL `PERCENTILE_CONT` interpolates; `PERCENTILE_DISC` returns an actual data value.
  State which you used; on large samples the difference is tiny, on small samples it is not.

## Choosing the summary
| Distribution                    | Center | Spread                   |
|---------------------------------|--------|--------------------------|
| Roughly symmetric, no outliers  | Mean   | Standard deviation       |
| Skewed or outlier-prone         | Median | IQR (or MAD)             |
| Nominal categories              | Mode   | Frequency table          |
| Comparing spread across scales  | —      | Coefficient of variation |

Always report `n` and the missing/excluded count alongside, and show a histogram or boxplot so the
reader can see the shape the numbers compress away.
