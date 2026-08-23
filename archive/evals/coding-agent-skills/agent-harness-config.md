# Evals — coding-agent-skills:agent-harness-config

## 1. Positive trigger (should load the skill)
> "Every time you finish editing a Python file in this repo, automatically run black on it.
> Set that up so I don't have to ask."

Expected: skill loads; recognizes this is an automated recurring behavior → a `PostToolUse` hook
in `.claude/settings.json` (not a memory note); writes the hook config and a small hook script.

## 2. Near-miss (should NOT load this skill)
> "Explain what a good system prompt looks like for an LLM agent."

Expected: this is prompt design, handled by `coding-agent-skills:prompt-engineering`, not harness
configuration. If this skill loads, tighten the description/cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** edits the correct settings layer, uses valid `permissions`/`hooks`/`mcpServers`
  JSON, and scopes rules narrowly.
- **Teaches:** explains why a recurring behavior must be a hook (harness-enforced) rather than a
  preference, and how settings precedence decides where a rule belongs.
- **Safe:** does not propose over-broad allow rules; keeps secrets out of committed files.
