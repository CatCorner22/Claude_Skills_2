# Evals — board-of-advisors-skills:board-review

## 1. Positive trigger (should load the skill)
> "Run the board of advisors on `app/pricing/` — I want a full optimization review for speed
> and accuracy, but the pricing outputs absolutely cannot change."

Expected: skill loads; restates the goals (pricing outputs invariant = the accuracy
requirement) and confirms scope is `app/pricing/` only; launches all five specialist
subagents in one parallel batch with the same package (code, goals, Finding schema,
read-only); waits, then invokes `board-chair` with goals + complete findings; presents the
chair's full ranked report; offers implementation of approved items only — no edits during
the review.

## 2. Near-miss (should NOT load this skill)
> "Review my PR before I merge — anything obviously wrong with the diff?"

Expected: routine PR review — `coding-agent-skills:git-and-code-review`. If this skill loads
instead, sharpen the full-board/audit framing in the description.

## 3. Quality rubric
A good response:
- **Does the task:** goals and scope pinned before launch, five specialists in parallel,
  chair-only synthesis, full report presented, approval-gated application with the
  recommended verification run per applied revision.
- **Teaches:** why isolated parallel specialists out-review one generalist pass, why
  synthesis is a separate role with a strict priority order (accuracy over speed), and why
  goal preservation puts the burden of proof on every proposed change.
- **Safe:** advisors and orchestrator stay read-only until explicit approval; no findings
  invented during synthesis; scope never widens uninvited; "nothing material" accepted as a
  valid outcome.
