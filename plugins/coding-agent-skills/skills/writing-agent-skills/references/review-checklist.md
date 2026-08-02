# Skill review checklist (definition of done)

A skill is done when every box is checked.

## Structure
- [ ] Folder is `plugins/<plugin>/skills/<skill-name>/` and contains `SKILL.md`.
- [ ] `name` frontmatter equals the folder name.
- [ ] Body is under 500 lines.
- [ ] `references/` (if any) is one level deep; files > 100 lines have a TOC.
- [ ] All paths use forward slashes.

## Frontmatter
- [ ] `name` passes all rules (see `frontmatter-rules.md`); no `claude`/`anthropic`.
- [ ] `description` is third-person, ≤ 1024 chars, states what + when, ends with `Triggers:`.

## Content (do + teach)
- [ ] `## When to use` includes a "Not for → see …" cross-link.
- [ ] `## Do it` steps actually accomplish the task; fragile steps are exact.
- [ ] `## Why / learn` explains the reasoning (teaches), not just commands.
- [ ] `## Common mistakes` lists real pitfalls with fixes.
- [ ] `## Tailor to your environment` points at `references/your-environment.md` and warns on privacy.
- [ ] Terminology is consistent; no time-sensitive claims ("as of 2026 …").

## Evals & validation
- [ ] `evals/<plugin>/<skill>.md` has a positive trigger, a near-miss, and a quality rubric.
- [ ] `bash scripts/validate.sh` passes with no warnings for this skill.
- [ ] `claude plugin validate plugins/<plugin>` passes.

## Trigger test (in a fresh session)
- [ ] The positive-trigger prompt loads the skill.
- [ ] The near-miss prompt does NOT load it.
