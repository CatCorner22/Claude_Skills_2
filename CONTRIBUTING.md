# Contributing to this skills library

## The one rule
Every skill follows the house **"do + teach"** standard, which is defined in
[`coding-agent-skills:writing-agent-skills`](plugins/coding-agent-skills/skills/writing-agent-skills/SKILL.md).
Read it (or invoke `/coding-agent-skills:writing-agent-skills`) before adding or editing a skill.
Start any new skill by copying
[`SKILL.template.md`](plugins/coding-agent-skills/skills/writing-agent-skills/assets/SKILL.template.md).

## Quick reference
- A skill = `plugins/<plugin>/skills/<skill-name>/SKILL.md` (+ optional `references/`, `assets/`, `scripts/`).
- Frontmatter: `name` (== folder name, lowercase-hyphen, no `claude`/`anthropic`) and a third-person
  `description` (≤ 1024 chars — a hard cap the validator errors on) that states **what + when** and
  ends with `Triggers:`. Past **973 chars** (within 5% of the cap) the validator emits a non-gating
  `NOTE`: the skill still passes, but any future edit to that description has to re-count before it
  overruns. Dozens of active descriptions sit in that band at any given time — `validate.sh`'s
  summary line reports the live note count, so read it rather than trusting a number written here.
- Body sections, in order: `When to use` → `Do it` → `Why / learn` → `Common mistakes` →
  `Tailor to your environment` → `References` → (optional) `Scripts`. Keep the body under 500 lines.
- Evals go in `evals/<plugin>/<skill>.md` (positive trigger, near-miss, quality rubric) — never in SKILL.md.
- Validate with `bash scripts/validate.sh` and `claude plugin validate plugins/<plugin>`.
  `validate.sh` calls `scripts/check-arithmetic.py`, so a worked example whose numbers do not
  add up now fails the build rather than waiting for a reviewer to catch it.
  Ship at **0 errors**; `NOTE` lines are informational.
- **Regenerate the catalog after any skill change:** `python3 scripts/gen-catalog.py` rewrites both
  [`docs/SKILLS.md`](docs/SKILLS.md) (full catalog) and [`docs/INDEX.md`](docs/INDEX.md) (the
  when-to-use / optimized-for / how-to-trigger router) from skill frontmatter. **Never hand-edit
  either file** — they are generated artifacts, and hand edits are silently destroyed on the next
  run. A skill change that isn't followed by a regen leaves the two published catalogs lying.
- **Bump the plugin's `version` in its `plugin.json` whenever its content changes** — installed
  copies only receive updates on a version bump (`claude plugin update` trusts the version).

## Privacy
Never commit real client, bank, or account data. Sanitize to structural examples; keep raw
artifacts in `*.private.md` or `references/*.local.*` (git-ignored).

## Build status (waves)
Current state: **121 active skills across 14 plugins** (plus 6 subagents, all in
`coding-agent-skills`). Nine domain plugins / 66 skills were archived in 2026-08, and the Oracle
and finance/treasury sets among them were then **deleted outright** on owner direction
(2026-08-18) — `archive/plugins/` no longer exists and they survive only in git history. Two
skills remain archived at skill level under [`archive/`](archive/README.md). `validate.sh` is clean —
0 errors, 0 warnings (the remaining `NOTE` lines are the non-gating near-cap description warnings).

Many waves have shipped since the original ten below: the **KSA waves A–D** (industrial
engineering, safety & reliability, decision science, and the Wave-D reference retrofits), the
**general-use expansion** (8 science/writing/communication/statistics skills), the **epic wave**
(12 cross-lane candidates), the **archive + consolidation pass** (domain plugins delisted,
`board-of-advisors-skills` merged, 2 dental-mounted skills archived), and **three review passes**
(adversarial review, text optimization, closing arithmetic audit) — all recorded in
[`docs/library-review-2026-08.md`](docs/library-review-2026-08.md).

### The original ten waves (day-job first)
Plugins marked **[archived]** were delisted when the library was re-aimed at general use, and the
Oracle and finance/treasury sets among them were later **deleted** on owner direction (2026-08-18).
They survive only in git history — see [`archive/README.md`](archive/README.md).

- **Wave 0 — Foundation:** ✅ repo scaffold, authoring standard + template, `bank-reconciliation`
  exemplar, validator.
- **Wave 1 — Day-job core:** ✅ `cash-management-skills` (6) **[archived]**, `oracle-otbi-skills`
  (5) **[archived]**, accounting core **[archived]**, `agent-harness-config`.
- **Wave 2 — Adjacent domains + analysis base:** ✅ `banking-skills` (6) **[archived]**,
  `finance-skills` (6) **[archived]**, accounting remainder **[archived]**, BI core.
- **Wave 3 — Advanced analytics + improvement + agents:** ✅ statistics,
  `machine-learning-skills` (6), `continuous-improvement-skills` (6), coding/agents remainder.
- **Wave 4 — Fusion Financials + data tools:** ✅ `oracle-fusion-finance-skills` (6)
  **[archived]**: GL/journals, FBDI, AP, AR, Cash Management module, period close;
  `data-tools-skills` (6): Excel automation, CSV wrangling, DuckDB, PDF extraction, REST API
  pulls, file hygiene.
- **Wave 5 — Advanced treasury & accounting ops:** ✅ `treasury-accounting-skills` (6)
  **[archived]**: debt facilities & covenants, hedging & derivatives, investment policy
  compliance, accruals & prepaids, intercompany accounting, audit readiness & PBC.
- **Wave 6 — Sponsored projects AR:** ✅ `sponsored-projects-ar-skills` (13) **[archived]**:
  master router, PPM-to-AR domain knowledge, unbilled/billed WIP reconciliation, revenue-to-billing
  reconciliation & GL tie-out, KPIs & trend forecasts, detailed aging & collections
  prioritization, reporting & recommendations, compliance risk & anomaly scanning, plus
  federal compliance — Uniform Guidance core, federal billing/cash management (LOC/PMS
  draws), effort reporting basics, cost allowability screening, and compliance/audit risk
  assessment.
- **Wave 8 — Board of Advisors:** ✅ shipped as `board-of-advisors-skills`: the `board-review`
  orchestration skill plus six read-only subagents (performance, accuracy/correctness,
  structure/architecture, clarity/maintainability, robustness/edge-cases, board-chair) in
  the plugin's `agents/` folder. **[merged]** — a one-skill plugin was pure install friction, so
  in the consolidation pass it was folded into `coding-agent-skills`: the skill is now
  `coding-agent-skills:board-review` and all six agents live in
  `plugins/coding-agent-skills/agents/`. Same content, new namespace; this is the only plugin
  that ships subagents.
- **Wave 7 — Full-stack development (completed after Wave 8):** ✅ `full-stack-dev-skills`
  (9): lean-code principles, app architecture, FastAPI backends, database/ORM, modern
  dynamic frontends, realtime features, ML in production, testing strategy, deploy &
  operate.
- **Wave 9 — Fusion Treasury Architect:** ✅ `fusion-treasury-architect` subagent (elite
  configuration-specific Oracle Fusion Financials/Treasury persona: FSM tasks, Redwood
  navigation, SLA, bank-file parsing, structured troubleshooting) + the
  `fusion-architect-consult` skill, added to `oracle-fusion-finance-skills`. **[deleted]** —
  both went with their host plugin in the Oracle deletion, so no subagent ships outside
  `coding-agent-skills` today.

Each plugin is independently installable and useful.

**Next.** The active library is general-use by standing directive — **no new content is built on
the archived finance/Oracle/treasury domains** (see [`CLAUDE.md`](CLAUDE.md)). Work from here goes
into: (1) the genuinely-unbuilt research tail (service-recovery, smed-setup-reduction,
queueing-methods, argument-and-fallacies — see [`docs/research/`](docs/research/), whose files
carry dated status blocks saying what shipped and what didn't); (2) depth on existing skills over
new-skill count, with an arithmetic-verification pass on every worked example and a
reciprocal-link pass on every new-skill wave (both standing lessons from the review waves); and
(3) role tailoring by whoever installs the library, through each skill's
`references/your-environment.md` — which is where role-specific systems, formats, and vocabulary
belong, never in the published skill body.
