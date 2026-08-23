# Skill review checklist (definition of done)

A skill is done when every box is checked.

## Contents
- [Structure](#structure)
- [Frontmatter](#frontmatter)
- [Content (do + teach)](#content-do-teach)
- [Evals & validation](#evals-validation)
- [Executable content — the bar prose does not need](#executable-content-the-bar-prose-does-not-need)
- [Trigger test (in a fresh session) — the only check that validates routing](#trigger-test-in-a-fresh-session-the-only-check-that-validates-routing)

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
      *every* authoring wave. `python3 scripts/check-arithmetic.py` (also run by
      `validate.sh`) now recomputes every `a = b = c` chain mechanically, so the hand pass is
      only for what it cannot parse: conclusions drawn *from* the numbers, figures carried
      across prose sentences, and any claim that an example's stated finding follows from its
      own setup. The script proves the sums; you still have to prove the story.
- [ ] **If you changed a skill's internal structure — its steps, phases, gates, or fields —
      re-check what other skills SAY about it.** `validate.sh` proves a `plugin:skill` reference
      resolves; nothing proves the sentence around it is still true. Deepening `reflective-learner`
      turned its four-step protocol into five, and three inbound references in two other files went
      on calling it "the four-step protocol" — resolving perfectly, describing something that no
      longer existed. `python3 scripts/check-cross-claims.py` finds counted claims about other
      skills (advisory, not gating). The durable fix is to *name* the thing rather than count it:
      "the correction protocol", not "the four-step protocol".
- [ ] **Reciprocal-link pass on the OLDER side of every new seam.** A new skill that cites 3–8
      neighbours while receiving zero inbound citations is a discovery dead-end: nobody starting
      from an existing skill will ever learn it exists. Add the `Not for:` line to the
      established skill, not just the new one.
- [ ] **When you fix a defect, grep the library for the same defect and fix every sibling in the
      same pass — including elsewhere in the skill you just fixed.** A fix applied to one skill
      does not propagate on its own, and the library has now been bitten by this twice.
      `fmea` was repaired for multiplicative risk scoring (a severity ceiling was added so a rare
      catastrophic failure cannot be averaged away), and `pre-mortem` went on ranking by
      likelihood × damage × detection-lateness for months — propagating downstream, because
      `break-glass-playbooks` selects which crises to arm from `pre-mortem`'s ranking. Then, fixing
      `pre-mortem`'s SKILL.md and method reference *still* missed the same formula sitting in its
      own `references/your-environment.md`, and a third copy in
      `lean-six-sigma-for-software`'s risk register.
      The procedure: name the defect as a *pattern* rather than a location, grep the whole tree for
      that pattern (`plugins/**` including `references/`, `assets/`, `scripts/`, and every
      `your-environment.md` template), and fix or explicitly clear each hit before you close the
      task. A template that still teaches the defect is the worst hit of all, because it is the
      thing users copy.
- [ ] Every cited `plugin:skill` resolves to a live skill directory; archived targets use the
      explicit `(archived: plugin:skill, restorable from archive/)` form.
      **`scripts/validate.sh` now enforces this** — it resolves every `plugin:skill` reference
      against active skills, active subagents (`plugins/*/agents/*.md` share the namespace), and
      `archive/`, and errors on any that resolves to none of them or that points at an archived
      target without saying so. So the manual version of this check is now a courtesy; the one
      thing still worth eyeballing is whether the *prose around* the link describes the target
      accurately, which no script can tell you.
- [ ] Any external number or attribution carries a provenance mark or an honest hedge; no
      invented statistics. **Use the house vocabulary, which means these and only these:**
      - `[snippet-only]` — taken from search snippets, primary source not opened. Add
        `, cross-checked` when independent snippets agreed, or `, ×N` for the number that did.
      - `[canon attribution]` — named to the standard source everyone cites, not
        independently re-verified. Use for "Klein's pre-mortem", "Rubin's taxonomy".
      - `[background — verify]` — general knowledge stated for orientation; the reader should
        confirm before relying on it.
      - `[unverified]` — a specific value that could not be confirmed. **Never quote a number
        beside this mark.** Say what is unknown, not what you half-remember.
      - `[rule text]` — quoted or closely paraphrased from a statute, rule, or standard, with
        the instrument named and its jurisdiction stated.
- [ ] **Epistemic hedging sits in the right section, and the Do-it step keeps its verb.** A
      `## Do it` step is an instruction: it carries the action plus at most a bracketed mark.
      The reasoning, the caveat, and the reason the number is doubted belong in `## Why / learn`
      or the reference. This is a real failure mode here — a step whose instruction ("have the
      user say it back") got demoted to a subordinate clause while three sentences of
      uncertainty about an effect size took the main verb.
- [ ] **Never ship the repo's own review history as skill content.** "An earlier version of
      this file said…" is legitimate when it teaches a trap the reader could fall into; "a
      reviewer showed…" and "this environment could not reach the sources" are not — the second
      reads to an installed user as a claim about *their* environment. State what is known and
      what is not; the audit trail belongs in git.
- [ ] **Every runnable path is written for the installed shape**, i.e. addressed from
      `${CLAUDE_PLUGIN_ROOT}` (or from the user's own project), never as a bare `scripts/…`
      relative to this repo. `validate.sh` errors on the bare form. Nothing else in this repo
      tests the installed artifact, so this is the author's job.

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
- [ ] Skill `metadata.version` bumped for any content change (three-part semver;
      `validate.sh` errors on a missing or malformed one and NOTEs an unbumped change).

## Executable content — the bar prose does not need

Prose survives a careless reader; code does not. Every finding rated critical in this
library's deepest review sat in executable content — two bundled scripts and about a dozen
copy-paste recipes — never in the prose, which by then had been through five passes. Reading
code is not reviewing it: each of these read fine.

- [ ] **Every bundled script has a `--self-test`, and it covers the failure the script exists
      to prevent** — not just its happy path. A citation verifier's self-test must include a
      fabricated identifier; a linter's must include a deck that violates each rule.
- [ ] **The self-test is mutation-tested at least once.** Break each guard deliberately and
      confirm the suite fails. A suite that passes with the check deleted is not a suite. Two
      real cases here: a linter whose five checks could each be removed with `--self-test`
      still exiting 0, and a script whose test asserted the buggy behaviour, so the bug was
      pinned rather than caught.
- [ ] **Every copy-paste recipe has been RUN once, against the failure case it describes** —
      in the actual language and library, not read. Found only by running: a `KeyError` on a
      spec the validator deliberately allows, a shell loop silently dropping the last line of
      a file with no trailing newline, a CI check whose "pass" branch was every kind of
      failure, a `FULL OUTER JOIN` counting one row as a break on both sides, and a header
      merge that discarded the caller's headers for two of three legal input shapes.
- [ ] **The recipe's own comments are checked against what the code does.** A comment
      asserting an invariant the code does not hold ("the key is never NULL here", "headers
      merge per-key") is worse than no comment: it stops the next reader looking.
- [ ] **Credentials, destructive operations, and deserialization are called out where they
      appear.** A session-scoped `drop_all`, a credential on a session that follows
      server-supplied URLs, and `joblib.load` on a settings path are each one line to guard
      and a bad afternoon to discover.

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
