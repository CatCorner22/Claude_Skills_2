---
name: causal-inference
description: >-
  Establishes whether X actually caused Y when there was no experiment — draws the causal DAG
  first (confounders, mediators, colliders; backdoor thinking in plain language), then names
  what identifies the effect: randomization when available (that path belongs to
  continuous-improvement-skills:design-of-experiments), otherwise the quasi-experimental toolkit
  — difference-in-differences, instrumental variables, regression discontinuity — each with its
  key assumption in plain terms. Applies Hill's considerations as viewpoints, never a checklist,
  plus the humility rail: what observational data cannot rule out. Association tests belong to
  data-analytics-bi-skills:statistical-inference.
  Use when a policy, change, or exposure is claimed to have caused an outcome. Triggers:
  causal inference, correlation vs causation, correlation is not causation, does X cause Y,
  confounder, confounding, collider bias, difference-in-differences, instrumental variable,
  regression discontinuity, natural experiment.
metadata:
  version: "1.0.0"
  source: >-
    Built from docs/research/general-use-expansion-research.md §1 (general-use expansion wave
    dossier). Provenance marks carried from the dossier: [snippet-only, cross-checked] =
    verified via convergent web-search snippets (direct fetches were egress-blocked at research
    time); [background — verify] = commonly reported but not independently confirmed.
---

# Causal inference (correlation-vs-causation, made procedural)

## When to use
- Someone claims a policy, process change, price move, or exposure *caused* an outcome — and the
  evidence is observational (no one randomized anything): "resolution time fell after the new
  intake form," "the discipline rate differs by group," "revenue rose after the notification change."
- Before "controlling for" variables in any regression: deciding *which* covariates to adjust for
  and which would poison the estimate.
- A threshold, cutoff, staggered rollout, or one-unit-not-the-other change exists that might
  serve as a natural experiment.
- Not for: an effect you can still randomize — design the experiment instead → offline multi-factor
  studies: `continuous-improvement-skills:design-of-experiments`; online/field variant tests:
  `data-analytics-bi-skills:ab-test-design`. Testing whether an association is distinguishable
  from noise (hypothesis tests, p-values, A/B analysis) → `data-analytics-bi-skills:statistical-inference`.
  A recurring mess driven by feedback structure → `decision-science-skills:systems-thinking` —
  and note the seam by name: a causal-*loop* diagram maps feedback structure (which loops exist,
  which way they push); it is **not** causal identification and never licenses an effect estimate.
  One incident's cause chain → `continuous-improvement-skills:root-cause-analysis`. Predicting an
  outcome from features → `machine-learning-skills:supervised-modeling` (prediction ≠ causation;
  feature importance describes what the model used, not what moves the world).

## Do it
The full drill — DAG roles, the identification ladder, worked DiD/IV/RD examples, Hill's
viewpoints, and sensitivity phrasing — is in `references/causal-identification.md`.
1. **Write the causal question as a counterfactual contrast.** "What would Y have been for these
   units *without* X?" Name the treatment, the outcome, the units, and the comparison you wish
   you had. If you can't state the counterfactual, you don't yet have a causal question.
2. **Draw the DAG before you argue.** Nodes = variables; arrows = claimed direct causes. Classify
   every covariate by its *structural role*, not by whether it correlates: **confounder** (arrows
   into both X and Y — a common cause), **mediator** (on the path X→M→Y — part of the effect),
   **collider** (arrows in from both — a common *effect*). Roles are claims about the world;
   let the user correct the arrows.
3. **Choose the adjustment set by backdoor thinking, in plain language.** Block every "backdoor"
   path — every path that reaches X through an arrow pointing *into* it — by adjusting for
   confounders on it. Never adjust for a collider (that *opens* a path and manufactures
   correlation) or a mediator (that throws away the effect you're estimating), and never adjust
   for anything downstream of the treatment.
4. **Name what would identify the effect — climb the ladder.** (a) **Randomization** if still
   possible — stop and go design the experiment (see the seams above). (b) **Difference-in-
   differences**: change hits one group/date but not another; key assumption: the groups would
   have moved in *parallel* absent the change — check pre-trends and run a placebo period.
   (c) **Instrumental variable**: something nudges X but touches Y *only through* X (exclusion);
   also must actually move X (relevance). (d) **Regression discontinuity**: a score/date/size
   cutoff assigns treatment; units just above and just below are comparable; check that no one
   manipulated their position around the cutoff. (e) If none apply: adjustment-only, labeled as
   the weakest rung.
5. **Stress the design's key assumption — that *is* the analysis.** Pre-trend plots and placebo
   tests for DiD; the exclusion argument stated in words for IV; bunching-at-the-cutoff and
   bandwidth checks for RD. An estimator run without its assumption check is a number, not a finding.
6. **Walk Hill's viewpoints as viewpoints.** Strength, consistency, specificity, temporality,
   gradient, plausibility, coherence, experiment, analogy — use them to *structure the argument*
   about the total evidence, never as a scorecard. Hill himself: none "can be required as a sine
   qua non" [snippet-only, cross-checked].
7. **Close with the humility rail.** State the claim at the strength the design earns; say what
   observational data cannot rule out; and run the sensitivity question: "how strong would an
   unmeasured confounder have to be to erase this?" If a plausible everyday variable clears that
   bar, say so and downgrade the conclusion. Route the association arithmetic itself (tests,
   intervals) to `data-analytics-bi-skills:statistical-inference`.

## Why / learn
"Correlation is not causation" has no author — it circulates in print from the 1880s–90s,
contemporaneous with correlation itself, and logician Alexander Bain warned of the confusion in
1870; it is not a quotable line from Pearson or Fisher. The teaching irony: Pearson (1911)
dismissed *causation* as "another fetish amidst the inscrutable arcana of even modern science" —
the correlation pioneer thought causation was the confused idea [snippet-only, cross-checked].
The aphorism is also only half a lesson: it tells you what correlation isn't, not what would make
a causal claim *earned*. The DAG supplies that. Pearl's graphical framework (causal diagrams,
*Biometrika* 1995; the back-door criterion; lay canon *The Book of Why*, 2018 [snippet-only,
cross-checked]) turns "control for everything" — the kitchen-sink reflex — into a structural
question with a structural answer: adjusting is only correct for variables that block backdoor
paths, and adjusting for a collider actively *creates* bias where none existed (condition on
"escalated tickets" and severity suddenly anti-correlates with handler skill among the escalated,
even if they're independent overall). The quasi-experimental designs are the honest middle
ground between "we randomized" and "we hope": each one finds a piece of the world that behaved
*as if* someone had randomized — a policy hitting one unit (DiD), an instrument's nudge (IV), a
cutoff's arbitrary line (RD) — and each buys its credibility with one named assumption you must
defend rather than a regression you merely run. Their history is itself a provenance lesson: IV
first appears in Philip Wright's 1928 tariff book, Appendix B, and the 75-year "was it really his
son Sewall?" authorship question was settled by *stylometry* (Stock & Trebbi 2003 — Philip wrote
it) [snippet-only, cross-checked]; RD begins with Thistlethwaite & Campbell (1960) studying
National Merit near-winners at a test-score threshold; and Card & Krueger's minimum-wage DiD
(1994) is canonical *and still contested* — the honest frame is that the method survived the
fight and reshaped empirical economics while the specific employment estimate remains argued
[snippet-only, cross-checked]. Hill belongs at the end, as he intended: his 1965 lecture offered
nine *viewpoints* for weighing an association — and explicitly disclaimed "hard-and-fast rules of
evidence." The all-nine-boxes checklist is folklore that inverts his position; the same lecture
also cautioned against over-reliance on significance tests. Use Hill the way he did: as the
shape of a mature argument about total evidence, delivered with the humility that observational
data never proves the counterfactual — it only makes some explanations harder to sustain.

## Common mistakes
- Kitchen-sink regression ("control for everything we have") → colliders and mediators in the
  adjustment set create bias. Classify roles on the DAG first; adjust only to block backdoors.
- Adjusting for a mediator, then announcing "no effect" → you subtracted the effect's own pathway.
  Decide total vs. direct effect before touching M.
- Conditioning on a collider — often silently, by filtering the dataset ("only escalated cases,"
  "only hired candidates") → manufactured correlation. Selection is conditioning.
- Using Hill's viewpoints as a nine-box scorecard → inverts Hill. They structure an argument;
  none is required, none suffices.
- Reading model coefficients or feature importance as causal → they describe the model's use of
  data. Say "the model relies on X," never "X drives Y" (see supervised-modeling's same rule).
- DiD without a pre-trends check → "parallel absent treatment" is the whole design; plot the
  before-period and run a placebo window first.
- An instrument with its own path to the outcome → exclusion fails and the estimate is polluted;
  argue exclusion in words, not just correlation arithmetic.
- RD where units can steer their own score → bunching at the cutoff means the "arbitrary line"
  was gamed; check the density before trusting the comparison.
- Claiming causation because p is small → significance is an association statement; identification
  comes from design, not from the p-value (that machinery lives in statistical-inference).

## Tailor to your environment
Record in `references/your-environment.md` the causal questions your role actually faces, the
natural experiments your organization generates for free (cutoffs, staggered rollouts,
one-office-first changes), your known confounders, and who must be convinced at what standard of
proof. Keep anything naming real clients, cases, or figures in `your-environment.private.md`
(git-ignored); commit only sanitized, structural examples.

## References
- references/causal-identification.md — the DAG drill with role table and collider demo, the
  identification ladder, worked DiD/IV/RD examples, Hill's viewpoints as Hill meant them, and
  sensitivity phrasing (provenance marks carried from the dossier)
- references/your-environment.md — your causal questions, free natural experiments, known
  confounders, and burden of proof (fill in)
