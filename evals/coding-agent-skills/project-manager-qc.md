# Evals — coding-agent-skills:project-manager-qc (and the project-manager subagent)

## 1. Positive trigger (should load the skill)
> "Build me a small pipeline that pulls last quarter's orders, cleans them, totals them by region
> and writes a one-page summary with a chart. Plan it properly and keep the token spend sensible —
> last time this kind of job burned through a lot."

Expected: skill loads. It sizes the management to the job (this is a several-deliverable task, so
a written plan and a quality gate), writes an outcome and checkable acceptance criteria for each
deliverable, a task list with owners and dependencies, a delegation shape that keeps narrow reads
inline, and a budget with a stop rule. It works with the token rules visible in its tool use
(sizing before reading, sliced reads, batched calls, bounded outputs), checkpoints at the phase
boundary, and runs the QC gate in a fresh context before the final message, fixing any LOAD item
first. The final message is short: outcome, evidence, what is left.

## 2. Positive trigger, gate only (should load)
> "Before you send me that report, have something independent check it against what I asked for."

Expected: skill loads and dispatches the `project-manager` subagent in QC mode with the acceptance
criteria, the deliverable paths and the check commands — not a summary of the work — and acts on
the verdict: LOAD items fixed and re-inspected, PUNCH items reported.

## 3. Near-miss A (should NOT load this skill)
> "We're about to start phase two of the warehouse migration with the ops team. Red-team the plan
> and give us an intervention log and a now-next-later board."

Expected: `continuous-improvement-skills:project-command-center` loads. A human team's project
doctrine, not the agent's own pipeline.

## 4. Near-miss B (should NOT load this skill)
> "The team says the payments module is done and wants to start building refunds on top of it.
> Can you check it's really finished first?"

Expected: `coding-agent-skills:the-foreman` loads. Inspecting a codebase's built state before the
next build phase.

## 5. Quality rubric
A good response:
- **Testable done:** every deliverable has a criterion a stranger could check.
- **Proportion:** no plan or gate on a trivial task; a subagent only where it reads a lot and
  returns a little.
- **Independent gate:** the QC subagent gets paths, criteria and check commands, never the
  author's summary; it opens files and runs checks; LOAD items are fixed before delivery.
- **Token discipline visible:** sizing before reading, slices instead of whole files, batched
  calls, bounded outputs, no polling, no re-reading after an edit.
- **Ledger and budget:** spend recorded at checkpoints; the stop rule used when the budget is short.
- **Teaches:** why self-review in the same context misses things; why input tokens dominate.

## 6. Subagent checks (QC mode)
On a deliverable with planted defects — a listed file that does not exist, a stated row count that
disagrees with the file, a self-test claimed to pass that fails, a headline figure with no source,
a credential in a folder that will be committed — and one correct item, the subagent returns HOLD,
lists every planted defect as LOAD with the evidence it ran or read, does not flag the correct item,
modifies nothing, and stays within its output limit.

## 7. Script checks
- `token_ledger.py --self-test` prints `all offline logic checks passed` and exits 0 (assert the pass
  line and exit code, not a total).
- **Estimate:** characters ÷ 3.5 rounded up; largest first, ordered by size not name; cache folders
  skipped; binary files flagged, not read; a file over `--max` gets slice advice; `--glob` filters;
  a missing path is an input error; the rendered output never contains file contents.
- **Ledger:** records append in order; empty task names, negative tokens and unknown kinds are
  refused and not written; a corrupt line is an error, not skipped; tokens must be integers.
- **Report:** totals by phase and kind; repeated task names found case-insensitively; over budget,
  near budget (over 80%) and one entry above a quarter of the spend are flagged; a balanced ledger
  raises no flags.
- **CLI:** exit 0 ok, 2 unreadable ledger, 5 bad usage.
- The self-test was mutation-tested: 20 deliberate breakages, all caught.
