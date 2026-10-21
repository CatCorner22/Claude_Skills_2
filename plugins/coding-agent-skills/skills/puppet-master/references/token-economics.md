# Token economics — the cost model, the levers, and the audit

Figures marked *measured* come from this library's 2026-10-21 benchmark: 74 subagent runs on
eleven sandboxed tasks, audited with `scripts/token_audit.py`. Price ratios are typical published
ratios at the time of writing [background — verify against your provider's current pricing].
Replace both with your own numbers in `your-environment.md`.

## Contents
- [The cost model](#the-cost-model)
- [A worked comparison](#a-worked-comparison)
- [The levers](#the-levers)
- [What can share a turn](#what-can-share-a-turn)
- [Bounding idioms](#bounding-idioms)
- [Delegation break-even](#delegation-break-even)
- [The audit procedure](#the-audit-procedure)

## The cost model

Each model call (a *turn*) sends the whole context: system prompt, tool definitions, every
earlier message and every earlier tool result. A harness with prompt caching splits that into:

| Part | What it is | Price ratio vs plain input |
|---|---|---|
| cache read | the unchanged prefix, re-read on this turn | ≈ 0.1 |
| cache write | content new since the last turn, stored for later turns | ≈ 1.25 |
| input | uncached remainder (usually tiny) | 1 |
| output | what the model writes, including tool calls | ≈ 5 |

So for a run of *T* turns whose context grows from *C₀* to *C*, processed tokens are roughly
*T × (C₀ + C)/2*, and the price-weighted cost is about *0.1 × processed + 1.25 × (C − C₀) +
5 × output*. Three consequences:

1. **Turns multiply everything.** Each extra turn re-reads the whole context.
2. **New content is paid twice:** once to write it, then on every later read.
3. **Start-up context is a floor.** *Measured:* a subagent here began at about 50k tokens before
   its first action; an unaided run's final context averaged 66k, of which tool results were
   about 3k.

## A worked comparison

The same task (vendor a byte-exact file from a refused CDN), same model, same final context:

| Run | Turns | Tool calls | Final context | Processed | Weighted |
|---|---|---|---|---|---|
| unaided | 18 | 18 | 69.9k | 1.12M | 158k |
| with the workaround skill's fast path | 8 | 9 | 69.9k | 0.52M | 93k |

*Measured.* The skill-guided run read a 4.6k-token skill file and still cost 41% less, because it
made its checks in 8 turns instead of 18: the unaided run probed one mirror per turn. The
reading was never the cost; the turn count was.

## The levers

| Lever | Typical saving | What keeps quality safe |
|---|---|---|
| Batch independent calls into one turn | one full context re-read per call saved | only calls whose inputs are already known |
| Chain dependent shell steps in one command | one turn per step folded in | `set -e` or `&&`, bounded output, check the exit status |
| Cheapest decisive look (`wc`, `grep -n`, slice, hash, one probe) | the size of everything not read | read whole when the answer needs the whole |
| Bound every output | the unbounded tail, paid on every later turn | bounds that keep the line you need; `tail` for errors |
| Read once, edit by replacement, no re-read after edit | a file's size per avoided read | the edit tool reports failure |
| Open references only when needed | a reference's size × remaining turns | the bar says which sources are required |
| Build and verify in one script run | the fix–rerun loop turns | checks inside the script, printed results |
| Inline small work instead of a subagent | a subagent's start-up context and turns | delegate when independence or a wide read is the point |
| Compact subagent briefs and returns | the pasted content, twice; a long return | paths, the exact question, a schema or line limit |
| Short final message | output at ≈ 5× | outcome, evidence, open items always present |

## What can share a turn

**Yes — independent:** reading several known files; several searches; probing several hosts once
each; running the test suite and the linter; `git status` with `git log`; checking a file's size
and its first lines in one command.

**No — dependent:** reading a file to learn a path you then open; a search whose result picks the
next file; running a fix before the test that checks it; anything whose input you would have to
guess. Guessing to save a turn is a quality defect; do the extra turn.

**Chaining in one command:** `cd dir && run && check | tail -20`. Stop on the first failure, keep
only the output you will use, and print a one-line status for each step so the result is still
evidence.

## Bounding idioms

| Need | Instead of | Use |
|---|---|---|
| size of a file | `cat file` | `wc -c file; wc -l file` |
| find a definition | reading the module | `grep -n "def name" -r src/ \| head` then `sed -n 120,170p file` |
| shape of a CSV | `cat data.csv` | `head -5 data.csv; wc -l data.csv` |
| fields of a JSON response | the whole body | `jq '.dist.integrity'` or a one-line `python3 -c` |
| errors in a log | the whole log | `grep -n -i error log \| tail -20` |
| what is in a tree | `ls -R` / `find /` | `find dir -maxdepth 2 -type f \| head -50` |
| whether something changed | re-reading it | a checksum before and after |

## Delegation break-even

A subagent pays its start-up context (*measured* about 50k here) on its first call and re-reads
its growing context on each of its turns; you then read its return. Inline the work when what it
would add to *your* context, times your remaining turns, is less than that. In practice:

- **Delegate:** a survey across many files or pages that ends in a short table; independent
  parallel streams that would otherwise run in sequence; a review that must not share your
  assumptions.
- **Inline:** reading two files; one command's output; a check you can script in a line.
- **Brief:** paths, the exact question, the bar the answer must meet, and the return shape.
  Never paste contents: they are paid in your context and again in theirs.
- **Shrink the start-up for repeated jobs.** An audit of one measured run put most of its 50k
  start-up in material the job never used: definitions for tools it never called, a skill
  listing, connector instructions. Those figures are an estimate from one transcript; measure
  your own. For a job you delegate repeatedly, an agent definition whose `tools:` line names only
  what the job needs avoids re-sending the rest on every turn. Check the next transcript's first
  turn to confirm the start-up actually fell, and give every arm the same agent type when you
  compare runs.

## The audit procedure

1. Run `token_audit.py` on the transcript. Note turns, weighted tokens, and the top results.
2. **Turns first.** Count single-call turns. For each run of single-call turns, ask which calls
   were independent. Those are the batching saving.
3. **Then the start-up.** When the audit says the start-up context is most of what each turn
   re-sends, list what it carries that the run never used: tool definitions, a skill listing,
   connector instructions. The transcript does not record the tool definitions themselves, so
   estimate from the definitions you can see and say it is an estimate.
4. **Then new content.** For each large result, ask what the smallest decisive look would have
   been. For repeated reads, what should have been remembered. For unbounded commands, the bound.
5. **Then subagents.** Did each repay its start-up context? What should its brief and its return
   have been?
6. **Then output.** Long narration, echoed tool output, restated requests.
7. **Write the fix as a habit, with its quality check:** "batch the three probes; each still
   reports its status", not just "use fewer tokens".
