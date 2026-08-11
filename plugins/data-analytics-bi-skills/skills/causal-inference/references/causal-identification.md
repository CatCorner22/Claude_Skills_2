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
5. [Worked example A — difference-in-differences](#5-worked-example-a--difference-in-differences)
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
- Conclusion someone will draw from the filtered data: "our experienced people get the mild
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
   together. Checkable in part: pre-period trend plots, placebo windows.
3. **Instrumental variable (IV).** Something nudges X without touching Y except through X.
   Key assumptions: **relevance** (it really moves X — testable) and **exclusion** (no other
   path to Y — an argument, not a test).
4. **Regression discontinuity (RD).** A cutoff on a score/date/size assigns treatment.
   Key assumption: units just above and just below the cutoff are comparable — no one
   manipulated their position. Checkable in part: density/bunching at the cutoff, covariate
   smoothness.
5. **Adjustment only.** Backdoor-valid covariate adjustment with no design behind it — the
   weakest rung; every conclusion inherits "assuming no unmeasured confounder," so §9 is
   mandatory here.

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

Lineage: the modern canon is Card & Krueger's minimum-wage study (*AER* 1994 — NJ raised its
minimum wage $4.25→$5.05 in April 1992, PA did not; 331 NJ + 79 eastern-PA fast-food
restaurants surveyed before and after; DiD ≈ +2.75 FTE, no detectable employment loss)
[snippet-only, cross-checked]. Honesty note, load-bearing: the finding was and is contested
(payroll-data re-analyses and a long debate); the *method* — credible design from a policy
discontinuity — survived the fight and reshaped empirical economics, while the specific
employment estimate remains argued [snippet-only, cross-checked]. DiD reasoning itself is far
older; John Snow's cholera comparison is the commonly cited precursor [background — verify].

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
