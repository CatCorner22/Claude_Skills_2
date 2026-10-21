---
name: project-manager-qc
description: >-
  Runs an agent's own multi-step work like a well-managed project, sized to the job. Builds a
  requirement ledger first — every deliverable, name, column, number, format, limit, exclusion
  and "don't" in the request, with later amendments superseding earlier lines — so nothing is
  dropped; plans with testable acceptance criteria and a token budget; and gates delivery with an
  exhaustive quality sweep (each requirement, each number recomputed from source, each claim in
  notes and summaries, code paths, what tests really assert, every file in the folder, format
  details) that does not stop at the first findings. The project-manager subagent runs the plan
  and the gate with fresh context when it can. Applies token discipline throughout. Use for any
  substantial task, before delivering anything that matters, or to check someone's finished work.
  Triggers: project manager, plan this task, quality control, QC gate, check the work before
  delivery, is this ready to send, review against the spec, token budget, save tokens.
metadata:
  version: "2.0.0"
---

# Project Manager & Quality Control

A substantial task fails in three predictable ways: a requirement buried in the request — often a
late amendment — is dropped; the work is checked by a reviewer who stops after the first few
problems; and tokens go to ceremony instead of the work. This skill puts a project manager on the
job for all three, and keeps the management cheaper than what it saves. The manager is a subagent,
`project-manager`, called for the plan and the gate on substantial work; on small work, and when
no subagent can be spawned, the main agent runs the same steps itself. **Everything a
single-session task needs is on this page** — the references are for briefing the subagent and
planning long work, so skip them otherwise.

## When to use
- A task with several deliverables or a written spec, any subagent work, or a deadline or budget —
  before starting it.
- Anything about to be delivered that someone will act on: a report, a release, a pull request, a
  data file, a skill. The gate runs before the final message, not after.
- Someone's finished work needs checking against what was asked: "is this ready to send?"
- A session that is visibly expensive: the same files read repeatedly, long outputs pasted into
  context, many subagents, polling.
- **In tandem.** The delegation audit (in this library's author environment,
  anthropic-skills:max-delegation-auditor) decides who owns each step;
  `coding-agent-skills:creative-workaround-genius` finds another route when a step fails; this skill
  plans the whole, keeps it inside budget, and checks it before it ships.
- Not for: running a human team's project with red-team and flow doctrine →
  `continuous-improvement-skills:project-command-center`; walking a codebase's built state before
  the next build phase → `coding-agent-skills:the-foreman` (whose bins the gate borrows); a
  multi-angle code optimization audit → `coding-agent-skills:board-review`.

## Do it

1. **Size the management to the job.** Management costs tokens too, so it must cost less than it
   saves. A one-to-three-step task gets none. Anything with a written spec or several deliverables
   gets the requirement ledger (step 2) and the sweep (step 5) — that pair carries most of the
   value. Plans, checkpoints and the subagent are for substantial or multi-session work. Do not
   produce planning documents nobody asked for. When you cannot spawn the subagent, you do not
   need its definition file: the steps here are the whole procedure.

2. **Build the requirement ledger before you start.** Read the whole request or spec to the end
   first — amendments, footnotes and "oh, and…" lines live at the bottom. Then list every
   requirement as one short numbered line with its source words: each deliverable and its path or
   name; each column, field and its order; each number, limit and rounding rule; each filter,
   exclusion and boundary (dates, time zones, inclusive or exclusive); each format detail
   (separators, decimals, index columns, line or word limits); each "don't" (do not modify inputs,
   no customer data). **Later statements supersede earlier ones** — an amendments section, an
   "instead", a "now called", a "drop X": strike the old line and point to the new one. Where the
   text is ambiguous, pick the reading it supports and note it; ask only if a wrong guess is
   costly. Keep the ledger short — in your head or your plan for a single session; a scratch file
   outside the project only when the work spans sessions.

3. **Plan with a testable "done", then work with token discipline.** Each ledger line becomes an
   acceptance check someone else could run. For substantial work, dispatch the subagent in PLAN
   mode (brief template in `references/plan-and-qc-templates.md`) and adopt or argue with its
   plan; set a budget and a stop rule. While working:
   - Measure before reading; grep, then read a slice. Size with
     `python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" estimate <paths> --max 20000`.
   - Read once; batch independent calls; bound every output.
   - Delegate wide reads, never narrow ones; brief with paths, not pastes; ask for compact returns.
   - Script what repeats; no polling; stop at the acceptance criteria.
   The reasoning and the cost model are in `references/token-efficiency-rules.md`.

4. **Checkpoint long work at phase boundaries.** What is done, the largest consumer, whether the
   rest fits, and anything unasked-for being built. Log usage as it arrives and read the ledger:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" log <ledger.jsonl> --task "<name>" --tokens <n> --phase <phase> --kind subagent --ms <ms>
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" report <ledger.jsonl> --budget <n>
   ```
   Keep the ledger outside any repository. Skip this step on short work.

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
Ceremony on easy work is waste; the ledger and the sweep stay because they target the cases that
do fail, and they are kept to one pass when the work is your own.

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
