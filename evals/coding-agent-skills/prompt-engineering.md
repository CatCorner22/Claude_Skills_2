# Evals — coding-agent-skills:prompt-engineering

## 1. Positive trigger (should load the skill)
> "My prompt that extracts fields from support emails works maybe 70% of the time — sometimes it adds
> a chatty intro, sometimes it invents a value that wasn't in the email. How do I make it reliable?"

Expected: skill loads; specifies an explicit output format (JSON, "output only the JSON"), adds
few-shot examples covering edge/missing-value cases, grounds it ("use only the provided email; if a
field is absent, return null / say unknown"), and sets up iteration against a small real eval set of
the failing emails rather than tuning on one example.

## 2. Near-miss (should NOT load this skill)
> "I'm building an agent that runs several tools in sequence and keeps looping forever — how should I
> bound it and add checkpoints?"

Expected: this is multi-step workflow reliability (guardrails, decomposition, loop bounds), handled by
`coding-agent-skills:agentic-workflow-design`, not single-prompt wording. If this skill loads instead,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** states the task + success criteria, gives the right context, adds few-shot
  examples, specifies an explicit output format, and grounds to prevent hallucination.
- **Teaches:** explains that specificity and structure drive quality, and that prompts should be
  tested like code (a small real eval set, change one thing at a time) rather than tuned by vibes.
- **Provider-agnostic:** the method doesn't depend on a specific vendor; any model-specific knob is
  flagged as "confirm your model's features," not assumed.
