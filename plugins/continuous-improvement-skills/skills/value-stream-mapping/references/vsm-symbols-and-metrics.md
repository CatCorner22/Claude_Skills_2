# VSM symbols, metrics, and the 8 wastes (reference)

Practical building blocks for a value stream map of an office/finance process.

## Contents
- SIPOC scoping table
- Data-box metrics (what to put under each step)
- The timeline ladder and the flow-efficiency math
- The 8 wastes (DOWNTIME) with finance examples
- Current-state → future-state moves

## SIPOC scoping table
Fill top-to-bottom before mapping. Keep Process to 5–7 verbs.

| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |
|-----------|--------|---------------------|---------|-----------|
| Who feeds the process | What they feed in | Receive → … → Deliver | What comes out | Who receives it |

Then state boundaries explicitly: **starts when** \<trigger\> / **ends when** \<done condition\>, and
name the one product/service family in scope.

## Data-box metrics (under each process step)
- **Cycle time (CT):** hands-on time to do the step once (minutes/hours).
- **%Complete & Accurate (%C&A):** share of outputs the *next* step can use with no correction,
  clarification, or rework. Ask the downstream step, not the doer.
- **Wait / queue time:** elapsed time the item sits *before* this step starts (record between boxes).
- **People / systems:** headcount touching the step and the IT system(s) used.
- Optional: batch size, uptime/availability, changeover, rework loops.

## The timeline ladder and flow-efficiency math
Draw a two-level line beneath the map:
- **Lower rungs = process (value-added) time** = Σ CT.
- **Upper rungs = lead time** = Σ CT + Σ all waits.
- **Process cycle efficiency (PCE) = value-added time ÷ lead time.**

Example: five steps, Σ CT = 45 min; total elapsed = 6 business days ≈ 2 880 min. PCE ≈ 45 ÷ 2 880 ≈
**1.6 %** — typical for transactional office work, and the reason to attack queues, not keystrokes.
(Little's Law: lead time = WIP ÷ completion rate — cut the backlog or raise throughput to cut time.)

## The 8 wastes (DOWNTIME) — finance examples
- **Defects** — miskeyed invoice, wrong GL code, a journal that fails to post; drives rework loops.
- **Overproduction** — reports and reconciliations nobody reads; producing ahead of need.
- **Waiting** — invoice idle in an approval queue; a step waiting for a nightly batch.
- **Non-utilized talent** — an analyst doing manual copy-paste a rule or bot could do.
- **Transportation** — hand-offs between systems, teams, or spreadsheets; emailing files around.
- **Inventory** — a backlog of unprocessed items; work-in-process piled between steps.
- **Motion** — toggling screens, hunting for the file, re-logging into systems.
- **Extra-processing** — duplicate data entry, redundant sign-offs, formatting no one needs.

## Current-state → future-state moves
- Remove or combine steps that add no value the customer would pay for.
- **Build quality in at the source** so defects never reach the next step (raises %C&A).
- Replace batch hand-offs with continuous flow; shrink queues and WIP limits.
- Level/smooth the workload (heijunka) so volume spikes don't create waits.
- Add pull or a clear trigger/signal so work starts only when the next step is ready.
- Set numeric targets: future-state lead time, CT, %C&A — then write owned, dated actions.
