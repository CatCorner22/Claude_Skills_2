# Evals — coding-agent-skills:project-manager-qc (and the project-manager subagent)

## 1. Positive trigger (should load the skill)
> "We're moving forty reporting tables to the new warehouse over the next few weeks. It will take
> several sessions, and I want subagents doing the per-table work. Before anything starts, plan it
> so any session can pick up where the last one stopped, and keep the token spend under control."

Expected: skill loads. It confirms the work spans sessions and agents; reads the whole request to
the end and builds a requirement ledger, kept in a file the next session and every agent can read (every deliverable, name, column, number, format, limit, exclusion and
"don't", with later amendments superseding earlier lines); writes a testable "done" for each line
and a budget with a stop rule; works with the token rules visible in its tool use (sizing before
reading, sliced reads, batched calls, bounded outputs); and before the final message runs the
quality sweep on its own output as one verification pass — ideally a single script that checks
every ledger line against the outputs and recomputes the figures a second way. The final message is
short: outcome, evidence, what is left.

## 2. Positive trigger, gate only (should load)
> "Before you send me that report, have something independent check it against what I asked for."

Expected: skill loads and dispatches the `project-manager` subagent in QC mode with the request
path, the deliverable paths and the check commands — not a summary of the work — or, where no
subagent can be spawned, walks the eight sweep categories itself after re-opening the request. It
acts on the verdict: LOAD items fixed and re-inspected, PUNCH items reported.

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

## 4a. Near-miss C (should NOT load this skill)
> "My analyst says the quarterly numbers are finished and wants to send them to the regional VPs
> today. Is it ready to go? What I originally asked for is in request.md."

Expected: no skill loads. A single-session check of one finished deliverable is work the model does
well unaided (see §8); the plugin eval case `ignores-single-review` asserts it.

## 4b. Near-miss D (should NOT load this skill)
> "Last night's agent run used far more budget than a job that size should. Here's its transcript —
> where did it all go?"

Expected: `coding-agent-skills:puppet-master` loads. Cutting the token cost of one task or run.

## 5. Quality rubric
A good response:
- **Requirement ledger:** every requirement in the request is listed, and a later amendment
  ("instead", an amendments section, a renamed field) supersedes the earlier line.
- **Testable done:** every deliverable has a criterion a stranger could check.
- **Proportion:** no ledger, plan or gate on single-session work; a subagent only where it reads a
  lot and returns a little.
- **Independent gate:** the QC subagent gets paths, criteria and check commands, never the
  author's summary; it opens files and runs checks; LOAD items are fixed before delivery.
- **Exhaustive sweep:** requirements, numbers recomputed from source, claims, code paths, what the
  tests assert, every file in the folder, format, documented examples — each category walked to the
  end, with "verified sound" reported as well as defects; correct work is not flagged.
- **Token discipline visible:** sizing before reading, slices instead of whole files, batched
  calls, bounded outputs, no polling, no re-reading after an edit.
- **Ledger and budget:** spend recorded at checkpoints; the stop rule used when the budget is short.
- **Teaches:** why self-review in the same context misses things; why input tokens dominate.

## 6. Subagent checks (QC mode)
On a deliverable with planted defects — a listed file that does not exist, a stated row count that
disagrees with the file, a self-test claimed to pass that fails, a headline figure with no source,
a credential in a folder that will be committed, an amendment in the spec that was never applied —
and one correct item, the subagent builds its own requirement ledger from the request, returns
HOLD, lists every planted defect with the evidence it ran or read, does not flag the correct item,
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

## 8. Benchmark — 2026-10-21 (version 2.0.0 against no skill and 1.0.0)
Six scenarios: two reviews of finished work with planted defects (a sales summary with seven,
including an off-by-one date boundary and a de-duplication result that is computed but never
used; a CLI release with six, including a skipped failing test and a token in an un-ignored `.env`),
one review with ten defects against a spec whose amendments supersede earlier sections, and three
builds (contacts clean-up with a buried filename amendment; inventory reconciliation with case units
and discontinued items; a KPI pack from a long spec with three late amendments). Two held-out
scenarios were added after a pilot showed the first ones at ceiling. Scripted checks on every
output, blind graded findings on every review; two runs per arm on held-out cases.

| Arm | Checks passed | Mean tokens | Mean time |
|---|---|---|---|
| No skill | 97/97 (100%) | 70k | 86 s |
| 1.0.0 | 97/97 (100%) | 83k | 120 s |
| 2.0.0 | 97/97 (100%) | 80k | 108 s |

Every arm found every planted defect and met every requirement, including all three late
amendments. 2.0.0 is cheaper than 1.0.0 (about 3% fewer tokens, 10% less time) at the same quality,
but at this task size it costs more than working without it (about 14% more tokens, 26% more time)
with no measurable gain: the model under test already reads specs to the end and sweeps reviews
thoroughly. The ledger and sweep are insurance for longer, multi-session or multi-agent work, which
this benchmark did not measure.

## 9. Version 2.1.0 — scope narrowed from measurement (2026-10-21)
§8 found no quality gain on single-session work and a cost of about 14% more tokens and 26% more
time. 2.1.0 therefore engages only when work spans several sessions or agents, or needs a reviewer
that did not build it, and hands single-run token cost to `coding-agent-skills:puppet-master`. The
procedure is unchanged; the description, the "When to use" list and step 1 now say when to stay
out. The routing evals moved with it: the single-session review case became `ignores-single-review`,
and the planning case became a multi-session migration. The multi-session benefit is still
unmeasured: a fair test needs work that really crosses sessions, which a single-run benchmark
cannot reproduce.
