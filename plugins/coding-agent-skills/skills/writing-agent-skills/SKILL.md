---
name: writing-agent-skills
description: >-
  Authors and reviews Agent Skills (SKILL.md files) to this library's "do + teach"
  house standard and the open Agent Skills spec — correct frontmatter, discoverable
  descriptions, progressive disclosure, and privacy-safe tailoring. Use when creating
  a new skill, editing an existing one, reviewing a skill for quality, or setting up a
  new plugin in this repo. Triggers: write a skill, new skill, SKILL.md, authoring
  standard, skill description, add a skill, review a skill, do and teach.
metadata:
  version: "1.2.0"
---

# Writing Agent Skills (house standard)

This is the single source of truth for how every skill in this library is built. When
you author or edit a skill here, follow this exactly. Copy `assets/SKILL.template.md`
as your starting point.

## When to use
- Creating a new skill in any plugin under `plugins/*/skills/`.
- Editing or reviewing an existing skill for quality/consistency.
- Adding a new plugin (needs a `.claude-plugin/plugin.json` and a `marketplace.json` entry).
- Not for: general prompt writing that is not a skill → see `coding-agent-skills:prompt-engineering`.

## Do it

### 1. Scaffold the folder
A skill is a directory whose name **is** the command:
```
plugins/<plugin>/skills/<skill-name>/
├── SKILL.md              # required
├── references/*.md       # optional, loaded on demand
├── assets/*              # optional, templates/boilerplate used in output
└── scripts/*             # optional, executed (never read into context)
```
Start by copying the template (run from the repo root; the source is addressed from the plugin
root, per §4b below):
```
mkdir -p plugins/<plugin>/skills/<name>
cp "${CLAUDE_PLUGIN_ROOT}/skills/writing-agent-skills/assets/SKILL.template.md" \
   plugins/<plugin>/skills/<name>/SKILL.md
```
(`cp` into a directory that does not exist yet fails with "No such file or directory", so the
`mkdir` is part of the step rather than an assumption about it.)

### 2. Write compliant frontmatter
```yaml
---
name: <skill-name>        # MUST equal the folder name exactly
description: >-
  <what it does> — use when <trigger situations>. Triggers: <phrases the user says>.
---
```
Hard rules (the `name` shape and the 1024-char cap are enforced by `scripts/validate.sh`; third
person, the `Triggers:` ending, and leading with the primary use case are enforced by review — see
`references/review-checklist.md`) — the full field reference, the optional fields,
the `metadata` house convention, and the measured description-budget reality are in
`references/frontmatter-rules.md`; read it before your first skill and whenever you reach for a
field not listed here:
- `name`: 1–64 chars, lowercase letters/digits/hyphens only, no leading/trailing/consecutive
  hyphens, **must equal the folder name**, must **not** contain the words `anthropic` or `claude`.
- `description`: non-empty, **≤ 1024 characters**, written in the **third person**, states
  **both what the skill does and when to use it**, and ends with a short `Triggers:` list of
  the exact phrases a user would say. Lead with the primary use case. Be slightly "pushy" so the
  skill triggers when it should — under-triggering is the common failure.

### 3. Write the body in the fixed section order
Every skill uses these H2 sections, in this order (omit only `scripts` when none is bundled):
1. `## When to use` — expand the description; include a "Not for: … → see `plugin:other-skill`" line.
2. `## Do it` — **the "do."** Numbered, procedural steps that actually accomplish the task.
   Match detail to fragility: prose for judgment calls; exact commands, column maps, or a bundled
   script for fragile/consistency-critical steps.
3. `## Why / learn` — **the "teach."** The mental model and the reasoning behind the steps, in
   plain language. Explain *why*, never bark "MUST/NEVER." This is what makes the user better.
4. `## Common mistakes` — pitfall → fix, one line each.
5. `## Tailor to your environment` — how to point the skill at the user's real artifacts via
   `references/your-environment.md` (see §5 on privacy).
6. `## References` — bullet links to `references/*.md` (one level deep only).
7. `## Scripts` *(optional)* — one line per bundled script: how to run it and what it outputs.

### 4. Keep it small (progressive disclosure)
- `SKILL.md` body **under 500 lines**; it is a table of contents, not a textbook.
- Push depth into `references/<topic>.md` — loaded only when read, so unread files cost zero tokens.
- Keep references **one level deep** (SKILL.md → reference.md; never reference → sub-reference).
- Add a short TOC to any reference file over ~100 lines so partial reads still reveal scope.
- Use forward slashes in every path.

### 4b. Write every path for the *installed* shape, not this repo
A skill is authored in this repo but runs from a plugin cache, with the user's own project as the
working directory. So **any path a skill tells the user to run or read must be addressed from
`${CLAUDE_PLUGIN_ROOT}`** — the plugin's installed root — never relative to the marketplace repo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill-name>/scripts/<script>.py" <args>
```

A bare `python scripts/thing.py` works for you and is a guaranteed file-not-found for everyone
else. The same applies to anything you tell the user to *write*: `references/your-environment.md`
lives inside the plugin cache, so a `/plugin marketplace update` can discard it — say so, and
prefer having the user keep their real specifics in their own project.

This rule exists because every quality gate in this repo — `validate.sh`, `gen-catalog.py`, every
review — operates on the *repository*, and the repository is not the product. Nothing here can
see the installed artifact, so path correctness is on the author.

### 5. Add the tailoring hook (privacy-safe)
Skills in this library are domain-neutral by design, and fit the user's real environment through
one file rather than through hard-coded domain content. Name the *kind* of artifact the skill
attaches to, not one employer's version of it — a recurring report and its source system, a
matter or case intake, an operational runbook, a service and its deploy path. In `## Tailor to
your environment`, instruct the user to drop their specifics into
`references/your-environment.md`, framed "wire in your current role here" so the skill survives
a job change. **Then tell them to keep the filled-in copy outside the plugin** — the shipped file is
a template living in the plugin cache, which `/plugin marketplace update` can overwrite; the house
wording points them at `.claude/skills-env/<skill-name>.md` in their own project. Every skill in this
library carries that paragraph; copy it verbatim. **Never commit raw real data.** Commit only sanitized, structural examples. Raw
artifacts go in files matching `.gitignore` patterns (`*.private.md`,
`references/*.local.*`).

### 6. Write evals (do not put them in SKILL.md)
Create `evals/<plugin>/<skill>.md` with at least three scenarios:
1. A **positive-trigger** prompt that should load the skill.
2. A **near-miss** prompt that should *not* load it (guards over-triggering).
3. A **quality rubric**: does the output both *do* the task and *teach* the reasoning?

### 7. Register a new plugin (only when adding one)
- Create `plugins/<plugin>/.claude-plugin/plugin.json` with `{ name, description, version }`.
- Add an entry to `.claude-plugin/marketplace.json` (`name`, `source: "./plugins/<plugin>"`,
  `description`, `category`). Do not put `version` in both files — `plugin.json` wins.

### 8. Validate, then work the definition-of-done checklist
Run `bash scripts/validate.sh` from the repo root, then `claude plugin validate plugins/<plugin>`.
Fix every warning before committing. **Then open `references/review-checklist.md` and work it
line by line** — the validator only checks what a script can see (frontmatter shape, body
length, cross-link resolution; it does *not* check that the seven sections are present or in
order). The checklist carries the guards that a script cannot: the
arithmetic-verification pass on every worked example, the reciprocal-link pass on the *older*
side of every new seam, the trigger-collision scan, and the fresh-session trigger test. Every
defect class that has survived a review in this library's history was one the validator was
structurally unable to catch, and is now a line on that checklist.

## Why / learn
Skills work by **progressive disclosure**: at startup Claude only sees each skill's `name` +
`description`, and matches your request against the `description` alone to decide whether to load
the body. So the description is a *discovery* tool, not documentation — that's why it must carry
the trigger phrases and be third-person (it is injected into the system prompt). Once loaded, the
body persists in context across the turn, so every line is a recurring cost: concise,
well-ordered instructions beat exhaustive ones.

**Know what the listing actually costs, because it decides whether your skill is findable at
all.** Measured in this library by `python3 scripts/measure-listing-cost.py`: 121 skills' names +
descriptions come to **≈110,000 characters ≈ 29,700 tokens ≈ 14.9% of a 200K context**, at a mean of
~890 chars (~240 tokens) per description — not the ~100 tokens per skill an earlier version of this section claimed.
That script counts characters and divides by ~3.7 chars/token, and the estimate runs **~30% light**
against the harness's own tokenizer: summing `claude plugin details <plugin>` across all 14 plugins
gives **≈38,800 tokens ≈ 19.4% of a 200K context**, which is the number to plan an install against
(method in `docs/live-routing-and-degradation-2026-08-18.md`). Figures are quoted to two or three
significant digits on purpose — they move with every description edit, so re-run the script
rather than trusting a number written down here. The `Triggers:` lists alone are 22% of that
spend. This has two consequences worth designing around:

- **The listing degrades before it errors, and the trigger is a character budget, not a skill
  count.** The budget is `floor(context_tokens × 4 × skillListingBudgetFraction)` — **8,000
  characters** at the 200K/1% defaults. Over budget, every non-bundled skill drops to a bare
  `- name` and is then upgraded back to its full description in **descending order of recent use**
  (`usageCount × max(0.5^(daysSinceUse/7), 0.1)`, so a never-used skill scores 0), greedily,
  skipping whatever no longer fits. Bundled skills are protected and never compete. Nothing fails
  loudly — `/plugin:skill` direct invocation keeps working, which is exactly the path an author
  testing their own skill uses, so the degradation is invisible from the inside. A trimmed skill's
  "Use when…" clause and every trigger phrase are simply absent from the router's context.
  Run `scripts/simulate-listing-budget.py` to see where your own library lands; for reference,
  this one needs ≈113,700 characters for 121 descriptions and keeps **3** at the default budget.
- **Therefore the name must carry task signal.** Under name-only trimming, a skill named for a
  metaphor or a persona is unroutable, while one named for its task survives. Evocative names are
  legitimate — this library has several by design, invoked deliberately — but a skill whose *only*
  intended path is automatic matching should be named for what it does.
- **A brand-new skill starts at the back of the queue.** Because the ranking is by *recent use*
  and an unused skill scores exactly zero, a skill you just wrote is among the first to lose its
  description on a crowded install — and it stays there until someone invokes it by name enough
  times to earn a place. Ship new skills with a name that routes on its own, and expect the
  description to be doing nothing for you in a large library until the skill has a usage history.

The practical lever is **skills per install, not characters per description**. Trimming a
description from 1000 to 900 chars saves ~27 tokens; not installing a 15-skill plugin saves
~3,700 (15 × the 910-char name+description mean, at 3.7 chars/token). Keep descriptions tight
because a tight one routes better, not because trimming solves the budget. The fixed "do + teach"
order exists so that each skill reliably both produces the deliverable and leaves you
understanding it — the
whole point of this library. Setting *degrees of freedom* to match fragility (loose prose vs. exact
scripts) keeps Claude accurate on the steps that break easily while staying flexible where judgment
helps.

## Common mistakes
- Vague description ("helps with reports") → the skill never triggers. Name the task and the triggers.
- Putting "claude" or "anthropic" in the skill `name` → invalid; the validator rejects it.
- `name` not matching the folder → the skill loads under the folder name and the mismatch confuses tooling.
- Dumping a textbook into SKILL.md → blows the context budget. Move depth into `references/`.
- Nested references (SKILL.md → a.md → b.md) → Claude may only partially read b.md. Keep it one level.
- Committing real client/bank data → privacy breach. Sanitize; keep raw data in `.gitignore`d files.
- Writing evals inside SKILL.md → they load every time and waste context. Keep them in `evals/`.

## Tailor to your environment
If you adopt house conventions of your own (naming, extra sections), record them in
`references/your-environment.md` here so future skills follow them. Keep this meta-skill and the
`assets/SKILL.template.md` in sync — the template must always reflect the current standard.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/writing-agent-skills.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- assets/SKILL.template.md — copy this to start any new skill
- references/frontmatter-rules.md — full frontmatter field reference and constraints (read at §2)
- references/review-checklist.md — the definition-of-done checklist for a finished skill (worked at §8)
- references/your-environment.md — your own house conventions: naming, provenance marks,
  versioning, review depth by skill type (fill in; the `.private.md` twin is git-ignored)

## Scripts
- `scripts/validate.sh` (at the repo root, not in this skill) lints every skill's structure and frontmatter.
