# Kaizen / co-design facilitation playbook

Method lineage: Masaaki Imai's *Kaizen* (1986) carried the term into Western management;
the time-boxed "kaizen event" is a later, largely Western adaptation of it. Co-design
descends from the Scandinavian participatory-design tradition of workers designing the
tools and processes they must live with. Respect-for-people is one of the two pillars of
the Toyota Way, alongside continuous improvement. The worked example's numbers are
illustrative, not research findings.

## Contents
- [Kaizen charter](#kaizen-charter)
- [A two-day event agenda](#a-two-day-event-agenda)
- [Facilitation techniques for equal voice](#facilitation-techniques-for-equal-voice)
- [Rapid PDCA inside the event](#rapid-pdca-inside-the-event)
- [Respect-for-people in practice](#respect-for-people-in-practice)
- [Worked example — the document-review handoff](#worked-example--the-document-review-handoff)
- [Follow-up / sustainment](#follow-up--sustainment)
- [Co-design beyond the event](#co-design-beyond-the-event)
- [Canon and misattribution notes](#canon-and-misattribution-notes)

## Kaizen charter

- **Process in scope:** <one narrow, real process> · **Boundaries:** starts/ends where <…>
- **Objective (measurable):** <e.g. cut this task's rework rate from a to b; halve its queue>
- **Dates / time-box:** <e.g. 2 days> · **Sponsor (removes obstacles / authorizes):** <…>
- **Participants:** the **operators who do the work**, a **downstream customer** who
  receives the output, and a **decision-maker** who can approve changes in the room.
- **Out of scope:** <what you will deliberately not touch>
- **Baseline:** <the objective's metric, measured before day 1 — without it, "improved" is a feeling>

Charter quality tests: can the objective be scored hit/miss by a neutral party? Could the
group plausibly move the metric within the time-box? Does the sponsor's name mean anything
(will obstacles actually be removed)? Three noes = re-scope.

## A two-day event agenda

**Day 1 — see, then diverge**
1. Kickoff (30 min): charter, objective, baseline, ground rules — equal voice; problem =
   process, not person.
2. **Gemba walk** (90 min): observe the real work where it happens; collect facts and
   timings; interview the doers in a low-stakes way — restate what you saw and let them
   correct you (`collaboration-skills:disarming-elicitation` has the stance).
3. Current-state view (60 min): quick map of the observed process, or the relevant slice of
   an existing value stream map; mark where the objective's metric is lost.
4. Idea generation (90 min): silent brainwriting → affinity grouping → dot-vote
   (`continuous-improvement-skills:structured-ideation` owns the technique detail).
5. Pick the first tests (30 min): from the top-voted ideas, choose the few that are small,
   reversible, and testable *tomorrow morning on real work*.

**Day 2 — converge by trying**
6. **Rapid PDCA loops** (most of the day): prototype → try on live work → observe → adjust →
   try again. Two or three loops per idea is normal; keep a visible scoreboard of the
   objective's metric per loop.
7. Draft the new **standard work** (60 min): the operators write it, in the steps /
   key-points / reasons format (`continuous-improvement-skills:standard-work`).
8. Close (45 min): results vs. objective and baseline; owners and dates for open items;
   30/60-day check scheduled; sponsor hears it from the team, not the facilitator; short
   after-action review of the event itself (`decision-science-skills:after-action-review`).

Half-day and single-day variants compress the same spine: see → diverge → try → standardize
→ schedule the check. Cutting the gemba walk or the live tests changes the method into a
meeting; cut duration instead.

## Facilitation techniques for equal voice

- **Round-robin** so everyone speaks, not just the confident.
- **Silent idea-writing (brainwriting)** before any discussion — decouples idea quality from
  status and volume.
- **Affinity grouping** to cluster ideas without early judgment.
- **Dot-voting / multivoting** to prioritize the vital few, with the decision rule stated
  before voting.
- **Speak-last leaders:** ask managers and the sponsor to hold their views until operators
  have spoken; the highest-paid opinion resets the room's anchor if it lands first.
- **Parking lot** for out-of-scope issues — visible, so raising them still counts.
- The facilitator owns the *process*; the group owns the *content*. A facilitator with a
  pet solution has left the role.

## Rapid PDCA inside the event

Bias to *trying*, not deliberating. Plan a small change → Do it on real work that day →
Check what happened against the baseline → Act (keep / adjust / discard) and loop again.
Rules that keep the loops honest:
- Test on **real work items**, not role-plays; the point of being at the gemba is that live
  material is on hand.
- Keep each test **reversible** — cheap to undo if the check says no.
- Measure every loop with the **charter's metric**, on the visible scoreboard.
- Discarding an idea after a fair test is a success of the method, not a failure of the
  proposer — say so out loud.

## Respect-for-people in practice

- Frame every problem as a **process** problem, never a person's fault — blame teaches
  people to hide problems, and hidden problems are unimprovable.
- Credit the people whose ideas were used, by name, in the close-out and to the sponsor.
- The operators present the results; the facilitator stays offstage.
- Nothing decided about the work without the people who do the work in the room.
- This is what makes the team bring the next idea — the event seeds a habit; it is not the
  habit itself.

## Worked example — the document-review handoff

Domain-neutral on purpose: the "documents" could be legal drafts going to a reviewing
partner, analyst reports going to a QA lead, code changes going to review, or work orders
going to a checker. **All numbers are illustrative.**

- **Charter.** Scope: the producer→reviewer handoff, from "draft ready" to "review
  complete." Objective: cut items returned for rework from 40% to under 20% in the event's
  test batches; baseline measured from last month's log. Time-box: 2 days. Room: three
  producers, one reviewer (the downstream customer), the team lead (decision-maker).
- **Gemba walk findings.** Producers guess at the reviewer's expectations; the reviewer
  re-explains the same three defects weekly; submissions batch up on Friday, so review
  happens under Monday pressure.
- **Brainwriting output → dot-vote.** Top ideas: (1) a five-item ready-to-submit checklist
  written *by the reviewer*; (2) submit-as-you-finish instead of Friday batching; (3) a
  15-minute weekly defect-review huddle.
- **Rapid PDCA.** Loop 1: checklist tested on the morning's four live drafts — two would
  have been returned; both caught pre-submission. Loop 2: checklist item 5 rewritten by a
  producer for clarity; zero returns in the afternoon batch of five. Idea 2 tested by
  submitting three items same-day: reviewer confirms small-batch review takes minutes, not
  the Monday hour.
- **Close.** Test batches: 1 return in 12 vs. a 40% baseline (illustrative). Checklist and
  submit-as-you-finish become standard work, written by the producers and reviewer
  together; the huddle gets an owner and a first date; 30/60-day check scheduled on the
  rework metric. Team lead approves in the room — no steering-committee lag.

Note the co-design signature: the reviewer wrote the checklist, producers rewrote its worst
item, and the standard was drafted by the people who will live with it.

## Follow-up / sustainment

- Capture the improved method as standard work before the room empties
  (`continuous-improvement-skills:standard-work`); the event's energy does not survive as
  memory.
- Assign owners and dates to every open action; set the metric to watch and who watches it.
- Schedule the **30/60-day check**: did the change hold, did it hit the objective? If not,
  cycle again — reversion is information, not shame.
- Carry the story to people who weren't in the room on a one-page A3
  (`continuous-improvement-skills:a3-thinking`) when the change needs wider adoption.
- The real success metric: improvements surfacing *between* events. Track ideas raised and
  tested outside workshops; that number rising means the habit took.

## Co-design beyond the event

The participatory principle scales down below the two-day format: a one-hour session where
the users of a template redesign the template; a standing agreement that no process change
ships without an operator on the design; customers invited into service redesign as
co-designers, not survey subjects. The invariants are the same three: the people who do the
work hold design authority, the downstream customer's need is in the room, and something
real gets tried before the session ends.

## Canon and misattribution notes

- **Kaizen (Imai):** ongoing improvement involving everyone — managers and workers — mostly
  small, mostly daily. The word does not mean "workshop."
- **The kaizen event / blitz** is a Western adaptation for jump-starting improvement in
  organizations that don't yet have the daily habit. Useful — but calling the event itself
  "kaizen" and stopping there is the standard misreading; Imai's point was the habit.
- **Participatory design** grew from Scandinavian workplace projects in which workers helped
  design the systems they would use; modern co-design/co-production extends the same
  authority to customers and service users. Citing it as a "facilitation trick" undersells
  it — it is a claim about who holds design authority.
- **Respect-for-people** is a named pillar of the Toyota Way (with continuous improvement),
  not a soft add-on: the improvement system runs on people volunteering problems, and
  people only volunteer problems where problems are safe to own.
