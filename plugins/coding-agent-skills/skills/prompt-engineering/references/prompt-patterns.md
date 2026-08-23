# Prompt patterns and failure modes

Reusable structures and the fixes for the failures you'll actually hit. The *shapes* here are
provider-agnostic; the *mechanisms* are not. Every mechanism named below was checked against the
Claude API reference available in this environment (in Claude Code, the bundled `claude-api` skill),
and each one differs by provider and by model generation — confirm yours before relying on it:
schema-constrained output, thinking/effort configuration, prompt caching, whether sampling
parameters are accepted at all, and whether assistant-turn prefill is still permitted.

## Contents
- Two prompt skeletons (short input vs. long input)
- The output contract: mechanism first, wording second
- Example strategy: few-shot, many-shot, ordering
- Reasoning and extended-thinking models
- Grounding to reduce hallucination
- Untrusted input: what delimiting does and does not do
- Where static content goes (prompt caching)
- Failure modes → fixes
- The iteration loop (with repeat runs)
- Patterns that aged out

## Two prompt skeletons (short input vs. long input)

Keep instructions and data visibly separate in both. What changes is where the instruction sits.

**Short input** — instructions first reads naturally:
```
Role/goal:    You are <role>. Your job is <task> for <audience>.
Instructions: 1) ... 2) ... 3) ...   (numbered, imperative, no volume knob)
Context:      <definitions, constraints>
Input:        <<< the data to act on, clearly delimited >>>
Output:       <schema-constrained; state the shape here only as a fallback>
Examples:     <2-5 input→output pairs, if format or style matters>
```

**Long input** (a big document, a large retrieved set) — the material comes first and the ask comes
last:
```
Role/goal:    You are <role>. Your job is <task> for <audience>.
Context:      <definitions, constraints>
Examples:     <the example block, if any>
Material:     <<< the long document / retrieved set, clearly delimited >>>
Task:         <the instruction or question, restated here — the last thing before the answer>
```
Two reasons, and the second is the durable one. The failure being fixed — an instruction that gets
dropped — is a long-input failure, and placing the instruction after the material puts it next to the
answer. And this ordering is what prompt caching requires anyway (see *Where static content goes*):
static material ahead of the varying question, or nothing is ever reused.

One honesty note on the first reason: "it ignores the instruction because the input is long" is a
hypothesis, not a law. Provider documentation for at least one model family states that instruction
following, tool calling, and reasoning stay strong across a full million-token window — so if the
long-input reordering doesn't fix it, the cause is elsewhere (a buried instruction competing with a
wall of same-priority bullets, a contradiction, or a missing criterion). Measure with repeat runs
before and after the move; the caching payoff is the reason the layout is worth keeping either way.

Do not read either skeleton as "structure harder." Structure and delimiters are for reference data;
behavioral guidance reads better as prose that carries its reason, and heavy formatting in a prompt
tends to bleed into the output's format.

## The output contract: mechanism first, wording second

**Order of preference:**

1. **Schema-constrained output.** On the Claude API: `output_config.format` with a JSON schema, and
   the SDK's `messages.parse()` to validate the response against that schema on arrival. The
   response is constrained to conform, rather than asked to.
2. **A forced tool call as the schema.** When the result should land as a structured call rather
   than as message text: define the tool so its `input_schema` *is* the output contract, set
   `strict: true` on the tool (which requires `additionalProperties: false` and an explicit
   `required` list), and force it with `tool_choice: {"type": "tool", "name": "<tool>"}`. Useful
   when the same schema also drives an action, or for classification via an `enum` field of valid
   labels. Give the tool a real description — under-described tools are the common failure, and
   detail there does more for behavior than adjectives in the prompt.
3. **Prompt-level shaping — the fallback for models and endpoints with neither.** Name the exact
   structure, show one instance, say what to emit for missing values (`null` / `"unknown"` / omit
   the key), and state whether anything may accompany the result.

**What the schema can't do, and what you keep doing yourself:**
- Shape only, not values: recursive schemas, numeric bounds (`minimum`, `maximum`, `multipleOf`),
  string-length limits, and complex array constraints are outside the supported subset; every object
  needs `additionalProperties: false`. Keep range/length validation in your code — some SDKs strip
  unsupported keywords and check them client-side, so know which behavior you're getting.
- Two residual failure modes: a **refusal** need not match the schema, and hitting the output-token
  cap **truncates**. Branch on the stop reason before parsing, and give `max_tokens` headroom.
- Composition limits are real: on the Claude API, constrained format and document **citations** are
  mutually exclusive (the combination errors), and a new schema pays a one-time compilation cost
  before it is cached. Constrained output does compose with batching, streaming, token counting, and
  extended thinking.
- If a preamble still appears in a *non*-constrained route, the fix is a plain system instruction
  ("Respond directly, with no preamble") — not escalating adjectives.

## Example strategy: few-shot, many-shot, ordering

Examples are the strongest single signal in a prompt: the model matches their length, tone, and
structure. Budget them deliberately.

- **2–5 pairs** is the default for stylistic or edge-case-heavy work. Cover the hard cases (empty
  field, ambiguous input, the "say you don't know" case). Keep example outputs in *exactly* the
  target format. Inconsistent examples teach inconsistency.
- **Many-shot** is worth testing when you have labeled cases and a long context window: the block
  is static, so it goes in the cached prefix and is read at a fraction of input price on every
  subsequent request. The in-context-learning literature reports blocks of dozens to hundreds
  outperforming a handful `[unverified here — the provider reference documents no number, and no
  citation was checked in this environment]`. Treat block size as a factor to measure on your eval
  set, not a setting to copy.
- **Order and label balance** are reported to move classification-style outputs `[same hedge]`.
  Cheap to test: shuffle the example order, balance the counts per label, re-run with repeats. If
  the answer moves, the dependency is real and your draft's success was partly luck.
- **Examples rot.** A block written for an earlier model freezes its behavior into a later one.
  Keep examples that pin a genuinely format-sensitive shape, mark them illustrative, and delete
  examples of judgment the model now handles unaided.
- One structural note: an example block that ends on the assistant side is ordinary conversation
  history and is fine. A *trailing* assistant turn at the end of the whole request is a prefill —
  see *Patterns that aged out*.

## Reasoning and extended-thinking models

Decide the model class first; the prompt changes shape, not just wording.

**Stop doing (on models with a thinking/reasoning mode):**
- "Think step by step", "take a deep breath", `<scratchpad>`/`<thinking>` instructions — redundant at
  best. Depth is a configuration: on the Claude API, adaptive thinking (`thinking: {type:
  "adaptive"}`) plus an `effort` level from `low` to `max`; on several models thinking is on by
  default or always on.
- "Plan before acting" / "use the think tool to plan" — causes over-planning. If behavior is still
  too aggressive after removal, lower `effort` rather than adding prose.
- "Double-check your answer", "re-verify before responding", separate verification steps in the
  harness — documented to cause over-verification on at least one model, where deleting them cost no
  capability. This inverts the familiar "ask it to self-check" advice, which is why it is a per-model
  check and not a rule.
- "Show your thinking" / a required reasoning section in the output — the raw chain of thought isn't
  returned to the caller, and on at least one model instructing reasoning reproduction can trigger a
  refusal. Read the thinking blocks the API returns instead; where a readable summary exists it is a
  display setting, not something to prompt for.
- Hard numeric output caps ("at most 120 words", "five bullets max") — these starve reasoning on hard
  problems. Express the goal as audience and outcome; keep a format requirement as a format
  instruction, not a word count.

**Keep doing, and invest more here:** an unambiguous task statement; the output contract; the
evidence, context, and definitions the model can't infer; the success criteria; and an explicit
scope statement if the model tends to widen the job. Where a model runs long or narrates heavily,
tune that with a short, plain instruction about length or communication style — and re-test, because
verbosity levers are model-specific and `effort` does not reliably control visible output length.

**On a model without a thinking mode**, the older shape still works: let it reason before committing,
and when you need a clean answer too, ask for reasoning first in one labeled field and the answer
last in another you can extract.

## Grounding to reduce hallucination
- Supply the source material and instruct: "Answer using only the provided context."
- Add the escape hatch: "If the answer isn't in the context, say you don't know." Without it, models
  fill gaps.
- Ask for quotes or citations back to the source when you need to verify. Some APIs do this
  natively — the Claude API's document `citations` return cited text with a location per claim, which
  beats asking for quotes in prose. Note the trade-off above: it doesn't combine with a constrained
  output format.
- "Do not hallucinate" as a bare instruction is weak; grounding plus the escape hatch is the
  mechanism.

## Untrusted input: what delimiting does and does not do

**Does:** keeps the model from confusing what to process with what to do. A reliability win, and
worth doing on every prompt that carries a payload.

**Does not:** create a security boundary. Content from a web page, a retrieved document, an email, a
tool result, or another user can carry instructions, and a fence or tag around it does not reliably
stop the model from acting on them. Do not present delimiting as a fix for prompt injection.

The controls that actually hold, in the order they matter:
1. **Keep authority in a channel the content can't write to.** Instructions embedded in user or
   tool text are forgeable by anything that can write that text. Where an API offers a distinct
   operator channel, use it: the Claude API's mid-conversation `role: "system"` message is documented
   as the non-spoofable form of the "system reminder inside the user turn" pattern (on the models
   that support it; elsewhere the user-turn block is the documented fallback, with its forgeability
   accepted).
2. **Constrain the blast radius.** Expose the narrowest useful tool set; keep read-only tools
   obviously read-only; treat model-emitted commands and paths as untrusted input on the way out
   (allowlist, never blocklist; resolve paths and confine them to a root); keep credentials out of
   any context the model's code can read.
3. **Human confirmation for consequential, hard-to-reverse actions** — sending, paying, deleting,
   publishing. Reversibility is the criterion, and a dedicated, typed tool is easier to gate and
   audit than a general shell call.
4. **Prompt-level mitigations, ranked as mitigation:** label the block untrusted, state that content
   inside it is data to analyze and never instructions to follow, and ask the model to report
   attempted redirection instead of complying. Useful; not sufficient.

Harness design for 2 and 3 is the archived `coding-agent-skills:agentic-workflow-design`'s subject. The
prompt-side obligation is to state the trust boundary honestly in the design notes.

## Where static content goes (prompt caching)

Caching changes prompt *layout*, so it belongs in prompt design rather than in a cost appendix.

- The cache is a **prefix match**: any byte change invalidates everything after it. Render order on
  the Claude API is `tools` → `system` → `messages`.
- Therefore: **stable content first, volatile content last.** Frozen instructions, tool definitions,
  the example block, and long reference documents go early; the varying question, per-request IDs,
  and timestamps go after the last breakpoint.
- **Shared prefix, varying suffix** is the common prompt-engineering shape (a fixed preamble of
  examples plus retrieved docs, then a different question each time). Put the breakpoint at the end
  of the *shared* portion — a breakpoint after the varying question writes a new entry every request
  and reads none.
- A prompt that differs from its first tokens has no reusable prefix; don't cache it.
- Constraints worth knowing before you design around it: a small number of breakpoints per request
  (four on the Claude API); a **minimum cacheable prefix that is model-dependent** and not monotonic
  across generations (documented values range from a few hundred to a few thousand tokens), below
  which nothing caches and nothing errors; cache reads cost a small fraction of input price while
  writes cost a premium, so a prefix read once is a loss.
- Verify rather than assume: a cache-read counter that stays at zero across identical prefixes means
  a silent invalidator — a `datetime.now()` or UUID in the system prompt, non-deterministic JSON
  serialization, a per-user ID or conditional section early in the prefix, or a tool list that
  varies per user.

## Failure modes → fixes
- **Wrong / unspecified format** → move the contract to a schema constraint. Only where none exists:
  specify the structure exactly and show an instance.
- **Unparseable output handled by a retry loop** → the loop is a symptom. Constrain the output, then
  delete the loop, its regex extraction, and any stop-sequence guard around it.
- **Ignores an instruction** → with a long input, move the instruction *after* the material (moving
  it earlier is the wrong direction there); with a short input, make it explicit and imperative or
  demonstrate it in an example. Check that it isn't buried in a wall of similar-priority bullets.
- **Inconsistent across runs** → measure it first with repeat runs; you cannot tell a prompt defect
  from sampling spread on one run each. Then reduce ambiguity and pin the format mechanically.
  Lowering randomness is often unavailable (some providers reject sampling parameters outright) and
  never guaranteed identical output where it was accepted.
- **Hallucinated facts** → ground in provided context; add "if not present, say you don't know";
  prefer native citations where offered.
- **Too verbose / chatty** → in a constrained route this can't happen for the payload; for prose,
  give a plain conciseness instruction and re-test. Avoid numeric caps on reasoning-heavy tasks.
- **Over-planning, over-verifying, excessive self-correction, narration** → look for scaffolding
  written for an earlier model and delete it before adding anything.
- **Fails only on edge cases** → add those exact cases as examples *and* as eval cases.
- **Does part of the task** → decompose; number the steps; or split into separate prompts.
- **Follows an instruction that came from the input** → an injection, not a wording problem. See
  *Untrusted input*.
- **Prompt is expensive** → check cache reads before shortening; layout usually beats trimming.

## The iteration loop (with repeat runs)
1. Gather real inputs, including current failures, each with a known-good output.
2. Decide the repeat count per case (3–5 is a workable default) and record a **pass rate** per case,
   not a pass/fail. This is what makes a flakiness claim measurable.
3. Change **one** thing when you are debugging — attributing a fix requires it.
4. Run the whole set, every case, at the agreed repeat count.
5. Keep the version that wins across the set; note what the change was for.
6. When several factors are in play at once (instruction style × example count × output mechanism ×
   model or effort level), stop iterating one edit at a time and design a factorial instead —
   `continuous-improvement-skills:design-of-experiments` covers the design matrix, randomized run
   order, replication as the noise yardstick, and the confirming run. Its worked example is exactly
   this eval-set case.
7. If a model grades the outputs, qualify the grader before its scores choose a prompt: repeat runs,
   a second judge, a human reference on a sample, and an agreement statistic —
   `continuous-improvement-skills:measurement-systems-analysis`.
8. When the set passes, freeze it as a regression check for future edits — including the next model
   change, which is the event most likely to break it.

## Patterns that aged out

Kept as a list of *old patterns* rather than dated commentary, so it stays readable as the ground
shifts. Each of these was correct advice for some model generation; each is now either superseded by
a mechanism or actively harmful. Re-audit against your provider's reference — the boundary at which
each changed is model-specific.

| Old pattern | What replaced it |
|---|---|
| Assistant-turn prefill (`{"role": "assistant", "content": "{"}`) to force JSON, a label, or skip a preamble | Schema-constrained output, an enum-field tool, or a plain "no preamble" instruction. On the Claude API a trailing assistant prefill errors on the 4.6-and-later Opus- and Sonnet-tier generations; assistant messages *earlier* in the array (few-shot history) remain fine |
| Stop-sequence guards, regex extraction, retry-on-parse-failure loops around a JSON prompt | The constraint itself. Remove the surrounding machinery, not just the prompt sentence |
| "Output ONLY valid JSON, nothing before or after" as the primary mechanism | The same sentence demoted to a fallback for endpoints without constrained output |
| "Think step by step" / `<scratchpad>` / "take a deep breath" | Thinking configuration and an effort level |
| "Plan before acting", "show your thinking", "double-check your work" | Deletion — on a model that plans and verifies unprompted these cause over-planning, an unsatisfiable request, or over-verification |
| Hard word/bullet caps and "summarize progress every N tool calls" | Audience-and-outcome framing; models that calibrate length and narration on their own read a numeric clamp literally, and caps starve hard reasoning |
| `temperature`/`top_p`/`top_k` tuning, fixed thinking-token budgets | Prompting plus effort configuration; several generations reject these parameters outright, and `temperature: 0` never guaranteed identical output |
| `CRITICAL:` / `MUST` / `NEVER` stacks, "do not be lazy", "be thorough" | One plain statement with its reason; emphasis is a scoped, tested fix for one demonstrably underweighted instruction |
| "You are a helpful assistant" as the context | A one-line role statement is fine — the defect is an identity line standing in for audience, product, and quality bar |
