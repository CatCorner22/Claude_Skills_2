---
name: the-challenger
description: >-
  Runs the revision review that momentum and sunk costs suppress — named for the 1986
  Challenger launch decision, where schedule fever inverted the burden of proof over the
  engineers' objection. When evidence changes mid-project, it zero-bases the
  continue-vs-revise decision: only forward-looking costs count (money spent argues
  nothing), continuation past a trigger carries the burden of proof, normalized
  anomalies are re-seen as on first sighting, options widen beyond stop/continue (slip,
  descope, phase, re-plan), a dissent channel guarantees the objector is restated
  before the decision, and the outcome is logged with the next review trigger. Use when
  a deadline is driving decisions the evidence argues against, when "we've come too
  far" appears in any form, or when a go/no-go needs honest structure. Triggers: the
  challenger, challenge the timeline, sunk cost, plan continuation, should we slip the
  date, launch fever, are we still go, normalization of deviance, escalation of
  commitment, revision review.
metadata:
  version: "1.1.1"
  source: >-
    Commissioned by the user to prevent momentum and sunk costs from holding a project to
    a timeline when revision would be optimal. Anchored on the documented record of the
    Challenger launch decision (Rogers Commission; Vaughan's normalization of deviance) —
    held soberly: seven people died; this skill borrows the lessons, not drama.
---

# The Challenger (revision review)

The night before launch, the question changed from "prove it is safe to fly" to "prove
it is NOT safe" — and the schedule flew the vehicle. This skill exists for the moment a
project reaches that inversion: evidence has changed, the date has not, and everyone can
feel which way the room is leaning. Its voice is grave and precise, because its
namesake earned that.

## When to use
- A deadline is driving decisions the evidence argues against; "we've come too far,"
  "we'll make it up later," or "it flew fine last time" appears in any form.
- A go/no-go decision (go-live, launch, cutover, release) needs structure that momentum
  cannot steer.
- A revision trigger fires: a named condition from the plan (missed integration date,
  new hazard, a Load Manifest number changing) that obligates this review.
- Not for: imagining failure BEFORE commitment → `decision-science-skills:pre-mortem`
  (this skill runs mid-flight, when momentum exists); the epistemics of tests and
  intervention logs → `continuous-improvement-skills:project-command-center` (any
  criteria change this review produces is logged there, openly, never silently);
  driving effort on the chosen plan → `coding-agent-skills:stay-hard-accountability`
  (see Why / learn for the seam: The Mirror governs effort, The Challenger governs
  whether the plan still deserves it); the blocker-hunting autopsy persona →
  `coding-agent-skills:chicken-little-executive-advisor`.

## Do it
The facilitation script, the Challenger record held soberly, the bias literature, a worked
go-live-that-should-slip example, and the decision-log template are in
`references/revision-review-method.md`.

1. **Install triggers at plan time** (the step that makes every later step possible):
   name, in the plan itself, the conditions that OBLIGATE a revision review — slipped
   milestones, anomaly counts, changed load numbers, dependency failures. A review held
   only when someone feels brave is a review momentum already won. Reviews fire on
   triggers, not on courage.
2. **Zero-base the decision.** Ask it exactly: "Starting today, knowing what we now
   know, with the money already spent belonging to someone else — would we choose this
   plan and this date?" Sunk costs are excluded by construction: everything spent is
   gone on every branch, so it cannot differentiate the branches. Andy Grove's form of
   the question works too: if the board replaced us tomorrow, what would our successors
   do? — then walk out the door and back in as them.
3. **Set the burden of proof where it belongs.** Past a fired trigger, CONTINUATION
   must prove the plan still holds; the challengers do not have to prove it fails. Say
   out loud who currently bears the burden — if the room is asking the objectors for
   certainty, the Challenger inversion has already happened.
4. **Run the normalization-of-deviance scan.** List every anomaly the project has
   reclassified from alarming to routine merely because it recurred without
   catastrophe (the O-ring blow-by had become "within experience"). For each: what did
   we say the FIRST time we saw it? Recurrence without consequence is exposure, not
   evidence of safety.
5. **Cost both branches honestly, forward-looking only.** Revision has real costs —
   contracts, dependencies, credibility, morale — and continuation-while-wrong has the
   retrofit clock (`safety-and-reliability-skills:weight-of-the-books`). Discipline the
   optimism on both sides with the base rates: what actually happened the last several
   times this team "made up the schedule later"
   (`decision-science-skills:reference-class-forecasting`)?
6. **Widen the options beyond stop/continue.** Slip the date; descope to the pencil
   (`coding-agent-skills:soviet-space-graphite`); phase the launch (partial go-live);
   attack the constraint instead of the calendar
   (`continuous-improvement-skills:theory-of-constraints`); or change acceptance
   criteria OPENLY, as a logged intervention — never silently. Binary framing is
   momentum's favorite trick: it makes revision look like surrender.
7. **Guarantee the dissent channel.** The objecting engineer gets a named path
   (PACE graded assertiveness —
   `safety-and-reliability-skills:sbar-structured-communication`), a written objection,
   and this rule: the decision-maker must restate the dissent to the dissenter's
   satisfaction BEFORE deciding. An objection that was never restated was never heard —
   it was survived.
8. **Decide, log, and date the next look.** Record: the decision, the evidence it
   rests on, the expected outcome, what evidence would have changed it, and the next
   review trigger. A continue decision without a next trigger is not a decision; it is
   the end of deciding.

## Why / learn
Three biases interlock to keep doomed timelines alive, and the steps are aimed one
each. **Sunk cost** (Arkes & Blumer; the Concorde fallacy is named for a project that
flew on it) makes spent money feel like an argument — zero-basing removes it by
construction, because sunk cost is identical on every branch and therefore can justify
none of them. **Escalation of commitment** (Staw's "knee-deep in the Big Muddy") makes
each increment easier to approve than the decision would be fresh — the Grove
walk-out-the-door question defeats it by deleting the self whose consistency is being
protected. **Plan-continuation bias** — aviation's "get-there-itis," overrepresented in
approach-phase accidents — strengthens as the destination nears, which is why triggers
are installed at plan time: the review must not depend on anyone's courage at the
moment courage is most expensive [snippet-only]. The Challenger record supplies the two
subtler lessons. Normalization of deviance (Vaughan) shows how evidence erodes:
anomalies become "within experience" through sheer recurrence, so the scan asks what
the first sighting felt like. And the burden inversion is the tell that momentum has
taken the chair: when objectors must prove failure, the decision has already been made
and the meeting is theater. The seam with The Mirror matters and is not a
contradiction: quitting the PLAN is not quitting the WORK — the 40% audit governs
whether effort remains on a chosen plan; this review governs whether the plan still
deserves the effort. Both replace feelings with evidence; they answer different
questions. Feynman's line — adapted here from technology and public relations to
projects and schedules; his exact words are in the reference — closes the loop and the
teach: for a successful project, reality must take precedence over the schedule, for
nature cannot be fooled.

## Common mistakes
- Holding the review only when someone dares to ask → triggers fire it; courage is not
  a control.
- Letting spent money argue → it is gone on every branch; forward-looking costs only.
- Asking dissenters for certainty → past a trigger, continuation carries the burden.
- Treating recurrence as evidence of safety → it is exposure; re-see the anomaly as on
  first sighting.
- Binary stop/continue framing → slip, descope, phase, re-plan, and open criteria
  change are all revisions.
- Changing acceptance criteria quietly to keep the date → that is the intervention-log
  violation; do it openly or not at all.
- A continue decision with no next trigger → deciding has ended; momentum is steering.
- Using this review to dodge hard work the plan legitimately needs → route effort
  questions to `coding-agent-skills:stay-hard-accountability`; the two are partners,
  not exits from each other.

## Tailor to your environment
Record in `references/your-environment.md`: the standing revision triggers for your
active projects (and where they're written), who holds the decision chair and who holds
the dissent channel, your schedule-slip base rates (feed the ledger), and where
revision-review logs live.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/the-challenger.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/revision-review-method.md — the full review protocol with facilitation
  script, the Challenger record held soberly, the bias literature, a worked go-live
  example, and the decision-log template
- references/your-environment.md — your triggers, chairs, base rates (fill in)
