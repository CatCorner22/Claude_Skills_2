---
name: git-and-code-review
description: >-
  Uses version control well and reviews changes constructively — branch-per-change, atomic commits
  with clear messages, the pull request flow, merge vs rebase (concept and when to use each),
  resolving merge conflicts calmly, and reading a diff for correctness and readability with useful
  feedback. Use when using git, opening or reviewing a pull request, resolving a merge conflict, or
  deciding how to structure a set of changes. Triggers: git, branch, commit, pull request, PR,
  merge conflict, code review, rebase, version control.
---

# Git and code review

## When to use
- Making changes under version control and wanting a clean, revertible history.
- Opening a pull request, or reviewing someone else's, and giving feedback that helps.
- Resolving a merge conflict, or deciding between merge and rebase.
- Not for: automating git behavior in the Claude Code harness (hooks that run on commit, allow-listing
  `git push`) → see `coding-agent-skills:agent-harness-config`.

## Do it
1. **One change per branch.** Start each piece of work from an up-to-date main:
   ```bash
   git switch main && git pull
   git switch -c fix/duplicate-fee-rows      # short, descriptive, kebab-case
   ```
   Keep the branch scoped to a single logical change — it is easier to review, test, and revert.
2. **Commit in atomic steps with messages that explain *why*.** Stage related edits together and
   write a message whose subject completes "If applied, this commit will…":
   ```bash
   git add -p                                 # stage in hunks, review as you go
   git commit -m "Drop duplicate fee rows before summing"
   ```
   Subject ≤ ~50 chars, imperative mood; add a body (blank line, then wrap ~72) when the *reason*
   isn't obvious from the diff. Small commits are a safety net: each one is a point you can return to.
3. **Open a pull request that a reviewer can say yes to.** Push the branch, open the PR, and in the
   description state **what changed, why, and how you verified it** (tests run, before/after numbers).
   Keep PRs small; link the issue; call out anything you're unsure about so review attention lands there.
4. **Integrate with merge or rebase — on purpose.** To update your branch with the latest main:
   - `git merge main` preserves exactly what happened and adds a merge commit — safe, truthful history.
   - `git rebase main` replays your commits on top of main for a linear history — cleaner, but rewrites
     your commit hashes. **Only rebase commits you have not shared** (or that no one has based work on),
     because force-pushing a rewritten shared branch breaks everyone else's copy.
5. **Resolve conflicts calmly.** A conflict just means two branches changed the same lines; git marks
   them with `<<<<<<<`, `=======`, `>>>>>>>`. For each: open the file, decide the *correct combined*
   result (not blindly "keep mine"), delete the markers, then `git add` the file. Finish with
   `git merge --continue` (or `git rebase --continue`). Re-run the tests — a clean merge can still be
   logically wrong. `git merge --abort` backs all the way out if you want to restart.
6. **Review a diff in a fixed order: correctness → readability → style.** Ask, in order: does it do
   the right thing and handle edge cases and errors? Can the next person understand it? Only then,
   naming/format nits (ideally automated away). Leave specific, kind, actionable comments — point at a
   line, explain the concern, suggest a fix. Separate "blocking" from "nice-to-have," and approve when
   it is correct and clear, not when it is perfect. The checklist is in `references/review-checklist.md`.

## Why / learn
Version control is two things at once: a **safety net** and a **collaboration protocol**. As a safety
net, every atomic commit is a checkpoint you can return to and every branch is a sandbox you can throw
away — which is what makes it safe to experiment. As a protocol, the history and the pull request are
how you *communicate* a change to other humans across time. That reframing explains every practice
here: small, well-described changes are reviewable changes, and reviewable changes are the ones that
actually get reviewed rather than rubber-stamped. A commit message answers the question the diff can't —
*why* — for the person (often future-you) running `git blame` a year from now to understand a strange
line. Merge versus rebase is a choice between two values: merge keeps a truthful record of what
happened; rebase keeps a clean, linear story — the golden rule ("don't rebase shared history") exists
because rewriting commits others have pulled forces them to untangle a history that no longer matches
theirs. And reviewing correctness-first matters because a beautifully formatted function that computes
the wrong number is worse than an ugly one that's right; style is the cheapest thing to fix and should
never crowd out the substance.

## Common mistakes
- One giant branch/commit mixing five changes → impossible to review or revert. One logical change per branch.
- Messages like "fix" / "update" / "wip" → useless in `git blame`. Say what changed and why.
- Rebasing or force-pushing a shared branch → rewrites history others have → breaks their clones. Never rebase shared commits.
- "Accept theirs / accept mine" to clear a conflict fast → silently drops real work. Decide the correct combined result.
- Assuming a conflict-free merge is a correct merge → re-run tests; logic can break with zero conflicts.
- Review comments that are vague ("this feels off") or nitpick style over a real bug → point at lines, prioritize correctness, be specific and kind.

## Tailor to your environment
Record your team's real conventions in `references/your-environment.md`: default branch name, branch
and commit-message format, whether you merge or rebase to update, PR template and required checks, and
who reviews what. **Never commit secrets or internal URLs** — keep anything sensitive (private repo
hosts, tokens, reviewer names/emails) in `references/your-environment.private.md`, which `.gitignore`
keeps out of git. This skill then follows your workflow instead of a generic one.

## References
- references/git-commands.md — task-oriented git commands: branch, stage, commit, update, undo, resolve conflicts
- references/review-checklist.md — what to check in a diff, and how to give feedback that helps
- references/your-environment.md — your branch/commit/PR conventions and required checks (fill in)
