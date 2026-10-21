# Claude Agent Skills Library

A career-portable library of [Claude Code Agent Skills](https://code.claude.com/docs/en/skills)
that make Claude a sharper partner for **decision-making, safe and reliable operations, writing
and communication, working with people, data analytics and BI, machine learning, coding and
autonomous agents, learning science, math foundations, continuous improvement, and deep
research**.

**80 active skills across 14 plugins — consolidated 2026-08-23 from 121, with deep-research and legal additions since.** Every skill here
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

**Working inside this repo? Run the bootstrap — nothing happens on its own.**

```
bash scripts/bootstrap-plugins.sh                              # all 14
bash scripts/bootstrap-plugins.sh deep-research-skills         # or just what you need
```

`.claude/settings.json` declares the marketplace and marks all 14 plugins enabled, and **that
configuration is inert until the marketplace is registered.** Verified against a clean HOME: a
fresh clone with those settings in place reports `No plugins installed`, so every skill in the
library is *absent* from that session — not trimmed to a bare name, absent. Registering the
marketplace is not sufficient either, because `enabledPlugins` does not trigger an install. The
script does both halves, is idempotent, and verifies afterwards that the plugins are being read
from your checkout rather than from a stale cache. *(An earlier version of this paragraph claimed
the settings file installs the plugins or prompts you on first open. It does not, and that
mistaken belief is how a session ends up unable to find any skill in this library.)*

It registers **this checkout** as a directory marketplace, so there is no network dependency and
what loads is the tree you are editing. The GitHub form below is for installing somewhere you have
not cloned.

**Anywhere else**, install globally. Run `python3 scripts/measure-listing-cost.py` for what the
full set currently costs — and read the subset section below before defaulting to all 14, because
the listing budget bites well before the context does:

```
/plugin marketplace add CatCorner22/Claude_Skills_2
/plugin install coding-agent-skills@treasury-analyst-skills
/plugin install collaboration-skills@treasury-analyst-skills
/plugin install continuous-improvement-skills@treasury-analyst-skills
/plugin install data-analytics-bi-skills@treasury-analyst-skills
/plugin install data-tools-skills@treasury-analyst-skills
/plugin install decision-science-skills@treasury-analyst-skills
/plugin install deep-research-skills@treasury-analyst-skills
/plugin install full-stack-dev-skills@treasury-analyst-skills
/plugin install machine-learning-skills@treasury-analyst-skills
/plugin install math-foundations-skills@treasury-analyst-skills
/plugin install metacognition-skills@treasury-analyst-skills
/plugin install safety-and-reliability-skills@treasury-analyst-skills
/plugin install writing-skills@treasury-analyst-skills
```

Installed skills are namespaced, e.g. `decision-science-skills:pre-mortem`. Type
`/<plugin>:<skill>` to invoke one directly, or just describe your task and Claude will pick it up.

### Install a subset — and there are named profiles

**Install the plugins you will actually use, not all fourteen.** Every installed skill's `name` and
`description` sit in the system prompt for the whole session, whether or not you use it. Run
`python3 scripts/measure-listing-cost.py` for the current figure rather than trusting one written
down here — figures quoted in prose go stale silently, and this paragraph used to carry three that
had (a skill count, a character total and a tokenizer correction factor whose cross-check no longer
reproduces).

**The binding limit is not the context window, it is the skill-listing budget** — about 8,000
characters at the defaults. The full library overruns it, so most skills reach the session as a
bare `- name` with no description and no trigger phrases, and **automatic matching cannot route to
a trimmed skill.** It stays invocable by its full address (`/deep-research-skills:dna-raw-data-audit`),
which is the reliable way to reach any skill regardless. Which skills survive trimming is not
predictable: the order is by recent use, so two sessions on the same install keep different ones.
`python3 scripts/simulate-listing-budget.py` shows the shape of it, but it under-predicts how many
survive — use it comparatively, not as a promise.

| Plugin | Skills | ~Tokens | % of 200K |
|---|---|---|---|
| `coding-agent-skills` | 13 | 3,274 | 1.64% |
| `decision-science-skills` | 10 | 2,628 | 1.31% |
| `full-stack-dev-skills` | 10 | 2,149 | 1.07% |
| `continuous-improvement-skills` | 7 | 1,750 | 0.88% |
| `safety-and-reliability-skills` | 6 | 1,617 | 0.81% |
| `data-analytics-bi-skills` | 6 | 1,527 | 0.76% |
| `machine-learning-skills` | 6 | 1,326 | 0.66% |
| `writing-skills` | 4 | 1,052 | 0.53% |
| `data-tools-skills` | 5 | 1,044 | 0.52% |
| `legal-skills` | 3 | 808 | 0.40% |
| `deep-research-skills` | 4 | Deep research with source-provenance control: multi-database literature investigation (medical-research-detective), video claims audited against the sources they cite (video-source-audit), a personal genome audited against the literature (dna-raw-data-audit), and the same genome turned into an evidenced ancestry story with open-tool haplogroup calls, proof-standard genealogy and lineage maps (dna-ancestry-research) |
| `metacognition-skills` | 3 | 737 | 0.37% |
| `deep-research-skills` | 4 | 1,014 | 0.51% |
| `collaboration-skills` | 2 | 549 | 0.27% |
| `math-foundations-skills` | 1 | 267 | 0.13% |
| **all 14** | **80** | **19,744** | **9.87%** |

**Install profiles** — curated bundles matched to a working day, with their measured cost. Usage
decay rewards a coherent working set: a profile keeps one warm cluster of skills defending its own
listing slots, where a scattershot install decays everything equally.

| Bundle | Plugins | Skills | ~Tokens | % of 200K |
|---|---|---|---|---|
| Analyst | `data-analytics-bi-skills` + `data-tools-skills` + `math-foundations-skills` | 12 | 2,838 | 1.42% |
| Developer | `full-stack-dev-skills` + `coding-agent-skills` | 23 | 5,424 | 2.71% |
| Operations / process | `continuous-improvement-skills` + `safety-and-reliability-skills` | 13 | 3,368 | 1.68% |
| Management / communication | `collaboration-skills` + `writing-skills` + `decision-science-skills` | 16 | 4,229 | 2.11% |


There is a second, sharper reason to subset, and it is worse than a round "~100 skills" threshold
suggests. **The listing has a character budget**, and this library does not come close to fitting
it. Read from the shipped CLI: the budget is
`floor(context_tokens × 4 × skillListingBudgetFraction)`, which at the 200K/1% defaults is
**8,000 characters**, and rendering the whole library with descriptions needs roughly eight times
that (`python3 scripts/measure-listing-cost.py` for today's figure). Under pressure every skill
starts as a bare `- name` and is upgraded back to its full description only while budget remains,
in **descending order of recent use** (`usageCount × max(0.5^(days/7), 0.1)`, so anything unused
scores 0).

**Measured in a real session on a full install: 22 skills kept a description and 52 arrived
name-only.** Two sessions on the same library kept a *different* 22, which is the ordering doing
exactly what it says — so the count is stable and the membership is not predictable at all.
`scripts/simulate-listing-budget.py` models this, and **under-predicts by about four times** (it
said 5 would survive where 22 did), so read it comparatively — how much worse a bigger install
gets, how much a 1M context buys — and never as a promise about a particular skill. A two-plugin
profile keeps essentially every description. `/plugin:skill` direct invocation works throughout —
it is description-matching that stops, which is why a skill you rely on is worth invoking by its
full address.

The one piece of good news the mechanism gives you: because the ordering is usage-weighted, the
skills you actually use keep their descriptions, so the worst case is a *first* session on a fresh
install rather than the steady state. Full derivation, and a correction of an earlier and wronger
account of this same mechanism:
[`docs/live-routing-and-degradation-2026-08-18.md`](docs/live-routing-and-degradation-2026-08-18.md).

Practical guidance:

- **Two to four plugins (~12-23 skills, under 3% of context)** is the sweet spot: comfortably below the
  point where any of this starts, and small enough that the router discriminates well.
- **Pick by the work you do**, not by breadth. Each bundle below is measured, not estimated:

| Bundle | Plugins | Skills | ~Tokens | % of 200K |
| --- | --- | ---: | ---: | ---: |
| Analyst | `data-analytics-bi-skills` + `data-tools-skills` + `math-foundations-skills` | 12 | 2,838 | 1.42% |
| Developer | `full-stack-dev-skills` + `coding-agent-skills` | 23 | 5,424 | 2.71% |
| Operations / process | `continuous-improvement-skills` + `safety-and-reliability-skills` | 13 | 3,368 | 1.68% |
| Management / communication | `collaboration-skills` + `writing-skills` + `decision-science-skills` | 16 | 4,229 | 2.11% |

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
| `coding-agent-skills` | 13 | Skill authoring (the house standard), prompt engineering with the injection-defense doctrine, git/code review with run-verified agent traps, the Board of Advisors review swarm (+6 subagents), defect epidemiology, rule stress-testing, software archaeology, Comrade Engineer's pencil pass, The Foreman, the Creative Workaround Genius (another route when the obvious one fails), the project manager and QC gate (requirement ledger and exhaustive sweep, with its own subagent), fitness and nutrition science, and Chicken Little (Aether) with its deploy-advisor / deploy-compiler autopsy modes |
| `full-stack-dev-skills` | 10 | Lean full-stack development: architecture, FastAPI backends (+ the production Python toolchain standard), databases/ORM, dynamic frontends, realtime, ML in production, testing strategy, deploy and operate, evidence-based UI/UX inspection |
| `continuous-improvement-skills` | 7 | The improvement methods with teeth: DMAIC (worked control-chart project), FMEA (evidence-gated Action Priority), MSA extended to LLM-as-judge gauge studies, DOE, EVOP, root-cause analysis, project command center |
| `safety-and-reliability-skills` | 6 | Split-tally evidence design (litigation-hold rail), detection-system tuning by disposition audit, reliability math incl. probability-of-failure-on-demand, rebuild rehearsal (irreversibility screen), break-glass playbooks, hash-rank sortition review |
| `data-analytics-bi-skills` | 6 | Statistical inference, causal inference (DAGs, DiD/IV/RDD), A/B test design, survey & sampling design, spreadsheet modeling, assertion-evidence decks with a build-and-lint toolchain |
| `machine-learning-skills` | 6 | Practical ML: project framing, feature engineering, supervised modeling, evaluation, horizon-aware time-series forecasting, anomaly detection |
| `data-tools-skills` | 5 | Data plumbing that survives real files: DuckDB local analytics, PDF extraction, REST API pulls, CSV/flat-file wrangling, file hygiene |
| `writing-skills` | 4 | Registers and explanation craft: smart-brevity professional/legal writing (risk-allocation carve-outs included), plain-grade accessible writing, explanation design, Diátaxis-routed technical documentation |
| `metacognition-skills` | 3 | Cumulative improvement across sessions: hierarchical memory management, reflective learning, knowledge crystallization |
| `collaboration-skills` | 2 | Disarming elicitation (the counter-elicitation stance inverted, with its honesty rails) and meeting design (decisions as owner-and-date read-backs) |
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
  for fourteen **plugins** under `plugins/`, mirroring Anthropic's own
  [`anthropics/skills`](https://github.com/anthropics/skills) layout.
- One plugin ships **subagents**: `coding-agent-skills` carries seven in its `agents/` folder — six
  read-only specialist reviewers (performance, accuracy/correctness, structure/architecture,
  clarity/maintainability, robustness/edge-cases, and the board-chair synthesizer), orchestrated by
  the `coding-agent-skills:board-review` skill, and the `project-manager` (plan, checkpoint and QC
  modes), used by the `coding-agent-skills:project-manager-qc` skill. After install they appear in
  `/agents` namespaced as `coding-agent-skills:<name>`.
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
