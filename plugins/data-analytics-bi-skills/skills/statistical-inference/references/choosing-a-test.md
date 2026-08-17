# Choosing a test (reference)

Pick from the *question*, the *data type*, the *design* (independent vs. paired groups), and the
**estimand** — the quantity the decision is about — not from habit. Then confirm the assumptions before you
trust the p-value.

## Contents
- Comparing means (numeric outcome)
- What each rank-based test's null actually is
- Resampling: bootstrap intervals and permutation tests
- Categorical outcomes (counts / proportions)
- Relationships between two numerics
- Assumptions to check
- When assumptions fail
- Effect sizes to report with the test

## Comparing means (numeric outcome)
The third column is **not** a drop-in substitute: each rank-based test answers a different question (next
section). Choose it when its question is yours, not merely because the data is non-normal.

| Question (about means) | Test | Rank-based test — *different null* |
|---|---|---|
| Is one mean different from a target value? | One-sample t-test | Wilcoxon signed-rank (centre of a *symmetric* difference distribution) |
| Do two independent groups differ? | Two-sample t-test (use **Welch's** if variances/ns differ) | Mann–Whitney U (`P(X > Y) = ½`) |
| Do two *paired* measurements differ (before/after, matched)? | Paired t-test | Wilcoxon signed-rank (pseudo-median of differences); sign test (median of differences) |
| Do 3+ groups' means differ? | One-way ANOVA (then Tukey HSD post-hoc) | Kruskal–Wallis (same distribution across groups) |
| Do means differ across two factors? | Two-way ANOVA | — |
| Means, but small / skewed / heavy-tailed data | **Bootstrap CI + permutation test on the difference in means** | — (this *is* the means-preserving route) |
| Means, unequal variances, and you want the dominance question anyway | — | Brunner–Munzel (`P(X > Y) = ½` without assuming identical distributions) |

## What each rank-based test's null actually is
Rank tests are good tests. They are just not tests of means, and the gap matters whenever the decision is
about a total.

- **Mann–Whitney U / Wilcoxon rank-sum.** The statistic estimates `P(X > Y) + ½P(X = Y)`; the null is
  `P(X > Y) = P(Y > X)` — no tendency for one group's draws to exceed the other's (*stochastic dominance*).
  It becomes a test of medians or means **only** under the location-shift model: identical distributions
  differing by a constant, which also implies equal variances and equal shapes.
- **Kruskal–Wallis.** The k-group extension; the null is that all groups' distributions are identical. It
  can reject on differences in spread or shape while every group mean is the same.
- **Wilcoxon signed-rank.** Needs the paired differences to be **symmetric** about their centre, or it can
  reject for asymmetry alone. Its estimand is the pseudo-median (median of pairwise averages), not the mean
  difference. When symmetry is doubtful, the **sign test** asks only "is the median difference 0?" and
  assumes almost nothing.
- **Unequal variances / unequal group sizes.** Used as location tests under heteroscedasticity, rank tests
  lose their nominal Type I error rate (the rank-based Behrens–Fisher problem). **Brunner–Munzel** (or
  Fligner–Policello) tests the dominance null without the identical-distribution assumption; Welch's t-test
  or a bootstrap keeps you on means.

**Two arithmetic examples of the gap** (both computed from their own setup):

1. *The test points away from the money.* Group A: value 0 for 90% of users, 20 for 10% → mean
   `0.9×0 + 0.1×20 = 2.0`. Group B: value 1 for everyone → mean `1.0`. A's mean is **double** B's, but
   `P(A > B) = 0.10` and `P(B > A) = 0.90`, so Mann–Whitney will (with enough data) declare **B** the
   dominant group. Both statements are true; only one of them is about revenue.
2. *The test fires when the means are identical.* Group A ≡ 1 → mean 1.0. Group B: 0 with probability 0.6,
   2.5 with probability 0.4 → mean `0.6×0 + 0.4×2.5 = 1.0`. The means are exactly equal, yet
   `P(A > B) = 0.6` vs `P(B > A) = 0.4`, so the dominance null is false and Mann–Whitney is right to reject
   — while "the groups differ in average value" is false.

Zero-inflated, long-tailed shapes like these are the norm for revenue, usage, claim size, and cycle time.

## Resampling: bootstrap intervals and permutation tests
The means-preserving answer to small, skewed data. They do different jobs: the **bootstrap** gives an
interval on your estimand; the **permutation test** gives a p-value.

**Bootstrap CI for a difference in means (or medians, ratios, trimmed means):**
1. Resample **within each group**, with replacement, to the group's own size.
2. Recompute the statistic (e.g. `mean(A*) − mean(B*)`).
3. Repeat `B` times and take the 2.5th/97.5th percentiles for a 95% interval.
4. `B = 10,000` is a cheap default. At `B = 1,000` each 95% endpoint rests on the 25th and 975th ordered
   replicate, which visibly wobbles between runs; more replicates cost only compute.
5. Use **BCa** or **bootstrap-t** when the statistic is skewed or the percentile interval looks
   asymmetric-in-the-wrong-direction. For paired data resample *pairs*; for clustered data resample
   *clusters* (a block bootstrap), never individual rows inside a cluster.
6. Honest limits: the bootstrap assumes your sample resembles the population. At `n` in the single digits,
   or for extreme quantiles (a 99th percentile), it is not trustworthy — no method conjures information
   the sample doesn't contain.

**Permutation test for a difference between groups:**
1. Compute the observed statistic (difference in means, or better a **Welch/studentized** difference).
2. Pool the observations, reshuffle the group labels, recompute — many times (10,000 is standard; enumerate
   exhaustively when the design is tiny).
3. The two-sided p is the share of shuffles whose |statistic| ≥ |observed| (add-one style:
   `(1 + #{≥ observed}) / (1 + #shuffles)` so p is never reported as 0).
4. Exact under **exchangeability** — under H₀ the labels carry no information — with no normality
   assumption anywhere. For paired data permute the *sign* within each pair; for stratified/clustered data
   permute within blocks or permute whole clusters.
5. Two honest limits. The sharp null is "no effect at all," not "equal means" — which is why the
   studentized version is the one to permute when variances differ. And granularity is a design property:
   with 5 vs 5 observations there are only `C(10,5) = 252` distinct label splits, so the smallest attainable
   two-sided p is `2/252 ≈ 0.008`; at 10 vs 10 there are `C(20,10) = 184,756` and granularity stops
   mattering.

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
Route by **what the decision is about**, not by "the data isn't normal":

| Situation | Keep the mean as the estimand | Change the question deliberately |
|---|---|---|
| Unequal variances | **Welch's** t-test / Welch's ANOVA | Brunner–Munzel (dominance) |
| Small, skewed, heavy-tailed | **Bootstrap CI** + **permutation test** on the difference in means | Mann–Whitney (dominance) — restate the conclusion |
| Outliers dominating the mean | Pre-specified winsorizing/trimming (state it; it changes the estimand slightly), or a robust regression | Median difference + Hodges–Lehmann CI |
| Clustered / repeated measures | Aggregate to the cluster, cluster-robust SE, or a mixed model | Permute whole clusters |
| Chi-square cells too thin | Fisher's exact | — |

**A transformation is not an assumption fix — it is an estimand change.** A t-test on `log x` tests the
difference in mean *logs*; exponentiating gives a ratio of **geometric** means. Because the geometric mean
is never above the arithmetic one and the gap grows with spread, the two can rank groups oppositely:

- Group A = {1, 100}: arithmetic mean `101/2 = 50.5`; geometric mean `√(1×100) = 10`; total 101.
- Group B = {12, 12}: arithmetic mean 12; geometric mean 12; total 24.
- The log-scale test prefers **B** (12 > 10). The revenue line prefers **A** by more than 4× (101 vs 24).

So when the decision is about a **total** — revenue, cost, hours, headcount — keep the arithmetic mean:
bootstrap the raw difference, or model `E[Y]` directly with a log-link GLM (Gamma/quasi-Poisson) rather than
taking logs and back-transforming. If you do report a log-scale result, label it as a ratio of geometric
means. Never "fix" a violated assumption by ignoring it — the reported p-value stops meaning what it claims.

## Effect sizes to report with the test
Report the effect size that belongs to the null you tested.
- Two means → **Cohen's d** (or, better for a business decision, the raw difference and its CI).
- Bootstrap/permutation on means → the raw difference with its **bootstrap CI**.
- ANOVA → **eta-squared / omega-squared** (share of variance explained).
- Mann–Whitney / Brunner–Munzel → the **probability of superiority** `P(X > Y)` (equivalently
  Cliff's delta or the rank-biserial correlation) — that is what the test estimated. Do not pair a
  Mann–Whitney p-value with Cohen's d and a sentence about means.
- Wilcoxon signed-rank → the **Hodges–Lehmann** estimate (pseudo-median of differences) and its CI.
- Chi-square → **Cramér's V** (or the odds ratio for a 2×2 table).
- Correlation → **r** itself (and r² as variance explained).
