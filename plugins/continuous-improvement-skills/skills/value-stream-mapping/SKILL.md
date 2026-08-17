---
name: value-stream-mapping
description: >-
  Maps a process end to end in current and future state to expose waste and improve flow — the
  Rother & Shook Learning-to-See method adapted to office work: scope one product/service family
  with SIPOC, walk the process with one real item, hang a data box (cycle time,
  %complete-and-accurate, people, systems) under each step, capture queue time between steps,
  build the timeline ladder, and compute flow efficiency (process time ÷ lead time); then tag
  the eight wastes and design a future state with an owned action plan. Fits any stream —
  request-to-resolution, intake-to-filing, order-to-delivery, commit-to-deploy. Use when
  analyzing a whole process, drawing a current- or future-state map, measuring lead vs cycle
  time, or scoping with SIPOC. Triggers: value stream mapping, VSM, current state, future state,
  process map, SIPOC, lead time, cycle time, waste, flow, flow efficiency, eight wastes, %C&A,
  where does all the time go.
metadata:
  version: "1.2.0"
---

# Value stream mapping

Value stream mapping is Toyota's material-and-information-flow diagram, codified for the
rest of the world by Rother & Shook's *Learning to See*: draw the whole stream one work item
travels, with data under every step and the waiting made visible, so a team can see where
the time and quality actually go — then design the future state on purpose.

## When to use
- Analyzing a whole end-to-end process (a request-to-resolution queue, an intake-to-filing
  pipeline, order-to-delivery, commit-to-deploy) to see where time, effort, and errors
  actually go.
- Drawing a **current-state** map, then designing a **future-state** map to improve flow.
- Scoping a process with **SIPOC** before you dig into any one step.
- Not for: driving the true cause of one recurring defect you find on the map → see
  `continuous-improvement-skills:root-cause-analysis`. To lock in an improved method as a
  documented standard → see `continuous-improvement-skills:standard-work`. For a full
  measured improvement project around what the map reveals → see
  `continuous-improvement-skills:dmaic-problem-solving` (its Define phase uses SIPOC the
  same way). For one person's overloaded task list rather than a multi-step stream → see
  `continuous-improvement-skills:priority-and-wip`.

## Do it
`references/vsm-symbols-and-metrics.md` has the SIPOC layout, data-box definitions, timeline
math with a worked example, and the eight wastes.
1. **Scope with SIPOC.** On one page list **S**uppliers, **I**nputs, **P**rocess (5–7
   high-level blocks only), **O**utputs, **C**ustomers. Pick a single product/service
   *family* (e.g. "standard requests of type X") and fix explicit start and end boundaries.
   SIPOC keeps the map from sprawling.
2. **Walk the process where the work happens (the gemba).** Follow one real work item — an
   actual request, one filing, one release — from start to finish, in order. Map what *is*,
   not the policy diagram. Talk to the people doing each step.
3. **Draw the steps with a data box under each.** For every process step capture: **cycle
   time (CT)** = hands-on processing time; **%complete-and-accurate (%C&A)** = fraction
   passed downstream with no rework — ask the *receiving* step, not the doer; number of
   people; and the system used. Note every place work is reviewed, approved, or re-keyed.
4. **Capture the wait/queue time *between* steps.** The item sitting in an approval inbox,
   the batch waiting for a nightly run, the draft waiting for review. This inter-step
   waiting is usually where most of the elapsed time lives, and it is invisible unless you
   write it down.
5. **Build the timeline ladder and do the math.** Draw a two-level line under the map:
   **process time** (sum of CT — hands-on time, value-added and not) on the lower rungs,
   **lead time** (total elapsed, including all waits) on the upper rungs. Compute **flow
   efficiency** (the activity ratio) **= process time ÷ lead time**; true process cycle
   efficiency divides only the value-added slice, so it reads lower still. Measure it — in
   transactional office work it routinely lands low enough to surprise the team that owns
   the process.
6. **Tag the 8 wastes (DOWNTIME).** Defects, Overproduction, Waiting, Non-utilized talent,
   Transportation (hand-offs), Inventory (backlog/WIP), Motion (screen-toggling, hunting for
   files), Extra-processing (duplicate keying, redundant reviews). Mark each on the
   current-state map with a kaizen burst.
7. **Design the future state.** Attack the biggest waits and lowest %C&A first: remove or
   combine steps, build quality in at the source (so defects don't flow), level the
   workload, replace batch hand-offs with flow, and add pull/triggers where useful. When one
   step clearly gates the whole stream, work it with the five focusing steps
   (`continuous-improvement-skills:theory-of-constraints` — the map finds the constraint;
   that skill says what to do with it). Set target lead time, CT, and %C&A.
8. **Turn the future state into an action plan.** List the changes as owned, dated actions
   with a measurable target for each; run the changes that need the team's design as kaizen
   events (`continuous-improvement-skills:kaizen-and-codesign` — the bursts on the map are
   the event backlog). The future-state map is a hypothesis; the plan is how you test it.

## Why / learn
The one insight value stream mapping delivers, again and again, is that **most lead time is
waiting, not working** — the item spends its life in queues between steps, while the actual
value-added touch time is a thin sliver. That is why you measure lead time and process time
*separately*: optimizing the busy steps (making people type faster) barely moves a number
dominated by queues, whereas removing a two-day approval wait can halve lead time without
anyone working harder. It follows from Little's Law — average WIP = arrival rate × average
time in system, so at a fixed completion rate, lead time moves with the backlog — which
means the levers on speed are shrinking WIP and smoothing flow, not adding effort. **%C&A is
the other half of the story:** every step that passes work downstream with defects forces
rework loops that inflate lead time invisibly, so building quality in at the source is a
flow improvement, not just a quality one. Mapping the *whole* stream — not one department's
slice — is what makes the waiting and the rework visible, because both hide precisely in the
hand-offs that no single owner sees. The map is a shared picture that lets a team reason
about the flow instead of defending their step.

On the canon: Rother & Shook's *Learning to See* (Lean Enterprise Institute) turned Toyota's
internal material-and-information-flow mapping into the practice everyone now calls VSM —
mapping a product *family* door to door, current state before future state, and a plan as
the third deliverable. Office adaptations of the method (Keyte & Locher; Martin & Osterling)
added %C&A to the data box, because in knowledge work the dominant defect is incomplete or
inaccurate hand-offs rather than scrap. The "eight wastes" are Ohno's seven from the Toyota
Production System plus non-utilized talent, an addition from later Western practice —
DOWNTIME is a mnemonic, not scripture. And treat your own measurements as the facts:
folklore says office flow efficiency is always tiny, and it often is, but the number that
persuades your team is the one computed from your own timeline ladder.

## Common mistakes
- Mapping the official procedure instead of walking the real work → you map fiction. Follow a real item.
- Recording only cycle time, not the waits between steps → you miss where the lead time actually is.
- Scoping too wide ("all of operations") → an unreadable map. Use SIPOC to pick one family and firm boundaries.
- Asking the doer for their own %C&A → inflated. The receiving step scores the hand-off.
- Jumping to a future state before the current state is measured → you improve blind. Baseline first.
- Treating the map as the deliverable → it's worthless without an owned action plan and targets.
- Ignoring %C&A → hidden rework loops keep lead time high even after you speed up the steps.
- Averaging wildly variable waits into one tidy number → note the range; the variation is
  itself a finding.

## Tailor to your environment
Wire in your current role here — the method is domain-neutral by design and maps whatever
stream your current job runs on, and the next one's too. In
`references/your-environment.md`, record the process family and boundaries you map most,
your data-box metrics and where you pull them (system timestamps, ticketing tools, manual
timing on the walk), your volume or takt, and your target lead time. Keep the committed file
structural; real vendor, client, system, or transaction detail goes in
`your-environment.private.md`, which is git-ignored and never committed.

## References
- references/vsm-symbols-and-metrics.md — SIPOC layout, data-box metric definitions, the
  timeline ladder with a worked domain-neutral example, the 8 wastes, future-state design
  questions, and canon notes
- references/your-environment.md — your value stream, metrics, and data sources (add when supplied)
