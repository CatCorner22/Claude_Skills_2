# Claude Agent Skills Library

A career-portable library of [Claude Code Agent Skills](https://code.claude.com/docs/en/skills)
that make Claude a sharper partner for **decision-making, safe and reliable operations, writing
and communication, working with people, data analytics and BI, machine learning, coding and
autonomous agents, learning science, math foundations, continuous improvement, and deep
research**.

**71 active skills across 13 plugins — consolidated 2026-08-23 from 121.** Every skill here
survived a blank-slate review against one test: *does invoking it beat an unaided, competent
frontier model?* The 50 that did not — competent summaries of canon a strong model reproduces
unaided — are archived, restorable with one `git mv` (see `archive/README.md`). Every survivor
is built to one house standard: it **does the task step by step and teaches the reasoning**, so
you get the deliverable *and* get better at the work. Nothing in the active library is tied to one employer, product, or industry — the
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

### Install a subset — and there are named profiles

**Install the plugins you will actually use, not all thirteen.** Every installed skill's `name` and
`description` sit in the system prompt for the whole session, whether or not you use it. This
repo's own estimate, from `python3 scripts/measure-listing-cost.py` across all 71 skills:
**64,136 characters ≈ 17,334 tokens ≈ 8.7% of a 200K context** (tokens estimated at ~3.7
chars/token; the harness's real tokenizer has historically run ~30% heavier than this estimate, so
budget ~22.5K tokens ≈ 11%). Re-run the script after any description change.

| Plugin | Skills | ~Tokens | % of 200K |
|---|---|---|---|
| `decision-science-skills` | 10 | 2,628 | 1.31% |
| `coding-agent-skills` | 10 | 2,454 | 1.23% |
| `full-stack-dev-skills` | 10 | 2,149 | 1.07% |
| `continuous-improvement-skills` | 7 | 1,750 | 0.88% |
| `safety-and-reliability-skills` | 6 | 1,617 | 0.81% |
| `data-analytics-bi-skills` | 6 | 1,527 | 0.76% |
| `machine-learning-skills` | 6 | 1,326 | 0.66% |
| `data-tools-skills` | 5 | 1,044 | 0.52% |
| `writing-skills` | 4 | 1,009 | 0.50% |
| `metacognition-skills` | 3 | 737 | 0.37% |
| `collaboration-skills` | 2 | 549 | 0.27% |
| `deep-research-skills` | 1 | 276 | 0.14% |
| `math-foundations-skills` | 1 | 267 | 0.13% |
| **all 13** | **71** | **17,334** | **8.67%** |

**Install profiles** — curated bundles matched to a working day, with their measured cost. Usage
decay rewards a coherent working set: a profile keeps one warm cluster of skills defending its own
listing slots, where a scattershot install decays everything equally.

| Bundle | Plugins | Skills | ~Tokens | % of 200K |
|---|---|---|---|---|
| Analyst | `data-analytics-bi-skills` + `data-tools-skills` + `math-foundations-skills` | 12 | 2,838 | 1.42% |
| Developer | `full-stack-dev-skills` + `coding-agent-skills` | 20 | 4,603 | 2.30% |
| Operations / process | `continuous-improvement-skills` + `safety-and-reliability-skills` | 13 | 3,368 | 1.68% |
| Management / communication | `collaboration-skills` + `writing-skills` + `decision-science-skills` | 16 | 4,186 | 2.09% |


There is a second, sharper reason to subset, and it is worse than a round "~100 skills" threshold
suggests. **The listing has a character budget**, and this library does not come close to fitting
it. Read from the shipped CLI: the budget is
`floor(context_tokens × 4 × skillListingBudgetFraction)`, which at the 200K/1% defaults is
**8,000 characters**. Rendering all 71 skills with descriptions needs **64,136** — about 8× the
budget. Under pressure every skill starts as a bare `- name` and is
upgraded back to its full description only while budget remains, in **descending order of recent
use** (`usageCount × max(0.5^(days/7), 0.1)`, so anything unused scores 0).

Simulated against this library's real descriptions: at a default 200K session, **5 of 71 skills
keep a description; 66 route on their bare name alone** (the consolidation nearly doubled
survival — it was 3 of 121). At 1M it is 40 of 71, and a two-plugin profile install keeps
essentially every description. `/plugin:skill` direct invocation still works throughout — it is
description-matching that stops.

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
| `decision-science-skills` | 10 | Structured judgment: pre-mortem (with the counsel rail), tabletop wargaming and no-win drills under full exercise control, weak-signal navigation, Bayesian updating via natural frequencies, reference-class forecasting, competing hypotheses analysis, minority-report dissent capture, the Rashomon protocol, The Challenger |
| `coding-agent-skills` | 10 | Skill authoring (the house standard), prompt engineering with the injection-defense doctrine, git/code review with run-verified agent traps, the Board of Advisors review swarm (+6 subagents), defect epidemiology, rule stress-testing, software archaeology, Comrade Engineer's pencil pass, The Foreman, and Chicken Little (Aether) with its deploy-advisor / deploy-compiler autopsy modes |
| `full-stack-dev-skills` | 10 | Lean full-stack development: architecture, FastAPI backends (+ the production Python toolchain standard), databases/ORM, dynamic frontends, realtime, ML in production, testing strategy, deploy and operate, evidence-based UI/UX inspection |
| `continuous-improvement-skills` | 7 | The improvement methods with teeth: DMAIC (worked control-chart project), FMEA (evidence-gated Action Priority), MSA extended to LLM-as-judge gauge studies, DOE, EVOP, root-cause analysis, project command center |
| `safety-and-reliability-skills` | 6 | Split-tally evidence design (litigation-hold rail), detection-system tuning by disposition audit, reliability math incl. probability-of-failure-on-demand, rebuild rehearsal (irreversibility screen), break-glass playbooks, hash-rank sortition review |
| `data-analytics-bi-skills` | 6 | Statistical inference, causal inference (DAGs, DiD/IV/RDD), A/B test design, survey & sampling design, spreadsheet modeling, assertion-evidence decks with a build-and-lint toolchain |
| `machine-learning-skills` | 6 | Practical ML: project framing, feature engineering, supervised modeling, evaluation, horizon-aware time-series forecasting, anomaly detection |
| `data-tools-skills` | 5 | Data plumbing that survives real files: DuckDB local analytics, PDF extraction, REST API pulls, CSV/flat-file wrangling, file hygiene |
| `writing-skills` | 4 | Registers and explanation craft: smart-brevity professional/legal writing (risk-allocation carve-outs included), plain-grade accessible writing, explanation design, Diátaxis-routed technical documentation |
| `metacognition-skills` | 3 | Cumulative improvement across sessions: hierarchical memory management, reflective learning, knowledge crystallization |
| `collaboration-skills` | 2 | Disarming elicitation (the counter-elicitation stance inverted, with its honesty rails) and meeting design (decisions as owner-and-date read-backs) |
| `deep-research-skills` | 1 | Multi-database literature investigation with source-provenance control, evidence appraisal, and triple-checked citations (the medical-research-detective) |
| `math-foundations-skills` | 1 | Units and dimensional analysis — the one basic-math skill that catches real errors; the rest of the set is archived |

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
  for thirteen **plugins** under `plugins/`, mirroring Anthropic's own
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

### Reading the provenance marks

External claims in these skills carry a bracketed mark saying how well the claim was checked.
They are there so you can tell a verified figure from a remembered one without opening the
source yourself:

| Mark | Means |
|---|---|
| `[snippet-only]` | Taken from search snippets; the primary source was not opened. `, cross-checked` or `, ×N` means that many independent snippets agreed |
| `[canon attribution]` | Named to the source everyone cites for it, not independently re-verified |
| `[background — verify]` | General knowledge, stated for orientation — confirm before relying on it |
| `[unverified]` | A specific value that could not be confirmed. No number is quoted beside this mark, deliberately |
| `[rule text]` | Quoted or closely paraphrased from a named statute, rule, or standard, with its jurisdiction stated |

An unmarked factual claim should be one you can check from the skill itself — a worked
example's arithmetic, a code path, a definition. If you find an unmarked external statistic,
that is a defect worth reporting.

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
