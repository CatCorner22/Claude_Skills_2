# Evals — continuous-improvement-skills:value-stream-mapping

## 1. Positive trigger (should load the skill)
> "Our standard requests take about three weeks end to end and nobody knows why — the actual
> work can't be more than a few hours. Can you help me map the whole value stream, current
> and future state, and figure out where all the time goes?"

Expected: skill loads; scopes one request family with SIPOC and explicit boundaries; walks
the process following one real item; captures cycle time, %C&A (scored by the receiving
step, not the doer), and the waits *between* steps; builds the two-level timeline ladder and
computes flow efficiency from the team's own numbers; tags the eight wastes as kaizen
bursts; designs a future state (quality at the source on the worst %C&A, batching artifacts
removed, pull/triggers) with owned, dated actions and measurable targets. Shows that most
lead time is waiting, not working.

## 2. Near-miss (should NOT load this skill)
> "Requests keep getting filed under the wrong category. Can you help me find the root
> cause?"

Expected: this is diagnosing one recurring defect, not mapping a whole process. The
`continuous-improvement-skills:root-cause-analysis` skill should handle it (5 Whys /
fishbone). If value-stream-mapping loads instead, tighten the description and cross-links.

## 2b. Near-miss (personal-workload guard)
> "I personally have way too much in flight — twenty open tasks, everything urgent, nothing
> finishing. Help me get my own workload under control."

Expected: one person's overloaded task list is
`continuous-improvement-skills:priority-and-wip` (Little's Law at personal scale), not a
multi-step stream to map. If value-stream-mapping loads as primary, the seam is failing.

## 3. Quality rubric
A good response:
- **Does the task:** scopes with SIPOC (one family, firm boundaries), maps steps with data
  boxes (CT, %C&A, people, systems) and inter-step waits including their ranges, computes
  lead time vs. process time and flow efficiency, marks rework loops and the information
  flow, tags the 8 wastes, and produces a future-state map plus a dated, owned action plan
  with targets — routing team-designed changes to kaizen events and a gating step to
  theory-of-constraints.
- **Teaches:** explains *why* lead time is dominated by queues (Little's Law: WIP = arrival
  rate × time in system, so shrink WIP and smooth flow rather than speed up steps), why
  %C&A's hidden rework loops inflate lead time, and why the whole stream must be mapped —
  waiting and rework hide in the hand-offs no single owner sees.
- **Grounded and honest:** walks the real work, not the policy diagram; treats the
  current-state map as a measured baseline and the future state as a hypothesis to test;
  gets the canon right — Rother & Shook's Learning to See codified Toyota's
  material-and-information-flow mapping, %C&A is an office-era addition (Keyte & Locher;
  Martin & Osterling), the eighth waste is a later Western addition to Ohno's seven, and
  DOWNTIME is a mnemonic; computes flow efficiency from the user's own numbers instead of
  quoting folklore, and labels any example numbers illustrative.
- **Routes at the seams:** one defect's cause → root-cause-analysis; locking in a method →
  standard-work; a measured improvement project → dmaic-problem-solving; the gating step →
  theory-of-constraints; team-designed changes → kaizen-and-codesign; a personal overload →
  priority-and-wip.
