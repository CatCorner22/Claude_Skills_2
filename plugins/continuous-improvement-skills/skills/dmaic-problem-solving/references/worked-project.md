# One DMAIC project, carried end to end

A single improvement project worked through all five phases with real numbers, so the method is
visible producing artifacts rather than described. Every figure recomputes; substitute your own
and the shape holds. The domain is deliberately ordinary — an internal support desk — because the
mechanics transfer and the arithmetic is checkable.

## Contents
- The project in one line
- Define — the charter that survived the tollgate
- Measure — the definition that moved the number, then the baseline
- Analyze — Pareto with denominators, then the mechanism fingerprint
- Improve — selection, pilot, and the denominator trap
- Control — the chart that proved it held, and the goal that was missed
- The finished package (deliverable contract)

## The project in one line

Tickets closed by an internal support desk are reopened by their requesters too often. Rework is
invisible in the team's throughput numbers (a reopened ticket is counted as two closures) and
visible to everyone who files one.

---

## Define — the charter that survived the tollgate

**Problem statement (quantified, blame-free).** "Over the last 12 weeks, 12.0% of closed tickets
were reopened by the requester. In this desk's own handling-time data a reopened ticket costs about
twice a first-time resolution, and reopens are the most frequent theme in requester feedback." No cause named, no team
named, no solution named.

**Goal.** Reduce the reopen rate to **≤ 6.0%** within two quarters, without increasing median
time-to-close.

The second clause is not decoration. A reopen-rate target with no counterweight is trivially met
by never closing anything — the goal statement has to name the metric the fix is most likely to
push in the wrong direction, or you will improve one number by exporting the problem into
another. That counterweight metric gets baselined and charted alongside the primary one.

**Scope, via SIPOC.** Start: ticket marked resolved by an agent. End: 14 days after closure.
In scope: closure decision, closure notes, requester notification. Out of scope: intake,
triage, routing, and the engineering backlog that produces underlying defects. The scope test
that mattered: *can the sponsor authorize every change inside this boundary?* The desk manager
could change closure practice; she could not change the engineering backlog. That is why the
backlog is out of scope — and it is why the project later had to escalate rather than act.

**VOC → CTQ.** Requester interviews (11 of them, not a survey) said the same thing three ways:
"it came back," "I had to re-explain everything," "nobody told me it was a workaround." Two CTQs:

| Customer need | CTQ characteristic | Spec |
|---|---|---|
| "It stays fixed" | Reopen within 14 days of closure | 0 per ticket; ≤ 6% of closures |
| "Tell me if it's temporary" | Closure note states permanent fix or workaround | 100% of closures classified |

The second CTQ looks like a documentation nicety. It became the stratifying variable that found
the cause — which is the usual fate of a well-written CTQ: it makes a distinction the data did
not previously carry.

**Tollgate outcome:** passed, with one condition. The sponsor could not answer "what fraction of
reopens do we expect to be genuinely unavoidable?", so the 6.0% target was recorded as an
*aspiration pending Analyze*, not a commitment. Recording the softness at Define is what let the
project end honestly instead of arguing about the goalpost at Control.

---

## Measure — the definition that moved the number, then the baseline

**Operational definition, v1.** "A ticket is *reopened* if its status returns to open after being
set to resolved." Two reviewers independently classified the same 60 resolved-then-reopened
tickets under v1 and agreed on **51 / 60 = 85%** — below the 90% bar this desk uses for attribute
agreement (`continuous-improvement-skills:measurement-systems-analysis` owns the study design and
the κ arithmetic).

All nine disagreements were the same thing: the requester replied "thanks, that worked," and the
ticketing tool reopened the ticket on inbound mail. One reviewer counted those, the other did not.

**Operational definition, v2 (frozen).** "A ticket is *reopened* if it returns to open **and** the
requester's message describes the original problem persisting or recurring. Courtesy replies,
new unrelated requests, and agent-initiated reopens for administrative correction do not count."
Re-run on a fresh 60: **57 / 60 = 95%**. Passed.

**This is where the most common DMAIC lie gets told, and where it gets prevented.** Reclassifying
the same 12 weeks under v2 moved the number from **1,152 reopens (12.0%)** to **912 reopens
(9.5%)** — a 2.5-point "improvement" produced entirely by a definition change, before anyone
touched the process. Because it happened *before* the baseline was frozen, it is a correction.
Had the same change landed during Improve, it would have manufactured most of the project's
claimed gain. Hence the rule: **the operational definition freezes at the Measure tollgate. If it
must change afterwards, every prior number is restated under the new definition and both versions
are shown.**

**Baseline.** 12 weeks, 800 closures per week, n = 9,600 closures, 912 reopens.

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Reopens | 70 | 82 | 75 | 68 | 91 | 77 | 84 | 72 | 79 | 88 | 63 | 63 |
| Rate % | 8.75 | 10.25 | 9.375 | 8.5 | 11.375 | 9.625 | 10.5 | 9.0 | 9.875 | 11.0 | 7.875 | 7.875 |

Baseline rate = 912 / 9600 = 0.095 → **9.5%**.

**Stability check before anything else.** p-chart limits at n = 800:
σ = √(0.095 × 0.905 / 800) = √0.000107469 ≈ **0.010367**;
UCL = 0.095 + 3 × 0.010367 = **0.126** (12.6%); LCL = 0.095 − 3 × 0.010367 = **0.0639** (6.39%).

All twelve points fall between 7.875% and 11.375% — inside the limits, no runs, no trend. The
process is **stable at a bad level**, which is the only condition under which a later shift can be
attributed to the change rather than to the process's own wandering. (Chart selection, limit
formulas, and the overdispersion check that qualifies these limits are in
`references/control-charts-and-control-plans.md`; that check returns σ_z ≈ 1.20 here, which on only
12 subgroups is inside what a perfectly binomial process produces about one time in five — recorded
and re-checked as data accumulates, not treated as evidence the limits are too tight.)

**Capability read.** Reopen/not-reopen is attribute data, so Cp/Cpk do not apply — those need
continuous measurements against two-sided specs (`continuous-improvement-skills:measurement-systems-analysis`
§6–7). The attribute equivalents: 0.095 × 1,000,000 = **95,000 DPMO**, which under the
conventional 1.5σ long-term shift is about a **2.8 sigma level**. Quote the DPMO; treat the sigma
level as a convention for comparing across processes, not as a measurement.

**The number that reframed the goal.** The charter target of 6.0% sits *below* the baseline LCL of
6.39%. Two consequences the team wrote down at the tollgate: the goal cannot be reached by luck —
it requires a genuine level shift, not a good week; and conversely, one week at 6.2% would be
ordinary noise and must not be reported as success.

**Tollgate outcome:** passed. Definition frozen and version-stamped, 12 subgroups of data (thin —
the desk's rule is 20–25 subgroups before limits are trusted, so the limits were flagged
provisional and stayed provisional: the rollout landed before another eight to thirteen
*pre-change* weeks could accumulate, and adding post-rollout weeks to a baseline would fold the
improvement into the very limits it is being measured against. The first firm limits this project
owns are the post-change ones computed in Control.)

---

## Analyze — Pareto with denominators, then the mechanism fingerprint

**Step 1: stratify by the CTQ-2 variable (closure reason), with denominators.**

| Closure reason | Closures | Reopens | Reopen rate |
|---|---|---|---|
| Workaround provided | 2,400 | 411 | 411 / 2400 = 17.1% |
| Permanent fix applied | 5,000 | 155 | 155 / 5000 = 3.1% |
| No response from requester | 1,800 | 274 | 274 / 1800 = 15.2% |
| Other / uncategorized | 400 | 72 | 72 / 400 = 18.0% |
| **Total** | **9,600** | **912** | 912 / 9600 = 9.5% |

Read it twice, because the two readings answer different questions. **By count**, workaround and
no-response together are 411 + 274 = 685 = 75.1% of all reopens — that is where the *volume* is,
and volume is what a Pareto ranks. **By rate**, "Other" is worst at 18.0% — that is where the
*mechanism* is most concentrated, but on 400 closures it can contribute at most 72 reopens. A team
that ranks only by rate chases a stratum too small to move the top-line metric; a team that ranks
only by count misses that "Other" is an uncategorized bucket hiding something. Both readings go in
the report; the project works count first and files a note to categorize "Other."

**Step 2: stratify the top stratum again.** Workaround closures by product area:

| Area | Workaround closures | Reopens | Rate |
|---|---|---|---|
| A | 1,100 | 96 | 96 / 1100 = 8.7% |
| B | 700 | 268 | 268 / 700 = 38.3% |
| C | 600 | 47 | 47 / 600 = 7.8% |
| **Total** | **2,400** | **411** | 411 / 2400 = 17.1% |

Area B holds 268 / 411 = 65.2% of workaround reopens at 4.6× the rate of A and C.

**Step 3: is it real, or is it 700 tickets of noise?** Two-proportion test, B against A+C pooled
(143 / 1700 = 8.4%):

- pooled p̂ = (268 + 143) / (700 + 1700) = 411 / 2400 = 0.17125
- SE = √(0.17125 × 0.82875 × (1/700 + 1/1700)) ≈ √0.000286232 ≈ 0.016918
- z = (0.382857 − 0.084118) / 0.016918 ≈ **17.7**

The honest reading is not "p < 0.001." It is that at these sample sizes the test is a formality —
a 30-point difference on 2,400 observations was never going to be noise, and the test's job here
is to document that someone checked, not to discover anything. Run the test when the difference is
small enough that you could be fooled; say so plainly when it isn't
(`data-analytics-bi-skills:statistical-inference` for the choice of test and its assumptions).

**Step 4: stratification found a location, not a cause.** "Area B" is a where, not a why, and
stopping here is the most common way Analyze fails while looking finished. Fishbone plus 5 Whys
with two Area B agents (`continuous-improvement-skills:root-cause-analysis`) produced a candidate
mechanism: the standard Area B workaround is "clear the local cache," which resolves the symptom;
the underlying configuration-sync defect recurs on the next scheduled sync, roughly every 10 days.

**Step 5: verify the mechanism with a prediction that could have failed.** If the mechanism is
right, Area B workaround reopens should not be spread evenly across the 14-day window — they
should cluster at the sync interval. Observed: **231 of 268 = 86.2%** of them reopened between
day 8 and day 12. Under an even spread across 14 days, a 5-day window would hold about 36%.

That clustered fingerprint is the actual verification, and it is worth more than the z of 17.7,
because it is a prediction the data could have refused. A cause is confirmed when you can state in
advance what the data must look like if you are right, and it looks like that. "The numbers are
big in Area B" is not confirmation; "reopens will pile up on days 8–12 and they do" is.

**Tollgate outcome:** passed, with the gap arithmetic on the record. The charter gap is 9.5% →
6.0% = 3.5 points = 336 reopens. Area B carries 290 reopens in total, so even driving them to
zero — an upper bound no fix reaches — leaves 622 / 9600 = **6.48%**, still above the 6.0% target.
The charter goal is therefore unreachable from this cause alone, whatever the fix achieves. Saying
that at the Analyze tollgate is what turned the missed target at Control from a failure into a
planned outcome.

Note which denominator that arithmetic used. 290 is about a third of the 912 *reopens*, but 86% of
the 336-reopen *gap to target* — two very different statements, and quoting the first while
meaning the second is the same denominator error this project spends the Improve phase avoiding.

---

## Improve — selection, pilot, and the denominator trap

**Candidates against the verified cause:**

| Candidate | Attacks | Effort | Risk | Decision |
|---|---|---|---|---|
| Fix the configuration-sync defect | The cause | High (engineering, ~6 weeks) | Low | **Pilot** |
| Forbid closing Area B tickets on cache-clear; route to engineering | The symptom's escape route | Low | Raises backlog and time-to-close | Hold as fallback |
| Add a 14-day follow-up email to every closure | Detection only | Low | Adds requester load; may *increase* measured reopens | Reject |
| Reclassify cache-clear closures as "pending" | Nothing | None | Moves the metric, not the process | Reject — this is metric surgery |

The last row is listed because a version of it gets proposed in nearly every project, usually with
a better disguise. The test that kills it: *would a requester notice the difference?* If no, it is
a reporting change wearing a solution's clothes.

**The sync fix is out of scope** (engineering backlog). The sponsor escalated rather than
descoping the project — an SBAR handoff to the engineering lead
(`safety-and-reliability-skills:sbar-structured-communication` supplies the format). The
escalation carried the day-8-to-12 fingerprint, which is why it was prioritized: it named a
specific defect with evidence, not a complaint about reopens.

**Pilot design.** Area B tenants only, 6 weeks, reversible by feature flag. Before running it, an
FMEA on the change (`continuous-improvement-skills:fmea`) surfaced one new failure mode worth a
guard: a sync fix that resolves conflicts by discarding the local copy would silently lose
requester-side configuration — silent success at D 9, so a reconciliation log was added.

**The denominator trap, avoided deliberately.** The pilot metric is reopen rate among **all Area B
closures**, not among Area B *workaround* closures. Fixing the defect removes workaround closures
as well as reopens; measured per workaround closure, numerator and denominator would both shrink
and the reported gain would understate — or, with a different change, wildly overstate — what the
process actually delivered. Whenever a change alters who enters the denominator, move the metric
up to a population the change cannot redefine.

Area B baseline on that population: 1,000 closures, 290 reopens = 29.0% (700 workaround closures
with 268 reopens, plus 300 other-reason closures with 22).

**Pilot result.** 6 weeks, 500 Area B closures, 58 reopens = 58 / 500 = **11.6%**, against 29.0%
baseline.

- pooled p̂ = (58 + 290) / (500 + 1000) = 348 / 1500 = 0.232
- SE = √(0.232 × 0.768 × (1/500 + 1/1000)) = √0.000534528 ≈ 0.023120
- z = (0.29 − 0.116) / 0.023120 ≈ **7.5**

**Two checks before believing it.** First, novelty: the last two weeks of the pilot were compared
against the first two separately, because a pilot everyone is watching improves for reasons that
do not survive the attention going away. No drift. Second, the counterweight metric: median
time-to-close was unchanged — the reopen gain was not bought by holding tickets open longer.

**Projection to the top-line metric, stated as a projection.** Holding every other stratum at
baseline, Area B's 12-week reopens fall from 290 to 1,000 × 0.116 = 116, so total reopens fall
from 912 to 912 − 290 + 116 = **738**, and the process rate becomes 738 / 9600 = 0.076875 →
**7.69%**. Against a 6.0% target. The project will not reach its charter goal.

**Tollgate outcome:** passed for rollout, failed for the charter goal, and both were written down.
The sponsor chose to roll out and re-charter the remaining gap as a second cycle against the
"no response from requester" stratum (274 reopens on 1,800 closures) rather than stretch this
project. Killing the goal is cheaper than stretching the project; a DMAIC cycle that is allowed to
expand until it hits its number stops being evidence of anything.

---

## Control — the chart that proved it held, and the goal that was missed

Full rollout, then 8 weeks of monitoring at 800 closures/week (n = 6,400):

| Week | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|
| Reopens | 62 | 59 | 67 | 56 | 64 | 60 | 72 | 54 |
| Rate % | 7.75 | 7.375 | 8.375 | 7.0 | 8.0 | 7.5 | 9.0 | 6.75 |

Observed rate = 494 / 6400 = 0.0771875 → **7.72%**, against the 7.69% projection. The projection
landing within 0.03 points is itself weak evidence that nothing else moved at the same time — a
large gap between projected and observed is a signal to go looking for a second change, in either
direction.

**How the shift was proved, and why the limit rule alone would have missed it.** Against the
*baseline* chart (centerline 9.5%, LCL 6.39%), **not one of the eight points is below the lower
control limit** — the lowest is 6.75%. A team watching only for out-of-limit points would have
seen eight ordinary weeks and concluded nothing had happened. What fires is the run rule: all
eight points fall below the old centerline. Under an unchanged process each point is a coin flip,
so eight on one side has probability 0.5^8 = 0.00390625, and two-sided 2 × 0.5^8 = 0.0078125 —
about 1 in 128. That is the formal evidence the level shifted.

This is the general lesson and it is why the run rules exist: **the 3σ limit rule detects large
shifts instantly and moderate shifts almost never.** The improvement here is about 1.7σ of the
weekly noise, comfortably invisible to the limit rule and obvious to the run rule.

**Then, and only then, recompute limits at the new level.** p̄ = 0.0771875, n = 800:
σ = √(0.0771875 × 0.9228125 / 800) ≈ **0.009436**;
UCL = 0.0771875 + 3 × 0.009436 = **0.1055** (10.55%); LCL = 0.0771875 − 3 × 0.009436 = **0.0489**
(4.89%). Limits are recomputed because a deliberate, documented process change occurred — never
because points were signalling. (See `references/control-charts-and-control-plans.md` §6.)

**The operating rule the desk now runs on:** a week between 4.89% and 10.55% is noise. Do nothing.
Week 19's 9.0% looked alarming in the stand-up and was ordinary variation; reacting to it would
have been textbook tampering.

**The honest ending.** Baseline 9.5% → sustained 7.72%, against a 6.0% goal:
(9.5 − 7.72) / (9.5 − 6.0) = 1.78 / 3.5 ≈ **51%** of the chartered gap closed. The charter was
closed as *partially met*, with the residual re-chartered. A project that reports "success"
against a goal it did not reach teaches the organization that DMAIC numbers are negotiable, which
costs more than the missing 1.7 points.

---

## The finished package (deliverable contract)

A DMAIC project is done when a stranger can audit it from these artifacts alone. Item by item:

1. **Signed charter** — quantified problem, measurable goal, named counterweight metric, scope
   boundary with the authority that matches it, sponsor, team, timebox.
2. **SIPOC** naming the process start and end points the metric is measured across.
3. **VOC record** — who was asked, how many, what they said, and the CTQ table that translates it
   into characteristics with specs.
4. **Operational definition, version-stamped and dated**, with its inclusion *and* exclusion rules
   written out, plus a note of any restatement and the number under both versions.
5. **Measurement-system evidence** — the agreement study, its result against the stated bar, and
   what was changed if it failed.
6. **Baseline** — the raw subgroup data (not just the mean), the run/control chart with limits,
   the stability verdict, and the subgroup count.
7. **Stratification tables with denominators**, not count-only Paretos.
8. **The verification of cause** — the prediction that was made in advance and the data that
   confirmed it, plus what would have refuted it.
9. **Gap arithmetic** — what fraction of the charter gap the verified cause can explain.
10. **Solution selection table** including the rejected candidates and why.
11. **Pilot design and result** — population, duration, reversibility mechanism, primary and
    counterweight metrics, the early-vs-late novelty check, and the comparison against baseline.
12. **New-risk review** (FMEA) of the change itself, with any guard added.
13. **Control plan** — the full contract in `references/control-charts-and-control-plans.md` §7.
14. **Standard work revision number** encoding the change
    (`continuous-improvement-skills:standard-work`).
15. **Named owner** — an individual, a review cadence, and a written if-then response rule.
16. **Post-rollout chart with the sustain evidence** and the recomputed limits, dated.
17. **Closure statement** saying plainly whether the goal was met, partially met, or missed, and
    what happened to the residual.

Items 4, 9, 15 and 17 are the ones most often absent, and each absence maps to a known failure
mode: no frozen definition invites metric drift, no gap arithmetic invites an unreachable goal, no
named owner guarantees the gain reverts, and no honest closure statement corrupts every future
project's numbers.
