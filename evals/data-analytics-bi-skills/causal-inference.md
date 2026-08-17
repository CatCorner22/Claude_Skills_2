# Evals — data-analytics-bi-skills:causal-inference

## 1. Positive trigger (should load the skill)
> "Resolution time in our Denver office dropped from 12 to 9 days after we rolled out the new
> intake form there — Phoenix stayed on the old form and only drifted from 11.5 to 10.5. Nobody
> randomized anything. Can we actually say the form caused the improvement, or is this just
> correlation vs causation?"

Expected: skill loads; states the counterfactual contrast; draws/describes the DAG and classifies
candidate covariates as confounder/mediator/collider; recognizes the one-office rollout as a clean
2×2 difference-in-differences design and computes the DiD contrast (−2.0 days), *conditional on
parallel trends*; demands pre-trend and placebo checks before believing it; **states that this
design supports no conventional standard error — one treated cluster — and does not manufacture one
from ticket counts**, naming synthetic control (with placebo permutation across untreated offices)
or randomization inference as the methods that would give an honest interval, or else reporting the
point estimate with its checks and an explicit "no inference available"; walks relevant Hill
viewpoints as argument structure (not a scorecard); closes with a **named** sensitivity method
(E-value, or Rosenbaum bounds if matched) rather than a qualitative gesture, and a claim stated at
design strength.

## 1b. Positive trigger (staggered rollout — the TWFE trap)
> "We launched the new intake form office by office over five months — eight offices, different
> start dates, two still on the old form. I ran a regression of resolution days on office and
> month fixed effects plus a 'has the new form' dummy and got a small positive coefficient, so it
> looks like the form made things slightly worse. Is that right?"

Expected: skill loads; recognizes **staggered adoption**, not a clean 2×2, and flags that the
two-way-fixed-effects specification the user ran is biased in this design — it is a weighted
average of all the 2×2 comparisons in the panel, some of which use **already-treated** offices as
controls, and some weights are negative, so with effects that change over time the coefficient can
carry the wrong sign even if every office improved (Goodman-Bacon 2021; de Chaisemartin &
D'Haultfœuille); therefore the "slightly worse" reading is not yet a finding. Names
staggered-adoption estimators explicitly (Callaway & Sant'Anna; Sun & Abraham for the event study;
de Chaisemartin & D'Haultfœuille's negative-weight diagnostic) without presenting any single one as
*the* fix; notes the two never-treated offices are carrying the identification; asks for cohort-wise
pre-trends (a cohort that adopted *because* things were bad breaks parallel trends regardless of
estimator); and separately notes that eight offices is still only eight clusters, so the inference
problem is not solved by fixing the estimator.

## 2. Near-miss (should NOT load this skill — statistical-inference seam)
> "We ran an A/B test on two intake-form versions; version B's completion rate was 62% vs 58%
> for A. Is that difference statistically significant, and what p-value should I report?"

Expected: this is *analysis of a randomized test* — hypothesis-test machinery, p-values,
confidence intervals — which `data-analytics-bi-skills:statistical-inference` owns (including the
bare "A/B test" trigger). Causation is already identified by the randomization; no DAG or
quasi-experimental design is needed. If causal-inference loads as the primary skill, tighten the
description/cross-links.

## 3. Near-miss (should NOT load this skill — design-of-experiments seam)
> "We can vary intake-form layout, question order, and reminder timing all at once — design of
> experiments to find which factors actually matter in the fewest runs."

Expected: a prospective multi-factor factorial study →
`continuous-improvement-skills:design-of-experiments`. When randomization is available, causal
identification is not the problem; this skill should at most be a cross-reference, never the
primary loader.

## 4. Quality rubric
A good response:
- **Does the task:** writes the counterfactual question; assigns DAG roles (and refuses to adjust
  for colliders/mediators, including a pre-treatment collider — M-bias — rather than treating
  "pre-treatment" as safe); names the identification rung explicitly (randomize → DiD → IV → RD →
  adjustment-only); asks whether a DiD is 2×2 or staggered *before* choosing an estimator; runs or
  demands the design's assumption checks (pre-trends/placebo for DiD, exclusion argument **plus a
  first-stage strength number** for IV, bunching/bandwidth for RD, positivity/overlap for
  adjustment-only); if the rung is adjustment-only, brings the actual toolkit (propensity
  matching/weighting or doubly-robust estimation, judged on covariate balance not model fit).
- **Teaches:** backdoor thinking in plain language; why conditioning on a collider *manufactures*
  correlation (selection filters included); that identification and inference are separate problems
  — a design can be defensible and still support no standard error; that every design answers a
  narrower question than the one asked (RD at the cutoff, IV on compliers, adjustment on the
  overlap region) and the scope statement belongs in the same sentence as the estimate; Hill's nine
  as viewpoints with his own "no sine qua non" disclaimer; the toolkit's lineage told honestly
  (Wright 1928/stylometry, Thistlethwaite & Campbell 1960, Card & Krueger 1994 as
  canonical-but-contested) and the fact that methods get revised — staggered adoption broke the
  standard TWFE implementation of DiD, so the writeup names the estimator, not just the family.
- **Stays honest:** never claims causation from a p-value; never presents Hill as a checklist;
  keeps the "correlation is not causation" aphorism unattributed (it has no author); states what
  observational data cannot rule out; answers the how-strong-a-confounder question with a **named**
  method (E-value for the point estimate *and* the near-null confidence limit, Rosenbaum bounds Γ
  for a matched design, negative controls) rather than an impression; never reads "doubly robust" as
  robust to unmeasured confounding; treats the F > 10 weak-instrument rule as a floor with its own
  documented limits rather than a certificate; presents the staggered-DiD estimators as an active
  literature to check rather than a settled winner; and words the conclusion at the strength the
  design earns.
