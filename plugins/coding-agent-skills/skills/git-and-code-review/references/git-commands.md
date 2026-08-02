# Git commands (task-oriented)

Grouped by what you're trying to do, not alphabetically. Commands are stable across recent git
versions; `git switch`/`git restore` are the modern verbs (older muscle memory uses `git checkout`
for both) — confirm your version with `git --version` if `switch` isn't available.

## Contents
- Start work
- See what's going on
- Stage and commit
- Update your branch
- Undo safely
- Resolve a conflict
- Share and open a PR

## Start work
```bash
git switch main && git pull            # get latest main
git switch -c feature/short-name       # create + switch to a new branch
git switch feature/short-name          # switch to an existing branch
```

## See what's going on
```bash
git status                              # what's staged, modified, untracked
git diff                                # unstaged changes
git diff --staged                       # what a commit would include
git log --oneline --graph --decorate -20
git blame path/to/file                  # who last changed each line, and in which commit
```

## Stage and commit
```bash
git add -p                              # stage hunk by hunk (review as you stage)
git add path/to/file                    # stage a specific file
git commit -m "Imperative subject line"
git commit                              # opens editor for subject + body (use for the 'why')
git commit --amend                      # fix the most recent commit (only if not yet pushed/shared)
```

## Update your branch with main
```bash
git switch feature/x
git merge main                          # merge commit; preserves history exactly
# or
git rebase main                         # linear history; rewrites YOUR commits — unshared only
```

## Undo safely
```bash
git restore path/to/file                # discard unstaged changes to a file
git restore --staged path/to/file       # unstage but keep the edits
git revert <commit>                     # new commit that undoes a commit — safe on shared history
git reset --soft HEAD~1                 # undo last commit, keep changes staged (local only)
git stash / git stash pop               # shelve work-in-progress and bring it back
```
Prefer `revert` over `reset --hard` on anything you've pushed — `revert` is additive and doesn't
rewrite shared history. Reach for `git reflog` to recover a commit you think you lost.

## Resolve a conflict
```bash
# after a merge/rebase reports conflicts:
git status                              # lists conflicted files
# edit each file: remove <<<<<<< ======= >>>>>>> markers, keep the correct combined result
git add path/to/resolved-file
git merge --continue                    # or: git rebase --continue
git merge --abort                       # or: git rebase --abort   (start over cleanly)
```
Then re-run the tests — a conflict-free resolution can still be logically wrong.

## Share and open a PR
```bash
git push -u origin feature/short-name   # first push sets upstream
gh pr create --fill                     # GitHub CLI: open a PR (or use the web UI)
gh pr view --web
```
Never `git push --force` a shared branch. If you must overwrite your *own* unshared branch after a
rebase, use `git push --force-with-lease` — it refuses if someone else pushed in the meantime.
