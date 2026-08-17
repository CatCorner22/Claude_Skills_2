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

Nine domain plugins (66 skills) and two individual skills were **delisted, not deleted**, when
the library was re-aimed at general use: the Oracle Fusion / OTBI, cash-management, treasury,
public-sector-treasury, sponsored-projects AR, accounting, banking, and finance plugins now live
under [`archive/`](archive/README.md) with full git history. They are preserved and restorable —
[`archive/README.md`](archive/README.md) carries the manifest, the reason, and a step-by-step
restore procedure. Locally installed copies of archived plugins keep working as pinned snapshots;
they simply stop receiving updates and no longer appear in the marketplace listing.

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
- `bash scripts/validate.sh` lints every skill and manifest (currently 0 errors).

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
