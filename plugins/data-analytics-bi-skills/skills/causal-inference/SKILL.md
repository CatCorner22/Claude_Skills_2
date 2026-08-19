---
name: causal-inference
description: >-
  Establishes whether X caused Y when there was no experiment — draws the causal DAG
  first (confounders, mediators, colliders; backdoor thinking), then names what identifies
  it: randomization when available (that path is
  continuous-improvement-skills:design-of-experiments), else the quasi-experimental toolkit
  — difference-in-differences, instrumental variables, regression discontinuity — each with its
  assumption, scope limit, and inference trap. Applies Hill's considerations as viewpoints,
  never a checklist, plus the humility rail: what observational data cannot rule out. Association
  tests belong to data-analytics-bi-skills:statistical-inference.
  Use when a policy, change, or exposure is claimed to have caused an outcome. Triggers:
  causal inference, correlation vs causation, correlation is not causation, does X cause Y,
  confounder, confounding, collider bias, difference-in-differences, staggered rollout,
  instrumental variable, regression discontinuity, natural experiment.
metadata:
  version: "1.2.0"
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
   for anything downstream of the treatment. And draw the *unmeasured* causes too: "pre-treatment"
   is not a safety certificate, because a pre-treatment variable that is a common effect of one
   cause of X and one cause of Y opens a path the moment you adjust for it (M-bias, §1–§2).
4. **Name what would identify the effect — climb the ladder.** (a) **Randomization** if still
   possible — stop and go design the experiment (see the seams above). (b) **Difference-in-
   differences**: change hits one group/date but not another; key assumption: the groups would
   have moved in *parallel* absent the change — check pre-trends and run a placebo period. Ask
   first whether adoption is **staggered** (offices phasing in over months): the standard two-way
   fixed-effects regression is *biased* there — it silently uses already-treated units as controls
   and can report the wrong sign even when every unit improved — so use a staggered-adoption
   estimator, named (§5a). (c) **Instrumental variable**: something nudges X but touches Y *only
   through* X (exclusion); must actually move X, and *strongly* — a weak-but-significant
   instrument biases the estimate back toward the confounded OLS answer. Scope: IV identifies the
   effect on **compliers**, not the population (§6). (d) **Regression discontinuity**: a
   score/date/size cutoff assigns treatment; units just above and just below are comparable; check
   that no one manipulated their position around the cutoff; the effect is the one **at the
   cutoff**. (e) If none apply: adjustment-only, labeled as the weakest rung — and run with its
   actual toolkit (propensity matching/weighting or doubly-robust estimation, judged on covariate
   balance) plus an explicit **positivity/overlap** check (§4a).
5. **Stress the design's key assumption — that *is* the analysis.** Pre-trend plots and placebo
   tests for DiD; the exclusion argument in words *plus* a first-stage strength number for IV;
   bunching-at-the-cutoff and bandwidth checks for RD; overlap plots for adjustment-only. Then say
   what **inference** the design can carry: one treated office is one cluster, and no standard
   error computed from its tickets describes the policy comparison — with one or two treated units
   the honest options are synthetic control or randomization inference (§5). An estimator run
   without its assumption check is a number, not a finding.
6. **Walk Hill's viewpoints as viewpoints.** Strength, consistency, specificity, temporality,
   gradient, plausibility, coherence, experiment, analogy — use them to *structure the argument*
   about the total evidence, never as a scorecard. Hill himself: none "can be required as a sine
   qua non" [snippet-only, cross-checked].
7. **Close with the humility rail.** State the claim at the strength the design earns; say what
   observational data cannot rule out; and run the sensitivity question — "how strong would an
   unmeasured confounder have to be to erase this?" — **with a named method rather than a feeling**:
   an E-value for the estimate *and* for the confidence limit nearest the null, or Rosenbaum bounds
   (Γ) for a matched design (§9). If a plausible everyday variable clears that bar, say so and
   downgrade the conclusion. Route the association arithmetic itself (tests, intervals) to
   `data-analytics-bi-skills:statistical-inference` — but not the few-clusters problem in step 5,
   which that skill does not cover and this one must handle itself.

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
"escalated tickets" and severity suddenly *correlates* with handler skill among the escalated —
the senior handlers look like they absorb every hard case — even if the two are independent
overall). The quasi-experimental designs are the honest middle
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

Three ideas hold the toolkit together once you have used it a few times. **First: every design
answers a narrower question than the one you asked.** RD gives you the effect at the cutoff, IV
gives you the effect on the units the instrument actually moved, adjustment-only gives you the
effect over the region where the treated and untreated populations overlap. None of these is a
defect — they are what "as if randomized" costs — and the discipline is to say which population
the number describes in the same sentence as the number. The scope statement *is* part of the
estimate. **Second: identification and inference are separate problems, and a design can solve the
first while leaving the second untouched.** Denver-vs-Phoenix can be a defensible identification
story and still support no standard error at all, because the unit that could have gone differently
is the office-quarter and there is exactly one of them. Software will happily print an interval
computed from thousands of tickets; the interval answers a question nobody asked. **Third: the
methods themselves get revised, so cite the design and not just the acronym.** "We ran a DiD"
described a settled procedure in 2015 and describes an ambiguity now: staggered adoption turned out
to break the standard two-way fixed-effects implementation badly enough that a whole family of
replacement estimators exists, and a rollout that phases in over months is the ordinary case, not
an exotic one. The lesson generalizes past DiD — a method's assumptions are load-bearing, someone
eventually checks them, and the honest writeup names the estimator and the year's guidance rather
than the family.

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
- Running two-way fixed effects on a staggered rollout → already-treated units become controls and
  the weights can go negative; the sign itself is unsafe. Use a staggered-adoption estimator (§5a).
- Reporting a standard error for a one-treated-unit DiD → the tickets are not independent draws and
  clustering over two offices is a label, not inference. Synthetic control or randomization
  inference, or report the estimate with no interval and say why.
- An instrument with its own path to the outcome → exclusion fails and the estimate is polluted;
  argue exclusion in words, not just correlation arithmetic.
- "The first stage was significant" as the relevance check → significance is not strength; a weak
  instrument drags 2SLS back toward the confounded OLS answer and its interval undercovers. Report
  the first-stage F, treat 10 as a floor.
- Reading an IV estimate as the population effect → it is the effect on compliers under
  monotonicity; name who they are, and report the complier share (the first stage).
- Propensity matching without an overlap check → where the arms don't overlap the model is
  extrapolating, not comparing; trim, then restate which population the estimate describes.
- Hearing "doubly robust" as robust to unmeasured confounding → it is robust to *model
  misspecification* only; both models still condition on the same measured set.
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

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/causal-inference.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/causal-identification.md — the DAG drill with role table, collider demo and M-bias,
  the identification ladder with the adjustment-only toolkit (propensity/doubly-robust, overlap),
  worked DiD/IV/RD examples plus the few-clusters inference problem and the staggered-adoption
  estimators, Hill's viewpoints as Hill meant them, and named sensitivity methods (E-value,
  Rosenbaum bounds) with provenance marks carried from the dossier
- references/your-environment.md — your causal questions, free natural experiments, known
  confounders, and burden of proof (fill in)
