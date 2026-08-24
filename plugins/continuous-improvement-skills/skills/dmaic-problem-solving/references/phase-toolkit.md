# DMAIC phase toolkit (reference)

Per-phase deliverable contracts, the tools each phase uses, and the tollgate questions that stop a
bad project — written as the questions plus **the answer that means "do not advance."** A tollgate
that only ever passes is a ceremony. For one project carried through all five phases with numbers,
see `references/worked-project.md`.

## Contents
- Define
- Measure
- Analyze
- Improve
- Control
- Tollgate discipline
- How DMAIC projects actually fail
- When DMAIC is the wrong machine

## Define

**Deliverable contract.** Charter (quantified blame-free problem statement, measurable goal, a
named *counterweight* metric the fix might damage, scope, business case, sponsor, team, timebox);
SIPOC with explicit start and end points; VOC record naming who was asked and what they said; CTQ
table translating each need into a characteristic with a spec.

**Tools:** SIPOC, VOC interviews (talk to people; a survey gives you your own words back), CTQ
tree (need → measurable characteristic → spec/limit), stakeholder map.

**Tollgate questions, with the failing answer:**
- *"Which solution are we going to implement?"* — **Failing answer: anyone can name one.** The
  project is a decision already made, looking for justification. Either kill it and just implement
  the thing, or restart Define with the solution explicitly out of scope.
- *"What is today's number, and where does it come from?"* — **Failing answer: a range, or "about,"
  or a recollection.** There is no problem statement yet, only a complaint.
- *"Who is the customer of this process, and what did they actually say?"* — **Failing answer: a
  manager's summary of what customers presumably want.** The CTQs are then guesses with specs
  attached, and specs derived from guesses will be met without anyone being happier.
- *"Can the sponsor authorize every change inside this scope?"* — **Failing answer: no, but we'll
  work with them.** A project whose fix lives outside its sponsor's authority dies in Improve,
  after all the measurement cost has been paid. Narrow the scope now or widen the authority now.
- *"What does the goal cost if we hit it?"* — **Failing answer: nothing.** Every real improvement
  trades against something; if no counterweight metric can be named, the goal is gameable.

**Phase failure envelope.** Define fails silently, and its failures surface two phases later. The
two that recur: a scope drawn to match ambition rather than authority, and a goal number chosen
because it is round rather than because anything supports it.

## Measure

**Deliverable contract.** Version-stamped operational definition with inclusion *and* exclusion
rules; data-collection plan (what, who, how, sample size, over what window); measurement-system
evidence against a stated bar; the baseline as raw subgroup data plus a chart, not a mean.

**Tools:** operational definitions tested by having two people count independently; attribute
agreement or gage R&R (`continuous-improvement-skills:measurement-systems-analysis` owns the study
design and the acceptance bars); run chart / control chart of the baseline
(`references/control-charts-and-control-plans.md`).

**Thresholds worth knowing before the tollgate:**
- **20–25 subgroups** before control limits are treated as established. Fewer, and the sampling
  error in the limits themselves makes the chart signal on its own noise; call them provisional
  and recompute.
- The baseline window must span **at least one full cycle of every known systematic driver** —
  month-end, seasonality, shift rotation, academic year. Otherwise the "improvement" you measure
  later may be the calendar.
- Attribute agreement bar in common use: **≥ 90% agreement**, with κ quoted alongside its base
  rate. Below it, fix the definition before collecting anything.

**Tollgate questions, with the failing answer:**
- *"If two people counted this independently, would they get the same number?"* — **Failing answer:
  probably.** Test it on 50–60 items; "probably" has been wrong every time it has been checked.
- *"Is the process stable at its current level?"* — **Failing answer: we haven't charted it.**
  A process with special-cause variation has no single baseline, and any later comparison is
  against a moving object. If it is unstable, the project's real first job is to remove the special
  causes, and that is a different (usually shorter) piece of work.
- *"Is the goal reachable without a level shift?"* — **Failing answer: nobody has compared the goal
  to the baseline's control limits.** If the target sits inside normal variation, the project can
  "succeed" on a lucky week; if it sits far below the LCL, the goal may be beyond what this process
  can do at all.
- *"Is the definition frozen?"* — **Failing answer: we'll refine it as we learn.** After this gate,
  any change to the definition forces a restatement of every prior number under both versions.

**Phase failure envelope.** Measure is where projects stall indefinitely, because data collection
has no natural end. Timebox it at Define. The opposite failure is baselining fast on data whose
definition nobody tested — cheaper to fix here than anywhere downstream, and unfixable after
Improve.

## Analyze

**Deliverable contract.** Stratification tables **with denominators**; the hypothesis that was
tested and the prediction it made in advance; the data that confirmed it and what would have
refuted it; the gap arithmetic — what fraction of the charter gap this cause can explain.

**Tools:** fishbone/6M and 5 Whys to *generate* hypotheses
(`continuous-improvement-skills:root-cause-analysis`); Pareto to prioritize; stratified comparison,
correlation, and hypothesis tests to *test* them (`data-analytics-bi-skills:statistical-inference`);
value-stream mapping when the problem is delay rather than defect
(the archived `continuous-improvement-skills:value-stream-mapping`); constraint analysis when the problem is
throughput (the archived `continuous-improvement-skills:theory-of-constraints`).

**Two rules that do most of the work:**
- **Pareto on counts, but always with denominators beside them.** Counts tell you where the volume
  is; rates tell you where the mechanism is. A stratum with the worst rate on a small base cannot
  move the top-line number; a stratum with the biggest count may simply be the biggest stratum.
- **A location is not a cause.** "Team B," "the night shift," "product area B" are where to look
  next, not answers. Analyze ends when you can state a mechanism.

**Tollgate questions, with the failing answer:**
- *"What would the data have looked like if this cause were wrong?"* — **Failing answer: silence.**
  A cause that made no falsifiable prediction was asserted, not verified, however much data was
  displayed beside it.
- *"What fraction of the gap does this cause explain?"* — **Failing answer: we haven't computed
  it.** If the verified cause accounts for a third of the gap, the charter goal is unreachable by
  this project, and the cheap moment to say so is now, not at Control.
- *"Is the stratifying variable confounded with something else that changed?"* — **Failing answer:
  we didn't check.** The classic: the "improved" region also got a new system, a new manager, and
  a volume drop in the same quarter.
- *"Did the analysis find a person?"* — **Failing answer: yes, and that's the finding.** Individual
  variation is nearly always the system's variation expressed through whoever is standing there.
  Keep going until you reach something a process change can act on.

**Phase failure envelope.** Analyze fails in two opposite directions: stopping at the first
plausible cause (usually the one someone suspected before the project started), and never
stopping — a search for the complete causal picture when the top cause plus a piloted fix would
have done. Set the exit condition at the tollgate: one verified cause explaining enough of the gap
to justify the Improve work.

## Improve

**Deliverable contract.** Candidate list scored on impact vs. effort/risk, including the rejected
options and why; the pilot's design (population, duration, reversibility mechanism, primary and
counterweight metrics); the pilot result compared to baseline with an effect size; the early-vs-late
novelty check; a new-risk review of the change itself; the projected effect on the top-line metric,
stated as a projection.

**Tools:** solution generation against the *verified* cause
(the archived `continuous-improvement-skills:structured-ideation`); error-proofing (poka-yoke) preferred over
added inspection; impact/effort or PICK selection; a reversible pilot;
`continuous-improvement-skills:fmea` on the change to catch risks it introduces; a designed
experiment when several candidate changes interact and one-at-a-time piloting would take too long
(`continuous-improvement-skills:design-of-experiments`); small-step tuning of live settings after
go-live (`continuous-improvement-skills:evolutionary-operation`).

**Tollgate questions, with the failing answer:**
- *"Could this pilot have failed?"* — **Failing answer: not really.** Sized too small to detect the
  effect, run only where it was expected to work, or judged by the people who designed it. A pilot
  that cannot produce a negative result is a demonstration.
- *"Can we turn it off?"* — **Failing answer: not easily.** Then it was a rollout, and the pilot
  language is providing false comfort about reversibility.
- *"Does the change alter who enters the denominator?"* — **Failing answer: we hadn't thought about
  it.** A fix that removes a category of work also removes it from the denominator, and the
  measured rate then moves for reasons unrelated to quality. Move the metric up to a population the
  change cannot redefine.
- *"What happened to the counterweight metric?"* — **Failing answer: we only measured the target.**
- *"Does the projected effect reach the charter goal?"* — **Failing answer: we'll see.** Compute it
  and say plainly whether the goal will be met, partially met, or missed. Deciding this before
  rollout is what allows an honest closure statement afterwards.

**Phase failure envelope.** Improve fails when the pilot's success came from the attention rather
than the change — guard by running long enough that novelty passes and comparing the pilot's last
weeks against its first. It also fails when the "solution" is a reporting change: the test is
whether a customer of the process would notice any difference.

## Control

**Deliverable contract.** Control plan with all eleven fields per row
(`references/control-charts-and-control-plans.md` §7); revised standard work with a revision number
(the archived `continuous-improvement-skills:standard-work`); a named individual owner and deputy; post-rollout
chart with sustain evidence and recomputed, provenance-stamped limits; a closure statement saying
whether the goal was met, partially met, or missed, and what happened to the residual.

**Tools:** control chart / SPC with an explicitly chosen rule set; poka-yoke and automated checks
in preference to added review steps; a formal handoff working session
(the archived `safety-and-reliability-skills:sbar-structured-communication` for the format); 30/60/90 audits.

**Tollgate questions, with the failing answer:**
- *"Name the person — not the team — who looks at this chart, and on what day."* — **Failing
  answer: a team, a role, or a dashboard.** There is no owner, and the gain has a shelf life of
  about two quarters.
- *"What do they do when it signals, and do they need anyone's permission?"* — **Failing answer:
  escalate for a decision.** That is a delay dressed as a response plan. Pre-grant the authority.
- *"Has the reaction plan ever been exercised?"* — **Failing answer: no signal yet.** Exercise it
  deliberately. An untested response plan is scenery.
- *"Which standard work document changed, and what is its revision number?"* — **Failing answer:
  we sent an email / we briefed the team.** Undocumented change cannot be audited and cannot be
  dated when it drifts.
- *"Did we meet the charter goal?"* — **Failing answer: a redefinition of the goal.** Report met,
  partially met, or missed, with the arithmetic. A project that renegotiates its target at closure
  devalues every number the organization's improvement programme will ever produce.

**Phase failure envelope.** Control is the phase teams skip because the interesting work is done
and the metric already looks better. Its characteristic failure is not collapse but **erosion**:
a slow return toward the old level over one to two quarters, usually starting with an exception
granted during a busy period and never withdrawn. The chart's 8-points-on-one-side rule firing on
the wrong side is what catches it.

## Tollgate discipline

Do not advance a phase until its deliverable contract is complete. Tollgates front-load rigor: each
checkpoint confirms the prior phase produced something trustworthy, which is far cheaper than
discovering it was hollow two phases later.

Three things make a tollgate real rather than ceremonial:

1. **It can end the project.** Killing at Define costs a week; killing at Control costs the whole
   project plus the credibility of the next one. Track how many of your tollgates have ever stopped
   anything — if the answer is none, they are status meetings.
2. **The reviewer is not the project team.** Someone with no stake in advancing asks the questions
   above and is allowed to be unsatisfied.
3. **The failing answers are written down in advance** — as above — so the gate is a comparison
   rather than a negotiation conducted by people who want to proceed.

## How DMAIC projects actually fail

Eight patterns, each with its symptom and its guard.

1. **Solving before measuring.** Symptom: Define finishes in a day and Measure drags for months,
   because the measurement's only job is to justify a decision already taken. Guard: the Define
   tollgate's "which solution?" question.
2. **The metric moved because the definition moved.** Symptom: the improvement appears in the
   reporting layer on exactly the date the definition or the extraction changed, and nowhere in
   the process. Guard: freeze the definition at the Measure tollgate; if it must change later,
   restate every prior number under both versions and show both.
3. **The denominator moved.** The subtler sibling: the fix removes a category of work from the
   population being measured, so the rate improves without the process improving. Guard: measure
   over a population the change cannot redefine.
4. **Regression to the mean sold as improvement.** Symptom: the project was chartered because last
   month was unusually bad, and the metric improves before the intervention lands. Guard: baseline
   long enough that the triggering period is one point among many, and check whether it was an
   out-of-limit point on the baseline chart.
5. **A control plan nobody owns.** Symptom: at the 90-day audit the chart is current, everyone
   agrees it is important, and nobody can say what it did last month. Guard: an individual owner
   with a deputy, a calendar entry, and a written line each review even when there is no action.
6. **The verified cause that was a location.** Symptom: the finding is a team, a shift, or a
   region. Guard: Analyze does not end until a mechanism is named that a process change can act on.
7. **Scope inflation.** Symptom: the charter's process boundary grows each month and the project
   acquires a second sponsor. Guard: scope is fixed at Define and changing it is a re-charter with
   a new tollgate, not an amendment.
8. **The stretched project.** Symptom: the timebox slips repeatedly and the definition of done
   moves toward whatever the data supports. Guard: partial credit is allowed. Close at the
   timebox, report the fraction of the gap closed, and re-charter the residual.

## When DMAIC is the wrong machine

DMAIC is expensive machinery and it has an operating envelope. Route elsewhere when:

- **The events are rare.** A defect occurring a handful of times a year cannot support a baseline,
  a stratified comparison, or a control chart with a usable lower limit
  (`references/control-charts-and-control-plans.md` §4). Investigate each occurrence properly
  instead: `continuous-improvement-skills:root-cause-analysis`.
- **The process cycle is long.** One number per quarter means 25 subgroups is six years. SPC is
  unavailable; be explicit that you are doing a before/after comparison with its confounds, and
  do not draw control limits from five points.
- **The cause is already known and the fix is obvious.** Just do it. The rigor exists to prevent
  changing the wrong thing, and when the right thing is not in doubt the rigor is pure cost →
  the archived `continuous-improvement-skills:kaizen-and-codesign`.
- **Nothing exists yet.** DMAIC improves a process that runs; designing a new one is DMADV/DFSS
  territory, where the customer requirement is decomposed into a design rather than a baseline
  (the archived `continuous-improvement-skills:qfd-house-of-quality` for the requirement decomposition,
  the archived `continuous-improvement-skills:lean-six-sigma-for-software` for the software case).
- **The process is wildly unstable.** With large special-cause variation there is no single
  baseline to improve against. Remove the special causes first — usually faster and more valuable
  than the project you were planning.
- **"Good" is contested.** DMAIC cannot arbitrate what the customer wants; it optimizes against a
  spec someone else has to set. Settle the requirement first.
- **The problem is flow, not defects.** Long queues and waiting are usually a constraint or a
  batching problem, and the constraint analysis gets there faster
  (the archived `continuous-improvement-skills:theory-of-constraints`,
  the archived `continuous-improvement-skills:value-stream-mapping`).
- **The organization needs the story on one page.** The rigor still applies; the artifact is an A3
  (the archived `continuous-improvement-skills:a3-thinking`), which can summarize a DMAIC project without
  replacing it.
