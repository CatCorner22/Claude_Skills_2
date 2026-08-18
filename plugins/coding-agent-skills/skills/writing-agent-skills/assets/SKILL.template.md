---
name: skill-name-here
description: >-
  <Third-person: what the skill does> — use when <the situations that should trigger it>.
  Triggers: <comma-separated phrases the user would actually type>.
metadata:
  version: "1.0.0"
  # source: >-   # OPTIONAL — only when built from external research or a supplied spec.
  #   <Which dossier or spec this came from, plus the provenance-mark legend if the
  #   skill's claims carry marks such as [snippet-only].>
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


**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/<skill-name>.md` works well — fill
it in there, and point this skill at that copy. Your specifics then survive updates and stay somewhere
you own rather than in a cache you may not realise is disposable.
## References
- references/<topic>.md — <what it contains>

## Scripts
<!-- Optional. One line per bundled script: how to run it and what it outputs. Delete if none. -->
- `scripts/<name>.py` — <what it does and its output>.
