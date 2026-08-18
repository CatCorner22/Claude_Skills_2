---
name: git-and-code-review
description: >-
  Uses version control well and reviews changes constructively — branch-per-change, atomic
  commits whose messages answer why, pull requests sized and described so a reviewer can say yes
  (what changed, why, how verified), merge vs rebase chosen on purpose under the golden rule of
  never rewriting shared history, calm conflict resolution that decides the correct combined
  result, and diff review in a fixed order — correctness, then readability, then style — with
  feedback that names the line, the concern, and a fix, severity labeled. Deep multi-specialist
  audits route to coding-agent-skills:board-review. Use when using git, opening or reviewing a
  pull request, resolving a merge conflict, structuring a set of changes, or writing history a
  future reader can trust. Triggers: git, branch, commit, pull request, PR, merge conflict, code
  review, rebase, version control, commit message, force push, git blame, revert, review this
  diff.
metadata:
  version: "1.2.0"
  source: >-
    Review-size and review-rate figures come from the SmartBear/Cisco peer-review study
    (2,500 reviews, 3.2M LOC), verified via web search snippets — claims carrying those
    numbers are marked [snippet-only].
---

# Git and code review

## When to use
- Making changes under version control and wanting a clean, revertible history.
- Opening a pull request, or reviewing someone else's, and giving feedback that helps.
- Resolving a merge conflict, or deciding between merge and rebase.
- Reading history to understand a change — blame, log, when did this break.
- Not for: automating git behavior in the Claude Code harness (hooks that run on commit,
  allow-listing `git push`) → see `coding-agent-skills:agent-harness-config`.
- Not for: a deep multi-angle audit of a module by parallel specialists →
  `coding-agent-skills:board-review` (routine PR review stays here; "run the board"
  goes there).
- Not for: critiquing a whole submitted work product — a plan, document, or script judged
  as a deliverable → `coding-agent-skills:sparring-partner`; review here is scoped to a diff
  against a base.
- Not for: excavating an accreted system nobody understands before demolition →
  `coding-agent-skills:software-archaeology` (this skill reads the history around one
  change; that one digs the whole site).

## Do it
The full review method — checklists, size evidence, feedback grammar, and a worked
example review — is in `references/review-checklist.md`; task-oriented commands are in
`references/git-commands.md`.

1. **One change per branch.** Start each piece of work from an up-to-date default branch:
   ```bash
   git switch main && git pull
   git switch -c fix/duplicate-fee-rows      # short, descriptive, kebab-case
   ```
   Keep the branch scoped to a single logical change — easier to review, test, and revert.
2. **Commit in atomic steps with messages that explain *why*.** Stage related edits together
   and write a subject that completes "If applied, this commit will…":
   ```bash
   git add -p                                 # stage in hunks, review as you go
   git commit -m "Drop duplicate fee rows before summing"
   ```
   Subject ≤ ~50 chars, imperative mood; add a body (blank line, wrap ~72) when the *reason*
   isn't obvious from the diff. Each small commit is a checkpoint you can return to.
3. **Open a pull request a reviewer can say yes to.** Push the branch, open the PR, and state
   **what changed, why, and how you verified it** (tests run, before/after numbers). Keep it
   small — reviewers' defect-finding ability measurably drops as diffs grow past a few
   hundred changed lines (see the size evidence in the reference) — link the issue, and call
   out anything you're unsure about so review attention lands there. A diff shows changes,
   not completion: when a PR claims a whole phase is done and the next phase will build on
   it, verify the claim with `coding-agent-skills:the-foreman` before relying on it.
4. **Integrate with merge or rebase — on purpose.** To update your branch with the latest main:
   - `git merge main` preserves exactly what happened and adds a merge commit — safe,
     truthful history.
   - `git rebase main` replays your commits on top of main for a linear history — cleaner,
     but it rewrites your commit hashes. Only rebase commits you have not shared (or that
     no one has based work on): force-pushing a rewritten shared branch breaks everyone
     else's copy.
5. **Resolve conflicts calmly.** A conflict just means two branches changed the same lines;
   git marks them with `<<<<<<<`, `=======`, `>>>>>>>`. For each: open the file, decide the
   *correct combined* result (not blindly "keep mine"), delete the markers, then `git add`
   the file. Finish with `git merge --continue` (or `git rebase --continue`); re-run the
   tests — a clean merge can still be logically wrong. `git merge --abort` backs all the
   way out.
6. **Review a diff in a fixed order: correctness → readability → style.** Does it do the
   right thing and handle edge cases and errors? Can the next person understand it? Only
   then naming/format nits (ideally automated away). Two hand-offs live inside this step:
   when review confirms a real bug, contact-trace its copies with
   `coding-agent-skills:defect-epidemiology` before closing the fix — a confirmed defect is
   evidence about a population, not a line; and when the change is correct but looks like
   more machine than the job needs, review it against
   `full-stack-dev-skills:lean-code-principles` before approving the extra moving parts —
   and if the *whole solution*, not the code, is the overbuilt thing, run the Pencil Pass
   in `coding-agent-skills:soviet-space-graphite`.
7. **Write feedback that names the line, the concern, and a fix.** Separate blocking from
   nice-to-have (`nit:` prefix), ask questions where you might lack context, praise what's
   genuinely good, and approve when the change is correct and clear — not when it is
   perfect. When a comment reads as a verdict on the author rather than the code, rewrite
   it with `collaboration-skills:feedback-that-lands` (behavior, impact, request — never
   inferred character).

## Why / learn
Version control is two things at once: a **safety net** and a **collaboration protocol**. As
a safety net, every atomic commit is a checkpoint and every branch is a sandbox you can throw
away — which is what makes it safe to experiment. As a protocol, the history and the pull
request are how you *communicate* a change to other humans across time. That reframing
explains every practice here: small, well-described changes are reviewable changes, and
reviewable changes are the ones that actually get reviewed rather than rubber-stamped. The
size discipline is measured, not folklore: the SmartBear study of Cisco's review data found
defect discovery effectiveness falls off beyond roughly 200–400 changed lines per review and
at inspection rates above ~500 lines per hour [snippet-only] — a thousand-line PR isn't
reviewed, it's skimmed with a signature. A commit message answers the question the diff
can't — *why* — for the person (often future-you) running `git blame` a year later. Merge
versus rebase is a choice between two values: merge keeps a truthful record; rebase keeps a
clean, linear story — and the golden rule against rebasing shared history exists because
rewriting commits others have pulled forces them to untangle a history that no longer matches
theirs. Reviewing correctness-first matters because a beautifully formatted function that
computes the wrong number is worse than an ugly one that's right; style is the cheapest thing
to fix and should not crowd out substance. And review is a *relationship* protocol too: the
comment that lands changes the code and keeps the colleague — which is why tone gets its own
step instead of being left to chance.

## Common mistakes
- One giant branch/commit mixing five changes → impossible to review or revert. One logical
  change per branch.
- Messages like "fix" / "update" / "wip" → useless in `git blame`. Say what changed and why.
- Rebasing or force-pushing a shared branch → rewrites history others have → breaks their
  clones. Rebase only what nobody else has.
- "Accept theirs / accept mine" to clear a conflict fast → silently drops real work. Decide
  the correct combined result.
- Assuming a conflict-free merge is a correct merge → re-run tests; logic can break with
  zero conflicts.
- The thousand-line PR ("it's all one feature") → split it; defect discovery collapses as
  diffs grow [snippet-only]. Stacked small PRs beat one unreviewable one.
- Review comments that are vague ("this feels off") or nitpick style over a real bug →
  point at lines, prioritize correctness, be specific and kind.
- Closing a review that found a real bug without asking where else the pattern lives → the
  fix ships, its copies don't hear about it. Contact-trace first.

## Tailor to your environment
Wire in your current team here — this skill is deliberately employer-neutral and moves with
you. Record real conventions in `references/your-environment.md`: default branch name, branch
and commit-message format, whether you merge or rebase to update, squash-merge policy, PR
template and required checks, and who reviews what. Once written down, those conventions are
a rule set — hunt their conflicts and loopholes with `coding-agent-skills:rule-stress-testing`
(house git rules are one of its named inputs) before they bite in production. Keep anything
sensitive (private repo hosts, tokens, reviewer names/emails) in
`references/your-environment.private.md`, which `.gitignore` keeps out of git.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/git-and-code-review.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/review-checklist.md — the full review method: order, checklists, size and pacing
  evidence, feedback grammar, and a worked example review
- references/git-commands.md — task-oriented git commands: branch, stage, commit, update,
  undo, resolve conflicts
- references/your-environment.md — your branch/commit/PR conventions and required checks
  (fill in per team)
