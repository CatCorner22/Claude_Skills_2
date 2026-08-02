# Treasury Analyst Skills

> **New in this PR:** Curve Hero dental notes benchmark + Dental Notes Standardizer app  
> See [`Curve-Hero-Clinical-Notes-Benchmark.md`](Curve-Hero-Clinical-Notes-Benchmark.md), [`CURVE_HERO_CLINICAL_NOTES.md`](CURVE_HERO_CLINICAL_NOTES.md), and `src/` (Vite + React notes app). Run with `npm install && npm run dev`.

---

A growing personal library of [Claude Code Agent Skills](https://code.claude.com/docs/en/skills)
that make Claude a sharper partner for cash management, Oracle Fusion Cloud Financials and OTBI
reporting, accounting, banking, finance, business-intelligence analytics, practical data tooling,
statistics, machine learning, continuous improvement (Lean / TPS / Six Sigma / co-design), and
coding / autonomous agents.

Every skill is built to one house standard: it **does the task step by step and teaches the
reasoning**, so you get the deliverable *and* get better at the work.

## Install

```
/plugin marketplace add blakereaganlaw-droid/claude_skills_2
/plugin install cash-management-skills@treasury-analyst-skills
/plugin install oracle-otbi-skills@treasury-analyst-skills
# ...install whichever plugins you want
```

Installed skills are namespaced, e.g. `cash-management-skills:bank-reconciliation`. Type
`/<plugin>:<skill>` to invoke one directly, or just describe your task and Claude will pick it up.

## Plugins

| Plugin | What it covers |
| --- | --- |
| `cash-management-skills` | Cash positioning, bank reconciliation, forecasting, liquidity, controls, netting |
| `oracle-otbi-skills` | Building OTBI reports in Oracle Fusion Cloud, with deep Cash Management coverage |
| `oracle-fusion-finance-skills` | Fusion Financials modules: GL/journals, FBDI loading, AP invoice-to-pay, AR/collections, Cash Management module, period close + `fusion-treasury-architect` subagent for configuration-specific consults |
| `sponsored-projects-ar-skills` | Sponsored/grants AR across Fusion Receivables + PPM: router, domain map, unbilled/WIP recon, KPIs & forecasts, reporting, federal compliance (Uniform Guidance, LOC draws, effort) |
| `banking-skills` | Payment rails, account structures, statement formats, fees, connectivity, KYC/AML |
| `accounting-skills` | Double-entry, journals, chart of accounts, close, reconciliations, statements |
| `finance-skills` | Time value of money, working capital, ratios, short-term investing, FX, capital budgeting |
| `treasury-accounting-skills` | Debt facilities & covenants, hedging & derivatives, investment policy compliance, accruals & prepaids, intercompany accounting, audit readiness |
| `data-analytics-bi-skills` | SQL, EDA, cleaning, statistics, inference, dashboards, spreadsheet modeling |
| `data-tools-skills` | Excel automation with Python, CSV wrangling, DuckDB, PDF extraction, REST API pulls, file hygiene |
| `machine-learning-skills` | Problem framing, time-series forecasting, supervised modeling, evaluation, features, anomalies |
| `continuous-improvement-skills` | VSM, root-cause analysis, DMAIC, standard work, A3, kaizen & co-design |
| `coding-agent-skills` | Python for analysts, Claude Code config, agent design, prompt engineering, git, skill authoring |
| `board-of-advisors-skills` | Multi-agent code review swarm: 5 read-only specialist subagents + board-chair synthesizer, orchestrated by `board-review` |
| `full-stack-dev-skills` | Lean full-stack development: architecture, FastAPI, databases/ORM, dynamic frontends, realtime, ML in production, testing, deployment |

**Full catalog:** [`docs/SKILLS.md`](docs/SKILLS.md) lists every skill, what it does, and the
exact phrases that trigger it (regenerate with `python3 scripts/gen-catalog.py`).

Skills are built in waves (day-job first). See the build status and design notes in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## How it's built

- One repo that is both a **plugin marketplace** (`.claude-plugin/marketplace.json`) and the home
  for fifteen **plugins** under `plugins/`, mirroring Anthropic's own
  [`anthropics/skills`](https://github.com/anthropics/skills) layout.
- Two plugins also ship **subagents** in their `agents/` folders — after install they appear
  in `/agents` namespaced as `<plugin>:<name>`: the `board-of-advisors-skills` review swarm
  (orchestrated by the `board-review` skill) and
  `oracle-fusion-finance-skills:fusion-treasury-architect` (consulted by
  `fusion-architect-consult`).
- The authoring standard lives in the `coding-agent-skills:writing-agent-skills` skill; its
  template is `plugins/coding-agent-skills/skills/writing-agent-skills/assets/SKILL.template.md`.
- `bash scripts/validate.sh` lints every skill and manifest.

## Recommended companion marketplaces

These skills complement (and deliberately don't duplicate) two official marketplaces:

- [`anthropics/skills`](https://github.com/anthropics/skills) — install `document-skills` for
  polished .xlsx/.pdf/.docx/.pptx document *creation* (source-available, first-party), and
  `skill-creator`/`mcp-builder` for tooling. Our `data-tools-skills` covers the scripting side
  (pandas/openpyxl automation, extraction, local SQL) and points to the official document skills
  where they're the better fit.
- [`oracle/skills`](https://github.com/oracle/skills) — Oracle's official marketplace for
  Database, OCI, APEX, and GraalVM skills (`/plugin install db@oracle-skills`, etc.). Its
  `fusion` domain is still a stub, which is exactly the gap `oracle-fusion-finance-skills` and
  `oracle-otbi-skills` fill here.

## Tailoring to your environment

Many skills leave a `references/your-environment.md` hook so they can fit your real Oracle OTBI
reports, reconciliation process, chart of accounts, and bank statement formats. **Real data is
never committed** — sanitize it, and keep raw artifacts in `*.private.md` / `references/*.local.*`
files, which `.gitignore` keeps out of git.
