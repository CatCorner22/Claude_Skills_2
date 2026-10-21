# Evals — coding-agent-skills:puppet-master

## 1. Positive trigger, audit (should load the skill)
> "Last night's agent run used far more budget than a job that size should. Its transcript is
> run.jsonl in this folder. Where did it all go, and how do we bring it down without dropping any
> of the checks it ran?"

Expected: skill loads. It runs `token_audit.py` on the transcript and reports turns, start-up and
final context, processed and price-weighted tokens, and the waste signals. It names the dominant
cost (usually the turn count, with the start-up context re-sent on every turn) rather than the size
of the tool results. Each proposed saving names the calls it changes and the check that keeps
quality: probes batched into one turn and each still reporting its status, a dependent chain folded
into one script with assertions, tools loaded in one lookup. The estimate of the saving shows its
arithmetic and says it is an estimate.

## 2. Positive trigger, working lean (should load)
> "This clean-up touches a dozen files and a few data checks, and the last run like it cost a
> fortune. Do it properly, but on as small a token bill as you can."

Expected: skill loads. The quality bar is named first (every file, every check). Independent reads
and checks share a turn; dependent shell steps are chained with bounded output; the build and its
checks run as one script; nothing is re-read after an edit. The final message is short and still
cites the evidence for each claim.

## 3. Near-miss A (should NOT load this skill)
> "This system prompt makes the model ramble and ignore the output format we asked for. Rewrite it
> so the answers come back in the right shape."

Expected: `coding-agent-skills:prompt-engineering` loads. A prompt's wording, not a run's cost.

## 4. Near-miss B (should NOT load this skill)
> "We're moving forty reporting tables to the new warehouse over several sessions, with subagents
> doing the per-table work. Plan it so any session can pick up where the last one stopped."

Expected: `coding-agent-skills:project-manager-qc` loads (it then uses this skill as its token
discipline). Planning and gating multi-session work.

## 5. Quality rubric
A good response:
- **Bar first:** the requirements, checks and sources the result needs are fixed before anything
  is cut; nothing on that list is dropped to save tokens.
- **Turns:** independent calls share a turn; dependent shell steps are chained; no turn spent on a
  read whose answer was already in hand.
- **Small new context:** sizes before reads, slices or filters instead of whole files, bounded
  output, no re-reads after edits, references opened only when needed.
- **Delegation as a cost decision:** a subagent only when its start-up context is repaid; briefs
  carry paths and the question, never pasted contents.
- **Short with proof:** the reply leads with the result and keeps the evidence for each claim (file
  and function, or command and output); no narration or recap.
- **Audit (when asked):** numbers taken from the transcript's usage, the dominant driver named,
  savings specific to the run, every original check kept.

## 6. Script checks
- `token_audit.py --self-test` prints `all offline logic checks passed` and exits 0 (assert the pass
  line and exit code, not a total).
- **Accounting:** assistant messages de-duplicated by message id (a message split across lines
  counts once); processed sums input, cache write, cache read and output; weighted applies 1, 1.25,
  0.1 and 5; final context is the last call; start-up context is the first call's input side, not
  its output, and its share of processed is scaled by the number of turns.
- **Results:** list-form tool results measured; largest first; `--top` honoured; contents never
  printed.
- **Signals:** a repeated read is the same file and slice (different slices are not a repeat);
  `cat` without a bound, recursive listings and unbounded `find` are flagged, a bounded `cat` is
  not; single-call turns flagged only when they dominate; start-up re-sending flagged only on runs
  of three or more turns where it is at least half of processed; subagent spawns and results over
  5k tokens reported.
- **CLI:** exit 0 ok, 2 unreadable or empty transcript (a torn line is tolerated), 5 bad usage.
- The self-test was mutation-tested: 28 deliberate breakages, all caught.

## 7. Benchmark — 2026-10-21 (version 1.0.0 against no skill)
Pre-registered before any skill run: the primary metric is price-weighted tokens from
`token_audit.py` (cache read 0.1, cache write 1.25, output 5, input 1). The quality rule is
non-inferiority: the skill arm must pass every assertion the no-skill arm passes on the same case.
Success means at least 10% lower mean weighted tokens across the 17 matched runs. The runs covered
eleven sandboxed tasks: five blocked-route tasks (render a diagram, fetch a dataset, read a model
card, vendor a file from a refused CDN, run a CLI that asks for a token), four builds and three
reviews with planted defects, one or two runs per arm. A twelfth task, auditing an expensive run's
transcript, was added for the skill's own audit job. Outputs were checked by script and replies
graded blind, with skill and no-skill replies mixed in each packet.

| Arm | Runs | Weighted | Processed | Turns | Time | Scripted checks | Blind-graded |
|---|---|---|---|---|---|---|---|
| No skill | 17 | 102k | 474k | 7.8 | 75 s | 62/62 | 66/68 |
| Puppet Master | 17 | 80k (−21%) | 297k (−37%) | 4.8 | 60 s | 62/62 | 65/68 |
| No skill, audit task | 2 | 330k | 1.71M | 17.5 | 480 s | — | 8/10 |
| Puppet Master, audit task | 2 | 159k (−52%) | 0.44M | 6.0 | 343 s | — | 10/10 |

The largest savings came where the unaided run probed or checked one call per turn: vendoring a file
from a refused CDN (−57%), the two KPI-pack tasks (−29% and −27%), a review (−23%). Two tasks cost
about the same in both arms (+3%, +2%), because the unaided run was already lean there. One
blind-graded assertion separated the arms. In one of the two skill runs on the token task, the
reply dropped its citation of the source file while shortening. Step 6 became "write short, and
keep the proof", with a matching quality rail. Two re-runs with the revised skill both cited the
code and cost 63k and 64k weighted, against 70k without the skill. One assertion (offering the user
a confirming command on the CDN task) failed in every arm, with and without the skill.

On the audit task, both unaided runs missed one pre-registered assertion: they named the unused
start-up context, not the turn count, as the main driver. That reading is defensible, because they
estimated that tool definitions the run never called made up most of a 50k start-up re-sent on
every turn. So the skill's 10/10 against 8/10 is a difference in emphasis, not a defect in the
unaided runs. Their finding led to the audit script's start-up signal and to step 5's note on
tool-limited agent types. Their extra digging cost about twice as many tokens.
