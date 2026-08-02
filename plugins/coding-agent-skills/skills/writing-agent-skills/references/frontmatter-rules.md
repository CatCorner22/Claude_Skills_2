# Frontmatter rules (full reference)

## Required fields

### `name`
- 1–64 characters.
- Lowercase letters, digits, and hyphens only.
- No leading, trailing, or consecutive hyphens.
- **Must equal the skill's folder name exactly.**
- Must **not** contain the reserved words `anthropic` or `claude`.
- Must not contain XML tags.
- Prefer gerund-ish or plain task names (`bank-reconciliation`, `time-value-of-money`).
  Avoid vague names (`helper`, `utils`, `tools`, `data`).

### `description`
- Non-empty, **maximum 1024 characters**.
- **Third person** (it is injected into the system prompt; first/second person hurts discovery).
- States **both** what the skill does **and** when to use it.
- Leads with the primary use case; ends with a short `Triggers:` list of literal phrases.
- Slightly "pushy" to avoid under-triggering, but specific enough not to over-trigger.
- Must not contain XML tags.
- In Claude Code the combined `description` + `when_to_use` is truncated at ~1536 chars in the
  skill listing, and the whole listing is budgeted to ~1% of the context window. With a large
  library, keep descriptions tight and put the trigger phrase early.

## Optional fields used in this library
- `when_to_use`: extra trigger phrases appended to the description (use sparingly).
- `license`, `metadata`: portable extras from the open spec. Put a `version` inside `metadata`
  if you want per-skill versioning (there is no standard top-level `version` for a skill).

## Claude-Code-only fields (use only for skills that will never run outside Claude Code)
`argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`,
`disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `paths`, `hooks`, `shell`.
Other agents ignore or may choke on these — keep them out of portable skills.

## YAML tips
- Use a block scalar (`>-`) for multi-line descriptions so they fold to a single line.
- Keep the frontmatter valid YAML: quote values containing colons.
