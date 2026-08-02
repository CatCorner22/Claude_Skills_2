# Evals — coding-agent-skills:git-and-code-review

## 1. Positive trigger (should load the skill)
> "I pulled main into my feature branch and now git says there's a merge conflict in
> `reconcile.py`. How do I resolve it without losing anyone's work, and how should I have
> structured this branch to begin with?"

Expected: skill loads; explains conflict markers (`<<<<<<<`/`=======`/`>>>>>>>`), deciding the
correct *combined* result rather than "accept mine/theirs", `git add` + `--continue`, and
re-running tests after; also advises one-logical-change-per-branch and atomic commits.

## 2. Near-miss (should NOT load this skill)
> "Set up Claude Code so that every time it makes a commit in this repo, it automatically runs the
> test suite first."

Expected: this is harness automation (a hook that runs on an event), handled by
`coding-agent-skills:agent-harness-config`, not git usage itself. If this skill loads instead,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** gives correct, runnable git steps (branch, commit, resolve, integrate) and, for
  a review, checks correctness before readability before style.
- **Teaches:** frames version control as a safety net + collaboration protocol; explains why small,
  well-described changes are reviewable, and the merge-vs-rebase trade-off and its golden rule.
- **Safe:** warns against rewriting shared history / force-pushing shared branches, and against
  clearing a conflict by blindly discarding one side.
