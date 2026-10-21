---
name: puppet-master
description: >-
  Does the whole job on the fewest tokens with no loss of quality or coverage. Fixes the quality
  bar first — every requirement, check, source and proof the result needs — then cuts only the
  path: fewer turns (independent calls in one turn, dependent steps chained in one command),
  less new context per turn (the cheapest decisive look, bounded output, slices not whole files,
  no re-reads, no references opened just in case), subagents only when they repay their start-up
  context, and short replies. Audits a finished run with a transcript analyser that ranks where
  the tokens went. Use at the start of any multi-step task, when a run or session is expensive or
  the context is filling up, or to review an agent workflow, prompt, skill or subagent brief for
  waste. Triggers: puppet master, save tokens, reduce token usage, token efficiency, cut token
  cost, cheaper run, context is filling up, why was this so expensive, audit token use.
metadata:
  version: "1.0.0"
---

# Puppet Master

A puppet master moves every figure on the stage with small, exact movements: nothing wasted,
nothing dropped. This skill holds the result to its full bar and makes every token move it.

**Where tokens actually go.** Every model call re-sends the whole context, so a run costs roughly
*turns × context*. Cached context is cheap per token (about a tenth of plain input) but it is
re-read on every turn; new content is written once at a premium and then re-read on every later
turn; output costs several times input. A subagent starts by loading its own full system context
before it does anything. In this library's benchmark, unaided runs averaged 7.8 turns and about
470k tokens processed, while the tool results they read came to about 3k. Re-sending the context
was the cost, not the reading. The levers, by yield: fewer turns, less new content per turn,
fewer subagents, shorter output.

## When to use
- At the start of any task with more than a couple of tool calls. The habits cost nothing and
  compound across a session.
- A run, a session or a subagent fleet was expensive, or the context is filling up, and the
  question is where the tokens went and how to cut them without cutting the result.
- Reviewing a workflow, a prompt, a skill or a subagent brief for token waste.
- **In tandem.** `coding-agent-skills:project-manager-qc` plans and gates multi-session or
  multi-agent work and uses this skill as its token discipline;
  `coding-agent-skills:creative-workaround-genius` applies the same economy to a blocked route.
- Not for: planning and quality-gating multi-session or multi-agent work →
  `coding-agent-skills:project-manager-qc`; making a working design simpler →
  `coding-agent-skills:soviet-space-graphite`; writing or tuning a prompt's wording →
  `coding-agent-skills:prompt-engineering`.

## Do it

1. **Fix the quality bar before cutting anything.** Name what the result must contain and prove:
   each requirement, each check you would run, each source the answer depends on, and the depth
   the user asked for ("thorough", "every", "full report" set a floor). Savings come only from
   the path to that bar. Keep the list in your head for a small task; write it for a large one.

2. **Plan turns, not just steps.** Before the first call, group the work. Everything independent
   goes in one turn as parallel calls: reads, searches, probes, checks. Dependent shell steps go
   in one command, chained with `&&`, every output bounded. Most "look, then look again"
   sequences are one turn of several looks.

3. **Take the cheapest decisive look.** Ask what small observation settles the next decision:
   `wc -c` before reading, `grep -n` then a slice, `head`, a count, a hash, one probe instead of a
   sweep, a one-line filter that pulls only the JSON fields you need. Read a file whole when you
   need all of it — a spec, a short script — because one full read is cheaper than three slices.
   Never `cat` a large file, list a tree recursively, or dump a whole log.

4. **Keep new context small and unrepeated.**
   - Bound every output (`| head -n 40`, `tail` of logs, quiet flags, counts instead of listings).
   - Read once and remember it; edit by exact replacement; never re-read a file you just edited.
   - Open a reference or a doc section only when this task needs it, not to be thorough.
   - Write a script once with its checks inside, so one run builds and verifies, instead of
     write–run–fix–rerun.

5. **Delegate only when it pays.** A subagent costs its start-up context plus its own turns, so
   inline any work that would add less than that to your context. Delegate a wide read whose
   conclusion is small, genuinely parallel independent streams, or work that needs a fresh view.
   Brief with paths and the exact question, never pasted contents; ask for a compact, structured
   return (a table, JSON, a line limit); give mechanical work the smallest capable model when you
   can choose one. Most of a subagent's start-up context is tool definitions, skill listings and
   connector instructions, so for repeated runs of one kind of job, an agent type limited to the
   tools that job needs starts much smaller.

6. **Write short, and keep the proof.** Lead with the result, then what is left. Every claim the
   user will act on keeps its evidence: the file and function that show it, or the command and
   what it printed. Cut narration, restated requests and echoed output the user can open, never
   the proof. Output costs several times input and sits in the context of everything after it.

7. **Audit a run, then fix the habit.** For an expensive run, or to review someone's workflow,
   analyse its transcript (Claude Code keeps them under `~/.claude/projects/<project>/`):
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/puppet-master/scripts/token_audit.py" <transcript.jsonl>
   ```
   It reports turns, final context, processed and price-weighted tokens, the largest tool
   results with the call that made each, and waste signals: a start-up context that dominates
   because it is re-sent every turn, repeated reads, unbounded commands, single-call turns that
   could have been batched, subagent spawns. Pair every saving you
   propose with the check that keeps the quality bar intact. Arithmetic, lever table and batching
   patterns: `references/token-economics.md`.

### Quality rails
- A saving that drops a check, skips a source the answer depends on, narrows coverage the user
  asked for, or shortens a deliverable they wanted in full is a defect, not a saving.
- When unsure whether a slice is enough, read more. A second look costs more than a sufficient
  first one.
- Batch only calls that are truly independent; never guess an input to save a turn.
- Never hide work to look cheap: the reply says what was checked and cites what proves each
  claim. "Short" means no narration, not no evidence.

## Why / learn

**Why turns dominate.** The model has no memory between calls; the harness re-sends the context
each time. So the seventh turn of a run pays again for everything read in the first six, and a
run that takes eight single-call turns where three batched turns would do pays for the context
five extra times. In the benchmark behind this skill, 16 of 17 unaided runs made mostly
single-call turns, and tool results were about 3k of a 66k final context: the cheap saving was in
the turn count, not in the reading.

**Why the bar comes first.** Cutting tokens is easy if quality may fall: read less, check less,
write less. The discipline is to cut only the path. The written bar is also what tells you a
slice was enough — without it, "efficient" quietly turns into "incomplete".

**Why delegation is a cost decision.** A subagent buys a clean context and parallel time, and it
pays for them with its own start-up context and turns. That trade is excellent for a fifty-file
survey that returns one table and poor for a two-file check. The economics, not the habit, decide.

## Common mistakes
- One tool call per turn when three were independent → batch them.
- Probing every mirror after the first policy refusal → one decisive check per channel, then stop.
- `cat` on a long file to find one function → grep, then read the slice.
- Re-reading a file after editing it → the edit tool already reports failure.
- Opening every reference "to be thorough" → open what this task needs.
- A subagent for a two-file read, or a brief that pastes files → inline it; brief with paths.
- Shrinking the deliverable to save tokens → the bar is fixed; cut the path.
- A closing recap of every step → outcome, evidence, what is left.

## Tailor to your environment
Record in `references/your-environment.md`: your measured start-up context per session and per
subagent, your price ratios, the output-bounding idioms of your stack, where your transcripts
live, and the audit findings that keep recurring.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/puppet-master.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/token-economics.md — the cost model with worked arithmetic, the lever table with
  what each saves and what keeps quality safe, what can share a turn, output-bounding idioms,
  the delegation break-even, and the audit procedure with a worked example.
- references/your-environment.md — your start-up costs, price ratios, idioms and recurring
  findings (fill in; the `.private.md` twin is git-ignored).

## Scripts
- `scripts/token_audit.py` — reads a Claude Code transcript (JSON lines) and reports turns, start-up
  and final context, processed tokens, price-weighted tokens, the largest tool results with their
  calls, and waste signals; never prints tool-result contents. `--top N`, `--json`, `--self-test` for the
  offline checks; exit 2 on an unreadable or empty transcript, 5 on bad usage.
