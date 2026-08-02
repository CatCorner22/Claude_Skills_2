# Evals — coding-agent-skills:writing-agent-skills

## 1. Positive trigger (should load the skill)
> "I want to add a new skill to the finance plugin for computing bond duration.
> How should I set it up so it matches the rest of the library?"

Expected: skill loads; directs the author to copy `assets/SKILL.template.md`, enforces the
frontmatter rules (name == folder, no claude/anthropic, third-person description with Triggers),
the fixed do+teach section order, progressive disclosure, the tailoring hook, and an eval file.

## 2. Near-miss (should NOT load this skill)
> "Write me a good prompt to get an LLM to summarize a contract."

Expected: this is prompt authoring, handled by `coding-agent-skills:prompt-engineering`, not skill
authoring. If this skill loads, tighten the description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** produces a compliant `SKILL.md` (correct frontmatter, exact section order,
  under 500 lines), plus the matching `evals/<plugin>/<skill>.md`, and registers a new plugin
  correctly if needed.
- **Teaches:** explains WHY the description is the trigger and why progressive disclosure keeps the
  body small — so the author internalizes the standard, not just copies it.
- **Safe:** enforces the privacy rule (never commit real data; use `*.private.md`).
