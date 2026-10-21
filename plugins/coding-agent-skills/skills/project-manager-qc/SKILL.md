---
name: project-manager-qc
description: >-
  Runs an agent's own multi-step work like a well-managed project: a kickoff plan with testable
  acceptance criteria, owners, dependencies and a token budget; task tracking at real
  transitions; checkpoints that catch scope creep and wasted tokens; and an independent quality
  gate before delivery, run by the project-manager subagent with fresh context so the work is
  not graded by the context that produced it. Applies token discipline throughout: measure
  before reading, read slices, batch calls, bound outputs, brief subagents with paths not
  pastes, right-size the fleet, script repeated work. Use for any substantial task, before
  delivering anything that matters, or when a session is burning tokens. Triggers: project
  manager, plan this task, task breakdown, quality control, QC gate, check the work before
  delivery, internal review, token budget, token efficiency, save tokens, reduce token usage,
  keep the task on track.
metadata:
  version: "1.0.0"
---

# Project Manager & Quality Control

A substantial task fails in three predictable ways: nobody wrote down what done means, so it
drifts; the work is graded by the same context that produced it, so its blind spots ship; and
tokens go to re-reading, re-deriving and over-delegating instead of to the work. This skill puts
a project manager on the job for all three. The manager is a subagent, `project-manager`, called
at kickoff, at phase boundaries and before delivery; between calls, the main agent follows the
token discipline below.

## When to use
- A task with several deliverables, more than about ten tool calls, any subagent work, or a
  deadline or budget — before starting it.
- Anything about to be delivered that someone will act on: a report, a release, a pull request, a
  data file, a skill. The quality gate runs before the final message, not after.
- A session that is visibly expensive: the same files read repeatedly, long outputs pasted into
  context, many subagents, polling.
- **In tandem.** The delegation audit (in this library's author environment,
  anthropic-skills:max-delegation-auditor) decides who owns each step;
  `coding-agent-skills:creative-workaround-genius` finds another route when a step fails; this skill
  plans the whole, keeps it inside budget, and checks it before it ships.
- Not for: running a human team's project with red-team and flow doctrine →
  `continuous-improvement-skills:project-command-center`; walking a codebase's built state before
  the next build phase → `coding-agent-skills:the-foreman` (whose bins the quality gate borrows);
  a multi-angle code optimization audit → `coding-agent-skills:board-review`.

## Do it

1. **Size the management to the job.** Management costs tokens too, so it must cost less than it
   saves. A one-to-three-step task gets none. A task of up to about ten steps gets an inline
   kickoff (step 2, written in a few lines) and an inline quality checklist (step 5, run yourself).
   Anything larger, or anything with subagents, gets the `project-manager` subagent for the plan
   and the gate. Long or multi-session work also gets checkpoints and a ledger.

2. **Kick off with a plan whose "done" is testable.** Write the outcome, the deliverables, and an
   acceptance test for each that someone else could check — a file with a property, a command
   that exits 0, a count, a cited source. Then the tasks (input, output, owner, dependency, rough
   cost, done test), the delegation shape, and a budget with a stop rule saying what gets cut first.
   For a substantial task, dispatch the subagent in PLAN mode with a short brief and adopt or argue
   with its plan; the brief template is in `references/plan-and-qc-templates.md`. Put the
   deliverable-level tasks in the task list, one in progress at a time, updated at real
   transitions rather than at every step.

3. **Work with token discipline.** These rules carry most of the savings; the reasoning and the
   cost model are in `references/token-efficiency-rules.md`.
   - **Measure before reading.** Size files first, then read a slice or grep:
     ```
     python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" estimate <paths> --max 20000
     ```
   - **Read once.** Keep what you learned; edit by exact replacement; re-read only what changed.
   - **Batch independent calls** in one turn; chain dependent ones.
   - **Bound every output** — `head`, `tail`, `cut`, quiet flags, counts instead of listings.
   - **Delegate wide reads, not narrow ones.** A subagent pays its own context cost before it does
     anything, so it earns its keep only when it reads a lot and returns a little. Brief it with
     paths and the exact question, not pasted contents; ask for a compact, structured return.
   - **Right-size the fleet.** Fewer, better-briefed subagents; parallel agents can exhaust a
     shared budget (searches, rate limits) for each other.
   - **Script what repeats.** The third time you do something by hand, write the script.
   - **Write durable facts down** — the plan, the ledger, memory files — instead of re-deriving.
   - **No polling.** Wait for notifications; schedule a check-in for what cannot notify.
   - **Stop at the acceptance criteria.** Work no criterion asks for is scope creep, however good.

4. **Checkpoint at phase boundaries.** Compare progress and spend with the plan: what is done,
   what the largest consumer was, whether the rest fits, and whether anything being built is
   unasked-for. Log usage figures as they arrive — a subagent's completion notice reports its
   tokens and duration — and read the ledger:
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" log <ledger.jsonl> --task "<name>" --tokens <n> --phase <phase> --kind subagent --ms <ms>
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/project-manager-qc/scripts/token_ledger.py" report <ledger.jsonl> --budget <n>
   ```
   On long work, dispatch the subagent in CHECKPOINT mode and follow its re-plan. Keep the ledger
   outside any repository.

5. **Run the quality gate before delivery.** Dispatch the subagent in QC mode with the acceptance
   criteria, the deliverable paths, the check commands and any rails (privacy, repository rules,
   claims that must be sourced). Fresh context is the point: it inspects the work, not your account
   of it. It returns PASS or HOLD with a punch list in three bins — LOAD (fix before delivery),
   PUNCH (fix soon), FUTURE (not asked for). Fix every LOAD item, then re-inspect only those items.
   Report the PUNCH items to the user plainly; leave FUTURE items out unless they matter.

6. **Close the loop.** Deliver with the evidence the gate produced, note what the budget actually
   was against the plan, and record the one or two lessons that would make the next plan better
   (for example, which phase overran and why) where the next session will find them.

## Why / learn

**Why a testable "done" comes first.** Most drift and most over-spend start from an outcome that
was never pinned down: without an acceptance test, every extra feature looks like progress and
every review is a matter of taste. A criterion someone else could check turns the quality gate
from opinion into inspection, and it is the stop rule for the work itself.

**Why the gate runs in a different context.** Self-review in the same context inherits the same
assumptions, the same misread file, and the same belief that a step happened because it was
planned. The construction trades solved this with independent inspection before the next payment
releases [canon attribution — draw inspections, as The Foreman uses them]; software solved it with
code review by someone who did not write the code. A fresh subagent is the cheapest independent
reviewer an agent has, and it should look at files and run checks, not read the summary.

**Why token discipline is mostly about context, not prose.** The expensive things are what lands
in context and stays there: whole files read to find one line, full logs pasted into a reply,
the same file read three times, a subagent briefed so vaguely that it re-reads everything the
caller already knew. Each of those costs input tokens on every later turn, not just once. So the
biggest savings come from reading less and returning less, not from writing shorter sentences.
Subagents trade one cost for another: they keep a wide read out of the main context, but each
starts by loading its own context, so delegating a narrow read costs more than doing it.

**Why management must pay for itself.** A plan for a three-step task, or a gate on a one-line
answer, is overhead with no return. Sizing the management to the job (step 1) keeps the manager
from becoming the waste it exists to remove.

## Common mistakes
- Acceptance criteria that only the author can judge ("looks good") → write a check a stranger
  could run.
- Grading your own work in the same context and calling it QC → dispatch the subagent with paths
  and criteria, not a summary.
- Briefing a subagent by pasting files into the prompt → give paths and the question; ask for a
  compact return.
- Delegating a two-file read to a subagent → do narrow reads inline; delegate wide ones.
- Launching many parallel researchers on a shared budget → fewer, better-briefed agents.
- Reading a large file whole to find one fact → size it, grep, read a slice.
- Updating the task list at every step → update at real transitions; the list is for the user and
  for recovery, not a diary.
- Fixing punch items while a LOAD item is open → LOAD first, then re-inspect only what changed.
- Treating the plan as fixed → re-plan at checkpoints; a plan that cannot change is a guess.
- Letting the manager cost more than the task → size it to the job.

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
- references/plan-and-qc-templates.md — the subagent briefs for PLAN, CHECKPOINT and QC, the
  kickoff plan format, the inline checklist for small tasks, and the punch-list bins.
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
