# Evals — continuous-improvement-skills:fmea

## 1. Positive trigger (should load the skill)
> "We're about to go live with a new auto-reconciliation rule set. Before we flip it
> on, run an FMEA: list the failure modes for each matching and parse rule, rate severity,
> occurrence, and detection, and give me an action priority ranking of what to fix first."

Expected: skill loads; structures the rule set (load → parse → auto-match → adjust), enumerates
mode → effect → cause chains (duplicate line, truncated addenda, wrong pair inside tolerance,
valid match missed), drafts anchored S/O/D ratings and marks them as proposals for the process
owner to adjudicate, prioritizes by Action Priority (not RPN), proposes actions that cut
Occurrence or improve Detection, and sets the re-rate/living-register cadence. Detection ratings
should distinguish "lands in the unreconciled report" from "silently auto-matches wrong."

## 2. Near-miss (should NOT load this skill)
> "Yesterday's reconciliation posted three duplicate statement lines and cash is overstated — can
> you help me figure out why this happened?"

Expected: this is a cause hunt on one incident that already happened —
`continuous-improvement-skills:root-cause-analysis` (containment, 5 Whys, fishbone) handles it.
FMEA anticipates future failures; it does not autopsy a specific occurrence. If fmea loads here,
tighten the description and the Not-for cross-link. (The RCA's output should later feed the FMEA
register — but that is a follow-on, not this ask.)

## 2b. Near-miss (seam guard: barrier architecture)
> "Map out our payment-fraud hazard: the preventive barriers on the left, the mitigating barriers
> on the right, escalation factors, and who owns each barrier."

Expected: hazard-and-barrier architecture is
`safety-and-reliability-skills:bowtie-barrier-analysis` territory — a bowtie diagram around a top
event, not a rated failure-mode register. If fmea loads on barrier/bowtie vocabulary, its trigger
surface has grown too greedy.

## 3. Quality rubric
A good response:
- **Does the task:** produces a structured register with explicit mode → effect → cause chains,
  anchored S/O/D ratings, an Action Priority column (High/Medium/Low), targeted actions
  (prevention on causes, detection controls), and a re-rating plan — grounded in the actual
  process described, not generic examples.
- **Teaches:** explains why Action Priority replaced RPN — S×O×D arithmetic let Severity-9
  failures rank low, and any one-number risk score can average away the dimension that matters
  most — and why silent-wrong-match (high D) outranks visible-failure modes.
- **Stays honest:** presents drafted ratings and failure modes as proposals requiring human
  adjudication by the process owner, prunes rather than defends implausible modes, and keeps the
  register framed as living (re-run on incidents), not a one-time deliverable.
