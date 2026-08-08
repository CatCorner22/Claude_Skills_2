# Five focusing steps and drum-buffer-rope (reference)

The five focusing steps expanded with a month-end-close worked example, drum-buffer-rope
mechanics, throughput accounting, and the evidence base.

## Contents
- The five focusing steps, expanded
- Worked example: the month-end close calendar
- Drum-buffer-rope mechanics
- Throughput accounting
- Queueing intuition (prose only)
- Evidence base

## The five focusing steps, expanded

1. **Identify the system's constraint.** Diagnostics that converge on it:
   - Where does work pile up in front, while everything downstream sits starved?
   - Which task's slip moves the *system's* finish date one-for-one? (Slips elsewhere get
     absorbed by slack.)
   - Which resource does everyone expedite around, negotiate with, or wait on?
   - In a calendar or plan: the longest dependent chain usually runs *through* the constraint.
   A constraint can be physical (a machine, one trained preparer), a policy (a batch cutoff, an
   approval threshold), or the market (demand itself, when capacity exceeds it). Policy
   constraints are the most common in office work and the cheapest to break.
2. **Exploit the constraint** — get everything out of existing capacity before spending:
   - Zero idle time on it: no waiting for inputs, approvals, or information.
   - Offload every task others can do; the constraint does only constraint-work.
   - Inspect inputs *before* they reach it — a constraint hour spent on junk or rework is
     throughput lost forever.
   - Sequence its work by value; protect it from interruptions and meetings.
3. **Subordinate everything else** to the constraint's pace:
   - Release work at the rate the constraint absorbs it (the rope, below) — early release is
     not a head start, it is WIP.
   - Re-measure non-constraints on constraint service (did it ever starve? was its input
     quality right?), not on their own utilization.
   - Accept visible idle time at non-constraints as the price of flow.
4. **Elevate the constraint** — only if it still binds after 2–3: add people, cross-train,
   automate, buy capacity, split the role. Because elevation costs money and exploitation is
   free, elevating first is the classic expensive mistake.
5. **Repeat — fight inertia.** Once broken, the constraint moves somewhere else. Re-run step 1,
   and audit for rules sized to the old constraint: batch sizes, buffers, approval thresholds,
   staffing patterns, calendar sequences. "We do it this way because of X" where X no longer
   binds is the inertia signature.

## Worked example: the month-end close calendar

A 9-business-day close. Walking the calendar shows every downstream task — flux review, reporting
package, sign-offs — waits on completion of the balance-sheet reconciliations, which one senior
accountant prepares on days 4–7. Nothing else on the calendar takes near that long once its
inputs exist.

- **Identify:** the reconciliation task is the constraint — its finish date sets the close date.
  Verify at the gemba: sit with the preparer for a session; confirm the wait is real preparation
  time, not (say) waiting for a subledger feed (which would make the *feed* the constraint).
- **Exploit:** pre-stage everything before day 1 — auto-match tuned so only true exceptions
  remain, supporting schedules prepped in advance, prior-period templates rolled forward. Clear
  the preparer's calendar of non-close work for days 4–7. Route questions to a backup so
  preparation never pauses. Feed accounts in validated batches so no constraint hour is spent on
  incomplete data.
- **Subordinate:** re-sequence the calendar around the constraint — upstream tasks are due when
  the *constraint* needs them, not "as early as possible"; downstream tasks are scheduled from
  the constraint's realistic finish, staged to start the moment their slice completes (flux
  review per completed area, not after all areas).
- **Elevate:** if the close must compress further, cross-train a second preparer on half the
  accounts, or automate the highest-volume reconciliations.
- **Repeat:** the close now finishes in 6 days and the constraint has moved — perhaps to the flux
  review meeting that only fits on day 6. Re-identify; and notice the old rule ("recs start day
  4") no longer binds anything. Retire it.

## Drum-buffer-rope mechanics

- **Drum:** the constraint's schedule is the beat of the whole system. Everything is planned
  from the drum, forward and backward — not from each department's own capacity.
- **Buffer:** a *time* buffer of ready, quality-checked work sits in front of the constraint so
  it never starves when upstream hiccups. Size it to upstream variability: start generous, shrink
  as flow stabilizes. In office work the buffer is a short queue of fully-prepared items (e.g.
  accounts ready to reconcile, complete with support). Watch buffer *penetration* — how often it
  runs near empty — as the early-warning signal, and expedite only on that signal.
- **Rope:** work is released into the system at the drum's rate — a release gate tied to
  constraint completions. The rope is what keeps WIP flat: without it, upstream "efficiency"
  floods the system and lead time balloons. A kanban/WIP limit is a rope by another name.

## Throughput accounting

Judge actions by three system-level measures, in this order of leverage:
- **Throughput (T):** the rate the system generates value — units completed and *delivered* per
  period (for a close: the close itself; for collections: cash collected). In business terms,
  revenue minus truly variable costs.
- **Inventory / WIP (I):** money and effort tied up inside the system — open items, unfinished
  work, backlog.
- **Operating expense (OE):** what it costs to run the system per period.

A change is good if it raises T, or cuts I or OE, *for the system*. Classic traps this exposes:
a non-constraint "efficiency" project cuts nobody's wait and no OE (it just makes WIP faster);
batch-size increases that improve a local cost-per-unit while inflating I and lead time; layoffs
at a non-constraint that save OE but destabilize the buffer feeding the constraint. Cost
accounting allocates; throughput accounting asks only: did the system make more, hold less, spend
less?

## Queueing intuition (prose only)

As any resource's utilization approaches 100%, the wait in front of it grows explosively, not
linearly — near capacity, small bursts of arrivals or variability translate into huge queues.
Two practical consequences: a non-constraint deliberately running below full utilization is
*buying* flow, not wasting capacity; and shaving variability (steadier arrivals, fewer defects)
shortens waits as surely as adding capacity. Full queue-wait mathematics is beyond this skill's
scope — the intuition is enough to justify subordination and buffer sizing.

## Evidence base

An independent meta-analysis (Mabin & Balderstone) across 80+ published TOC applications reported
mean lead-time reductions of roughly 70%, inventory reductions of roughly 49%, and substantial
throughput/financial gains, with results consistent across industries `[snippet-only]`. Treat the
figures as reported-case evidence (published applications skew toward successes), but the
direction and size are unusually well documented for a management method.
