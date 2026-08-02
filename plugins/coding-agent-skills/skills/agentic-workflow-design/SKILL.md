---
name: agentic-workflow-design
description: >-
  Designs reliable autonomous and multi-step agent workflows — deciding agent vs deterministic
  script, decomposing a task into steps and subtasks, defining tools and their contracts, adding
  verification, guardrails, and checkpoints, handling failure and human-in-the-loop review, and
  evaluating the workflow against real cases. Use when building an agent, an automation pipeline,
  or a multi-step LLM workflow. Triggers: agent, autonomous agent, agentic workflow, tool use,
  orchestration, multi-step, pipeline, human in the loop, guardrails.
---

# Agentic workflow design

## When to use
- Building an autonomous or semi-autonomous agent, or a multi-step LLM pipeline.
- Deciding whether a task even needs an agent, or a plain script would be more reliable.
- Adding verification, guardrails, checkpoints, or human review to an existing flow that's flaky.
- Not for: wording a single prompt or system message → see `coding-agent-skills:prompt-engineering`;
  packaging repeatable instructions as a Claude Code skill → see `coding-agent-skills:writing-agent-skills`.

## Do it
1. **Decide agent vs. deterministic script first.** If the steps are fixed and the inputs are
   predictable, write a script — it's cheaper, faster, and testable. Reach for an agent only when the
   task genuinely needs *open-ended decisions*: unpredictable branching, judgment over messy input, or
   tool selection that can't be hard-coded. Many "agent" problems are a script with one LLM call inside.
2. **Decompose the task into small, checkable steps.** Break the goal into subtasks where each has a
   clear input and a verifiable output. Prefer the simplest structure that works: a fixed **chain** of
   steps; a **router** that classifies then dispatches; **parallel** subtasks fanned out and merged; an
   **orchestrator** that spins up workers for a dynamic number of subtasks. Patterns and when to use
   each are in `references/workflow-patterns.md`. Small steps are what make failures isolatable.
3. **Define each tool as a contract.** For every action the agent can take, specify: name, purpose,
   typed inputs, output shape, side effects, and failure behavior. Make tools **narrow and hard to
   misuse** — validate arguments, make read-only tools obviously read-only, and make destructive tools
   require explicit confirmation or a dry-run mode. A vague tool ("do the thing") is where agents go
   off the rails.
4. **Add verification at every step that can be wrong.** Don't trust a step's output because it looks
   plausible — check it. Use cheap deterministic checks where possible (schema/type validation, row
   counts, totals reconcile, a value is in range) and an LLM-as-judge only where the criterion is
   genuinely fuzzy. A step should *fail loudly* on a bad output rather than pass it downstream.
5. **Put in guardrails and checkpoints.** Bound the loop (max steps/iterations, max tool calls, max
   spend/time) so a confused agent can't run forever. Save state at checkpoints so a failure resumes
   instead of restarting. Constrain side effects: least-privilege tool access, and a human approval
   gate before anything irreversible (sending money, emailing customers, deleting data).
6. **Design the failure and human-in-the-loop paths on purpose.** Decide, per step, what happens on
   error: retry with backoff, fall back to a simpler path, or escalate to a human. Route low-confidence
   or high-stakes decisions to a person, and give them the context to decide quickly. "Ask a human" is
   a feature, not a failure.
7. **Evaluate the whole workflow like software.** Assemble a set of real, representative cases with
   known-good outcomes. Run the workflow end-to-end against them, measure task success (not vibes),
   inspect the failures, and fix the specific step that broke. Re-run the suite after every change so
   you catch regressions. Build the eval set before you tune.

## Why / learn
The core lesson: **reliability comes from decomposition and verification, not from a bigger prompt.**
A single mega-prompt asking a model to "do the whole thing" fails opaquely — when the output is wrong
you can't tell *which* part broke, and every fix is a guess. Treat the agent instead like a **process
you can test**: a chain of small steps, each with a defined input, a defined output, and a check that
the output is actually right. Now a failure localizes to one step, verification catches the error
before it compounds, and you can improve that step in isolation. This is also why the agent-vs-script
decision comes first — determinism is a feature, and every step you can make a plain function instead
of an LLM call is a step that can't hallucinate. Guardrails exist because an autonomous loop amplifies
mistakes: without a step limit or an approval gate, one wrong turn becomes fifty tool calls or an
irreversible action. And human-in-the-loop isn't a crutch — routing the genuinely ambiguous or
high-stakes decisions to a person is what lets you deploy the automatable 90% safely. Start with the
simplest thing that could work (often a script), add agency only where the task demands it, and let
your eval suite — not intuition — tell you whether a change made the system better.

## Common mistakes
- Using an agent where a deterministic script would do → needless cost, latency, and failure modes. Script first.
- One giant prompt for a multi-step task → opaque failures. Decompose into checkable steps.
- Trusting a step because its output *looks* right → errors compound silently. Verify each step.
- Broad, ambiguous, or over-powerful tools → the agent misuses them. Narrow contracts, least privilege, dry-runs.
- No loop bound or budget → a confused agent runs forever or overspends. Cap steps/tools/time/cost.
- Full autonomy on irreversible actions → an approval gate before anything you can't undo.
- Tuning on vibes with no eval set → you can't tell if a change helped. Build real test cases first.

## Tailor to your environment
Record your real setup in `references/your-environment.md`: the task you're automating, the tools/APIs
the agent may call and their permissions, where human approval is required, your latency/cost budget,
and where the workflow runs. **Never commit secrets or customer data** — keep API keys, endpoints,
and real case data in `references/your-environment.private.md`, which `.gitignore` keeps out of git.
This skill then shapes its generic pattern around your constraints.

## References
- references/workflow-patterns.md — chain, router, parallel, orchestrator-worker, evaluator-optimizer, and when to use each
- references/your-environment.md — your task, tools, approval gates, and budgets (fill in)
