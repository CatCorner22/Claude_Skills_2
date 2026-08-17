# Evals — data-analytics-bi-skills:statistical-inference

## 1. Positive trigger (should load the skill)
> "We ran an A/B test: variant B converted at 4.1% vs. 3.8% for A over two weeks. Is that difference
> statistically significant, and how should I interpret the p-value?"

Expected: skill loads; frames H₀/H₁ and α up front; **runs the validity gate before interpreting
anything** — asks for the assignment counts and runs the SRM chi-square, asks whether the stopping rule
was pre-committed (two weeks by plan, or stopped when it crossed?), whether the exposure window covers
whole cycles, and whether the analysis unit matches the randomization unit — routing to
`data-analytics-bi-skills:ab-test-design` for how those are designed; then picks the right test
(two-proportion z / chi-square); checks assumptions; reports a confidence interval and effect size, not
just the p-value; interprets the p-value correctly (not "the probability B is better") and separates
statistical from practical significance; flags multiple-comparison risk if many variants/metrics are
involved.

## 2. Near-miss (should NOT load this skill)
> "Here's last quarter's order-value column. Give me the mean, median, spread, and a sense of how
> skewed it is."

Expected: this is describing one sample, not inferring to a population —
`data-analytics-bi-skills:descriptive-statistics` should handle it. If statistical-inference loads as
the primary skill, tighten the description / cross-links.

## 3. Near-miss (should NOT load this skill — design seam)
> "We're about to launch a new checkout page against the current one. How many users per arm do we
> need, what do we randomize on, and how long should it run?"

Expected: this is pre-launch design and sizing of a randomized experiment —
`data-analytics-bi-skills:ab-test-design` owns it (MDE → n per arm → duration, randomization unit,
variance reduction, stopping rule). statistical-inference may be cited for the α/power machinery, but
must not lead. The split the two skills state identically: sizing a *randomized experiment* is
ab-test-design's; margin-of-error sizing for a *survey estimate* is survey-and-sampling-design's;
statistical-inference owns the α/power/effect-size machinery and sizing a *non-randomized* comparison.

## 4. Quality rubric
A good response:
- **Does the task:** states hypotheses and α before results, gates an experimental readout on validity
  (SRM, stopping rule, exposure window, analysis unit) before computing anything, chooses a test justified
  by data type/design/estimand, checks assumptions, and reports a p-value **with** a confidence interval
  and effect size.
- **Teaches:** explains the sampling-distribution logic and gives the correct p-value meaning —
  `P(data | H₀)`, not `P(H₀ | data)` — plus statistical vs. practical significance and Type I/II errors.
- **Names each test's actual null:** treats Mann–Whitney as a test of stochastic dominance
  (`P(X > Y) = ½`), Kruskal–Wallis as a test of distributional difference, and Wilcoxon signed-rank as
  requiring symmetric differences — never as "the t-test/ANOVA for non-normal data." A response that
  offers a rank test as a drop-in substitute for a comparison of means, or that concludes "A's mean is
  higher" from one, has failed this item.
- **Reaches for resampling:** for small, skewed, or heavy-tailed data where the decision is about means,
  offers a bootstrap CI on the difference in means and a permutation test (studentized when variances
  differ) rather than defaulting to ranks or to a log transform whose estimand is the geometric mean.
- **Safe:** never calls the p-value the probability the hypothesis is true, never reads a
  non-significant result as proof of no effect, warns about p-hacking / multiple comparisons, and never
  hands back a p-value on an experiment that failed a validity check.
- **Delivers the contract:** an inference readout — pre-registered hypotheses/α/effect threshold, validity
  gate results, method with its estimand, point estimate + CI in real units beside the p-value, effect
  size with a practical-significance judgment, multiplicity policy, and a conclusion sentence phrased in
  the estimand the method actually supports.
