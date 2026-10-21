---
name: project-manager-qc
description: >-
  Runs multi-session and multi-agent work like a well-managed project. Builds a requirement ledger
  first — every deliverable, name, column, number, format, limit, exclusion and "don't", later
  amendments superseding earlier lines — then plans phases with testable acceptance criteria,
  owners, a token budget and checkpoints that survive across sessions, and gates delivery with an
  independent quality sweep by the project-manager subagent in fresh context: each requirement,
  each number recomputed from source, each claim, code paths, what tests really assert, every
  file, format — not stopping at the first findings. Stays out of single-session tasks, where a
  benchmark found no gain. Use when work spans several sessions or agents, or a deliverable needs
  a reviewer that did not build it. Triggers: project manager, multi-session project, coordinate
  the subagents, independent QC gate, multi-agent project, phase plan, track the work across
  sessions.
metadata:
  version: "2.1.0"
---

# Project Manager & Quality Control

Work that spans sessions or agents fails in three predictable ways: a requirement buried in the
request — often a late amendment — is dropped between hand-offs; the work is checked only by the
context that produced it; and nobody can say where the effort or the budget went. This skill puts
a project manager on that kind of job. The manager is a subagent, `project-manager`, called for the
plan, at phase boundaries and for the gate; between calls the main agent keeps the ledger and runs
lean with `coding-agent-skills:puppet-master`. **Everything a session needs is on this page** — the
references are for briefing the subagent and planning long work.

**Scope, from measurement.** On single-session tasks of up to a few deliverables, a benchmark found
an unaided agent already met every requirement and caught every planted defect, so this skill
added cost without adding quality there. It engages when the work outlasts one context: several
sessions, several agents, or a deliverable that needs a reviewer who did not build it.

## When to use
- Work that will span several sessions — a migration, a multi-week build, a research programme —
  and needs a ledger, a phase plan and checkpoints that the next session can pick up.
- Work split across several agents or subagents that need briefs, a budget, and one place where
  their results are checked against the request.
- A deliverable that must be reviewed by something that did not build it before it ships.
- A long-running effort whose spend needs tracking against a budget at phase boundaries.
- **In tandem.** The delegation audit (in this library's author environment,
  anthropic-skills:max-delegation-auditor) decides who owns each step;
  `coding-agent-skills:creative-workaround-genius` finds another route when a step fails;
  `coding-agent-skills:puppet-master` keeps each step lean; this skill plans the whole, keeps it
  inside budget across sessions, and checks it before it ships.
- Not for: running a human team's project with red-team and flow doctrine →
  `continuous-improvement-skills:project-command-center`; walking a codebase's built state before
  the next build phase → `coding-agent-skills:the-foreman` (whose bins the gate borrows); a
  multi-angle code optimization audit → `coding-agent-skills:board-review`; cutting the token cost
  of a single task or run → `coding-agent-skills:puppet-master`; a single-session task or review
  → no skill needed.

## Do it

1. **Confirm the work needs managing.** A single-session task gets none of this. Engage when the
   work spans sessions or agents, or needs an independent reviewer; then the ledger (step 2), the
   plan (step 3), checkpoints (step 4) and the subagent-run sweep (step 5) all pay for themselves.
   Do not produce planning documents nobody asked for. When you cannot spawn the subagent, you do
   not need its definition file: the steps here are the whole procedure.

2. **Build the requirement ledger before you start.** Read the whole request or spec to the end
   first — amendments, footnotes and "oh, and…" lines live at the bottom. Then list every
   requirement as one short numbered line with its source words: each deliverable and its path or
   name; each column, field and its order; each number, limit and rounding rule; each filter,
   exclusion and boundary (dates, time zones, inclusive or exclusive); each format detail
   (separators, decimals, index columns, line or word limits); each "don't" (do not modify inputs,
   no customer data). **Later statements supersede earlier ones** — an amendments section, an
   "instead", a "now called", a "drop X": strike the old line and point to the new one. Where the
   text is ambiguous, pick the reading it supports and note it; ask only if a wrong guess is
   costly. Keep the ledger in a file outside the project, where the next session and every agent
   can read it.

3. **Plan with a testable "done", then run lean.** Each ledger line becomes an acceptance check
   someone else could run. Dispatch the subagent in PLAN mode (brief template in
   `references/plan-and-qc-templates.md`) and adopt or argue with its plan: phases, owners,
   dependencies, the delegation shape, a budget and a stop rule. While working, follow
   `coding-agent-skills:puppet-master` — fewer turns, small new context, subagents only where they
   repay their start-up cost — and size files before reading them:
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" estimate <paths> --max 20000`.
   The cost model is in `references/token-efficiency-rules.md`.

4. **Checkpoint long work at phase boundaries.** What is done, the largest consumer, whether the
   rest fits, and anything unasked-for being built. Log usage as it arrives and read the ledger:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" log <ledger.jsonl> --task "<name>" --tokens <n> --phase <phase> --kind subagent --ms <ms>
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" report <ledger.jsonl> --budget <n>
   ```
   Keep the ledger outside any repository.

5. **Run the quality sweep before delivery — every category, every time.** Reviewers find the
   first few loud problems and stop; the quiet ones ship. So the sweep ends when every category
   below is done, not when the findings feel like enough. Re-open the request or spec file; do not
   work from memory. On **your own build**, put the checks at the end of the build itself —
   assertions that each ledger line holds and an independent recount of the headline figures —
   so one run builds and verifies; dismiss categories that do not apply in a word. On **someone
   else's work**, walk every category with one profiling-and-recompute script, and read what the
   tests assert rather than re-engineering them.
   1. **Requirements** — each ledger line, pass or fail, with evidence from the artefact itself.
   2. **Numbers** — recompute every headline figure from the source, independently of the code
      under review; totals that should agree across files must agree.
   3. **Claims** — every statement in handoff notes, summaries, changelogs and READMEs ("all tests
      pass", "reconciled", "attached", "follows the spec"): true, false, or unverifiable.
   4. **Code paths** — does the shipped path use the cleaned or filtered data; date and time-zone
      boundaries; status and account filters; joins, de-duplication, units, rounding.
   5. **Tests** — run them; then read what each asserts and whether it exercises the shipped path.
      A skipped, vacuous or missing test is not coverage.
   6. **Files** — list the deliverable folder: anything missing, and anything that should not be
      there (debug dumps, personal data, secrets, a `.env` not covered by `.gitignore`).
   7. **Format** — exact headers and column order, index columns, separators, decimals, line and
      word limits, names, encodings.
   8. **Examples** — run documented commands exactly as written.
   Every finding carries its evidence (the command and what it showed), a concrete fix, and a bin:
   **LOAD** (fix before delivery), **PUNCH** (real, does not block), **FUTURE** (not asked for).
   A finding needs a violated requirement or a real risk; do not flag correct work to look
   thorough. On substantial work, dispatch the subagent in QC mode with the request path, the
   deliverable paths and the check commands, so the gate has fresh eyes. If you cannot spawn one
   (you are already a subagent, or the tool is absent), run the sweep yourself as a separate pass.

6. **Fix, re-inspect, and report short.** Fix every LOAD item in your own work, then re-check only
   those items. When reviewing someone else's work, change nothing — report. The final message
   leads with the verdict or the outcome; then the must-fix items with evidence and fix; then what
   was verified sound, in a line or two; then anything for the user to decide. Record the one
   lesson that would make the next plan better where the next session will find it.

## Why / learn

**Why a requirement ledger, and why amendments win.** Most delivery failures are not hard
problems solved wrongly; they are easy requirements never registered — a renamed column in an
appendix, a time zone changed in a review meeting, a file name amended in the last line of the
message. A request is read top to bottom but obeyed as a whole, so the reader who starts building
at line three builds the superseded version. Writing every requirement down, with the later word
winning, turns "did I miss anything?" from memory into a checklist.

**Why the sweep is exhaustive by category.** Radiologists call it satisfaction of search: after
the first finding, the chance of spotting a second falls, because the search feels complete
[background — verify]. Review shows the same pattern — the loud bug is found and the quiet
date-boundary error ships. A fixed list of categories, each walked to the end, is the
countermeasure, and it makes precision visible, because each category also yields "verified
sound". A fresh-context subagent adds independence — the inspector is not the builder [canon
attribution — draw inspections, as The Foreman uses them] — and when none can be spawned,
re-opening the source files and walking the categories gets most of the way.

**Why management must pay for itself.** A benchmark of this skill's first version found an
unaided agent already caught every planted defect in a seven-defect review and met every
requirement of a nine-requirement build, while the skill added up to three-quarters more time.
Ceremony on easy work is waste, which is why this skill now engages only when the work outlasts
one context; the ledger and the sweep stay because hand-offs between sessions and agents are where
requirements get dropped and blind spots go unchecked.

## Common mistakes
- Starting to build before reading the request to the end → the amendment is at the bottom.
- Building to the superseded requirement → later words win; strike the old ledger line.
- Stopping the review after the big findings → finish every sweep category.
- Trusting the author's numbers or notes → recompute from source; test every claim.
- Counting passing tests as coverage → read what they assert and whether they run the real path.
- Missing the extra file → list the folder; debug dumps and secrets hide in plain sight.
- Flagging correct work to look thorough → a finding needs a violated requirement or a real risk.
- Writing plans and checkpoints for a short task → size the management to the job.
- Briefing a subagent by pasting files → give paths and the question; ask for a compact return.
- Running eight separate investigations on your own small build → checks inside the build run.
- Opening every reference file for a one-session task → this page is the whole procedure.
- A final message that recaps every step → verdict, must-fix items, verified items, decisions.

## Tailor to your environment
Record in `references/your-environment.md`: the check commands that define "green" in your
projects, the rails every deliverable must respect, your usual budget per task size, where the
ledger lives, and the lessons from past checkpoints that should shape the next plan.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/project-manager-qc.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/token-efficiency-rules.md — the cost model, each rule with its reasoning and an
  example, the anti-patterns, and how to estimate a task's budget.
- references/plan-and-qc-templates.md — the requirement-ledger format, the subagent briefs for
  PLAN, CHECKPOINT and QC, the sweep as a checklist, and the punch-list bins.
- references/your-environment.md — your green checks, rails, budgets and lessons (fill in; the
  `.private.md` twin is git-ignored).

## Scripts
- `scripts/token_ledger.py` — `estimate <paths>` sizes files in estimated tokens (characters ÷
  3.5), largest first, and flags anything over `--max` with a cheaper way to read it; `log` appends
  usage to a JSON-lines ledger; `report` totals by phase and kind, names the largest consumers and
  repeated task names, and flags budget overrun. `--self-test` for the offline checks; exit 2 on
  unreadable input, 5 on bad usage.
- The subagent definition ships beside the skills: `agents/project-manager.md` in this plugin,
  invoked as the `coding-agent-skills:project-manager` agent type.
