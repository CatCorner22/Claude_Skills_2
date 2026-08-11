# Library review — August 2026 full-catalog audit and overhaul

The user's four-part request: (1) enhance skills needing improvement, (2) suggest
consolidations, (3) build an index of when-to-use / optimized-for / how-to-trigger,
(4) add new skills in science, technical writing, communication, and statistics —
plus the archive directive that landed during scoping: move all Oracle/Fusion/OTBI/
treasury/finance-domain plugins out of the active marketplace.

**Outcome in one line:** the library went from 181 skills / 24 plugins (mixed
domain-specific and general) to a career-portable active library of **123 skills /
15 plugins** (115 kept + 8 new), with 66 domain skills preserved in `archive/`,
every mechanical audit finding fixed, a generated quick-router index at
[INDEX.md](INDEX.md), and zero validator errors.

## 1. Structural audit (what "needs improvement" actually meant)

A full mechanical audit of all 181 pre-overhaul skills found **zero violations of
any hard rule**: 181/181 had evals (positive + near-miss + rubric), references
folders, conforming names/descriptions/section order, and bodies far under the
500-line cap (max was 193). The library's hygiene was already clean; the real
findings were quality-tier and tooling:

| Finding | Scale | Fix |
|---|---|---|
| `gen-catalog.py` frontmatter parser bug — bare `metadata:` keys leaked version/source text into descriptions; 33 catalog entries carried fake triggers reading `metadata: version: "1.0.0"…` | 33 entries | Parser regex fixed; catalog regenerated clean |
| `validate.sh` suppressed all per-skill OK lines after the first error anywhere (global counter tested per skill) | cosmetic | Per-skill error flag |
| No early warning before the 1024-char description cap | 39 skills within 5% | Non-gating NOTE tier added to the validator |
| Stub-only references folders (no substantive method file) | 4 skills (2 active) | `autopsy-method.md` written for both chicken-little Forward-Deployed editions; the 2 Oracle ones archived |
| Missing `references/your-environment.md` | 1 active skill | Added to assertion-evidence-deck |
| Zero cross-links | 1 skill | medical-research-detective linked to competing-hypotheses-analysis, probability-fundamentals, explanation-design |
| Undocumented `metadata: {version, source}` convention (34/181 adoption, all August-wave) | convention gap | Codified in the authoring standard; applied to touched skills only — no mass retrofit |
| July-vs-August generation gap: early-wave skills conforming but thin (descriptions ~580 vs ~980 chars; 1–3 cross-links vs 7; ~75 reference lines vs ~142) | ~70 skills matched ≥1 weakness criterion | The 15 weakest **active** skills deep-rewritten to the current standard (see §4) |

## 2. Consolidation analysis (suggestions only — none executed)

Seven suspected overlap zones were examined skill-by-skill. Verdicts:

| Zone | Skills | Verdict |
|---|---|---|
| Statistics ladder | probability-fundamentals → descriptive-statistics → statistical-inference → model-evaluation | **LAYERED** — boundaries written into the descriptions; cleanest zone in the repo |
| Reconciliation | bank-reconciliation vs account-reconciliations vs the two sponsored-projects recon skills | bank-vs-GL: **DISTINCT** (boundary in the description). The two sponsored-projects skills (revenue-billing-reconciliation vs unbilled-billed-ar-wip-recon): **OVERLAPPING** — same PPM↔AR boundary from two angles, colliding trigger surfaces |
| Forecasting | cash-forecasting vs time-series-forecasting vs reference-class-forecasting vs sponsored-ar-kpi-trends-forecast | **LAYERED** (driver-based domain / statistical method / outside view); one soft seam: the KPI skill's "forecast" is a thin bolt-on |
| Review personas | sparring-partner, the-foreman, the-challenger, board-review, reflective-learner | **DISTINCT** on three different axes (mechanism / object / subject); closest pair is the-foreman vs sparring-partner, separated by the phase-gate question |
| Chicken Little family | 4 editions | **DISTINCT** — three are gated on literal invocation phrases; `chicken-little-college-kid` is *misnamed rather than redundant* (shares only the name) |
| Anomaly/detection | anomaly-detection vs detection-system-tuning vs compliance-risk-anomaly (+ federal-sponsored-ar-compliance-risk) | Named trio: **DISTINCT** (build → operate → apply). The unnamed pair compliance-risk-anomaly vs federal-sponsored-ar-compliance-risk: **OVERLAPPING** — near-identical exception lists, superset/subset populations |
| Writing/communication | writing-skills ×4, assertion-evidence-deck, collaboration ×3 | **DISTINCT** — three registers + one structure + one artifact + three live-interaction skills |

**Recommendations:**
- **No active-library merges.** Both genuinely overlapping pairs live in
  `sponsored-projects-ar-skills`, which is now archived — consolidation is moot
  unless the plugin is restored. If it ever is: merge
  `federal-sponsored-ar-compliance-risk` into `compliance-risk-anomaly` as a
  federal-awards reference file, and split the two PPM↔AR recon skills' seam
  explicitly (ledger tie-out vs billing-pipeline state) or merge them.
- `chicken-little-college-kid` would be better named for what it does
  (patient/staff-facing copy sensitivity) than for the family it shares a name
  with — a rename is cosmetic and was deliberately not executed (trigger gating
  works; renames break user habit).
- The review-persona crowd (~8–10 adversarial-critique skills) is dense but
  functionally separated; INDEX.md now makes the separation visible instead of
  requiring a merge.

## 3. The archive

Nine plugins / 66 skills moved to `archive/plugins/` + `archive/evals/` with full
git history (see [archive/README.md](../archive/README.md) for manifest and restore
procedure): oracle-fusion-finance-skills, oracle-otbi-skills,
sponsored-projects-ar-skills, cash-management-skills, treasury-accounting-skills,
public-sector-treasury-skills, accounting-skills, banking-skills, finance-skills.

- Marketplace name kept (`treasury-analyst-skills`) for install compatibility;
  description rewritten general-use.
- All 66 active-tree cross-references into archived plugins were rewritten:
  re-pointed to verified active siblings where a real seam exists, otherwise
  plain-prose task descriptions with explicit `archived: plugin:skill` pointers.
  Evals carry no archived routing at all.
- Deliberate residuals, kept by design: `coding-agent-skills:chicken-little`'s
  Oracle Fusion data-model reference (the persona's identity, user-commissioned)
  and `assertion-evidence-deck`'s `oracle-cm-domain.md` reference file (inert
  domain reference; flagged here for a future prune decision).

## 4. Enhancement pass

**Point fixes** — listed in §1's table.

**Deep rewrites (15)** — selected by ranking every active skill on three weakness
criteria (description < 650 chars, ≤ 3 cross-links, < 80 substantive reference
lines), capped at 15: a3-thinking, standard-work, kaizen-and-codesign,
value-stream-mapping (continuous-improvement); dashboard-design,
spreadsheet-modeling, data-cleaning, exploratory-data-analysis (data-analytics-bi);
excel-automation-python, csv-and-flat-file-wrangling (data-tools);
ml-project-framing (machine-learning); adams-plain-grade (writing);
git-and-code-review (coding-agent); hierarchical-memory-manager,
knowledge-crystallizer (metacognition). Each was upgraded to the current authoring
contract: routing-grade description, 5+ verified cross-links, ≥120-line method
reference with TOC and a domain-neutral worked example, metadata version block, and
a refreshed eval.

## 5. New skills (8)

Built from a research-verified dossier
([docs/research/general-use-expansion-research.md](research/general-use-expansion-research.md))
with collision-scanned triggers and misattribution warnings as load-bearing content:

| Skill | Plugin | Anchor (verified) |
|---|---|---|
| causal-inference | data-analytics-bi-skills | Pearl DAGs; DiD/IV/RDD; Hill's 1965 viewpoints (not a checklist) |
| ab-test-design | data-analytics-bi-skills | Kohavi online-experiments canon; SRM, peeking, MDE; Twyman's law (Ehrenberg's formulation) |
| survey-and-sampling-design | data-analytics-bi-skills | Groves total survey error; Dillman; Literary Digest died of nonresponse (Squire 1988) |
| bayesian-updating | decision-science-skills | Natural frequencies (Gigerenzer); Tetlock update discipline; honest Bayes/Price/Laplace history |
| technical-documentation | writing-skills | Diátaxis (Procida); ADR (Nygard 2011); Keep a Changelog; Django-predates-Diátaxis honesty note |
| executive-briefing | collaboration-skills | BLUF doctrine (DA Pam 600-67, 1986); Minto SCQA; completed staff work (dual attribution) |
| stakeholder-mapping | collaboration-skills | Power-interest grid is Johnson & Scholes/Eden & Ackermann — NOT in Mendelow 1981; RACI has no inventor |
| reproducible-analysis | data-tools-skills | Knuth literate programming; FAIR; ACM's reversed terms 2013–2020; OSC-2015 contested honestly |

## 6. Tooling changes

- `scripts/gen-catalog.py`: parser bug fixed; refactored into `collect()` + two
  emitters; now also generates [INDEX.md](INDEX.md) — the quick router (task →
  skill by category, per-plugin when-to-use / optimized-for / trigger tables,
  archived-plugins manifest).
- `scripts/validate.sh`: per-skill OK flag; NOTE tier for near-cap descriptions.

## 7. What to watch next

- 40+ descriptions sit within 5% of the 1024 cap (validator now NOTEs them) —
  any future edit to those must re-count.
- The archived plugins receive no updates; locally installed copies keep working
  as pinned snapshots. Restore procedure is in archive/README.md.
- If a future role lands in a new domain, the pattern is established: found a new
  domain plugin, keep the general-use core untouched, wire the role specifics
  through each skill's `references/your-environment.md`.
