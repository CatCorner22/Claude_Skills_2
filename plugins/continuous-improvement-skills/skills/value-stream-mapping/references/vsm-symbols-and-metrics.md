# VSM: SIPOC, data boxes, timeline math, and the eight wastes

Method lineage: Mike Rother & John Shook, *Learning to See* (Lean Enterprise Institute),
which codified Toyota's material-and-information-flow mapping — one product family, door to
door, current state → future state → plan. Office/knowledge-work adaptations (Beau Keyte &
Drew Locher; Karen Martin & Mike Osterling) added %complete-and-accurate to the data box.
The worked example's numbers are illustrative, not research findings.

## Contents
- [SIPOC scoping table](#sipoc-scoping-table)
- [Mapping conventions for office streams](#mapping-conventions-for-office-streams)
- [Data-box metrics](#data-box-metrics)
- [The timeline ladder and flow-efficiency math](#the-timeline-ladder-and-flow-efficiency-math)
- [Worked example — a standard-request stream](#worked-example--a-standard-request-stream)
- [The 8 wastes (DOWNTIME) across roles](#the-8-wastes-downtime-across-roles)
- [Future-state design questions](#future-state-design-questions)
- [From map to plan](#from-map-to-plan)
- [Canon and misattribution notes](#canon-and-misattribution-notes)

## SIPOC scoping table

Fill top-to-bottom before mapping. Keep Process to 5–7 verbs.

| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |
|-----------|--------|---------------------|---------|-----------|
| Who feeds the process | What they feed in | Receive → … → Deliver | What comes out | Who receives it |

Then state boundaries explicitly: **starts when** \<trigger\> / **ends when** \<done
condition\>, and name the one product/service *family* in scope. A family is work that
follows roughly the same path — mixing families onto one map averages away everything the
map exists to show.

## Mapping conventions for office streams

No special software needed — a whiteboard or one slide works. The conventions that matter:
- **Process boxes** left to right in the order the *work item* experiences them, with a
  data box under each.
- **Queues** between boxes drawn as triangles (the classic inventory symbol) labeled with
  the observed wait — an inbox, an approval queue, a nightly batch window, "waiting for
  review."
- **Information flow** drawn above the stream: who tells each step what to do next (the
  ticketing system, the email chain, the standing meeting). In office work the information
  flow is often the tangled half of the picture.
- **Rework loops** drawn as arrows returning upstream, labeled with the fraction sent back —
  this is %C&A made visible.
- **Kaizen bursts** (starbursts) marking waste observations where they occur; these become
  the improvement backlog.

## Data-box metrics

Under each process step:
- **Cycle time (CT):** hands-on time to do the step once (minutes/hours).
- **%Complete & Accurate (%C&A):** share of outputs the *next* step can use with no
  correction, clarification, or rework. Ask the downstream step, not the doer.
- **Wait / queue time:** elapsed time the item sits *before* this step starts (record
  between boxes). Note the range, not just the average — variation is a finding.
- **People / systems:** headcount touching the step and the system(s) used.
- Optional: batch size (does the step wait to accumulate work?), availability (is the
  approver reachable one hour a day?), demand rate, rework loops.

## The timeline ladder and flow-efficiency math

Draw a two-level line beneath the map:
- **Lower rungs = process time** = Σ CT — hands-on time, value-added *and* not.
- **Upper rungs = lead time** = Σ CT + Σ all waits.
- **Activity ratio = process time ÷ lead time** — the number most office maps report and
  the one the example computes. True **process cycle efficiency (PCE)** divides only the
  value-added slice by lead time, so it is always lower.

Little's Law connects the queues to the calendar: average WIP = arrival rate × average time
in system, so at a fixed completion rate, lead time moves with the backlog. Cut WIP or
smooth arrivals and lead time falls with no one working faster; add WIP (start more, batch
more) and lead time grows with no one working slower.

## Worked example — a standard-request stream

Domain-neutral on purpose: the "request" could be a client matter opening, a data-analysis
request, a purchase requisition, or a feature ticket. **All numbers are illustrative.**

Scope (SIPOC): standard requests of one type; starts when the request form arrives, ends
when the requester confirms receipt of the result.

| # | Step | CT | %C&A | Wait *before* this step |
|---|------|----|------|--------------------------|
| 1 | Intake check | 10 min | 60% | 4 h in the shared inbox |
| 2 | Assignment | 5 min | 95% | 1.5 days (twice-weekly triage batch) |
| 3 | Do the work | 90 min | 85% | 2 days in the assignee's queue |
| 4 | Approval | 10 min | 90% | 1.5 days in the approver's inbox |
| 5 | Send + file | 10 min | 98% | 2 h |

Ladder math (1 day = 480 working min):
- **Process time** = 10 + 5 + 90 + 10 + 10 = **125 min**
- **Lead time** = 125 min + (240 + 720 + 960 + 720 + 120) wait min = 125 + 2,760 =
  **2,885 min ≈ 6 working days**
- **Flow efficiency** = 125 ÷ 2,885 ≈ **4.3%**
- 125 min is process time, not value-added time — a customer pays for step 3, not for
  assignment or a second sign-off, so PCE here sits well under the 4.3% activity ratio.

Reading the map:
- The item is worked ~2 hours and waits ~5.75 days. Nobody typing faster changes the
  headline; the queues own it.
- Step 1's 60% %C&A is Assignment's score of Intake, not Intake's own: 4 in 10 items reach
  Assignment unusable — missing information that has to be chased back to the requester before
  the item can move, re-entering the 4-hour inbox wait each time. Fixing the request form
  (quality at the source) attacks both %C&A and lead time.
- The two biggest waits are batching artifacts: twice-weekly triage and a single approver's
  inbox. Daily triage and a deputy approver are future-state candidates that touch no one's
  CT.
- Future-state targets (owned, dated): lead time ≤ 2 days, intake %C&A ≥ 90%, flow
  efficiency ≥ 12% — then re-walk the stream and re-measure against this baseline.

## The 8 wastes (DOWNTIME) across roles

Examples chosen to travel across jobs — analyst, attorney, ops manager, developer:
- **Defects** — a miskeyed field, a wrong citation, a mispicked item, a bug shipped; each
  drives a rework loop.
- **Overproduction** — reports nobody reads, memos beyond the ask, stock ahead of demand,
  features nobody requested.
- **Waiting** — the item idle in an approval queue, a review inbox, a nightly batch, a CI
  pipeline.
- **Non-utilized talent** — an expert doing manual copy-paste a rule, template, or script
  could do; the doers are never asked how to fix the process.
- **Transportation** — hand-offs between systems, teams, or spreadsheets; emailing files
  around; re-briefing at every transfer.
- **Inventory** — a backlog of unprocessed items: open tickets, unreviewed drafts,
  unassigned requests — WIP piled between steps.
- **Motion** — toggling screens, hunting for the current version, re-logging into systems,
  walking the file to the signer.
- **Extra-processing** — duplicate data entry, redundant sign-offs, formatting no one
  needs, precision beyond the decision's requirement.

## Future-state design questions

Adapted from Rother & Shook's future-state questions for office streams; ask them in order
against the current-state map:
1. What does the customer of this stream actually need, and at what pace (demand rate or
   takt)?
2. Where can steps flow directly into each other — no queue, no batch — because they're
   done by the same person or back-to-back?
3. Where flow breaks, can the downstream step *pull* (a trigger, a WIP limit) instead of
   upstream pushing batches?
4. Which single step should pace the whole stream, and how is work leveled into it so
   spikes don't become queues?
5. Where must quality be built in at the source so defects stop flowing (raise the worst
   %C&A first)?
6. Which waits are batching artifacts (approval windows, weekly triage, nightly runs) that
   a policy change removes for free?
7. What targets does the future state commit to — lead time, CT, %C&A — and by when?

If one step clearly gates the stream, the five focusing steps
(`continuous-improvement-skills:theory-of-constraints`) govern what to do at that step;
the map's job was finding it.

## From map to plan

*Learning to See*'s third deliverable is the one most often skipped: the plan. One line per
change — what, owner, date, measurable target, which map segment it touches. Changes that
need the team to design them become kaizen events
(`continuous-improvement-skills:kaizen-and-codesign`); methods that stabilize become
standard work (`continuous-improvement-skills:standard-work`). Re-walk and re-measure the
stream after the plan lands: the future-state map was a hypothesis, and the second walk is
its test.

## Canon and misattribution notes

- **VSM is Toyota's tool with a Western name.** Inside Toyota the artifact was the material-
  and-information-flow diagram; "value stream mapping" is the term *Learning to See* gave
  the practice it codified.
- **%C&A is an office-era addition** (Keyte & Locher; Martin & Osterling), not part of the
  original manufacturing data box — in knowledge work the dominant defect is the incomplete
  or inaccurate hand-off, so the metric earned its slot.
- **The "eighth waste" (non-utilized talent) is a later Western addition** to Ohno's seven
  (defects, overproduction, waiting, transport, inventory, motion, extra-processing).
  DOWNTIME is a mnemonic for remembering them, not a Toyota artifact.
- **Folklore says office flow efficiency is always tiny.** It very often is — but the number
  that persuades a team is the one computed from their own timeline ladder, so measure
  rather than quote.
