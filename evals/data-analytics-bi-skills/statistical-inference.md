# Evals — data-analytics-bi-skills:statistical-inference

## 1. Positive trigger (should load the skill)
> "We ran an A/B test: variant B converted at 4.1% vs. 3.8% for A over two weeks. Is that difference
> statistically significant, and how should I interpret the p-value?"

Expected: skill loads; frames H₀/H₁ and α up front; picks the right test (two-proportion z /
chi-square); checks assumptions; reports a confidence interval and effect size, not just the p-value;
interprets the p-value correctly (not "the probability B is better") and separates statistical from
practical significance; flags multiple-comparison risk if many variants/metrics are involved.

## 2. Near-miss (should NOT load this skill)
> "Here's last quarter's order-value column. Give me the mean, median, spread, and a sense of how
> skewed it is."

Expected: this is describing one sample, not inferring to a population —
`data-analytics-bi-skills:descriptive-statistics` should handle it. If statistical-inference loads as
the primary skill, tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** states hypotheses and α before results, chooses a test justified by data
  type/design, checks assumptions, and reports a p-value **with** a confidence interval and effect size.
- **Teaches:** explains the sampling-distribution logic and gives the correct p-value meaning —
  `P(data | H₀)`, not `P(H₀ | data)` — plus statistical vs. practical significance and Type I/II errors.
- **Safe:** never calls the p-value the probability the hypothesis is true, never reads a
  non-significant result as proof of no effect, and warns about p-hacking / multiple comparisons.
