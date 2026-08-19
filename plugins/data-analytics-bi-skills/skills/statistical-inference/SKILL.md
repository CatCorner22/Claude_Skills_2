---
name: statistical-inference
description: >-
  Reasons from a sample to a population with confidence intervals and hypothesis tests (t-test,
  chi-square, ANOVA, plus bootstrap and permutation methods) — choosing the right test, checking its
  assumptions, naming what each test's null actually is, gating an experiment's validity before
  interpreting it, and reading p-values, effect size, and Type I/II errors correctly rather than
  treating "significant" as a verdict. Use when testing a claim, comparing groups, running an A/B test,
  or quantifying the uncertainty of an estimate from a sample. Triggers: hypothesis test, p-value,
  statistical significance, confidence interval, t-test, chi-square, ANOVA, effect size, sampling,
  sampling distribution, type I error, type II error, statistical power, A/B test, significance level,
  null hypothesis, bootstrap confidence interval, permutation test, Mann-Whitney, nonparametric test.
metadata:
  version: "1.1.1"
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
- Not for: designing and operating the experiment itself — randomization unit and interference,
  variance reduction, sizing the arms, stopping rules, guardrail metrics, and how to run the
  trust checks → see `data-analytics-bi-skills:ab-test-design` (this skill owns the analysis once
  the data is in, and runs that skill's validity gates as step 5 before interpreting anything);
  claiming causation from observational (non-randomized) data →
  `data-analytics-bi-skills:causal-inference`.
- **The sizing split, stated the same way on all three sides:** sizing a **randomized experiment**
  (MDE → n per arm → duration, where n interacts with the randomization unit, the variance-reduction
  choice, and the stopping rule) belongs to `data-analytics-bi-skills:ab-test-design`, its step 3;
  **margin-of-error sizing for a survey estimate** belongs to
  `data-analytics-bi-skills:survey-and-sampling-design`; **this skill** owns the α/power/effect-size
  machinery all three use, and sizes a **non-randomized** comparison — an observational two-group
  comparison, a before/after study, a one-off means test you are about to collect (step 2).

## Do it
1. **State the population claim and hypotheses first — before seeing results.** Write the null `H₀`
   (no effect / no difference) and the alternative `H₁`, and decide one- vs. two-sided. Fixing this in
   advance is what keeps the test honest.
2. **Set α, the effect that matters, and power up front.** Choose the significance level `α` (commonly
   0.05 — the tolerated Type I error rate), the smallest effect size worth detecting, and a target
   power (commonly 0.80). Use these to size the sample *before* you collect data — here for a
   non-randomized comparison; for a randomized experiment the sizing worksheet (n per arm, duration,
   variance reduction) is `data-analytics-bi-skills:ab-test-design` step 3, and for a survey estimate
   it is `data-analytics-bi-skills:survey-and-sampling-design`. The machinery is the same; the owner
   depends on what you're sizing.
3. **Choose the test from the data type, the design, AND the estimand** — the quantity the decision is
   about: one/two/paired means → t-test (Welch's by default); 3+ means → one-way ANOVA; counts /
   association in a contingency table → chi-square. If the decision is about **means** and the data is
   small, skewed, or heavy-tailed, reach for a **bootstrap CI or a permutation test on the difference
   in means** (step 5) — *not* automatically for a rank-based test. Rank-based tests
   (Mann–Whitney, Kruskal–Wallis, Wilcoxon signed-rank) are excellent tests of a *different* null:
   they answer "does one group tend to produce larger values?", not "do the means differ." Pick one
   when that is the question you have. See `references/choosing-a-test.md` for each test's actual null.
4. **Check the assumptions.** Independence of observations; approximate normality *of the sampling
   distribution* (large `n` buys this via the Central Limit Theorem even when the raw data is
   non-normal); equal variances (or use Welch's t-test, a safe default); expected count ≥ 5 per cell
   for chi-square (else Fisher's exact). If violated, move to a method that **keeps your estimand** —
   Welch, a bootstrap CI, a permutation test — rather than pushing on; switching to a rank-based test
   is also fine, but it changes the claim you are entitled to make (step 10).
5. **Gate the experiment's validity before you interpret anything.** If the data came from a live
   randomized test, four checks run *before* the p-value means anything, and any one of them failing
   means the readout is void rather than negative. `data-analytics-bi-skills:ab-test-design` owns how
   to design and diagnose each; this skill refuses to interpret until they pass.
   - **Sample ratio mismatch (SRM).** Compare observed assignment counts with the designed split via a
     1-df chi-square. Designed 50/50, observed 10,200 / 9,800 of 20,000: `χ² = 200²/10,000 × 2 = 8`,
     p ≈ 0.005 → **failed**; the assignment or logging is biased and every downstream metric inherits
     it. "Close to 50/50" is a chi-square judgment scaled by n, not an eyeball judgment.
   - **The stopping rule.** Was it pre-committed? A fixed-horizon test stopped the moment the dashboard
     crossed p < 0.05 has an actual Type I error rate several times α (roughly 5× nominal per Johari et
     al., KDD 2017, as cited in ab-test-design), so the nominal p-value is not a p-value. Report the
     stopping rule with the result; if it was broken, say the test is inconclusive and re-run — no
     adjustment recovers an unplanned stop after the fact.
   - **The exposure window.** Whole weeks/cycles covered, and is the effect still moving with exposure
     (novelty decaying, primacy building)? A week-one estimate of a still-moving curve is precise about
     the wrong quantity.
   - **Analysis unit = randomization unit.** Randomizing users and testing page-views (or sessions,
     rows, events) treats correlated observations as independent: the standard error is understated and
     the significance is phantom. Aggregate to the randomization unit, or use a cluster-robust /
     delta-method standard error.
6. **Compute the statistic, the p-value, AND a confidence interval for the effect.** The CI shows the
   plausible range of the true effect in real units — report it, not just the p-value. When `n` is
   small, the data is skewed or heavy-tailed, or the statistic has no clean formula (a median, a ratio,
   a trimmed mean, a difference of ratios), use the resampling pair instead of forcing a textbook test:
   - **Bootstrap** for the interval — resample each group with replacement, recompute the difference,
     and take the 2.5th/97.5th percentiles of ≥ 10,000 replicates (BCa or bootstrap-t when the
     statistic is skewed). It estimates the sampling distribution of *your* estimand, so a bootstrap CI
     on the difference in **arithmetic means** answers the revenue question directly.
   - **Permutation** for the p-value — shuffle the group labels many times and count how often the
     shuffled difference beats the observed one. Under exchangeability it is exact in finite samples,
     with no normality assumption. Permute a **Welch/studentized** statistic when variances differ, and
     permute *within* blocks/strata for paired or clustered data.
   - Know their limits: the bootstrap is asymptotic and unreliable at very small `n` or in extreme
     tails; a plain permutation test targets the sharp null of *no effect at all*, not equal means; and
     with 5 vs 5 observations there are only C(10,5) = 252 distinct label splits, so the smallest
     attainable two-sided p is 2/252 ≈ 0.008 — a fact about the design, not about the data.
   Mechanics and worked resampling recipes are in `references/choosing-a-test.md`.
7. **Interpret the p-value correctly.** It is `P(data this extreme or more | H₀ true)` — *not* the
   probability that H₀ is true, not the probability the result is "due to chance," and not `1 −`
   anything useful. `p < α` ⇒ reject H₀ ("statistically significant"); `p ≥ α` ⇒ *fail to reject*,
   which is **not** proof of no effect (absence of evidence ≠ evidence of absence).
8. **Report the effect size and judge practical significance separately.** A tiny,
   business-irrelevant effect can be "significant" with a big enough `n`; a large effect can miss
   significance with too small an `n`. Give Cohen's d / correlation / odds ratio / Cramér's V beside
   the p-value and ask whether the effect *matters*.
9. **Guard against multiple comparisons and p-hacking.** Testing many hypotheses inflates false
   positives (20 tests at α = 0.05 ⇒ ~1 expected false "hit"). Pre-specify your comparisons; when you
   run a family of them, adjust (Bonferroni, or Benjamini–Hochberg for the false-discovery rate).
10. **Write the conclusion in the quantity the test actually tested.** Match the sentence to the
   estimand: a t-test / bootstrap on means supports "group A's **mean** is higher by X (95% CI …)"; a
   Mann–Whitney supports "a randomly drawn A value **tends to exceed** a randomly drawn B value"; a
   Wilcoxon signed-rank supports a claim about the differences' centre (the pseudo-median), not the mean
   difference; a chi-square supports "the variables are associated," never "A causes B"; a t-test on
   **log** values supports a claim about the **geometric** mean or the ratio, not the total. If the
   decision is about a total — revenue, cost, hours, headcount — the estimand has to be the arithmetic
   mean, because only arithmetic means multiply up to totals. Rewriting the conclusion sentence back to
   "the mean is higher" after a rank-based test is the most common way a correct analysis becomes a
   false report.

**Deliverable — the inference readout.** The finished output states: (1) H₀/H₁, α, sidedness, and the
effect size that would matter, all fixed before the numbers; (2) for experimental data, the validity
gate results — SRM chi-square, the stopping rule as actually followed, exposure window, analysis
unit = randomization unit (a failure voids the readout rather than making it negative); (3) the test or
resampling method chosen, the estimand it targets, and the assumption check behind it; (4) the point
estimate with its confidence interval **in real units**, next to the p-value; (5) the effect size and an
explicit practical-significance judgment; (6) the multiplicity policy and how many comparisons the
family contains; (7) a conclusion sentence phrased in the estimand the method supports. The assistant
runs the analysis; the human owns α, the effect that matters, and the decision.

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

**Every test has a null, and the null is not always the one you wanted.** This is where "just use the
nonparametric equivalent" quietly goes wrong. **Mann–Whitney U** estimates `P(X > Y)` and its null is
that a random draw from one group is as likely to exceed a draw from the other as the reverse — *stochastic
dominance*, not means. It coincides with a test of means/medians only under the location-shift model
(identical distributions differing by a constant shift, which also implies equal variances and shapes).
Break that and the two questions come apart, sometimes with opposite answers. Take group A = 0 for 90% of
users and 20 for 10%, versus group B = 1 for everyone: A's **mean is 2** against B's **1**, yet
`P(A > B) = 0.10` — Mann–Whitney will declare B the dominant group with enough data while A generates
twice the revenue. Or make the means exactly equal (A ≡ 1; B = 0 with probability 0.6 and 2.5 with
probability 0.4, so E[B] = 1.0) and `P(A > B) = 0.6`: a test with nothing to find, finding something.
That zero-inflated, long-tailed shape is not exotic — it is what revenue and usage per user look like.
**Kruskal–Wallis** extends the same logic to k groups: its null is that the groups' distributions are the
same, so it can reject on a difference in spread or shape while all k means match. **Wilcoxon signed-rank**
adds a requirement of its own — the differences must be **symmetric** about their centre, or it can reject
for asymmetry alone; it speaks about the pseudo-median of the differences (the sign test is the
assumption-light fallback that speaks only about their median). Under unequal variances or unequal group
sizes, rank tests used as location tests also lose their nominal error rate; **Brunner–Munzel** tests
`P(X > Y) = ½` without assuming identical distributions, and Welch or a bootstrap keeps you on means.
Transformations have the same trap in a friendlier costume: a t-test on `log x` is a test about the
**geometric** mean, and back-transforming gives a ratio of geometric means, not of arithmetic ones. Group A
= {1, 100} has arithmetic mean 50.5 and geometric mean 10; group B = {12, 12} has both at 12. The log-scale
test prefers B (12 > 10) while A's total is 101 against B's 24. If the decision is about a total, model the
mean of the outcome directly (a GLM with a log link, or a bootstrap on the raw difference) rather than
transforming and hoping.

**Bootstrap and permutation are the modern answer to "small, skewed, and I need an interval on the
difference in means."** They earn that place by separating two things textbook tests bundle: the
permutation test builds the null distribution *from your own data* by relabelling (exact under
exchangeability, no normality anywhere), and the bootstrap builds the sampling distribution of *whatever
statistic you chose* by resampling (so you get a CI on the estimand the decision is about, means included).
Neither is magic: a plain permutation test's null is "the labels are irrelevant," which is stronger than
"the means are equal," so pair it with a studentized statistic when variances differ; and the bootstrap
leans on the sample resembling the population, which is exactly what tiny samples cannot promise.

**Finally, an analysis of an invalid experiment is not a conservative analysis — it is a confident wrong
answer.** Sample-ratio mismatch, a broken stopping rule, and a mismatch between the randomization and
analysis units all corrupt the inputs to every formula downstream, and none of them shows up as a large
p-value. That is why the validity gate sits *before* the test rather than in the caveats paragraph: a
p-value computed on a void experiment is arithmetic, not evidence.

## Common mistakes
- "p is the probability H₀ is true" → false. p is computed *assuming* H₀; it cannot be that probability.
- Reading `p ≥ α` as "proven no effect" → it only means not enough evidence. Absence ≠ evidence of absence.
- Reporting only the p-value → give the confidence interval and effect size; significance ≠ importance.
- Huge `n` makes a trivial effect "significant" → check the effect size, not just the asterisk.
- Running many tests and reporting the winners → p-hacking. Pre-specify and correct for multiplicity.
- Choosing the test after seeing the data, or ignoring assumptions → invalid p-value. Decide first, check fit.
- Reading a 95% CI as "95% probability the true value is in this interval" → the 95% is the
  procedure's long-run capture rate, not a probability about this one interval.
- Calling Mann–Whitney/Kruskal–Wallis "the t-test/ANOVA for non-normal data" → they test stochastic
  dominance / distributional difference, not means. Under unequal shapes they can point the opposite way
  from the means. Use them when that null is your question; use a bootstrap or permutation test on the
  difference in means when the decision is about means.
- Concluding "group A's mean is higher" from a rank-based test → the test did not estimate a mean.
  Phrase the conclusion in the estimand the method supports.
- Log-transforming a skewed variable and reporting the result as if it were about the average → the log
  test is about the geometric mean; only arithmetic means add up to totals.
- Analyzing a live A/B test without checking SRM, the stopping rule, and the analysis unit → a clean
  p-value on a void experiment. Run the validity gate first (step 5); design them with
  `data-analytics-bi-skills:ab-test-design`.
- Testing per-event rows from a user-randomized test → correlated observations, understated SE, phantom
  significance. Aggregate to the randomization unit or use cluster-robust errors.

## Tailor to your environment
Record your setup in `references/your-environment.md`; keep anything sensitive (real metric names,
client data, actual test results) in `your-environment.private.md`, which is git-ignored — commit only
sanitized, structural examples. Capture the decisions you routinely test (A/B tests, group
comparisons, KPI shifts), your house α and power conventions, the minimum effect size that matters for
each metric, whether your data meets the independence/normality assumptions, which estimand each decision
is really about (a mean that rolls up to a total, a median, a rate), your validity-gate expectations for
experimental readouts, and the tool you run tests in (Python `scipy`/`statsmodels`, R, Excel, a BI stats
add-in). Keep the experiment-side conventions consistent with
`data-analytics-bi-skills:ab-test-design`'s `references/your-environment.md`. The skill then targets its
workflow at your real decisions.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/statistical-inference.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/choosing-a-test.md — decision guide: which test for which data type and design, what each test's null actually is, bootstrap and permutation recipes, and assumptions
- references/your-environment.md — your tested decisions, conventions, and tools (add when supplied)
