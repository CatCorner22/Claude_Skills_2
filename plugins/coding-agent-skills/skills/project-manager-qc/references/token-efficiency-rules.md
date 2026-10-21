# Token efficiency — the cost model and the rules

Tokens are spent where text enters a context and stays there. That single fact explains almost
every rule below: reading less, returning less and re-deriving less save far more than writing
shorter sentences. Figures here are orders of magnitude for planning, marked as such; measure
your own with the ledger.

## Contents
- [The cost model](#the-cost-model)
- [The rules](#the-rules)
- [Anti-patterns](#anti-patterns)
- [Estimating a task's budget](#estimating-a-tasks-budget)

## The cost model

- **Input dominates.** Everything in the context — the system prompt, every earlier turn, every
  tool result — is input again on the next model call. A 10,000-token file read early is paid for on
  every later turn of that context, not once. Prompt caching softens the price of a stable prefix
  but not the attention and room it takes [background — verify against current pricing docs].
- **Tool results are the biggest lever.** A full file, a full log, a full directory listing or a
  full web page is usually far more than the answer needed from it.
- **A subagent is a second context.** It starts by loading its own instructions and environment,
  so it costs tens of thousands of tokens before it does useful work, and a substantial subagent
  run commonly lands in the tens to hundreds of thousands [background — verify with your own
  ledger]. In return, only its final answer enters the caller's context. It pays off when it reads
  a lot and returns a little.
- **Repeated work is the purest waste.** Reading the same file twice, re-deriving a fact already
  established, re-running a search, or two agents researching the same thing.

## The rules

| # | Rule | Why | Example |
|---|---|---|---|
| 1 | Measure before reading | Size decides the reading strategy | `token_ledger.py estimate src/ --max 20000`, then read slices of anything flagged |
| 2 | Grep, then read a slice | One fact rarely needs the whole file | `grep -n "def parse" -r src/` → `sed -n 120,180p src/parse.py` |
| 3 | Read once | Every re-read is pure repeat cost | keep notes of what a file says; edit by exact replacement |
| 4 | Batch independent calls | Fewer round trips, less repeated context | three reads in one turn, not three turns |
| 5 | Bound every output | Logs and listings balloon | `| tail -20`, `--quiet`, `wc -l` instead of the listing |
| 6 | Delegate wide reads only | A subagent's fixed cost must buy something | a 40-file survey → subagent; a 2-file check → inline |
| 7 | Brief with paths, not pastes | Pasted content is paid twice, in your context and theirs | "read `docs/api.md` §3 and answer X in 10 lines" |
| 8 | Ask for compact returns | The return lands in your context | a schema, a table, a line limit |
| 9 | Right-size the fleet | Shared budgets (searches, rate limits) run out across parallel agents | three researchers with sharp briefs beat six vague ones |
| 10 | Script what repeats | Code is written once and run many times | the third manual repetition triggers a script |
| 11 | Write durable facts down | Re-deriving costs the same each time | the plan, the ledger, a memory entry, a tailoring file |
| 12 | Don't poll | Each check re-reads state | notifications; one scheduled check-in for what cannot notify |
| 13 | Stop at the acceptance criteria | Gold-plating is spend with no buyer | an unasked-for feature goes to the FUTURE bin |
| 14 | Match effort to the stage | Mechanical stages need little reasoning | low effort for format conversions; high for judgement and verification |
| 15 | Keep the final message short | It is the one thing the user must read | the outcome, the evidence, what is left — no recap of every step |

## Anti-patterns

- **The paste-brief.** A subagent prompt containing whole files "for context". Give the paths.
- **The echo.** Re-printing a tool result in prose so the user can see it. Summarise in one line.
- **The scatter-read.** Opening ten files to find which one matters. Grep first.
- **The swarm.** Six parallel agents for a question three could answer, each re-reading the same
  sources and exhausting a shared search budget.
- **The narrated loop.** Running the same check every few minutes "to see if it finished".
- **The rewrite.** Rewriting a whole file to change three lines. Replace the lines.
- **The re-verify.** Re-reading a file just edited to confirm the edit; the edit tool already
  reports failure.
- **The over-manager.** A plan, a checkpoint and a gate on a three-step task.

## Estimating a task's budget

Use rough sizes, then correct them with the ledger as the work proceeds:
- **S (under ~20k tokens):** a few reads and edits in one context.
- **M (~20k–100k):** a feature or a report built inline, or one focused subagent.
- **L (over ~100k):** several subagents, research fan-outs, or long iterative runs.

Sum the tasks, add a reserve for the quality gate and one round of fixes, and write the stop
rule: which deliverable or polish step is cut first if the budget runs short. These bands are
house planning conventions, not measured constants; replace them with your own medians once the
ledger has a few tasks in it.
