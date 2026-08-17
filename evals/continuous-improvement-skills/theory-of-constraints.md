# Evals — continuous-improvement-skills:theory-of-constraints

## 1. Positive trigger (should load the skill)
> "Our month-end close takes nine business days and the whole calendar seems to wait on one
> senior accountant's balance-sheet reconciliations. Walk me through the theory of constraints —
> find the bottleneck, exploit it, and re-sequence the close around it before we ask for headcount."

Expected: skill loads; works the five focusing steps in order — drafts the constraint hypothesis
from the calendar (the task whose slip moves the close date one-for-one) and requires gemba
verification before acting; exploits first (pre-staging, offloading, input quality, protected
time) explicitly *before* elevating (headcount); subordinates the calendar to the constraint's
pace; sets up a buffer of ready-to-reconcile accounts and a release rope; evaluates options with
throughput accounting rather than local efficiency; ends with step 5 — re-identify after the
change and retire rules sized to the old constraint.

## 2. Near-miss (should NOT load this skill)
> "Our invoice-to-cash process takes three weeks and nobody knows where the time goes. Can you
> map it end to end, current and future state, with the waits between steps?"

Expected: this is whole-stream discovery — `continuous-improvement-skills:value-stream-mapping`
owns it (SIPOC, data boxes, timeline ladder). The VSM *finds* the bottleneck; only once one step
is known to gate the system does theory-of-constraints take over. If theory-of-constraints loads
on a mapping ask, tighten the description and the Not-for cross-link.

## 2b. Near-miss (greedy-token guard: bare "constraint")
> "Add a unique constraint on invoice_number to the payments table, and check which foreign-key
> constraints are missing indexes."

Expected: database/ORM work — `full-stack-dev-skills:database-and-orm` territory (the word
"constraint" is a schema term there, not a throughput term). Bare "constraint" must never trigger this
skill; its triggers are qualified (bottleneck, five focusing steps, exploit the constraint,
drum-buffer-rope). If it loads here, the trigger surface has grown too greedy.

## 3. Quality rubric
A good response:
- **Does the task:** identifies a specific constraint with the one-for-one slip test, insists on
  gemba verification of the hypothesis, produces a concrete exploit plan (free) before any
  elevate proposal (costs money), re-sequences the surrounding work to subordinate it, sizes a
  buffer and gates release (drum-buffer-rope), and judges each option by throughput, inventory/WIP,
  and operating expense.
- **Teaches:** explains why the constraint alone sets system output — an hour lost there is lost
  forever, an hour saved elsewhere is a mirage — why keeping non-constraints fully busy makes
  things worse (WIP, exploding queues near full utilization), and why the steps are ordered
  exploit-before-elevate.
- **Stays honest:** treats the inferred constraint as a hypothesis until verified where the work
  happens, cites the meta-analysis evidence as reported-case (`[snippet-only]`) rather than
  guaranteed results, and frames the constraint as a system property — never a person to blame.
