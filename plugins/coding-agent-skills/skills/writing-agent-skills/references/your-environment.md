# Your authoring conventions (sanitized template)

House conventions of your own that every new skill in this repo should follow. This file is the
one place they live, so a future author — or a future session — inherits them instead of
re-deriving them. Keep it structural: no client names, no real data.

## Naming
- **Skill names:** <task-named by default; evocative/persona names only where the skill is meant
  to be invoked deliberately by name. Under name-only listing degradation a persona name carries
  no task signal — see `references/frontmatter-rules.md`.>
- **Plugin membership rule:** <what makes a skill belong in plugin X rather than Y — the kind of
  work the user is doing, not the topic.>

## Sections beyond the fixed order
- <any extra H2 this repo allows, and when. Default: none — the fixed order is the standard.>
- **Deliverable contract:** <whether skills in this repo must state what the finished artifact
  contains. Recommended yes: a skill that teaches a method but never says what lands is the most
  common gap found in review.>

## Provenance marks in use here
Record the legend so marks stay consistent across authors:
- `[snippet-only]` — <verified via convergent search snippets from a research dossier.>
- `[snippet-only, cross-checked]` — <as above, corroborated across independent results.>
- `[canon attribution]` — <author/year named but not independently re-verified; check before quoting.>
- `[background — verify before citing]` — <recalled context, not verified in this environment.>
- `[unverified here]` — <could not be checked in this environment; stated as a claim, not a fact.>

## Versioning
- `metadata.version`: <minor bump on content revision, patch on typo-grade fixes.>
- `plugin.json`: <bump on any content change in the plugin — installed copies are version-pinned
  snapshots and pick up nothing without it.>

## Review depth by skill type
- <e.g. arithmetic-heavy skills get every worked example recomputed; tooling-facing skills get
  every command and config executed; method skills get the value test.>

## Local practice notes
- <anything a future author would otherwise re-learn the hard way.>

---

**Privacy.** Never commit real client, employer, or personal data here or in any skill. Anything
sensitive belongs in `your-environment.private.md`, which `.gitignore` keeps out of git.
