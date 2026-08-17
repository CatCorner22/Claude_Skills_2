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
- [ ] `metadata: version` present (see `frontmatter-rules.md`); bumped if this is a revision.
- [ ] **Trigger phrases are collision-checked**: grep every phrase in the `Triggers:` list
      against the frontmatter of every other active skill. A phrase claimed by two skills
      mis-routes users, and the validator does not catch it. Qualify or yield the loser.
- [ ] Description leaves editing headroom (aim ≤ 984 chars). The validator NOTEs above 973 —
      a description at the cap cannot absorb a future seam sentence.

## Content (do + teach)
- [ ] `## When to use` includes a "Not for → see …" cross-link.
- [ ] `## Do it` steps actually accomplish the task; fragile steps are exact.
- [ ] `## Why / learn` explains the reasoning (teaches), not just commands.
- [ ] `## Common mistakes` lists real pitfalls with fixes.
- [ ] `## Tailor to your environment` points at `references/your-environment.md` and warns on privacy.
- [ ] Terminology is consistent; no time-sensitive claims ("as of 2026 …").
- [ ] **Every worked example's arithmetic recomputed from its own inputs.** This is the defect
      class that has survived every other check in this library's history — it appeared in
      *every* authoring wave. Recompute totals, percentages, rates, and any conclusion drawn
      from them; confirm an example's stated finding actually follows from its own setup.
- [ ] **Reciprocal-link pass on the OLDER side of every new seam.** A new skill that cites 3–8
      neighbours while receiving zero inbound citations is a discovery dead-end: nobody starting
      from an existing skill will ever learn it exists. Add the `Not for:` line to the
      established skill, not just the new one.
- [ ] Every cited `plugin:skill` resolves to a live skill directory; archived targets use the
      explicit `(archived: plugin:skill, restorable from archive/)` form.
      **`scripts/validate.sh` now enforces this** — it resolves every `plugin:skill` reference
      against active skills, active subagents (`plugins/*/agents/*.md` share the namespace), and
      `archive/`, and errors on any that resolves to none of them or that points at an archived
      target without saying so. So the manual version of this check is now a courtesy; the one
      thing still worth eyeballing is whether the *prose around* the link describes the target
      accurately, which no script can tell you.
- [ ] Any external number or attribution carries a provenance mark or an honest hedge; no
      invented statistics.

## Evals & validation
- [ ] `evals/<plugin>/<skill>.md` has a positive trigger, a near-miss, and a quality rubric.
- [ ] The eval's positive prompt actually contains a phrase the description advertises. An eval
      written in vocabulary the skill does not claim tests a route that does not exist.
- [ ] `bash scripts/validate.sh` passes with no warnings for this skill.
- [ ] `python3 scripts/gen-catalog.py` re-run, and the skill's row in `docs/INDEX.md` reads
      correctly — the generator derives that row by parsing the description, so a row that reads
      as a fragment means the description's shape defeated the parser.
- [ ] `claude plugin validate plugins/<plugin>` passes.
- [ ] Plugin `version` bumped in `plugins/<plugin>/.claude-plugin/plugin.json` — installed
      copies are version-pinned snapshots and pick up nothing without a bump.

## Trigger test (in a fresh session) — the only check that validates routing
Everything above can pass on a skill that never loads. This is the one item that proves the
description works, and it cannot be automated from inside a session that already knows the
answer. The full protocol — setup, scoring, and the ranked rows — is `docs/trigger-test.md`;
add a row there for the skill you are shipping and log the result.
- [ ] The positive-trigger prompt loads the skill.
- [ ] The near-miss prompt does NOT load it.

Four rules that decide whether the result means anything:
- **One fresh session per prompt.** Once a skill loads, its body is in context and biases every
  later turn, so a second prompt in the same session tests nothing.
- **Do not paste a trigger phrase verbatim.** Write the prompt in the words a user would actually
  type. A test that quotes the trigger string passes by construction and measures nothing.
- **Record the install set.** The listing trims descriptions to name-only somewhere around 100
  installed skills, silently. A pass with four plugins installed is not evidence of a pass with
  fourteen — they are different experiments.
- **Distinguish the two failures.** Nothing loaded (**MISS**) means the description lacks the
  user's vocabulary — add it. A different plausible skill loaded (**WRONG**) means two descriptions
  are competing and neither names the boundary — write reciprocal `Not for:` lines in *both*, in
  matching words. Never fix a WRONG by deleting the loser's trigger phrase: doing that to a word
  three skills shared is what left `standardize` with no owner at all.
