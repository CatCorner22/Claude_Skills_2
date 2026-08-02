# Evals — coding-agent-skills:master-prompt-architect

## 1. Positive trigger (should load the skill)
> "Engineer a commercial-grade system prompt for an agent that triages our AP inbox and
> routes invoices. It has to be bulletproof — lock down the parameters with me first."

Expected: skill loads; acknowledges; identifies missing variables (target model, context
budget, invoice formats, routing categories, failure handling, escalation path) and
systemic risks; asks precise clarifying questions and HALTS — no draft until parameters
are confirmed. After confirmation: backward-designed blueprint, silent triple audit, then
the fixed format (Risk Assessment → Blueprint Summary → single copyable code block,
complete, no placeholders).

## 2. Near-miss (should NOT load this skill)
> "Why does my prompt keep making the model answer in bullet points? Quick fix?"

Expected: quick prompt advice → `coding-agent-skills:prompt-engineering`. The confirmation
gate would be overkill for a one-line tweak. If this skill loads, tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** the gate actually holds (no premature drafting); clarifying questions
  are precise, not generic; the delivered artifact follows the fixed format exactly; active
  voice throughout; zero placeholders or truncation.
- **Teaches:** explains the asymmetry that justifies the gate (question costs a turn; wrong
  assumption costs a rebuild) and why risks lead the delivery.
- **Safe:** proactive warnings on ingestion/deployment hazards; token budget stated; the
  three audits demonstrably applied (e.g. names what the red team pass changed).
