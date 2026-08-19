# Claude Agent Skills Library

A career-portable library of [Claude Code Agent Skills](https://code.claude.com/docs/en/skills)
that make Claude a sharper partner for **decision-making, safe and reliable operations, writing
and communication, working with people, data analytics and BI, machine learning, coding and
autonomous agents, learning science, math foundations, continuous improvement, and deep
research**.

**121 active skills across 14 plugins.** Every skill is built to one house standard: it **does
the task step by step and teaches the reasoning**, so you get the deliverable *and* get better at
the work. Nothing in the active library is tied to one employer, product, or industry — the
domain-specific mounts live in each skill's `references/your-environment.md`, which is yours to
fill in.

> **On the name:** the marketplace ID is still `treasury-analyst-skills`. That is **deliberate,
> not an oversight** — it is kept so existing installs keep resolving. The library itself is
> general-use; the finance/Oracle/treasury plugins it was named for are archived (see
> [The archive](#the-archive)).

## Install

```
/plugin marketplace add CatCorner22/Claude_Skills_2
/plugin install decision-science-skills@treasury-analyst-skills
/plugin install coding-agent-skills@treasury-analyst-skills
# ...install whichever plugins you want
```

Installed skills are namespaced, e.g. `decision-science-skills:pre-mortem`. Type
`/<plugin>:<skill>` to invoke one directly, or just describe your task and Claude will pick it up.

### Install a subset — the full library does not fit comfortably

**Install the plugins you will actually use, not all fourteen.** Every installed skill's `name` and
`description` sit in the system prompt for the whole session, whether or not you use it. This
repo's own estimate, from `python3 scripts/measure-listing-cost.py` across all 121 skills:
**110,178 characters ≈ 29,796 tokens ≈ 14.90% of a 200K context** (tokens estimated at ~3.7
chars/token). That estimate has been cross-checked against the harness's own real tokenizer
(`claude plugin details <plugin>`, summed across all 14 plugins) and runs **~30% light**: the
real, tokenizer-computed cost is **≈38,800 tokens ≈ 19.4% of a 200K context**. Full measurement
and method: [`docs/live-routing-and-degradation-2026-08-18.md`](docs/live-routing-and-degradation-2026-08-18.md).
Re-run the script after any description change — the char-based figure is directional, not exact.

| Plugin | Skills | ~Tokens | % of 200K |
| --- | ---: | ---: | ---: |
| `coding-agent-skills` | 20 | 4,793 | 2.40% |
| `continuous-improvement-skills` | 16 | 4,038 | 2.02% |
| `decision-science-skills` | 15 | 3,937 | 1.97% |
| `data-analytics-bi-skills` | 11 | 2,757 | 1.38% |
| `safety-and-reliability-skills` | 10 | 2,587 | 1.29% |
| `full-stack-dev-skills` | 11 | 2,420 | 1.21% |
| `data-tools-skills` | 7 | 1,576 | 0.79% |
| `math-foundations-skills` | 6 | 1,561 | 0.78% |
| `machine-learning-skills` | 7 | 1,545 | 0.77% |
| `collaboration-skills` | 5 | 1,365 | 0.68% |
| `writing-skills` | 5 | 1,268 | 0.63% |
| `metacognition-skills` | 4 | 955 | 0.48% |
| `learning-skills` | 3 | 718 | 0.36% |
| `deep-research-skills` | 1 | 276 | 0.14% |
| **all 14** | **121** | **29,796** | **14.90%** |

There is a second, sharper reason to subset, and it is worse than a round "~100 skills" threshold
suggests. **The listing has a character budget**, and this library does not come close to fitting
it. Read from the shipped CLI: the budget is
`floor(context_tokens × 4 × skillListingBudgetFraction)`, which at the 200K/1% defaults is
**8,000 characters**. Rendering all 121 skills with descriptions needs **113,677** — about 14× the
budget. Under pressure every skill starts as a bare `- name` (5,575 chars for 121 of them) and is
upgraded back to its full description only while budget remains, in **descending order of recent
use** (`usageCount × max(0.5^(days/7), 0.1)`, so anything unused scores 0).

Simulated against this library's real descriptions: at a default 200K session, **3 of 121 skills
keep a description; 118 route on their bare name alone.** At 1M it is 38 of 121. `/plugin:skill`
direct invocation still works throughout — it is description-matching that stops.

The one piece of good news the mechanism gives you: because the ordering is usage-weighted, the
skills you actually use keep their descriptions, so the worst case is a *first* session on a fresh
install rather than the steady state. Full derivation, and a correction of an earlier and wronger
account of this same mechanism:
[`docs/live-routing-and-degradation-2026-08-18.md`](docs/live-routing-and-degradation-2026-08-18.md).

Practical guidance:

- **Two to four plugins (~24-31 skills, 3-4% of context)** is the sweet spot: comfortably below the
  point where any of this starts, and small enough that the router discriminates well.
- **Pick by the work you do**, not by breadth. Each bundle below is measured, not estimated:

| Bundle | Plugins | Skills | ~Tokens | % of 200K |
| --- | --- | ---: | ---: | ---: |
| Analyst | `data-analytics-bi-skills` + `data-tools-skills` + `math-foundations-skills` | 24 | 5,895 | 2.95% |
| Developer | `full-stack-dev-skills` + `coding-agent-skills` | 31 | 7,213 | 3.61% |
| Operations / process | `continuous-improvement-skills` + `safety-and-reliability-skills` | 26 | 6,624 | 3.31% |
| Management / communication | `collaboration-skills` + `writing-skills` + `decision-science-skills` | 25 | 6,569 | 3.28% |

  Note that a bundle's skills cross-reference skills in plugins you have not installed. Those
  pointers name the plugin (`other-plugin:skill`), so they read as "install that plugin if you want
  this" rather than as broken links — but they will not resolve until you do.
- **The lever is skills per install, not description length.** Trimming a description from 1,000 to
  900 characters saves ~27 tokens; skipping a 15-skill plugin saves ~3,900. Descriptions here are
  kept tight because a tight description *routes* better, not because trimming buys back context.
- Swapping plugins between sessions is cheap. Install narrowly and add what you find yourself
  reaching for.

## Plugins

| Plugin | Skills | What it covers |
| --- | --- | --- |
| `decision-science-skills` | 15 | Structured judgment: competing hypotheses, reference-class forecasting, pre-mortem, after-action review, tabletop wargaming, principled negotiation, systems thinking, Bayesian updating, weak-signal navigation, revision review, plus the fiction-anchored set (no-win drills, Ulysses pact, Rashomon, minority report) |
| `safety-and-reliability-skills` | 10 | High-hazard-industry methods for ordinary work: checklist design, bowtie/HAZOP barrier analysis, SBAR + PACE communication, reliability math, design-basis review, break-glass playbooks, detection tuning, rebuild rehearsal, selection by lot, tamper-evident records |
| `continuous-improvement-skills` | 16 | Lean / TPS / Six Sigma / co-design: VSM, root-cause analysis, DMAIC, standard work, A3, kaizen, plus the IE methods set (FMEA, theory of constraints, DOE, EVOP, MSA, QFD) and personal WIP limits |
| `collaboration-skills` | 5 | Working with humans: meeting design, feedback that lands, executive briefing (BLUF/SCQA), stakeholder mapping, and eliciting what people know but haven't said |
| `writing-skills` | 5 | Registers and explanation craft: smart-brevity professional writing, plain-grade accessible writing, explanation design (analogy + teach-back), and Diátaxis-routed technical documentation |
| `data-analytics-bi-skills` | 11 | SQL, exploratory analysis, cleaning, statistics and inference, dashboard design, spreadsheet modeling, plus causal inference, A/B test design, and survey & sampling design |
| `data-tools-skills` | 7 | Data plumbing: Excel automation with Python, CSV/flat-file wrangling, DuckDB local analytics, PDF extraction, REST API pulls, file hygiene, reproducible analysis |
| `machine-learning-skills` | 7 | Practical ML: project framing, feature engineering, supervised modeling, evaluation, time-series forecasting, anomaly detection, bespoke LLM architecture (PEFT/QLoRA) |
| `math-foundations-skills` | 6 | Domain-neutral math: number sense and Fermi estimation, percentages, algebra and formula rearrangement, units and dimensional analysis, exponential growth and logs, probability fundamentals |
| `coding-agent-skills` | 20 | Python, Claude Code harness config, agent design, prompt engineering, git and code review, skill authoring, software archaeology, defect epidemiology, the Board of Advisors review swarm, and expert personas |
| `full-stack-dev-skills` | 11 | Lean full-stack development: architecture, FastAPI backends, databases/ORM, dynamic frontends, realtime, ML in production, testing strategy, deploy and operate, evidence-based UI/UX inspection |
| `metacognition-skills` | 4 | Cumulative improvement across sessions: hierarchical memory management, reflective learning, adaptive analysis, knowledge crystallization |
| `learning-skills` | 3 | Learning science applied: spaced retrieval practice, deliberate practice, habit design |
| `deep-research-skills` | 1 | Multi-database literature investigation with source-provenance control, evidence appraisal, and triple-checked citations (includes the medical-research-detective) |

## Finding the right skill

- **[`docs/INDEX.md`](docs/INDEX.md) — the quick router.** Grouped by category, it gives every
  skill's *when to use*, *what it's optimized for*, and *how to trigger* it in one table per
  plugin. Start here when you know the problem but not the skill.
- **[`docs/SKILLS.md`](docs/SKILLS.md) — the full catalog.** Every skill, what it does, and the
  exact trigger phrases.

Both files are **generated** by `python3 scripts/gen-catalog.py` from skill frontmatter — never
hand-edit them; regenerate after any skill change.

Design notes and the wave-by-wave build log live in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## The archive

**There are no archived plugins.** Nine domain plugins were delisted in 2026-08 when the library
was re-aimed at general use, and all nine were then **deleted outright** on owner direction: the
two Oracle Fusion / OTBI plugins (17 skills, 70 files) and the seven finance/treasury plugins —
cash-management, treasury-accounting, public-sector-treasury, sponsored-projects AR, accounting,
banking, finance (49 skills, 154 files). Git history still contains them; nothing else does.
Locally installed copies keep working as version-pinned snapshots, but they will never update and
no longer appear in the marketplace listing.

What remains under [`archive/`](archive/README.md) is two individual dental-mounted skills
(preserved with a restore procedure) and a set of standalone applications that predate the
re-aim. [`archive/README.md`](archive/README.md) carries the manifest of what was deleted and
why.

## How it's built

- One repo that is both a **plugin marketplace** (`.claude-plugin/marketplace.json`) and the home
  for fourteen **plugins** under `plugins/`, mirroring Anthropic's own
  [`anthropics/skills`](https://github.com/anthropics/skills) layout.
- One plugin ships **subagents**: `coding-agent-skills` carries six read-only specialist reviewers
  in its `agents/` folder (performance, accuracy/correctness, structure/architecture,
  clarity/maintainability, robustness/edge-cases, and the board-chair synthesizer). After install
  they appear in `/agents` namespaced as `coding-agent-skills:<name>`, orchestrated by the
  `coding-agent-skills:board-review` skill.
- The authoring standard lives in the `coding-agent-skills:writing-agent-skills` skill; its
  template is `plugins/coding-agent-skills/skills/writing-agent-skills/assets/SKILL.template.md`.
- `bash scripts/validate.sh` lints every skill and manifest (currently 0 errors). It also runs
  `scripts/check-arithmetic.py`, which recomputes every worked `a = b = c` chain in the library
  and fails on the ones that disagree — the defect class that survived four hand review passes.
- `python3 scripts/gen-catalog.py` regenerates `docs/SKILLS.md` and `docs/INDEX.md` from the skills
  themselves — never edit those two by hand.
- **[`docs/trigger-test.md`](docs/trigger-test.md) — routing compliance.** Validation proves a skill
  is well-formed; it cannot prove the skill is *findable*, because routing depends only on the
  description. The protocol has now been run three times — twice as a blind simulation and once
  live against the real harness (`docs/trigger-test-results.md`,
  `docs/trigger-test-tier-d-rerun.md`, `docs/live-routing-and-degradation-2026-08-18.md`). The live
  run is the one that matters, and it found that fixes verified under a full listing fail once the
  listing is degraded. Coverage is still partial, so this remains recorded as **partially met**
  rather than assumed passing.

## Recommended companion marketplaces

These skills complement (and deliberately don't duplicate) Anthropic's own marketplace:

- [`anthropics/skills`](https://github.com/anthropics/skills) — install `document-skills` for
  polished .xlsx/.pdf/.docx/.pptx document *creation* (source-available, first-party), and
  `skill-creator`/`mcp-builder` for tooling. Our `data-tools-skills` covers the scripting side
  (pandas/openpyxl automation, extraction, local SQL) and points to the official document skills
  where they're the better fit.

The gap this library fills is the **method-and-reasoning layer** above any particular product: how
to frame the decision, design the test, run the review, structure the message, and make the
learning stick. Vendor marketplaces (Anthropic's, [`oracle/skills`](https://github.com/oracle/skills),
and others) cover their own tools; these skills cover the thinking you bring to whatever tool the
job hands you.

## Tailoring to your environment

Most skills leave a `references/your-environment.md` hook so they can fit your real systems,
processes, formats, and vocabulary — whatever role you're in. **Real data is never committed** —
sanitize it, and keep raw artifacts in `*.private.md` / `references/*.local.*` files, which
`.gitignore` keeps out of git.
