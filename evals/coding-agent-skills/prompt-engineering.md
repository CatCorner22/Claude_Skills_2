# Evals — coding-agent-skills:prompt-engineering

## 1a. Positive trigger — flaky extraction prompt (should load the skill)
> "My prompt that extracts fields from support emails works maybe 70% of the time — sometimes it adds
> a chatty intro, sometimes it invents a value that wasn't in the email. How do I make it reliable?"

Expected: skill loads and leads with the **mechanism, not the wording** — schema-constrained output
(on the Claude API, `output_config.format` with a JSON schema, or a forced tool call whose
`input_schema` is the contract), with "return only JSON, no prose" named as the fallback for models
that lack it, and no retry-and-repair loop proposed. Grounds the extraction ("use only the provided
email; if a field is absent, `null`"), covers the missing-value rule inside the schema or the format
spec, and sets up iteration against a small real eval set of the failing emails **with repeat runs
per case**, noting that the "70% of the time" figure is unmeasured until each case has been run more
than once. Bonus: flags that the emails are untrusted input and that a delimited block is a
reliability practice, not an injection defence.

Fails if it recommends persuading the model into JSON as the primary fix, proposes a parse-retry
loop, or offers "lower the temperature" without noting that the parameter may not exist on the
target model and never guaranteed identical output.

## 1b. Positive trigger — prompt written for an older model (should load the skill)
> "We're moving this system prompt to a reasoning model. It says 'think step by step', has five
> few-shot examples and a 'double-check your answer before responding' line. What should change?"

Expected: skill loads and answers by model class. Removes the chain-of-thought incantation in favour
of thinking/effort **configuration**; flags the self-check line as a documented over-verification
trigger on at least one model rather than harmless; re-examines the example block (examples are the
strongest signal in a prompt, and a block written for an earlier model freezes its behavior) instead
of assuming five is right; keeps the task statement, output contract, grounding, and success criteria
as the parts that matter more, not less. Verifies the specifics against the provider's current API
reference rather than asserting them from memory, and treats the migration as a reason to re-run the
eval set.

Fails if it recommends adding "think step by step", more examples, or a verification step — or if it
states capability claims (thinking configuration, prefill, sampling parameters) without checking them
against a current reference.

## 2a. Near-miss — multi-step agent reliability (should NOT load this skill)
> "I'm building an agent that runs several tools in sequence and keeps looping forever — how should I
> bound it and add checkpoints?"

Expected: this is multi-step workflow reliability (guardrails, decomposition, loop bounds), handled by
`coding-agent-skills:agentic-workflow-design`, not single-prompt wording. If this skill loads instead,
tighten the description / cross-links.

## 2b. Near-miss — qualifying a judge model (should NOT load this skill)
> "Before I let my grader model choose between prompt versions, how do I show its scores can be
> trusted? I want inter-rater agreement numbers."

Expected: this is measurement-system rigor — repeat runs, a second judge, a human reference, an
agreement statistic — owned by
`continuous-improvement-skills:measurement-systems-analysis`. This skill names that seam in its
iteration step, so the correct behavior is a hand-off, not an answer. If prompt-engineering loads
and improvises an agreement protocol of its own, the seam sentence is not doing its job.

## 3. Quality rubric
A good response:
- **Does the task:** states the task + success criteria at normal volume, gives the right context and
  only that, orders long inputs material-first with the ask last, sets the output contract at the
  mechanism layer, chooses an example strategy deliberately, matches the reasoning strategy to the
  model class, and grounds to prevent hallucination.
- **Mechanism before wording:** where the platform can constrain an outcome, the answer reaches for
  the constraint and demotes the sentence that asks for it. Retry-and-repair machinery around
  unparseable output is removed, not tuned.
- **Honest about limits:** names what a schema cannot express (value ranges, lengths, recursion) and
  the residual failure modes (refusal, truncation); presents delimiting as reliability and prompt
  injection as mitigated-not-solved, with the real controls (authority channel, constrained tool
  surface, human confirmation for irreversible actions) placed where they belong.
- **Measures instead of asserting:** repeat runs per case with a pass rate; one factor at a time while
  debugging; a factorial with an eval set when optimizing several factors at once
  (`continuous-improvement-skills:design-of-experiments`); a qualified judge before model scores pick
  a prompt (`continuous-improvement-skills:measurement-systems-analysis`).
- **Deliverable shape:** delivers the prompt as the skill's package — copyable prompt block, the
  mechanisms it depends on named so a reader can check them, design notes on what each constraint
  prevents, input assumptions including trust level, and the eval cases (failing ones first) with the
  repeat count — not a bare rewritten prompt.
- **Teaches:** explains that a mechanism beats a wording, that specificity and structure still drive
  quality (context is never cruft), that prompts are tested like code with repeats rather than tuned
  by vibes, and that a prompt is a per-model artifact to re-audit on a model change.
- **Provider-honest:** the method doesn't depend on a specific vendor, but any capability claim is
  checked against that provider's current reference rather than recalled — and where the reference
  documents nothing (e.g. an optimal many-shot block size), the answer says so and turns it into
  something to measure.
