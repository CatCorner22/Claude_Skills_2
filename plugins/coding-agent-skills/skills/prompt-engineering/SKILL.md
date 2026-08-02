---
name: prompt-engineering
description: >-
  Writes effective, provider-agnostic prompts and instructions for LLM agents — stating the task
  and success criteria, giving the right context and only that, few-shot examples, an explicit
  output format, decomposing complex asks, and iterating against real test cases. Use when crafting
  a prompt, instruction, or system message, or debugging a flaky prompt that gives inconsistent or
  wrong results. Triggers: prompt, prompt engineering, system prompt, instructions, few-shot,
  output format, prompt not working, improve a prompt.
---

# Prompt engineering

## When to use
- Writing a prompt, instruction, or system message for any LLM or agent.
- Debugging a prompt that's flaky — inconsistent, wrong format, ignores instructions.
- Turning a vague ask into a specific, testable instruction.
- Not for: orchestrating a multi-step or autonomous workflow → see
  `coding-agent-skills:agentic-workflow-design`; packaging instructions as a reusable Claude Code
  skill with frontmatter → see `coding-agent-skills:writing-agent-skills`.

## Do it
1. **State the task and what "good" means.** Open with the specific job and the success criteria the
   output must meet. "Summarize this contract in 5 bullets, each naming a party and an obligation, no
   legal advice" beats "summarize this." If you can't name the criteria, you can't tell whether the
   prompt worked.
2. **Give the right context — and only that.** Include the inputs, definitions, constraints, and
   background the model needs; leave out the rest. Put reference material (documents, data) clearly
   delimited and separate from your instructions, and tell the model what to do with it. Too little
   context and it guesses; too much and the instruction drowns.
3. **Show, don't just tell: add a few examples.** For anything with a specific style, format, or edge
   behavior, include 2–5 input→output examples (few-shot). Make them cover the tricky cases (an empty
   value, an ambiguous input) — the model imitates the pattern in your examples more reliably than it
   follows an abstract description.
4. **Specify the output format explicitly.** Say exactly what to return: the structure (JSON schema,
   fields, a table), what to do when a value is missing, and whether to include anything besides the
   result. If you need machine-readable output, say "return only valid JSON matching this shape, no
   prose," and show the shape. Unspecified format is the most common cause of "it added a chatty
   preamble."
5. **Decompose a complex ask.** If the task has several parts, either number the steps in the prompt
   ("First… then… finally…") or ask for reasoning before the answer for genuinely hard reasoning tasks.
   A prompt that bundles five loosely-related requests fails on the hardest one — split it, and if the
   parts are truly separate, consider separate prompts or a workflow.
6. **Iterate against real cases, not one lucky example.** Collect a handful of representative real
   inputs *including the ones that currently fail*. Change one thing at a time, run the whole set, and
   keep the version that does best across all of them — not the one that fixed your favorite example
   while quietly breaking two others. Write down what each change was for.
7. **Diagnose failures by cause.** Wrong format → tighten the format spec and add an example of it.
   Ignores an instruction → move it up, make it explicit, or show it in an example. Inconsistent across
   runs → add structure/examples and reduce ambiguity (and lower randomness/temperature if you control
   it). Hallucinated facts → supply the source material and instruct "use only the provided context;
   if it's not there, say so." More failure modes are in `references/prompt-patterns.md`.

## Why / learn
Two ideas carry almost all of prompt quality. First, **specificity and structure drive quality**: a
model can only satisfy criteria it can infer, so every ambiguity you leave — undefined terms, an
unstated format, a missing edge case — is a decision you've handed to a coin flip. Naming the task,
the audience, the constraints, and the exact output shape removes those coin flips. Structure (numbered
steps, delimited context, an example of the target format) does the same by making the pattern
concrete instead of abstract; examples work because imitation is more reliable than instruction-
following for anything stylistic. Second, **prompts should be tested like code, not tuned by vibes.**
It is dangerously easy to "improve" a prompt against the single example in front of you and ship a
regression on the cases you didn't look at. A tiny eval set — a few real inputs with known-good
outputs, especially the failing ones — turns prompt work from guesswork into measurement: change one
thing, run the set, compare. That discipline, more than any clever phrasing, is what separates a
prompt that works in the demo from one that works in production. These principles are provider-
agnostic; specific models expose extra knobs (system messages, temperature, structured-output modes),
but the task-context-examples-format-iterate loop is the same everywhere.

## Common mistakes
- Vague task ("summarize this") → generic output. State the job, audience, and success criteria.
- No output format → chatty preambles and unparseable results. Specify the exact structure; show it.
- Describing a style instead of showing it → inconsistent results. Add 2–5 few-shot examples of edge cases.
- Dumping everything as context → the instruction gets buried. Include only what's needed; delimit sources.
- One giant prompt for five tasks → it fails the hardest part. Decompose or split into separate prompts.
- Tuning on a single example → silent regressions elsewhere. Keep a small real eval set; change one thing at a time.
- Hallucinations from missing grounding → "use only the provided context; if absent, say you don't know."

## Tailor to your environment
Record your real specifics in `references/your-environment.md`: the model/runtime and any provider
features you use (system prompt, temperature, structured output), the recurring task types you prompt
for, your house output formats, and where your eval cases live. **Never commit sensitive prompt
content or real customer data** — keep proprietary prompts and real examples in
`references/your-environment.private.md`, which `.gitignore` keeps out of git. This skill then adapts
its generic method to your models and tasks.

## References
- references/prompt-patterns.md — reusable prompt structures, failure modes, and before/after fixes
- references/your-environment.md — your model/runtime, house formats, and eval cases (fill in)
