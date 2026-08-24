# Agent workflow patterns (and when to use each)

These are the building blocks. Most real systems are a small composition of them. The rule of thumb:
use the **simplest** pattern that meets the accuracy bar, and add complexity only when an eval shows
you need it. These are provider-agnostic — they apply to any LLM or agent runtime.

## Contents
- Prompt chaining
- Routing
- Parallelization
- Orchestrator–worker
- Evaluator–optimizer (self-correction)
- Autonomous agent (open loop)
- Choosing between them

## Prompt chaining
A fixed sequence: output of step 1 feeds step 2, and so on, with a check between steps.
- **Use when:** the task splits into predictable, ordered subtasks (extract → transform → summarize).
- **Why it helps:** each step is smaller and independently verifiable; you can gate on a bad step.
- **Watch for:** compounding errors — validate between links so a bad output doesn't propagate.

## Routing
A classifier step decides which of several downstream paths handles the input.
- **Use when:** inputs fall into distinct categories that need different handling (billing vs. tech
  support; simple query → cheap model, hard query → strong model).
- **Why it helps:** each path can be specialized and simpler than one path trying to do everything.
- **Watch for:** misclassification at the router — measure and verify the routing decision itself.

## Parallelization
Fan a task out into independent subtasks, run them concurrently, then aggregate.
- **Sectioning:** split into independent pieces (analyze 10 files at once), then merge.
- **Voting:** run the same task several times and take a consensus for higher confidence.
- **Use when:** subtasks don't depend on each other, or you want redundancy for reliability.
- **Watch for:** the aggregation step — how conflicting sub-results are reconciled is where bugs hide.

## Orchestrator–worker
An orchestrator LLM decomposes the task *at runtime* into a dynamic number of subtasks and delegates
each to a worker, then synthesizes the results.
- **Use when:** you can't predict how many subtasks or what they are until you see the input (e.g.
  "make the needed changes across however many files this touches").
- **Why it helps:** handles variable structure a fixed chain can't.
- **Watch for:** cost and loops — bound the number of workers and verify the synthesis.

## Evaluator–optimizer (self-correction)
One step produces a result; an evaluator step critiques it against criteria; the producer revises. Loop
until the evaluator passes or a max-iteration cap is hit.
- **Use when:** there are clear quality criteria and revision measurably improves the output (drafting,
  translation, code that must pass tests).
- **Why it helps:** turns a fuzzy "make it good" into an explicit check-and-improve loop.
- **Watch for:** infinite polishing — cap iterations; make sure the evaluator's criteria are real.

## Autonomous agent (open loop)
The model plans, calls tools, observes results, and decides the next action in a loop until it judges
the task done — no fixed script.
- **Use when:** the path genuinely can't be pre-planned and the environment gives reliable feedback the
  agent can act on.
- **Why it helps:** maximum flexibility for open-ended tasks.
- **Watch for:** everything — this is the least predictable pattern. Require a step/cost budget, a
  human approval gate before irreversible actions, and strong per-step verification.

## Choosing between them
- Steps fixed and inputs predictable → **script** (no agent) or a simple **chain**.
- Distinct input categories → **routing**.
- Independent subtasks or want redundancy → **parallelization**.
- Structure only known at runtime → **orchestrator–worker**.
- Clear quality bar + revision helps → **evaluator–optimizer**.
- Truly open-ended with good feedback → **autonomous agent**, heavily guardrailed.
Prefer composing simple patterns over one clever complex one; each added degree of autonomy is another
thing your eval set must cover.
