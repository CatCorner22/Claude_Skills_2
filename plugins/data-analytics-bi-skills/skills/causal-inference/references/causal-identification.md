# Causal identification — the full drill

Depth for `data-analytics-bi-skills:causal-inference`. Provenance marks carried from the
research dossier (`docs/research/general-use-expansion-research.md` §1):
**[snippet-only, cross-checked]** = verified via convergent web-search snippets, direct source
fetches egress-blocked at research time; **[background — verify]** = commonly reported, not
independently confirmed — do not repeat as fact without checking.

## Contents
1. [The DAG drill: roles, not labels](#1-the-dag-drill-roles-not-labels)
2. [Backdoor thinking in plain language](#2-backdoor-thinking-in-plain-language)
3. [The collider demonstration](#3-the-collider-demonstration)
4. [The identification ladder](#4-the-identification-ladder)
4a. [The adjustment-only toolkit (the weakest rung, run properly)](#4a-the-adjustment-only-toolkit-the-weakest-rung-run-properly)
5. [Worked example A — difference-in-differences](#5-worked-example-a--difference-in-differences)
5a. [Staggered adoption: why plain DiD breaks](#5a-staggered-adoption-why-plain-did-breaks)
6. [Instrumental variables in plain terms](#6-instrumental-variables-in-plain-terms)
7. [Worked example B — regression discontinuity](#7-worked-example-b--regression-discontinuity)
8. [Hill's viewpoints, as Hill meant them](#8-hills-viewpoints-as-hill-meant-them)
9. [The humility rail: sensitivity and limits](#9-the-humility-rail-sensitivity-and-limits)

## 1. The DAG drill: roles, not labels

Draw nodes for the treatment X, the outcome Y, and every variable anyone proposes to "control
for." Add an arrow only for a claimed *direct* cause. Then classify each covariate by where its
arrows point — the role is structural, not statistical (Pearl, "Causal diagrams for empirical
research," *Biometrika* 1995; lay canon *The Book of Why*, Pearl & Mackenzie 2018
[snippet-only, cross-checked]):

| Role | Arrow pattern | What it does | Adjust? |
|---|---|---|---|
| Confounder Z | Z→X and Z→Y | Common cause; creates a spurious X–Y association | **Yes** — blocking it is the point |
| Mediator M | X→M→Y | Carries part of the effect | **No** for the total effect (adjusting subtracts the pathway) |
| Collider C | X→C←Y (or two causes → C) | Common *effect*; harmless until conditioned on | **Never** — conditioning opens a spurious path |
| Descendant of X | X→D | Downstream of treatment | **No** — adjusting for it is partial conditioning on X's effects |

**A collider need not sit downstream of X.** The row above is the easy case. The dangerous case is
a *pre-treatment* variable that is a common effect of two things you never measured: U1→X and
U1→Z, U2→Z and U2→Y. Z arrives in the analyst's list looking innocent — measured before treatment,
correlated with both X and Y, plainly "not a mediator" — but the path X ← U1 → Z ← U2 → Y is
blocked *until you adjust for Z*, and adjusting opens it. Drawn out, the graph looks like the
letter M, hence **M-bias**. See §2 for the procedural guard.

The correlation-vs-causation aphorism this drill operationalizes has no author: it appears in
print by the 1880s–90s, alongside the birth of correlation itself, and Alexander Bain warned of
the confusion in 1870. Pearson (1911), ironically, dismissed *causation* as "another fetish
amidst the inscrutable arcana of even modern science" [snippet-only, cross-checked].

## 2. Backdoor thinking in plain language

A **backdoor path** is any route from X to Y that begins with an arrow pointing *into* X — the
association flowing along it is not X's doing. The back-door criterion (Pearl, stated in his
1993 work and restated in the 1995 paper [snippet-only, cross-checked]) says an adjustment set
Z is valid when: (i) nothing in Z is a descendant of X, and (ii) Z blocks every backdoor path.

Plain-language procedure:
1. List every path from X to Y on the DAG (ignore arrow directions while listing).
2. A path is a **backdoor** if its first step enters X against the arrow.
3. A path is already blocked if it passes through a collider you have *not* conditioned on.
4. Block the open backdoors by adjusting for a confounder on each.
5. Confirm nothing you adjusted for is a collider, a mediator, or downstream of X.
6. **Draw the unmeasured causes too — the ones you would never put in a regression.** Steps 3 and 5
   only protect you against colliders that are *on the drawing*. The usual way M-bias (§1) slips
   through is that U1 and U2 are unmeasured, so nobody drew them, so Z's collider role is invisible
   and Z passes step 5 as an ordinary pre-treatment covariate. Before adding any variable, ask
   the question the DAG answers: "could this be a common effect of something that causes X and
   something else that causes Y?" **"Pre-treatment" is not a safety certificate.**

How much M-bias costs in practice is genuinely contested — one line of work argues the induced bias
is usually small next to the confounding you remove by adjusting, while the graphical camp holds
that you cannot know that without the graph [background — verify]. The defensible rule is not "never
adjust for pre-treatment covariates"; it is **draw the unmeasured causes and decide on the graph**,
and say out loud which variables you are adjusting for on faith.

If no set of *measured* variables blocks all backdoors, adjustment cannot identify the effect —
you need a design from §4, not more covariates.

## 3. The collider demonstration

Colliders punish the "control for everything" reflex, and filtering a dataset is conditioning
in disguise. Structural example (attorney/ops/developer alike):

- Tickets get **escalated** when they are severe *or* when the first handler is inexperienced.
- Severity and handler experience are independent in the full queue.
- Now analyze *only escalated tickets* (a filter — i.e., conditioning on the collider): within
  that subset, a severe ticket needed no inexperienced handler to get escalated, and vice versa —
  so severity and handler inexperience become *negatively* associated.
- Conclusion someone will draw from the filtered data: "our senior people get all the severe
  cases" — a pattern manufactured entirely by the selection.

Same skeleton: studying only *hired* candidates makes skill and connections trade off; studying
only *litigated* disputes makes claim strength and stakes trade off. Whenever a dataset is
defined by an outcome of two causes, expect ghost correlations between those causes.

## 4. The identification ladder

Name the rung out loud in every writeup — the rung, not the estimator, is the credibility.

1. **Randomization.** If you can still randomize, stop analyzing and go design the experiment:
   offline multi-factor studies → `continuous-improvement-skills:design-of-experiments`;
   online/field variant tests → `data-analytics-bi-skills:ab-test-design`.
2. **Difference-in-differences (DiD).** A change hits one group or date but not another.
   Key assumption: **parallel trends** — absent the change, both groups would have moved
   together. Checkable in part: pre-period trend plots, placebo windows. **DiD is not one
   method.** The clean 2×2 (one treated group, one control group, one switch date) is the case
   every textbook draws; **staggered adoption** — units switching on at different dates — is a
   different estimand with a different literature and its own failure mode (§5a). Ask which one
   you have before you pick an estimator.
3. **Instrumental variable (IV).** Something nudges X without touching Y except through X.
   Key assumptions: **relevance** (it really moves X — testable, and the test is *strength*, not
   significance) and **exclusion** (no other path to Y — an argument, not a test), plus
   **monotonicity** if you want to name what the estimate is an average over. Scope limit, as
   binding as RD's: IV identifies the effect on **compliers**, not the population (§6).
4. **Regression discontinuity (RD).** A cutoff on a score/date/size assigns treatment.
   Key assumption: units just above and just below the cutoff are comparable — no one
   manipulated their position. Checkable in part: density/bunching at the cutoff, covariate
   smoothness. Scope limit: the effect **at the cutoff**, not for the whole population (§7).
5. **Adjustment only.** Backdoor-valid covariate adjustment with no design behind it — the
   weakest rung; every conclusion inherits "assuming no unmeasured confounder," so §9 is
   mandatory here. Weakest ≠ toolless: §4a is the equipment this rung is supposed to be run with.

## 4a. The adjustment-only toolkit (the weakest rung, run properly)

Naming this rung "weakest" and then leaving it bare is how it gets run as a raw regression with
twelve controls. It has a real toolkit. All of it presumes you already have a *backdoor-valid
adjustment set* from §2 — none of these methods finds one for you.

- **Propensity score** (Rosenbaum & Rubin 1983 [snippet-only, cross-checked]): the estimated
  probability of treatment given the covariates. Conditioning on it — by **matching**,
  **stratification**, or **inverse-probability weighting (IPW)** — balances the covariates that
  went into it, and nothing else. It is a dimension-reduction device for an adjustment set, not a
  substitute for having the right one. Matching on a collider is still conditioning on a collider.
- **Judge the propensity model by balance, not by fit.** Report standardized mean differences for
  every covariate after matching/weighting (a common bar: |SMD| < 0.1). A propensity model with a
  beautiful AUC is a warning, not an achievement: near-perfect prediction of treatment means the
  arms barely overlap, which is the next bullet.
- **Positivity / overlap (the check that is always skipped).** Every unit must have a real chance
  of both treatment states within the strata you compare. Plot the propensity-score distributions
  by arm and look at the ends: where they do not overlap there is no comparison, only the outcome
  model extrapolating. Symptom in IPW: a handful of weights blowing up as p̂ → 0 or 1, so a few
  units carry the estimate. Remedy: **trim to the overlap region — and then restate the population
  the estimate is now about.** That is the same scope honesty RD owes at its cutoff and IV owes on
  its compliers; adjustment-only owes it on its overlap region.
- **Doubly robust estimation** (AIPW — Robins, Rotnitzky & Zhao 1994; TMLE — van der Laan & Rubin
  2006; double/debiased ML — Chernozhukov et al. 2018 [snippet-only, cross-checked]): fit both an
  outcome model and a treatment model; the estimator stays consistent if *either* is correctly
  specified. The limit that gets misread constantly: doubly robust means robust to **model
  misspecification**, not to unmeasured confounding. Both models condition on the same measured
  set, so an incomplete backdoor set makes both of them wrong in the same direction. Two wrong
  models do not average out to identification.
- **Then §9, non-optionally**, with a named sensitivity method — because everything above still
  ends at "assuming no unmeasured confounder."

## 5. Worked example A — difference-in-differences

*"Did the policy change work?"* — a new intake form rolls out in the Denver office in Q3;
Phoenix keeps the old form. Outcome: average days-to-resolution. (Numbers illustrative.)

| | Before (Q1–Q2) | After (Q3–Q4) | Change |
|---|---|---|---|
| Denver (treated) | 12.0 | 9.0 | −3.0 |
| Phoenix (control) | 11.5 | 10.5 | −1.0 |

DiD estimate = (−3.0) − (−1.0) = **−2.0 days** attributable to the form, *if* parallel trends
holds. The naive before/after (−3.0) overstates it because everything drifted down anyway —
that shared drift is exactly what the control differences out.

Checks that earn the "if":
- **Pre-trends:** plot monthly Denver vs Phoenix for Q1–Q2 (longer if you have it). Converging
  or diverging lines *before* the change kill the design.
- **Placebo window:** pretend the change happened in Q2 and re-estimate; a "significant effect"
  where nothing happened means the comparison is broken.
- **Composition:** did the change itself alter what counts as a ticket, or route different work
  to Denver? An outcome-definition change masquerades as an effect.

### The number this table cannot give you: a standard error

**−2.0 days is a point estimate with no inference attached, and that is not an oversight — it is
the design.** There is **one treated cluster** (Denver) and **one control cluster** (Phoenix).
Two traps follow, and both get sprung routinely:

- **Do not run the ticket-level regression and read its standard error.** With thousands of
  tickets it will be small and it will be meaningless: it prices ticket-to-ticket noise, while the
  thing that could have gone differently is *the office's whole quarter*. Denver's tickets share
  every shock Denver had — a staffing change, a system outage, a seasonal mix shift — so they are
  nowhere near independent draws. This is the Bertrand–Duflo–Mullainathan result: DiD standard
  errors that ignore within-group correlation "severely understate" the true variability — in
  their placebo experiments, effects came out significant at the 5% level in up to **45%** of
  interventions where nothing had happened (Bertrand, Duflo & Mullainathan, *QJE* 119(1), 2004)
  [snippet-only, cross-checked].
- **And do not reach for the usual fix either.** Their remedy — cluster the standard errors at the
  group level where treatment is assigned — works when the number of groups is not too small
  (they show correct size at 50 and at 20 clusters) [snippet-only, cross-checked]. With **one**
  treated cluster there is nothing for a cluster-robust variance estimator to average over; the
  treatment indicator is collinear with the treated office's own fixed effect. "I clustered by
  office" over two offices is a label, not inference.

What the literature actually offers when there is one treated unit:

- **Synthetic control** (Abadie, Diamond & Hainmueller — the California tobacco-tax study is the
  canonical application [snippet-only, cross-checked]). Instead of picking Phoenix, build a
  weighted blend of *all* available untreated offices that reproduces Denver's pre-period path,
  and read the post-period gap. Inference is by **placebo permutation**: re-run the whole
  procedure pretending each control office was treated, and see whether Denver's gap stands out
  against that distribution of placebo gaps. Needs several untreated units and a decent pre-period.
- **Randomization / permutation inference.** Reassign the treatment label across the units (or
  across candidate dates) many times, recompute the DiD each time, and report where the real
  −2.0 sits in the resulting placebo distribution. This is what the "placebo window" check above
  becomes when you run it systematically instead of once. It yields an honest p-value under a
  sharp null without pretending to a standard error. Conley & Taber's few-treated-groups work is
  the standard citation [background — verify].
- **Or report it as what it is.** With two offices and no untreated pool, the honest write-up is
  "a −2.0-day difference-in-differences, one treated office, no inference available; the pre-trend
  and placebo checks are the entire evidence for it." That sentence is a finding. A confidence
  interval manufactured from ticket counts is not.

Seam note, stated plainly because the hand-off does not cover it: this skill routes association
arithmetic to `data-analytics-bi-skills:statistical-inference`, but the few-clusters problem is
*identification-adjacent*, not a test-selection question, and it is not covered there. Do not
assume the seam catches it — the checks above are this skill's own responsibility.

Lineage: the modern canon is Card & Krueger's minimum-wage study (*AER* 1994 — NJ raised its
minimum wage $4.25→$5.05 in April 1992, PA did not; 331 NJ + 79 eastern-PA fast-food
restaurants surveyed before and after; DiD ≈ +2.75 FTE, no detectable employment loss)
[snippet-only, cross-checked]. Honesty note, load-bearing: the finding was and is contested
(payroll-data re-analyses and a long debate); the *method* — credible design from a policy
discontinuity — survived the fight and reshaped empirical economics, while the specific
employment estimate remains argued [snippet-only, cross-checked]. DiD reasoning itself is far
older; John Snow's cholera comparison is the commonly cited precursor [background — verify].
(Note in passing that Card & Krueger is a two-state comparison, so the inference caution above
applies to the canonical study too.)

## 5a. Staggered adoption: why plain DiD breaks

The most common real-world shape is not Denver-vs-Phoenix. It is **eight offices adopting over
five months** — the "phased rollout" that `references/your-environment.md` invites you to hunt for.
That is a *staggered-adoption* design, and a literature that built up through the late 2010s and
after established that the obvious way to analyse it is biased — arguably the most consequential
methodological revision the DiD toolkit has had.

**The obvious way** is a two-way fixed-effects (TWFE) regression: outcome on a unit fixed effect,
a period fixed effect, and a 0/1 "treated now" indicator. Read the coefficient as "the effect."

**Why it breaks.** Goodman-Bacon showed that this one coefficient is a *weighted average of every
possible 2×2 DiD* in the panel — and some of those 2×2s use **already-treated** units as the
control group for later-adopting units (Goodman-Bacon, "Difference-in-differences with variation
in treatment timing," *Journal of Econometrics* 225(2):254–277, 2021) [snippet-only,
cross-checked]. When an already-treated office serves as a control, what gets subtracted is that
office's *change* over the window — which contains its own still-evolving treatment effect. So if
effects grow, fade, or ramp (they usually do), those comparisons are contaminated. Worse, some of
the implicit weights are **negative**, which means the estimate is not a convex average of the
underlying effects at all: **it can come out negative when every single unit's true effect is
positive** (de Chaisemartin & D'Haultfœuille formalize the negative-weight problem)
[snippet-only, cross-checked]. Sign, not just magnitude. And the dynamic "event-study" version of
the same regression has the same disease: each event-time coefficient is contaminated by effects
from other event times (Sun & Abraham) [snippet-only, cross-checked].

**What to use instead** — name the estimator in the writeup:

| Estimator | The idea in one line |
|---|---|
| **Callaway & Sant'Anna** | Estimate a separate ATT(g,t) for each adoption cohort g and period t using only **never-treated or not-yet-treated** units as controls, then aggregate deliberately (overall, by cohort, or as a clean event study) [snippet-only, cross-checked] |
| **Sun & Abraham** | Interaction-weighted event study: saturate in cohort × relative-time so no coefficient borrows from another period's effect [snippet-only, cross-checked] |
| **de Chaisemartin & D'Haultfœuille** | Estimators built from clean switcher-vs-not-yet-switcher comparisons, plus a **diagnostic that reports how much negative weight** your TWFE spec carries [snippet-only, cross-checked] |
| **Imputation / Borusyak–Jaravel–Spiess** | Fit the untreated potential outcome on untreated observations only, impute it for treated ones, average the residuals [background — verify] |

Practical rails:
- **Run the negative-weight diagnostic before defending a TWFE number.** "How much of my estimate
  rides on already-treated controls?" is answerable, and the answer is sometimes most of it.
- **Never-treated units are precious.** A design where every unit eventually adopts has no clean
  control at the end of the panel; the late adopters are carrying the identification.
- **Staggered timing is also a pre-trends question**, cohort by cohort — a group that adopted
  *because* things were going badly is a parallel-trends failure no estimator repairs.
- **Honest scope on all of this:** these are active methods, and which to prefer depends on the
  design (cohort count, panel length, whether treatment can switch off). Do not present any one of
  them as *the* fix; present "we used a staggered-adoption estimator and here is which one and
  why" as the minimum standard, and check the current guidance before publishing
  [background — verify].
- Fixing the estimator does not fix the inference problem from §5. Eight offices is still eight
  clusters.

## 6. Instrumental variables in plain terms

When confounding between X and Y looks hopeless, look for an **instrument**: a variable that
(a) genuinely moves X (*relevance* — show it in the data), (b) affects Y only through X
(*exclusion* — argue it in words; no test exists), and (c) isn't itself caused by the
confounders (*independence*). The IV estimate then uses only the slice of X's variation that
the instrument produced — variation that is as-good-as-random with respect to the confounders.

Domain-neutral shapes: assignment quirks (which analyst/judge/reviewer a case happened to draw),
distance or timing accidents (a deadline landing on a holiday), eligibility rules that nudge
uptake without forcing it. The permanent caution: instruments fail quietly on exclusion — a
"weather" instrument for attendance fails if weather also directly changes the outcome.

### Weak instruments: the failure that hides behind a significant first stage

"Relevance is testable — show it in the data" is true and not sufficient, because the thing to show
is **strength**, and a first stage can be statistically significant while being far too weak to use.

- **A weak instrument biases 2SLS toward OLS** — toward the confounded answer the instrument was
  supposed to rescue you from. The relative-bias approximation behind the standard rule of thumb is
  roughly `1/(1 + C)` in the concentration parameter C, so as the instrument's explanatory power
  goes to zero, the 2SLS bias approaches the OLS bias [snippet-only, cross-checked]. This is the
  trap's cruel shape: the estimate looks like an escape from confounding and is quietly a
  re-run of it, now with wider intervals and a methods section that sounds rigorous.
- **Coverage collapses too.** With a weak instrument the conventional 2SLS confidence interval
  undercovers badly — a nominal 95% interval that contains the truth far less than 95% of the time
  — because the finite-sample distribution of the estimator is nothing like the normal the interval
  assumes.
- **The heuristic, with its provenance and its limits.** Report the **first-stage F**. Staiger &
  Stock (1997) proposed the rule of thumb F > 10 for a single instrument, and Stock & Yogo (2005)
  gave it a formal basis by tying critical values to a bound on either the maximum relative bias of
  2SLS versus OLS (~10%) or the maximum size distortion of Wald tests [snippet-only,
  cross-checked]. Honest hedge, because this is where the folklore stops: **F > 10 is a floor, not
  a certificate.** Later work shows the rule does not guarantee correct size for the IV t-test and
  argues for a substantially higher bar; treat 10 as "below this, stop," not "above this, relax"
  [snippet-only, cross-checked].
- **When strength is marginal, change the inference, not the adjectives.** Weak-instrument-robust
  procedures — the Anderson–Rubin test and its confidence sets are the standard example — stay
  valid whatever the instrument's strength, at the cost of wider (sometimes unbounded) intervals
  [background — verify]. An unbounded interval is an honest answer. "The first stage was
  significant (p = 0.03)" is not.

### The LATE scope rail: whose effect did you just estimate?

RD gets told plainly that it identifies the effect **at the cutoff** (§7 step 4). IV owes the same
sentence, and it is easier to forget because IV produces a single number with no visible boundary.

**With a binary instrument and heterogeneous effects, IV identifies the Local Average Treatment
Effect — the average effect among *compliers*: the units whose treatment status the instrument
actually moved.** It is not the population ATE, and not the effect on the treated, unless compliers
happen to resemble everyone else. The extra assumption that buys the interpretation is
**monotonicity (no defiers)**: nobody is pushed the *opposite* way by the instrument (Imbens &
Angrist 1994) [snippet-only, cross-checked].

Three consequences worth stating in a writeup:

1. **Name the compliers in words.** With a "which reviewer the case happened to draw" instrument,
   the estimate speaks for cases whose handling genuinely turns on the reviewer draw — not for the
   obvious ones that would go the same way with any reviewer, and not for the ones no reviewer
   would ever move. Phrase it the way RD does: *"this is the effect for the cases the assignment
   lottery actually swung, not for the portfolio."*
2. **The first stage is not just a strength check — it is the complier share.** With a binary
   instrument and binary treatment under monotonicity, `P(D=1 | Z=1) − P(D=1 | Z=0)` **is** the
   proportion of compliers. So a first stage of 0.08 is telling you two things at once: the
   instrument is weak, *and* the estimate is an average over roughly 8% of your sample. Report that
   percentage next to the estimate.
3. **Two valid instruments can legitimately disagree.** They define different complier
   subpopulations, so different LATEs are not necessarily a contradiction — and "our two IVs give
   different numbers, so one must be broken" is a reasoning error. (It is also not a licence: an
   *implausible* gap is still evidence that exclusion fails somewhere.)

Provenance lesson worth teaching with the method: IV first appears in Philip G. Wright's *The
Tariff on Animal and Vegetable Oils* (1928), Appendix B — structural supply/demand equations,
weather as an instrument, even an early path-diagram. Whether Philip or his son Sewall (the
path-analysis inventor) wrote it stayed an open question for 75 years, until Stock & Trebbi
(*J. Economic Perspectives* 2003) settled it by **stylometric analysis: Philip wrote Appendix
B** [snippet-only, cross-checked]. Evidence-based citation hygiene, applied to the method's own
birth certificate.

## 7. Worked example B — regression discontinuity

*"The threshold is your experiment."* Accounts scoring ≥ 700 on an internal risk model got the
streamlined approval flow; accounts below did not. Did streamlining cause faster funding?

1. **Plot the outcome against the running variable** (score), separately on each side of 700.
   The causal estimate is the *jump* in the fitted lines at the cutoff — units at 698 vs 702
   are nearly identical except for treatment.
2. **Stay local.** Use a bandwidth around the cutoff (e.g., 650–750) rather than the whole
   range; report how the estimate moves as the bandwidth shrinks. A jump that only appears with
   the widest window is curve-fitting, not a discontinuity.
3. **Check for manipulation.** Histogram the running variable: a pile-up just above 700 means
   someone could steer scores across the line (resubmissions, discretionary bumps) — the
   comparability assumption dies. Also check that other covariates move *smoothly* through the
   cutoff; only treatment should jump.
4. **State the scope honestly.** RD identifies the effect *at the cutoff* — for accounts near
   700, not for the whole portfolio.

Same template fits any score/date/size line: tickets created after date Y got the new routing;
matters above a dollar threshold got senior review. Lineage: Thistlethwaite & Campbell,
"Regression-Discontinuity Analysis: An Alternative to the Ex Post Facto Experiment"
(*J. Educational Psychology* 1960) — near-winners of the 1957 National Merit program, assigned
by test-score threshold (5,126 Certificate of Merit recipients vs 2,848 commendation-letter
recipients) [snippet-only, cross-checked]. Citation-hygiene footnote: the first author's name
is spelled "Thistlewaite" in some bibliographic records — cite carefully [snippet-only,
cross-checked].

## 8. Hill's viewpoints, as Hill meant them

Austin Bradford Hill, "The Environment and Disease: Association or Causation?" (*Proc. Royal
Society of Medicine* 1965) offered nine considerations for judging whether an association is
causal: **strength, consistency, specificity, temporality, biological gradient (dose-response),
plausibility, coherence, experiment, analogy** [snippet-only, cross-checked].

The load-bearing honesty point: **Hill never said "criteria."** He called them viewpoints and
wrote that none "can bring indisputable evidence for or against the cause-and-effect
hypothesis and none can be required as a sine qua non" — explicitly disclaiming "hard-and-fast
rules of evidence." The nine-box checklist that circulates under his name inverts his position.
In the same lecture he also cautioned against over-reliance on significance tests
[snippet-only, cross-checked].

How to use them as he did — as the shape of an argument about *total* evidence:
- Lead with **temporality** (the only one that is close to non-negotiable: causes precede effects).
- Use **strength, gradient, consistency** to ask how hard the association is to explain away —
  a large, dose-responsive, everywhere-replicated association needs a large, dose-responsive,
  everywhere-present confounder.
- Use **plausibility, coherence, analogy** as context, stated with their era-bound weakness:
  plausibility is limited by current knowledge.
- Use **experiment** as the invitation: does any semi-experimental evidence (a rung from §4)
  exist or could it be created?
- Never total a score. A viewpoint absent is a question, not a disqualification — and eight
  boxes ticked is not proof.

## 9. The humility rail: sensitivity and limits

What observational data cannot tell you, said plainly in every deliverable:
- It cannot prove the counterfactual; it can only make rival explanations harder to sustain.
- It cannot rule out confounders nobody measured; "we adjusted for everything we had" is an
  inventory statement, not an identification argument.
- A small p-value is an association statement — the significance machinery (and its correct
  interpretation) lives in `data-analytics-bi-skills:statistical-inference`, and none of it
  substitutes for design.

Sensitivity thinking, in plain words: ask **"how strong would an unmeasured confounder have to
be to erase this estimate?"** Sketch the answer by comparison — "to wipe out the −2.0-day
effect, a hidden factor would need to shift resolution times by more than seasonality does, in
Denver only, timed to the rollout." If a mundane candidate clears the bar (a staffing change, a
mix shift, a measurement change), name it, check it if you can, and downgrade the claim if you
can't. State conclusions at the strength the design earns: "consistent with a causal effect
under parallel trends" is a finding; "proves the form caused it" is not.

### Answer that question with a named method, not a feeling

Asked without a method, "how strong would a confounder have to be?" gets answered by whoever
speaks with most confidence. Two named quantifications, both reportable:

- **E-value** (VanderWeele & Ding, *Annals of Internal Medicine* 2017 [snippet-only,
  cross-checked]). The minimum strength of association — on the **risk-ratio scale** — that an
  unmeasured confounder would need to have with *both* the exposure and the outcome, beyond the
  measured covariates, to fully explain away the observed association. Report it for the point
  estimate **and** for the confidence limit nearest the null: a finding whose point estimate needs
  a confounder of 2.5 but whose lower limit needs only 1.1 is fragile. The interpretation is
  comparative, and that is the whole value: an E-value of 1.3 sitting beside measured risk factors
  that already carry risk ratios near 2 says "a confounder no stronger than ones we know about
  could erase this." Two limits to state: it lives on a ratio scale (differences and standardized
  mean differences need the published conversion), and it is a *minimum* — a bound, not a
  probability that confounding exists.
- **Rosenbaum bounds** (Rosenbaum's sensitivity analysis for matched observational studies
  [snippet-only, cross-checked]). For a matched design, Γ (gamma) asks how much two units matched
  on covariates could differ in their *odds* of treatment before the study's conclusion stops
  holding. Reported as "the result is insensitive to hidden bias up to Γ ≈ 1.8." Same comparative
  logic: Γ = 1.1 means a whisper of hidden selection undoes the finding.
- **Negative controls**, the design-side sibling: a negative-control *outcome* the treatment cannot
  plausibly affect, or a negative-control *exposure* that shares the suspected confounding but not
  the causal path. If the "effect" also shows up where it cannot exist, you have found your
  confounder rather than your effect. (The DiD placebo window in §5 is exactly this move in time.)

Neither number rules confounding out. Both convert an unfalsifiable objection ("but there could be
something else") into a quantity a reader can argue with — which is the most an observational
design can offer, and much more than a vibe.
