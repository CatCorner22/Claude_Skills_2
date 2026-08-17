---
name: writing-agent-skills
description: >-
  Authors and reviews Agent Skills (SKILL.md files) to this library's "do + teach"
  house standard and the open Agent Skills spec — correct frontmatter, discoverable
  descriptions, progressive disclosure, and privacy-safe tailoring. Use when creating
  a new skill, editing an existing one, reviewing a skill for quality, or setting up a
  new plugin in this repo. Triggers: write a skill, new skill, SKILL.md, authoring
  standard, skill description, add a skill, review a skill, do and teach.
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
Start by copying the template: `cp assets/SKILL.template.md plugins/<plugin>/skills/<name>/SKILL.md`
(the template lives in this skill's `assets/`).

### 2. Write compliant frontmatter
```yaml
---
name: <skill-name>        # MUST equal the folder name exactly
description: >-
  <what it does> — use when <trigger situations>. Triggers: <phrases the user says>.
---
```
Hard rules (validated by `scripts/validate.sh`):
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

### 5. Add the tailoring hook (privacy-safe)
Skills in this library are domain-neutral by design, and fit the user's real environment through
one file rather than through hard-coded domain content. Name the *kind* of artifact the skill
attaches to, not one employer's version of it — a recurring report and its source system, a
matter or case intake, an operational runbook, a service and its deploy path. In `## Tailor to
your environment`, instruct the user to drop their specifics into
`references/your-environment.md`, framed "wire in your current role here" so the skill survives
a job change. **Never commit raw real data.** Commit only sanitized, structural examples. Raw
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

### 8. Validate
Run `bash scripts/validate.sh` from the repo root, then `claude plugin validate plugins/<plugin>`.
Fix every warning before committing.

## Why / learn
Skills work by **progressive disclosure**: at startup Claude only sees each skill's `name` +
`description`, and matches your request against the `description` alone to decide whether to load
the body. So the description is a *discovery* tool, not documentation — that's why it must carry
the trigger phrases and be third-person (it is injected into the system prompt). Once loaded, the
body persists in context across the turn, so every line is a recurring cost: concise,
well-ordered instructions beat exhaustive ones.

**Know what the listing actually costs, because it decides whether your skill is findable at
all.** Measured in this library (2026-08-11): 121 skills' names + descriptions come to ~107,700
characters ≈ **29,000 tokens ≈ 14.6% of a 200K context**, at a mean of ~870 chars (~235 tokens)
per description — not the ~100 tokens per skill an earlier version of this section claimed. The
`Triggers:` lists alone are 22% of that spend. This has two consequences worth designing around:

- **The listing degrades before it errors.** Observed at roughly 100 installed skills: the
  listing trims the least-used skills' descriptions to **name-only**. Nothing fails loudly —
  `/plugin:skill` direct invocation keeps working, which is exactly the path an author testing
  their own skill uses, so the degradation is invisible from the inside. A trimmed skill's
  "Use when…" clause and every trigger phrase are simply absent from the router's context.
- **Therefore the name must carry task signal.** Under name-only trimming, a skill named for a
  metaphor or a persona is unroutable, while one named for its task survives. Evocative names are
  legitimate — this library has several by design, invoked deliberately — but a skill whose *only*
  intended path is automatic matching should be named for what it does.

The practical lever is **skills per install, not characters per description**. Trimming a
description from 1000 to 900 chars saves ~27 tokens; not installing a 15-skill plugin saves
~3,900. Keep descriptions tight because a tight one routes better, not because trimming solves
the budget. The fixed "do + teach" order exists
so that each skill reliably both produces the deliverable and leaves you understanding it — the
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

## References
- assets/SKILL.template.md — copy this to start any new skill
- references/frontmatter-rules.md — full frontmatter field reference and constraints
- references/review-checklist.md — the definition-of-done checklist for a finished skill

## Scripts
- `scripts/validate.sh` (at the repo root, not in this skill) lints every skill's structure and frontmatter.
