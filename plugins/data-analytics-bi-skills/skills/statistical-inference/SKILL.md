---
name: statistical-inference
description: >-
  Reasons from a sample to a population with confidence intervals and hypothesis tests (t-test,
  chi-square, ANOVA) — choosing the right test, checking its assumptions, and interpreting p-values,
  effect size, and Type I/II errors correctly rather than treating "significant" as a verdict. Use
  when testing a claim, comparing groups, running an A/B test, or quantifying the uncertainty of an
  estimate from a sample. Triggers: hypothesis test, p-value, statistical significance, confidence
  interval, t-test, chi-square, ANOVA, effect size, sampling, sampling distribution, type I error,
  type II error, statistical power, A/B test, significance level, null hypothesis.
---

# Statistical inference

## When to use
- Deciding whether an observed difference or effect is real or could just be sampling noise.
- Comparing groups: two means (t-test), several means (ANOVA), or categorical association (chi-square).
- Putting a confidence interval around a sample estimate to quantify its uncertainty.
- Not for: describing the sample you already hold (center, spread, shape) → see
  `data-analytics-bi-skills:descriptive-statistics`. For scoring a predictive model's performance →
  see `machine-learning-skills:model-evaluation`. For framing the whole improvement project
  around the analysis → see `continuous-improvement-skills:dmaic-problem-solving`.

## Do it
1. **State the population claim and hypotheses first — before seeing results.** Write the null `H₀`
   (no effect / no difference) and the alternative `H₁`, and decide one- vs. two-sided. Fixing this in
   advance is what keeps the test honest.
2. **Set α, the effect that matters, and power up front.** Choose the significance level `α` (commonly
   0.05 — the tolerated Type I error rate), the smallest effect size worth detecting, and a target
   power (commonly 0.80). Ideally use these to size the sample *before* you collect data.
3. **Choose the test from the data type and design**, not habit: one/two/paired means → t-test;
   3+ means → one-way ANOVA; counts / association in a contingency table → chi-square; non-normal
   small samples → the nonparametric equivalent. See `references/choosing-a-test.md`.
4. **Check the assumptions.** Independence of observations; approximate normality *of the sampling
   distribution* (large `n` buys this via the Central Limit Theorem even when the raw data is
   non-normal); equal variances (or use Welch's t-test, a safe default); expected count ≥ 5 per cell
   for chi-square (else Fisher's exact). If violated, switch to a robust or nonparametric test rather
   than pushing on.
5. **Compute the statistic, the p-value, AND a confidence interval for the effect.** The CI shows the
   plausible range of the true effect in real units — report it, not just the p-value.
6. **Interpret the p-value correctly.** It is `P(data this extreme or more | H₀ true)` — *not* the
   probability that H₀ is true, not the probability the result is "due to chance," and not `1 −`
   anything useful. `p < α` ⇒ reject H₀ ("statistically significant"); `p ≥ α` ⇒ *fail to reject*,
   which is **not** proof of no effect (absence of evidence ≠ evidence of absence).
7. **Report the effect size and judge practical significance separately.** A tiny,
   business-irrelevant effect can be "significant" with a big enough `n`; a large effect can miss
   significance with too small an `n`. Give Cohen's d / correlation / odds ratio / Cramér's V beside
   the p-value and ask whether the effect *matters*.
8. **Guard against multiple comparisons and p-hacking.** Testing many hypotheses inflates false
   positives (20 tests at α = 0.05 ⇒ ~1 expected false "hit"). Pre-specify your comparisons; when you
   run a family of them, adjust (Bonferroni, or Benjamini–Hochberg for the false-discovery rate).

## Why / learn
Inference exists because you almost never measure the whole population — you measure a *sample* and
have to reason back to the whole under uncertainty. The engine is the **sampling distribution**: if
you repeated the study, your statistic would land somewhere different each time, and that variation is
what a standard error, a confidence interval, and a p-value all quantify. A hypothesis test is a
structured bet against a straw man: assume H₀ (nothing is going on), ask how surprising your data
would be in that world, and if it would be very surprising (`p < α`) you reject the straw man. The
**p-value is one narrow, easily-misread slice of this** — it measures surprise *given H₀*, so it can
never by itself tell you the probability that H₀ is true, or how big or important the effect is. That
is why a mature analysis carries three things together: the p-value (is it distinguishable from
noise?), the **confidence interval and effect size** (how big, in real units, with what uncertainty?),
and the **error framing** — a Type I error is crying wolf on a true null, a Type II error is missing a
real effect, and **power** is your chance of catching an effect that is genuinely there. "Significant"
is not a verdict of truth or importance; it is one bounded statement about how much this particular
sample can tell you about the world.

## Common mistakes
- "p is the probability H₀ is true" → false. p is computed *assuming* H₀; it cannot be that probability.
- Reading `p ≥ α` as "proven no effect" → it only means not enough evidence. Absence ≠ evidence of absence.
- Reporting only the p-value → give the confidence interval and effect size; significance ≠ importance.
- Huge `n` makes a trivial effect "significant" → check the effect size, not just the asterisk.
- Running many tests and reporting the winners → p-hacking. Pre-specify and correct for multiplicity.
- Choosing the test after seeing the data, or ignoring assumptions → invalid p-value. Decide first, check fit.
- Reading a 95% CI as "95% probability the true value is in this interval" → the 95% is the
  procedure's long-run capture rate, not a probability about this one interval.

## Tailor to your environment
Record your setup in `references/your-environment.md`; keep anything sensitive (real metric names,
client data, actual test results) in `your-environment.private.md`, which is git-ignored — commit only
sanitized, structural examples. Capture the decisions you routinely test (A/B tests, group
comparisons, KPI shifts), your house α and power conventions, the minimum effect size that matters for
each metric, whether your data meets the independence/normality assumptions, and the tool you run tests
in (Python `scipy`/`statsmodels`, R, Excel, a BI stats add-in). The skill then targets its workflow at
your real decisions.

## References
- references/choosing-a-test.md — decision guide: which test for which data type and design, plus assumptions
- references/your-environment.md — your tested decisions, conventions, and tools (add when supplied)
