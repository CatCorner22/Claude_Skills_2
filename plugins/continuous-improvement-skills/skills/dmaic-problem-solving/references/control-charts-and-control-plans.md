# Control charts and the control plan

The Control phase's machinery: which chart, what its limits are, when the chart stops being able
to tell you anything, which signal rules to arm and what they cost, and what a control plan
contains such that the gain survives the project team's departure. The charts are also what the
Measure phase uses to establish stability and what Improve uses to prove a shift is real — so read
this before the baseline, not after the rollout.

## Contents
- §1 Common cause vs special cause — the two mistakes
- §2 Choosing the chart
- §3 The limit formulas you will actually use
- §4 When the chart cannot work (failure envelope)
- §5 Signal rules and what each one costs
- §6 Recomputing limits — the goalpost rule
- §7 The control plan contract, item by item
- §8 Ownership, handoff, and the 30/60/90 audit

## §1 Common cause vs special cause — the two mistakes

Every measurement varies. A control chart exists to answer one question: **is this variation the
process being itself, or is something new acting on it?** Deming named the two ways of getting
that wrong, and both are expensive:

- **Mistake 1 — reacting to noise as if it were signal (tampering).** Adjusting a stable process
  in response to an ordinary point makes its variation *worse*, not better, because the adjustment
  is uncorrelated with the deviation and adds its own. In the worked project, week 19's 9.0%
  reopen rate sat well inside a 4.89–10.55% band; a "root-cause review" of week 19 would have
  produced a plausible story, a process change, and more variation.
- **Mistake 2 — dismissing a signal as noise.** The complement, and the one that turns an
  early-warning system into an ornament: a genuine new failure mode explained away as a blip
  because someone can always name a reason a week was unusual.

The chart's whole value is that it decides between the two by a rule set in advance, before anyone
has an interest in the answer. That is also why the rules must be written into the control plan
rather than left to judgement: a rule chosen after seeing the point is not a rule.
(`continuous-improvement-skills:lean-six-sigma-for-software` carries this same material translated
to delivery metrics and pipelines.)

## §2 Choosing the chart

Two questions decide it. First: **is the measurement continuous or a count?** Second, for counts:
**can one unit carry more than one defect?**

| Your data | Chart | Subgroup |
|---|---|---|
| Continuous, several measurements per period | X̄-R (subgroup ≤ 8) or X̄-S (larger) | The rational subgroup |
| Continuous, one measurement per period | I-MR (individuals + moving range) | The single value |
| Pass/fail per unit, subgroup size varies | **p-chart** (proportion defective) | The period's units |
| Pass/fail per unit, subgroup size constant | np-chart (count defective) | The period's units |
| Defects per unit, constant opportunity | c-chart | The inspection unit |
| Defects per unit, varying opportunity | u-chart | The period's opportunity |

The count question is the one people get wrong: a ticket either reopened or did not, so reopens
are a **p-chart**; typographical errors per document can be several per document, so those are a
**c/u-chart**. Using a p-chart on multi-defect counts understates the variation and produces a
chart that signals constantly.

**Rational subgrouping is the decision that matters more than the formula.** Group so that within
a subgroup only common-cause variation can act, and the thing you want to detect acts *between*
subgroups. Weekly subgroups on a desk with a strong day-of-week pattern bury that pattern inside
the subgroup — which is correct if you want to detect week-to-week shifts, and wrong if the
day-of-week pattern is the problem. Pick the subgroup to match the shift you need to catch.

## §3 The limit formulas you will actually use

All are centerline ± 3 standard deviations of the *plotted statistic*.

- **p-chart:** centerline p̄ = (total defectives) / (total units).
  σ_i = √(p̄(1 − p̄) / n_i); limits = p̄ ± 3σ_i. **Limits vary with n_i** — a week with half the
  volume gets wider limits, and drawing one flat pair of limits over a varying denominator is the
  most common p-chart error.
- **np-chart** (constant n): centerline n·p̄; limits = n·p̄ ± 3√(n·p̄(1 − p̄)).
- **c-chart:** centerline c̄; limits = c̄ ± 3√c̄.
- **u-chart:** centerline ū; limits = ū ± 3√(ū / n_i).
- **I-MR:** σ̂ = MR̄ / 1.128, where MR̄ is the mean of the successive absolute differences.
  Individuals limits = X̄ ± 3σ̂ = X̄ ± 2.66·MR̄ (since 3 / 1.128 ≈ 2.66). Moving-range chart:
  UCL = 3.267·MR̄, LCL = 0.
- **X̄-R:** X̄̄ ± A₂·R̄ for the averages; D₃·R̄ and D₄·R̄ for the range. Standard constants by
  subgroup size (check against your own reference table before relying on them):

| n | A₂ | D₃ | D₄ | d₂ |
|---|---|---|---|---|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |

Note what the constants encode: **σ is estimated from *within*-subgroup spread** (R̄/d₂), never
from the standard deviation of all the data pooled together. Pooling folds any between-subgroup
shift into σ, which widens the limits by exactly the amount of the thing you are trying to detect
— the chart then declares a drifting process to be in control. If your limits look suspiciously
generous, check whether someone computed σ with a spreadsheet's STDEV over the whole column.

## §4 When the chart cannot work (failure envelope)

Four conditions under which a control chart returns confident nonsense. Check all four before
trusting limits.

**1. The lower limit collapses to zero (rare events).** LCL = p̄ − 3√(p̄(1−p̄)/n) falls below zero
exactly when n·p̄ < 9(1 − p̄) — for small p̄, roughly **when the expected defects per subgroup is
under 9**. The chart then has no lower limit at all: it can detect deterioration and can *never*
confirm an improvement from a single point. What you see: a chart with a floor at zero, occasional
spikes, and no way to answer "did it get better?" Fixes, in order of preference: enlarge the
subgroup until n·p̄ ≥ 9 (aggregate to months rather than weeks); chart **time between events** on
an I-MR chart instead of a rate, which is the right tool for genuinely rare defects; or accept
that you will need run rules and many periods. In the worked project n·p̄ = 800 × 0.095 = 76,
comfortably clear.

**2. Overdispersion (the limits are too tight).** p/np/c/u limits assume binomial or Poisson
variation and nothing else. Real periods differ in ways the model does not know about — mix,
staffing, seasonality — and the true period-to-period variation exceeds the theoretical. What you
see: a chart where a third of the points are outside the limits and every investigation ends in
"nothing special happened." Diagnostic: standardize each point, z_i = (p_i − p̄)/σ_i, take the mean
moving range of the z series, and compute σ_z = MR̄_z / 1.128. If σ_z ≈ 1 the binomial model holds.
Materially above 1 and the limits are too tight by that factor — multiply them by σ_z (this is the
p′ chart, due to Laney) or chart the rate on an I-MR chart, which estimates variation empirically
and sidesteps the assumption entirely. Around 1.2 is the usual "borderline, proceed with a note";
by 1.4 switch. The worked project's baseline returns σ_z ≈ 1.20 — usable, flagged, and worth
re-checking as data accumulates.

**3. Too few subgroups.** Limits computed from a handful of subgroups carry so much sampling error
*in the limits themselves* that the chart signals on its own estimation noise. The customary
minimum is **20–25 subgroups** before limits are treated as established. Below that, plot the
data, call the limits provisional, and recompute when you reach 25. What you see if you ignore
this: limits that move noticeably every time you add data, and early "signals" that vanish on
recomputation.

**4. Autocorrelation and slow processes.** If each point depends on the previous one — a backlog,
a queue, an inventory level, anything with memory — successive points are not independent draws,
run rules fire constantly, and the 3σ limits are wrong. What you see: long smooth excursions that
trip the 8-points rule with no assignable cause. Chart the *differences*, or model the
autocorrelation, or chart a different statistic. Separately, if the process produces one number
per quarter, 25 subgroups is six years: SPC is simply unavailable on that timescale and you are
back to a before/after comparison with all of its confounding — say so rather than drawing limits
from five points.

## §5 Signal rules and what each one costs

Arm rules deliberately. Each adds detection power and each adds false alarms, and the arithmetic
is not intuitive.

| Rule | Detects | False-alarm rate on a stable process |
|---|---|---|
| One point beyond 3σ | Large sudden shift | 2 × (1 − Φ(3)) ≈ 0.0027 → ~1 in 370 points |
| 8 consecutive points on one side of the centerline | Sustained moderate shift | 2 × 0.5^8 = 0.0078125 → ~1 in 128 |
| 2 of 3 consecutive beyond 2σ, same side | Moderate shift, faster than the 8-rule | ≈ 0.0031 → ~1 in 327 |
| 4 of 5 consecutive beyond 1σ, same side | Small sustained shift | ≈ 0.0055 → ~1 in 181 |

**The number nobody computes — and do not compute it by adding the column.** Summing the four
rates (0.0027 + 0.0078 + 0.0031 + 0.0055 ≈ 0.019, "one alarm every 52 points") is wrong, because
the rules overlap heavily: a point beyond 3σ is also beyond 2σ and beyond 1σ and sits on one side
of the centerline, so it can satisfy several rules at once, and the run rules share the same
points as they slide. Union ≠ sum. The correct figure comes from the run-length distribution:
**ARL₀ ≈ 92 points with all four armed** — a false-alarm rate of about **0.011 per point**, not
0.019. (Verified two independent ways: a Markov chain over the rule state space, and a 40,000-run
Monte Carlo giving 91.6 ± 0.4. The same machinery reproduces the two known closed forms — 370.4
for the 3σ rule alone and 255 for the 8-in-a-row rule alone — so it is calibrated.)

Read that as: on a weekly chart, a spurious investigation roughly every other year. On a daily
chart, one every three months. On an hourly chart, about two a week — which is still how a
control chart trains its owner to ignore it. Match the rule set to the plotting frequency and to
how expensive an investigation is: high-frequency charts with cheap consequences get the 3σ rule
only. The general lesson outlives these four rules: **whenever you arm several detectors on one
stream, the combined false-alarm rate must be derived from the run-length distribution, never by
adding the individual rates** — adding overstates it whenever the detectors can fire together.

The 3σ limit rule alone detects large shifts immediately and moderate shifts almost never — the
worked project's 1.7σ improvement produced eight consecutive weeks below the old centerline and
**not one point outside the old limits**. If the shift you care about is smaller than about 2σ of
the plotted statistic, the run rules are not optional decoration; they are the detection.

## §6 Recomputing limits — the goalpost rule

Recompute limits when, and only when, a **deliberate, documented change** to the process has
occurred and enough new subgroups exist to estimate the new level. Record the date, the change,
and the data range the new limits came from, on the chart.

Never recompute because points are signalling. Recalculating limits to absorb out-of-control
points is the SPC form of moving the goalposts: it converts every special cause into common cause
by definition, and the chart stops being able to say anything. The tell is a chart whose limits
step outward every few months with no change log beside the steps.

Two related disciplines: keep the *old* limits visible on the chart for a period after a
recompute, so the shift is legible to someone reading it later; and freeze limits during a pilot
rather than letting them absorb the pilot's own effect.

## §7 The control plan contract, item by item

A control plan is not a paragraph promising to keep an eye on things. One row per controlled
characteristic, each row carrying all eleven fields:

1. **Characteristic** — what is controlled, in CTQ terms.
2. **Operational definition** — version-stamped, with inclusions and exclusions, identical to the
   one frozen at the Measure tollgate.
3. **Data source and extraction** — the system, the query or report, and who runs it. A metric
   whose extraction lives in one person's saved filter is already broken.
4. **Chart type and subgroup rule** — including how varying subgroup size is handled.
5. **Centerline and limits, with their provenance** — the value, the date computed, and the data
   range they came from.
6. **Signal rules in force** — named explicitly, from §5, chosen for this plotting frequency.
7. **Reaction plan** — written as if-then, with the *authority* attached: "if two consecutive
   points exceed the UCL, the desk lead pauses cache-clear closures in the affected area and
   raises a P2 to engineering — no further approval required." A reaction plan whose first step is
   "escalate for a decision" is a delay, not a plan.
8. **Escalation** — what happens, and who is told, if the reaction plan does not restore control
   within a stated period.
9. **Owner** — one named individual, plus a named deputy. Not a team, not a role, not a dashboard.
10. **Review cadence and evidence** — when they look, and where the record that they looked lives.
11. **Recompute rule** — the §6 conditions and who approves a recompute.

Fields 5, 7 and 9 are the ones that decay first. A plan whose limits carry no provenance cannot be
audited; a reaction plan without pre-granted authority converts a signal into a meeting; and an
ownerless plan is a document, not a control.

## §8 Ownership, handoff, and the 30/60/90 audit

**Handoff is an event with a deliverable, not an email.** The process owner accepts the control
plan in a working session where they run the extraction themselves, read the current chart, and
state aloud what they would do at a signal. If they cannot do those three things unaided, the
handoff has not happened regardless of what was signed.
(`safety-and-reliability-skills:sbar-structured-communication` supplies a format for the handoff
itself; `continuous-improvement-skills:standard-work` owns the document the change is encoded in,
which must carry a revision number so a later drift can be dated.)

**The three ways ownership fails, and what each looks like:**

- *The dashboard owner.* The metric is on a dashboard nobody has an appointment with. Symptom: at
  the 90-day audit the chart is current and no one can say what it did last month. Fix: the review
  is a calendar entry with a person's name, and it produces a written line each time — even "in
  control, no action."
- *The owner who cannot act.* The named owner watches a metric driven by a process they do not
  control. Symptom: signals are logged and escalated, and nothing changes. This is a Define-phase
  failure surfacing late — the scope was drawn wider than the sponsor's authority. Fix: move
  ownership to the authority, or narrow what is controlled.
- *The departed owner.* The owner changes role and the plan does not. Symptom: an unopened chart
  and a metric that has drifted back to baseline. Fix: name a deputy in field 9 from the start, and
  make control-plan handover an explicit item in the role's transition.

**The audit schedule.** Check at **30 days** that the chart is being produced and the reaction plan
has been exercised at least once (deliberately, if no real signal has occurred — an untested
reaction plan is scenery). At **60 days**, that the standard work matches what people actually do,
by watching rather than asking. At **90 days**, that the level has held and the limits still fit
the data; this is the point where the project team formally stops owning it.

**The revert signature.** Gains almost never collapse; they erode. What you see is a slow return
toward the old centerline over one to two quarters, usually beginning with an exception granted
for a busy period that is never withdrawn. Watch for the 8-points-on-one-side rule firing on the
*wrong* side — that is the erosion announcing itself, and it is the single most useful thing a
control chart does after the project ends.
