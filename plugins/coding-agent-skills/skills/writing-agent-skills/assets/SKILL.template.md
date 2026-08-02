---
name: skill-name-here
description: >-
  <Third-person: what the skill does> — use when <the situations that should trigger it>.
  Triggers: <comma-separated phrases the user would actually type>.
---

# Human-readable skill title

## When to use
- <Primary situation this skill is for.>
- <Secondary situation.>
- Not for: <adjacent case> → see `<plugin>:<other-skill>`.

## Do it
1. <First concrete step — state inputs and the goal.>
2. <Next step. Use prose for judgment calls.>
3. <For fragile/consistency-critical steps, give exact commands, a column map, or a bundled script.>
4. <Produce the deliverable and state how to check it is correct.>

## Why / learn
<The mental model and the reasoning behind the steps, in plain language. Explain *why* the
approach works so the reader can generalize. Never bark "MUST/NEVER" — teach instead.>

## Common mistakes
- <Pitfall> → <fix>.
- <Pitfall> → <fix>.

## Tailor to your environment
<How the user points this skill at their real setup. Instruct them to drop specifics into
`references/your-environment.md`. Never commit raw real data — sanitize; raw files use the
`.private`/`.local` suffix so `.gitignore` keeps them out of git.>

## References
- references/<topic>.md — <what it contains>

## Scripts
<!-- Optional. One line per bundled script: how to run it and what it outputs. Delete if none. -->
- `scripts/<name>.py` — <what it does and its output>.
