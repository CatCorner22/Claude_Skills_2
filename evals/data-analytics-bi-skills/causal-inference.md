# Evals — data-analytics-bi-skills:causal-inference

## 1. Positive trigger (should load the skill)
> "Resolution time in our Denver office dropped from 12 to 9 days after we rolled out the new
> intake form there — Phoenix stayed on the old form and only drifted from 11.5 to 10.5. Nobody
> randomized anything. Can we actually say the form caused the improvement, or is this just
> correlation vs causation?"

Expected: skill loads; states the counterfactual contrast; draws/describes the DAG and classifies
candidate covariates as confounder/mediator/collider; recognizes the one-office rollout as a
difference-in-differences design and computes the DiD contrast (−2.0 days), *conditional on
parallel trends*; demands pre-trend and placebo checks before believing it; walks relevant Hill
viewpoints as argument structure (not a scorecard); closes with the sensitivity question and a
claim stated at design strength.

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
  for colliders/mediators); names the identification rung explicitly (randomize → DiD → IV → RD →
  adjustment-only); runs or demands the design's assumption checks (pre-trends/placebo for DiD,
  exclusion argument for IV, bunching/bandwidth for RD).
- **Teaches:** backdoor thinking in plain language; why conditioning on a collider *manufactures*
  correlation (selection filters included); Hill's nine as viewpoints with his own "no sine qua
  non" disclaimer; the toolkit's lineage told honestly (Wright 1928/stylometry, Thistlethwaite &
  Campbell 1960, Card & Krueger 1994 as canonical-but-contested).
- **Stays honest:** never claims causation from a p-value; never presents Hill as a checklist;
  keeps the "correlation is not causation" aphorism unattributed (it has no author); states what
  observational data cannot rule out; runs the how-strong-a-confounder sensitivity question; and
  words the conclusion at the strength the design earns.
