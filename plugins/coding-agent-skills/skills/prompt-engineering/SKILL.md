---
name: prompt-engineering
description: >-
  Writes and debugs prompts, instructions, and system messages for LLM agents — task and success
  criteria, the right context and only that, an output contract enforced by provider-native
  structured output rather than by wording, example strategy (few-shot, many-shot, ordering
  effects), what changes on reasoning and extended-thinking models, an honest prompt-injection
  rail, cache-aware ordering, and iteration against an eval set with repeat runs. Delivers a
  package: copyable prompt, design notes, input assumptions, eval cases. Use when crafting a
  prompt, instruction, or system message, making model output
  machine-readable, or debugging a flaky prompt that gives inconsistent or wrong results.
  Triggers: prompt, prompt engineering, system prompt, instructions, few-shot, many-shot, output
  format, structured output, JSON output, prompt injection, reasoning model, extended thinking,
  prompt caching, flaky prompt, prompt not working, improve a prompt.
metadata:
  version: "2.0.0"
---

# Prompt engineering

## When to use
- Writing a prompt, instruction, or system message for any LLM or agent.
- Making output machine-readable, or making an existing prompt's output parse reliably.
- Debugging a flaky prompt — inconsistent between runs, wrong format, ignores an instruction.
- Turning a vague ask into a specific, testable instruction.
- Not for: orchestrating a multi-step or autonomous workflow, tool contracts, and the guardrails
  that gate consequential actions → see `coding-agent-skills:agentic-workflow-design`; packaging
  instructions as a reusable skill with frontmatter → see
  `coding-agent-skills:writing-agent-skills`; optimizing several prompt factors at once and reading
  their interactions → see `continuous-improvement-skills:design-of-experiments`; qualifying a
  model that grades other outputs before its scores pick your prompt → see
  `continuous-improvement-skills:measurement-systems-analysis`.

## Do it

**Read the provider's own API reference before asserting anything about model capability** —
structured output, thinking configuration, caching, sampling knobs. This is the part of prompt
craft with the shortest shelf life: mechanisms differ by provider *and* by model generation, and
recalled ones are frequently a generation out of date. In Claude Code, the bundled `claude-api`
skill is that reference for Anthropic models; every mechanism named below was checked against it.

1. **State the task and what "good" means — at normal volume.** Open with the specific job and the
   success criteria the output must meet. "Summarize this contract in 5 bullets, each naming a party
   and an obligation, no legal advice" beats "summarize this." If you can't name the criteria, you
   can't tell whether the prompt worked. Say it plainly: forcefulness was a workaround for models
   that underweighted instructions, and on models that follow instructions closely it over-applies
   — stacked `CRITICAL`/`MUST`/`NEVER` markers stop carrying information, and the prompt's anxious
   register becomes the output's. Hedges get read literally too, so "try to include a summary if
   possible" is a bug when the summary is required.
2. **Give the right context — and only that.** Include the inputs, definitions, constraints, and
   background the model needs; leave out the rest. Keep instructions and reference material visibly
   separate: the data in its own delimited block (fences, tags, headers) with a sentence saying what
   to do with it. Too little context and the model guesses; too much and the instruction competes
   with noise. **Order by input length, not by habit.** With a short input, instructions-first reads
   naturally. With a long document or a large retrieved set, put the material first and the
   instruction or question *last*, after it — the failure this fixes (a dropped instruction) is a
   long-input failure, and late placement puts the instruction next to the answer. The same
   ordering is what prompt caching requires anyway: the cache is a prefix match, so static content
   (documents, examples, standing instructions) must sit ahead of the varying question or nothing is
   ever reused. Placement details are in `references/prompt-patterns.md`.
3. **Make the output contract a constraint, not a request.** If the output must be machine-readable,
   reach for the provider's schema-constrained output *before* writing any format instruction. On
   the Claude API that is structured outputs: `output_config.format` with a JSON schema — the SDK's
   `messages.parse()` validates the response against your schema — or, when the result should arrive
   as a tool call, a tool whose `input_schema` *is* the contract, with `strict: true` and
   `tool_choice: {"type": "tool", "name": …}` forcing that tool. The model is then constrained to
   conforming JSON rather than persuaded toward it. Then know the edges, because they are where the
   prompt-level fallback still earns its place: a schema pins **shape, not values** (no recursion,
   no numeric bounds, no string lengths — range checks stay in your code); a refusal or a
   truncated response still won't match it, so branch on the stop reason before parsing; and it
   doesn't compose with everything (on the Claude API, constrained format and document citations are
   mutually exclusive). Where the model or endpoint has no such feature, *then* shape by prompt:
   name the exact structure, show one instance, say what to emit for a missing value (`null`?
   `"unknown"`? omit the key?), and say whether anything may accompany the result. Keep that labeled
   as the fallback — a format request narrows the distribution, a schema constrains it. Mechanism
   details and the full limits list are in `references/prompt-patterns.md`.
4. **Choose an example strategy on purpose.** Examples are the strongest single signal in a prompt —
   the model matches their length, tone, and structure — which is what makes them powerful and a
   careless set expensive. **Default to 2–5 input→output pairs** for stylistic or edge-case-heavy
   work, covering the hard cases (an empty value, an ambiguous input, the "say you don't know" case)
   in *exactly* the format you want back; inconsistent examples teach inconsistency. **Scale up when
   you have the labels and the window** — a long context plus a cacheable static prefix makes a block
   of dozens or hundreds affordable, and many-shot blocks are reported to beat the classic handful
   `[unverified here — no provider documentation for a number, no citation checked in this
   environment]`, so measure block size on your eval set (step 8) rather than copying one. **Probe
   the sensitivities** rather than trusting them: example order and label balance are reported to
   move classification-style output `[same hedge]`, and both are cheap to test — shuffle, rebalance,
   re-run. And remember examples **rot**: a block written for an earlier model freezes its behavior
   into a later one, so keep the ones that pin a format-sensitive shape, mark them illustrative, and
   delete examples of judgment the model now handles unaided.
5. **Match the reasoning strategy to the model class, not to the task's difficulty.** Ask what kind
   of model this is *before* writing anything about how it should think.
   - **With a thinking/reasoning mode, depth is configuration, not prose.** The Claude API exposes
     adaptive thinking (`thinking: {type: "adaptive"}`) and an `effort` level (`low` … `max`), and on
     several models thinking is on by default or always on. So "think step by step" and
     `<scratchpad>` instructions are redundant at best; "plan before acting" causes over-planning;
     and "double-check your answer" is documented to cause *over*-verification on at least one model
     where removing it cost no capability. That last one inverts a long-standing prompting habit,
     which is exactly why it belongs in a per-model check rather than a reflex. Don't ask for the
     reasoning back either — the raw chain of thought isn't returned to the caller, and on at least
     one model asking can trigger a refusal; read the thinking blocks the API returns instead.
   - **What still matters, and matters more:** an unambiguous task statement, the output contract
     (step 3), the evidence and context the model cannot infer, and the success criteria. Reasoning
     models remove the need to *elicit* reasoning. They do not remove the need to *specify the job*.
   - **Without a thinking mode**, the older shape still applies: let the model work through steps
     before committing, and when you need both a clean answer and the reasoning, ask for reasoning
     first in one labeled field and the answer last in another you can extract.
   - Either way, a prompt written for an earlier generation is often *too prescriptive* for a later
     one, and that over-specification is documented to reduce output quality. A model change is a
     reason to re-test the prompt, not only to swap the model string. The full stop-doing list is in
     `references/prompt-patterns.md`.
6. **Decompose a complex ask.** If the task has several parts, number the steps ("First… then…
   finally…"); if the parts are truly separate, use separate prompts or a workflow. A prompt that
   bundles five loosely-related requests fails on the hardest one. Reserve step-by-step
   choreography for work where the order genuinely matters — scripting a judgment task is the
   documented over-specification failure, and stating the outcome, the constraints, and how to
   verify usually beats a hand-written procedure.
7. **Treat untrusted content as data, and be honest about what delimiting does.** Delimiting a
   document is a genuine *reliability* practice: it keeps the model from confusing what to process
   with what to do. It is **not** a security boundary. Text that arrives from a web page, a
   retrieved document, an email, a tool result, or another user can carry instructions, and a fence
   or a tag around it does not reliably stop the model from following them. Say so plainly in your
   design notes rather than claiming a fix, then put the real controls where they hold:
   - **Authority belongs in a channel the content can't reach.** Instructions embedded in user or
     tool text are forgeable by anything that can write that text; some APIs offer an operator
     channel that isn't (the Claude API's mid-conversation `role: "system"` message is documented as
     the non-spoofable form of exactly this pattern, on the models that support it).
   - **Constrain what a successful injection could do, and gate what it could not undo.** Narrow the
     exposed tool set, treat model-emitted commands and paths as untrusted on the way *out*
     (allowlist, not blocklist), keep credentials out of reach of the model's execution context, and
     put a human in front of hard-to-reverse actions — sending, paying, deleting, publishing.
     Reversibility is the criterion. Those harness controls are
     `coding-agent-skills:agentic-workflow-design`'s subject; the prompt-side job is to state the
     trust boundary and not to overclaim.
   - **Prompt-level mitigations, ranked as mitigation:** label the block untrusted, say that content
     inside it is data to analyze and never instructions to follow, and ask the model to report
     attempted redirection instead of complying. Useful; not sufficient.
8. **Iterate against real cases, with repeat runs.** Collect a handful of representative real inputs
   *including the ones that currently fail*, each with a known-good output. Then:
   - **Run every case more than once.** Sampling variance alone produces different outputs for an
     identical prompt, so a single run per case cannot distinguish a bad prompt from ordinary
     spread — and any claim that a prompt is "flaky" is unmeasured until you have repeats.
     3–5 runs per case is usually enough to see whether a failure is systematic or occasional;
     record the pass *rate* per case, not a pass/fail. Turning randomness off is not the escape
     hatch you may remember: some providers have removed sampling parameters outright (the Claude
     API rejects non-default `temperature`/`top_p`/`top_k` on its 4.7-and-later generations and
     steers by prompting instead), and even where `temperature: 0` is accepted it never guaranteed
     identical outputs. Variance is something you measure, not something you switch off.
   - **Change one thing at a time while debugging.** When you are attributing a specific failure to
     a specific cause, one edit per run is what makes the attribution valid.
   - **Switch to a designed experiment when you are optimizing, not debugging.** Once several
     factors are in play at once — instruction style, example count, output mechanism, model or
     effort level — one-factor-at-a-time buys one comparison per run and can never see an
     interaction (examples that help a terse prompt and hurt a stepwise one). A balanced factorial
     spends the same runs better: every run informs *every* factor's estimate, so one design yields
     all the main effects and the interactions between them, which is information OFAT cannot
     produce at any run count. Prompt runs against an eval set are cheap, so the full design is
     usually affordable. Hand that off to
     `continuous-improvement-skills:design-of-experiments`, which covers the design matrix,
     randomized run order, replication as the noise yardstick, and the confirming run. The two rules
     are not in conflict: one-factor-at-a-time is for attributing a fix, a factorial is for finding
     the best combination.
   - **If a model grades the outputs, the grader is an instrument and needs qualifying first.**
     Repeat runs, a second judge, a human reference on a sample, and an agreement statistic —
     before its scores decide which prompt ships. That protocol is
     `continuous-improvement-skills:measurement-systems-analysis`; a judge that can't agree with
     itself can't rank your prompt versions.
   - Keep the version that wins across the whole set — not the one that fixed your favorite example
     while quietly breaking two others — and write down what each change was for. When the set
     passes, freeze it as a regression check.
9. **Diagnose failures by cause.** Wrong format → move to a schema constraint (step 3); tighten the
   spec and show an instance only where no constraint exists. Ignores an instruction → check input
   length first: with a long input, move the instruction *after* the material, not earlier; with a
   short one, make it explicit and imperative or demonstrate it in an example. Inconsistent across
   runs → quantify it with repeat runs before treating it as a prompt defect, then reduce ambiguity
   and pin the format mechanically. Hallucinated facts → supply the source material and instruct
   "use only the provided context; if it's not there, say so." Over-planning, over-verifying, or
   padding → look for scaffolding written for an earlier model and delete it. More failure modes are
   in `references/prompt-patterns.md`.

**Deliver the prompt as a package**, not bare text:
- the prompt itself, in one copyable block;
- the mechanisms it depends on (schema-constrained output, thinking/effort configuration, cache
  breakpoints) named explicitly, so a reader can check them against their own model;
- design notes — what each constraint, example, and format rule is there to prevent;
- assumptions about the inputs (encoding, language, size, trust level, edge cases);
- the eval cases used or recommended, the currently-failing ones first, with the repeat count;
- when iterating: what changed from the previous version and which failure it targets.

The assistant drafts the prompt, examples, and eval cases; the human owns the success criteria and
validates against real inputs before relying on it.

## Why / learn
Three ideas carry almost all of prompt quality, and the first one is the newest.

**Prefer a mechanism over a wording.** Wherever the platform can *constrain* an outcome, a sentence
asking for that outcome is the weaker tool — and much classic prompt lore is wording that predates
the constraint. Valid JSON is the clearest case: "return only valid JSON, no prose" reduces the
probability of a chatty preamble, while a schema-constrained decode removes the possibility of a
non-conforming object, which is why the retry-and-repair loop wrapped around a JSON prompt is a
workaround for a missing constraint rather than a design. The same move applies to reasoning depth
(a configuration setting, not an incantation), to authority (an operator channel, not a stern
sentence), and to cost (a cache breakpoint, not a shorter prompt). Ask of every instruction: is this
something only I know — the audience, the quality bar, the constraint and its reason — or is it a
mechanism I should be using instead?

**Specificity and structure drive quality.** A model can only satisfy criteria it can infer, so
every ambiguity you leave — undefined terms, an unstated format, a missing edge case — is a decision
handed to a coin flip. Naming the task, the audience, the constraints, and the exact output shape
removes those coin flips; structure and a concrete example do the same by making the pattern
concrete instead of abstract. This is the part that has *not* aged: context is never cruft. The
common modern failure is the opposite one — a prompt padded with restatements of things the model
already does (be thorough, plan first, verify your work), which now cause over-application.

**Prompts are tested like code, not tuned by vibes — and the test is repeated.** It is dangerously
easy to "improve" a prompt against the single example in front of you and ship a regression on the
cases you didn't look at. A tiny eval set — a few real inputs with known-good outputs, especially
the failing ones — turns prompt work into measurement. Repeat runs are what make that measurement
real: LLM output is nondeterministic, so a one-run-per-case comparison confuses a genuine effect
with the spread you'd see from running the same prompt twice. Once you accept repeats, the natural
next step is a designed experiment across factors rather than a long series of single edits.

One consequence worth internalizing: **a prompt is a per-model artifact.** Instructions that were
load-bearing on one generation become dead weight or active harm on the next — pressure language,
elicited chain-of-thought, self-check scaffolding, word caps, prefill tricks. Re-audit prompts when
you change models, and read this skill the same way: the method (criteria, context, contract,
examples, iteration) travels; every named mechanism gets re-verified against the provider's current
reference.

## Common mistakes
- Persuading where you could constrain ("return only valid JSON") → use the provider's schema-
  constrained output; keep wording as the documented fallback.
- Retry-and-repair loops around unparseable output → you are patching a missing constraint. Move the
  contract to the API layer, then delete the loop.
- "Think step by step" or a `<scratchpad>` block on a thinking model → redundant noise and cost.
  Configure thinking/effort instead.
- Adding "double-check your work" everywhere → documented over-verification on at least one model.
  Delete it and re-test rather than assuming it helps.
- Moving an ignored instruction *earlier* on a long input → it is the wrong direction there. Put the
  material first and the instruction last.
- Treating a delimited block as an injection defence → it is a reliability practice. Constrain
  tools, keep authority out of user/tool text, and gate irreversible actions with a human.
- One run per case, then calling the prompt flaky (or fixed) → you measured sampling noise. Repeat
  each case and record a pass rate.
- Reaching for temperature to stop inconsistency → the knob may not exist on your model, and never
  guaranteed identical output where it did.
- One-factor-at-a-time while optimizing four factors → interactions stay invisible however many runs
  you spend. Design factorially (`continuous-improvement-skills:design-of-experiments`).
- Trusting a model judge's single-run scores to pick a prompt → qualify the judge first
  (`continuous-improvement-skills:measurement-systems-analysis`).
- Vague task ("summarize this") → generic output. State the job, audience, and success criteria.
- Dumping everything as context → the instruction competes with noise. Include only what's needed;
  delimit sources; put a timestamp or request ID anywhere but the top of a cached prefix.
- Stale few-shot block carried across a model upgrade → it freezes the old model's behavior. Re-test
  the examples with the prompt.

## Tailor to your environment
Record your real specifics in `references/your-environment.md`: the models and runtimes you target
and, for each, the mechanisms it actually supports (schema-constrained output, thinking/effort
configuration, caching minimums, whether sampling parameters are accepted) with the date you last
checked them against the provider's reference; the recurring task types you prompt for; your house
output schemas; where your eval cases live and how many repeats you run; and who signs off on a
prompt that touches customers or money. **Never commit sensitive prompt content or real customer
data** — keep proprietary prompts and real examples in `references/your-environment.private.md`,
which `.gitignore` keeps out of git. This skill then adapts its generic method to your models and
tasks.

## References
- references/prompt-patterns.md — prompt skeletons, output-contract mechanisms, example strategy,
  reasoning-model prompting, the untrusted-input rail, caching placement, failure modes → fixes, the
  repeat-run iteration loop, and the patterns that aged out
- references/your-environment.md — your models and their verified mechanisms, house formats, and
  eval cases (fill in)
