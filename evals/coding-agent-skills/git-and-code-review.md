# Evals — coding-agent-skills:git-and-code-review

## 1. Positive trigger (should load the skill)
> "I pulled main into my feature branch and now git says there's a merge conflict in
> `reconcile.py`. How do I resolve it without losing anyone's work, and how should I have
> structured this branch to begin with?"

Expected: skill loads; explains conflict markers (`<<<<<<<`/`=======`/`>>>>>>>`), deciding the
correct *combined* result rather than "accept mine/theirs", `git add` + `--continue`, and
re-running tests after; also advises one-logical-change-per-branch and atomic commits with
why-bearing messages.

## 2. Near-miss (harness-automation guard)
> "Set up Claude Code so that every time it makes a commit in this repo, it automatically runs the
> test suite first."

Expected: this is harness automation (a hook that runs on an event), handled by
`coding-agent-skills:agent-harness-config`, not git usage itself. If this skill loads instead,
tighten the description / cross-links.

## 2b. Near-miss (deep-audit guard)
> "Run the board on the pricing module — I want a full multi-angle optimization audit:
> performance, accuracy, structure, robustness, everything suboptimal, before we touch it."

Expected: that is the parallel-specialist swarm → `coding-agent-skills:board-review`.
This skill owns routine PR/diff review; a commissioned deep multi-agent audit of a module is
the board's job. If this skill loads as primary, the seam is failing.

## 3. Quality rubric
A good response:
- **Does the task:** gives correct, runnable git steps (branch, stage in hunks, commit,
  integrate, resolve, undo safely) and, for a review, works in the fixed order —
  correctness, then readability, then style — with comments that name the line, the concern,
  and a fix, severity-labeled (blocking / should / nit / question), approving on
  correct-and-clear rather than perfect.
- **Teaches:** frames version control as a safety net + collaboration protocol; explains why
  small, well-described changes are the reviewable ones; explains the merge-vs-rebase
  trade-off (truthful record vs linear story) and why the golden rule exists.
- **Routes the seams:** a real bug confirmed in review → contact-trace copies via
  `coding-agent-skills:defect-epidemiology` before closing; comment tone that indicts the
  author → `collaboration-skills:feedback-that-lands`; correct-but-overbuilt code →
  `full-stack-dev-skills:lean-code-principles` (an overbuilt *whole solution* → the Pencil
  Pass in `coding-agent-skills:soviet-space-graphite`); "phase is done, build on it" claims →
  `coding-agent-skills:the-foreman`; deleting long-standing code → scream test /
  `coding-agent-skills:software-archaeology`.
- **Stays honest:** review-size/pacing numbers (200–400 LOC, ~500 LOC/hour, 60–90 min,
  70–90% discovery) are quoted with their [snippet-only] provenance mark and attributed to
  the SmartBear/Cisco study — never rounded into invented statistics; qualitative claims
  stated as established practice, not fake citations.
- **Safe:** warns against rewriting shared history / force-pushing shared branches, and
  against clearing a conflict by blindly discarding one side; re-run tests after any merge.
