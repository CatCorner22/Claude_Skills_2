---
name: value-stream-mapping
description: >-
  Maps a process end to end in current and future state, quantifying cycle time, lead time, and
  value-added vs non-value-added time to expose waste and improve flow; scopes the effort first
  with SIPOC. Use when analyzing a whole process, mapping a value stream, drawing a current- or
  future-state map, measuring lead vs cycle time, or scoping a process with SIPOC. Triggers: value
  stream mapping, VSM, current state, future state, process map, SIPOC, lead time, cycle time,
  waste, flow.
---

# Value stream mapping

## When to use
- Analyzing a whole end-to-end process (invoice-to-cash, procure-to-pay, the month-end close, a
  bank-account opening) to see where time, effort, and errors actually go.
- Drawing a **current-state** map, then designing a **future-state** map to improve flow.
- Scoping a process with **SIPOC** before you dig into any one step.
- Not for: driving the true cause of one recurring defect you find on the map → see
  `continuous-improvement-skills:root-cause-analysis`. To lock in the improved method as a documented
  standard → see `continuous-improvement-skills:standard-work`.

## Do it
1. **Scope with SIPOC.** On one page list **S**uppliers, **I**nputs, **P**rocess (5–7 high-level
   blocks only), **O**utputs, **C**ustomers. Pick a single product/service *family* (e.g. "supplier
   invoices paid on standard terms") and fix explicit start and end boundaries. SIPOC keeps the map
   from sprawling — see `references/vsm-symbols-and-metrics.md`.
2. **Walk the process where the work happens (the gemba).** Follow one real work item — an actual
   invoice, one close task — from start to finish, in order. Map what *is*, not the policy diagram.
   Talk to the people doing each step.
3. **Draw the steps with a data box under each.** For every process step capture: **cycle time
   (CT)** = hands-on processing time; **%complete-and-accurate (%C&A)** = fraction passed downstream
   with no rework; number of people; and the IT system used. Note every place work is reviewed,
   approved, or re-keyed.
4. **Capture the wait/queue time *between* steps.** The invoice sitting in an approver's inbox, the
   batch waiting for a nightly run. This inter-step waiting is usually where most of the elapsed time
   lives, and it is invisible unless you write it down.
5. **Build the timeline ladder and do the math.** Draw a two-level line under the map: **process
   time** (sum of value-added CT) on the lower rungs, **lead time** (total elapsed, including all
   waits) on the upper rungs. Compute **process cycle efficiency = value-added time ÷ lead time**.
   In office/finance work this is frequently in the single-digit percents.
6. **Tag the 8 wastes (DOWNTIME).** Defects, Overproduction, Waiting, Non-utilized talent,
   Transportation (hand-offs), Inventory (backlog/WIP), Motion (screen-toggling, hunting for files),
   Extra-processing (duplicate keying, redundant reviews). Mark each on the current-state map with a
   burst/kaizen symbol.
7. **Design the future state.** Attack the biggest waits and lowest %C&A first: remove or combine
   steps, build quality in at the source (so defects don't flow), level the workload, replace batch
   hand-offs with flow, and add pull/triggers where useful. Set target lead time, CT, and %C&A.
8. **Turn the future state into an action plan.** List the changes as owned, dated actions with a
   measurable target for each. The future-state map is a hypothesis; the plan is how you test it.

## Why / learn
The one insight value stream mapping delivers, again and again, is that **most lead time is waiting,
not working** — the item spends its life in queues between steps, while the actual value-added touch
time is a thin sliver. That is why you measure lead time and process time *separately*: optimizing the
busy steps (making people type faster) barely moves a number dominated by queues, whereas removing a
two-day approval wait can halve lead time without anyone working harder. It follows from Little's Law
— lead time = work-in-process ÷ completion rate — so the levers on speed are shrinking the backlog and
smoothing flow, not adding effort. **%C&A is the other half of the story:** every step that passes work
downstream with defects forces rework loops that inflate lead time invisibly, so building quality in at
the source (right the first time) is a flow improvement, not just a quality one. Mapping the *whole*
stream — not one department's slice — is what makes the waiting and the rework visible, because both
hide precisely in the hand-offs that no single owner sees. The map is a shared picture that lets a team
reason about the flow instead of defending their step.

## Common mistakes
- Mapping the official procedure instead of walking the real work → you map fiction. Follow a real item.
- Recording only cycle time, not the waits between steps → you miss where the lead time actually is.
- Scoping too wide ("all of AP") → an unreadable map. Use SIPOC to pick one family and firm boundaries.
- Jumping to a future state before the current state is measured → you improve blind. Baseline first.
- Treating the map as the deliverable → it's worthless without an owned action plan and targets.
- Ignoring %C&A → hidden rework loops keep lead time high even after you speed up the steps.

## Tailor to your environment
Record your real value stream in `references/your-environment.md` (use `your-environment.private.md`,
which is git-ignored, if it names real vendors, systems, or people). Capture the process family and
boundaries you map most, your data-box metrics and where you pull them (ERP timestamps, ticketing
tools), your team's takt or volume, and your target lead time. Never commit real client, vendor, or
transaction data — sanitize to structure only.

## References
- references/vsm-symbols-and-metrics.md — SIPOC layout, data-box metrics, the 8 wastes, timeline math
- references/your-environment.md — your value stream, metrics, and data sources (add when supplied)
