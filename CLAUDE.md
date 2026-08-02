# CLAUDE.md — treasury-analyst-skills

This repo is the `treasury-analyst-skills` plugin marketplace (100+ skills, 16+ plugins).
Authoring standard: `plugins/coding-agent-skills/skills/writing-agent-skills/SKILL.md` — read it
before creating or editing any skill. Validate with `bash scripts/validate.sh` and regenerate
`docs/SKILLS.md` via `python3 scripts/gen-catalog.py` after any skill change.

## Standing metacognition engagement (user-mandated, permanent)

The `metacognition-skills` suite is always engaged in this repo, not on-request:

1. **Session start:** read `MEMORY.md` (repo root) and apply the relevant facts, preferences,
   and avoidance rules to the current task. It is the validated semantic store.
2. **During work** (`hierarchical-memory-manager`): capture durable new facts, decisions, and
   preferences; keep working notes lean; flag contradictions with stored memory instead of
   overwriting.
3. **On any user correction** (`reflective-learner`): acknowledge → restate the corrected
   understanding → apply immediately → record the rule in `MEMORY.md`.
4. **At milestones and session end** (`knowledge-crystallizer`): run a crystallization pass —
   harvest → validate → distill → integrate into `MEMORY.md` → prune → append one line to its
   Crystallization log. Only validated, atomic, high-leverage entries become permanent.
5. **Never store** secrets, credentials, account numbers, or client data in `MEMORY.md` or any
   committed file. Sensitive tailoring detail goes in `*.private.md` (git-ignored).

## Git rules for this repo (hard-learned — see MEMORY.md lessons)

- The working branch is a **shared integration branch**: other agents (e.g. Cursor) also push
  to it. Before ANY push: `git fetch`, inspect the remote tip in its own step, and only then
  push in a separate command. Never chain a verification command with a push.
- PRs are squash-merged: after your PR merges, restart the branch from `origin/main`
  (`git fetch origin main && git checkout -B <branch> origin/main`). Prove "already-merged
  content" with a content diff against main, never by commit ancestry.
- Force-push only after the separate-step inspection shows the remote tip's content is fully
  contained in main or in your local branch.
