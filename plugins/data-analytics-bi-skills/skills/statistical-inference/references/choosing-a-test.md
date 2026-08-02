# Choosing a test (reference)

Pick from the *question*, the *data type*, and the *design* (independent vs. paired groups) — not from
habit. Then confirm the assumptions before you trust the p-value.

## Comparing means (numeric outcome)
| Question | Test | Nonparametric alternative |
|---|---|---|
| Is one mean different from a target value? | One-sample t-test | Wilcoxon signed-rank |
| Do two independent groups differ? | Two-sample t-test (use **Welch's** if variances/ns differ) | Mann–Whitney U |
| Do two *paired* measurements differ (before/after, matched)? | Paired t-test | Wilcoxon signed-rank |
| Do 3+ groups' means differ? | One-way ANOVA (then Tukey HSD post-hoc) | Kruskal–Wallis |
| Do means differ across two factors? | Two-way ANOVA | — |

## Categorical outcomes (counts / proportions)
| Question | Test |
|---|---|
| Are two categorical variables associated? | Chi-square test of independence |
| Does one categorical variable match expected proportions? | Chi-square goodness-of-fit |
| Any expected cell count < 5? | Fisher's exact test |
| Do two proportions differ (e.g. A/B conversion)? | Two-proportion z-test (or chi-square) |
| Paired categorical (before/after on the same units)? | McNemar's test |

## Relationships between two numerics
- **Pearson correlation** — strength of a *linear* relationship (assumes roughly bivariate normal).
- **Spearman correlation** — strength of a *monotonic* relationship; robust to outliers/nonlinearity.
- **Simple linear regression** — direction, slope, and a CI/test on the slope.

## Assumptions to check
- **All tests:** observations are **independent** (no repeated units, no clustering) and the sample is
  representative of the population you want to conclude about. No test rescues a biased sample.
- **t-test / ANOVA:** the *sampling distribution of the mean* is approximately normal — satisfied for
  large `n` by the Central Limit Theorem even when raw values are skewed; for small `n` the raw data
  should be roughly normal. ANOVA and the pooled t-test also assume **equal variances** (Welch's
  t-test and Welch's ANOVA drop that assumption — good defaults).
- **Chi-square:** expected count ≥ 5 in (almost) every cell; put counts, not percentages, in the table.
- **Correlation / regression:** linearity (Pearson), no extreme leverage points, roughly constant spread.

## When assumptions fail
Prefer a **nonparametric** test (right column above) for small, non-normal samples; **transform** a
skewed variable (e.g. log) when appropriate; or use a **robust/Welch** variant. Never "fix" a violated
assumption by ignoring it — the reported p-value stops meaning what it claims.

## Effect sizes to report with the test
- Two means → **Cohen's d** (or the raw difference and its CI).
- ANOVA → **eta-squared / omega-squared** (share of variance explained).
- Chi-square → **Cramér's V** (or the odds ratio for a 2×2 table).
- Correlation → **r** itself (and r² as variance explained).
