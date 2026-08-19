# Library review — August 2026 full-catalog audit and overhaul

The user's four-part request: (1) enhance skills needing improvement, (2) suggest
consolidations, (3) build an index of when-to-use / optimized-for / how-to-trigger,
(4) add new skills in science, technical writing, communication, and statistics —
plus the archive directive that landed during scoping: move all Oracle/Fusion/OTBI/
treasury/finance-domain plugins out of the active marketplace.

**Outcome in one line:** the library went from 181 skills / 24 plugins (mixed
domain-specific and general) to a career-portable active library of **121 skills /
14 plugins**, with 66 domain skills preserved in `archive/`, every mechanical audit
finding fixed, a generated quick-router index at [INDEX.md](INDEX.md), and zero
validator errors.

**Current state, 2026-08-18** (the counts below are the running history; this is where the
tree stands today): 121 active skills across 14 plugins and **zero archived plugins**. All nine
domain plugins the first pass archived were later deleted on owner direction — the two Oracle ones
(17 skills / 70 files) and then the seven finance/treasury ones (49 skills / 154 files). What
remains in `archive/` is two skill-level archives and the standalone apps. Every cross-link that
used to point into a deleted plugin was rewritten to name the domain rather than promise a restore;
`validate.sh` enforces that none is left dangling.

The arithmetic: 181 pre-overhaul skills − 66 archived with their nine plugins
(§3) = 115 kept, + 8 new (§5) = 123 across 15 plugins at the end of the first pass;
then the second-pass consolidation (§7) archived 2 more skills at skill level and
merged the one-skill `board-of-advisors-skills` into `coding-agent-skills`, landing
at the current **121 skills / 14 plugins**.

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

## 2. Consolidation analysis (first-pass findings)

Seven suspected overlap zones were examined skill-by-skill. Nothing was merged
during this first pass — the verdicts and recommendations below were handed to the
owner as options. **Consolidation was executed in the second pass, on different
grounds: see §7** (`board-of-advisors-skills` merged into `coding-agent-skills` for
install friction, not overlap; `chicken-little-college-kid` and
`curve-hero-design-language` archived at skill level as dental-direction mounts).
Verdicts:

| Zone | Skills | Verdict |
|---|---|---|
| Statistics ladder | probability-fundamentals → descriptive-statistics → statistical-inference → model-evaluation | **LAYERED** — boundaries written into the descriptions; cleanest zone in the repo |
| Reconciliation | bank-reconciliation vs account-reconciliations vs the two sponsored-projects recon skills | bank-vs-GL: **DISTINCT** (boundary in the description). The two sponsored-projects skills (revenue-billing-reconciliation vs unbilled-billed-ar-wip-recon): **OVERLAPPING** — same PPM↔AR boundary from two angles, colliding trigger surfaces |
| Forecasting | cash-forecasting vs time-series-forecasting vs reference-class-forecasting vs sponsored-ar-kpi-trends-forecast | **LAYERED** (driver-based domain / statistical method / outside view); one soft seam: the KPI skill's "forecast" is a thin bolt-on |
| Review personas | sparring-partner, the-foreman, the-challenger, board-review, reflective-learner | **DISTINCT** on three different axes (mechanism / object / subject); closest pair is the-foreman vs sparring-partner, separated by the phase-gate question |
| Chicken Little family | 4 editions | **DISTINCT** — three are gated on literal invocation phrases; `chicken-little-college-kid` is *misnamed rather than redundant* (shares only the name) |
| Anomaly/detection | anomaly-detection vs detection-system-tuning vs compliance-risk-anomaly (+ federal-sponsored-ar-compliance-risk) | Named trio: **DISTINCT** (build → operate → apply). The unnamed pair compliance-risk-anomaly vs federal-sponsored-ar-compliance-risk: **OVERLAPPING** — near-identical exception lists, superset/subset populations |
| Writing/communication | writing-skills ×4, assertion-evidence-deck, collaboration ×3 | **DISTINCT** — three registers + one structure + one artifact + three live-interaction skills |

**Recommendations (as written in the first pass — superseded in part by §7):**
- **No active-library merges *on overlap grounds*.** Both genuinely overlapping pairs live in
  `sponsored-projects-ar-skills`, which is now archived — consolidation is moot
  unless the plugin is restored. If it ever is: merge
  `federal-sponsored-ar-compliance-risk` into `compliance-risk-anomaly` as a
  federal-awards reference file, and split the two PPM↔AR recon skills' seam
  explicitly (ledger tie-out vs billing-pipeline state) or merge them.
- `chicken-little-college-kid` would be better named for what it does
  (patient/staff-facing copy sensitivity) than for the family it shares a name
  with — a rename is cosmetic and was deliberately not executed (trigger gating
  works; renames break user habit). *Moot as of §7: the skill was archived instead.*
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

## 7. Addendum (2026-08-11, second pass): consolidation + adversarial review

**Consolidation executed** (owner-authorized):
- `board-of-advisors-skills` (1 skill + 6 subagents) **merged into `coding-agent-skills`** —
  board-review and all six advisors keep working under the new namespace; 9 citing files
  re-namespaced. A one-skill plugin was pure install friction.
- `curve-hero-design-language` and `chicken-little-college-kid` **archived at skill level**
  (`archive/skills/`) — both were mounted on the dental-practice direction that was not
  chosen at the career re-aim. lean-six-sigma-for-software's sync-audit step rewritten as
  generic build-your-own-map guidance with an archived pointer to the worked dental example.
- Active library after consolidation: **121 skills / 14 plugins**.

**Adversarial review** (15 agents: 7 reviewers → 7 skeptics → synthesizer; 62 raw findings,
23 refuted, **39 confirmed → 30 work items, all executed**). The wave verdict, verbatim from
the synthesis: *"one compromised skill, roughly a dozen worked-example numbers to correct,
and about twenty one-line seam and residue fixes."* What held up under attack: all section
order/eval/naming hygiene, every archived pointer, the full attribution layer (Cleveland &
McGill, Wickham, Rubin, CRISP-DM, Hill, Twyman→Ehrenberg, the TPS canon), and a clean
privacy sweep. Highlights of what was fixed:
- **Taught-something-false tier**: causal-inference's collider example had its sign inverted;
  spreadsheet-modeling's cross-foot "catch" was an algebraic tautology and its breakeven was
  ~7 points off its own inputs; excel-automation's verification assert ended in `or True`
  (dead code); ml-project-framing's leakage remedy didn't fix the leak it named;
  ab-test-design's A/A advice recreated the peeking setup its own §5 condemns; VSM labeled
  process time as value-added time; standard-work asserted a postwar TWI column as wartime.
- **The one standing-directive breach**: assertion-evidence-deck still named the former
  employer and an internal ERP nickname in its published routing contract, and its build
  script defaulted to the employer's brand palette. De-mounted; the UT palette survives as
  an explicit non-default legacy option; oracle-cm-domain.md relabeled a legacy reference.
- **Discovery seams**: six of eight new skills had zero inbound citations — reciprocal
  Not-for lines added to statistical-inference, probability-fundamentals, meeting-design;
  assertion-evidence-deck's bare `briefing` trigger narrowed so executive-briefing can
  receive its own traffic.
- **Kept by explicit exception** (recorded in MEMORY.md): chicken-little's Oracle Fusion
  data-model reference — name-gated (zero routing pollution) and the only surviving copy of
  that commissioned depth in the repo. **Superseded 2026-08-18** — see §"Oracle deletion"
  below: the owner directed deletion of all Oracle skills, the exception was retired, and the
  reference files were removed.

**Text-optimization pass** (10 agents: 5 optimizers + 5 diff-level verifiers, zero
must-fix flags): the 46 earlier-vintage skills the review didn't line-check were each
assessed against seven criteria (deliverable contract, Do-it executability, division of
labor, routing contract, token economy, teaching integrity, cross-links). **19 optimized,
27 confirmed already at standard** — churn explicitly avoided. The dominant real gap was
the missing deliverable contract: 12 skills (all five general ML skills, three CI method
skills, anomaly/feature/eval/forecast outputs, agentic-workflow-design, prompt-engineering)
gained compact end-of-Do-it Deliverable blocks with matching eval-rubric lines, so each now
states what the finished artifact contains. Other wins: ui-and-ux-inspection's dormant
Fitts/NASA-TLX retrofit is now wired into its inspection steps; dmaic and root-cause-analysis
descriptions upgraded with 9 collision-checked new triggers; sql-for-analysts' OTBI residue
generalized; descriptive-statistics restructured cleanly. All verified additive — no lost
provenance marks, no meaning inversions, no cap breaches.

**Closing assessment** (9 agents over the ~46 August-wave skills no prior pass had
line-checked, arithmetic-first): **10 real defects fixed, 31 skills confirmed at standard,
zero verifier flags.** Every authoring wave contributed at least one worked-example error:
weak-signal-navigation's fused band didn't follow from its own inputs (34-37 → 34-36),
systems-thinking's loop legend cited a hiring node its diagram doesn't have, pre-mortem's
"30-45 min" total was unreachable from its own step budgets, the-challenger's Feynman
paraphrase had drifted from the verbatim quote in its own reference, detection-system-tuning's
projected queue and flood-share denominator were off, reliability-engineering's "one failure
every four months" is actually every ~5.5 months at its own SLO, weight-of-the-books' 7-year
retention ignored its manifest's own +12%/yr compounding (~97M → ~140M),
exponential-growth-and-logs shipped a false same-CAGR equation (fixed to +38%/−12%), and
medical-research-detective's "relative risk is 100%" was misreadable as RR = 1.0 (now
"relative risk increase is 100% (RR = 2.0)"). Plus defect-epidemiology's R0 example counted
7 instances against an 8-node tree (fixed inline). Every active skill has now had line-level
review this session.

**Standing lessons adopted for future waves**: (1) every worked example gets an
arithmetic-verification pass before ship — examples are the part readers lift; (2) every
new-skill wave gets a reciprocal-link pass so additions don't land as citation sinks.

## 8. What to watch next

- **57 of the 121 active descriptions** sat within 5% of the 1024-char cap (> 973
  chars) as measured at the close of this review; the validator now NOTEs each one,
  so its summary line is the live count. Any future edit to a near-cap description
  must re-count before it overruns.
- The archived plugins receive no updates; locally installed copies keep working
  as pinned snapshots. Restore procedure is in archive/README.md.
- If a future role lands in a new domain, the pattern is established: found a new
  domain plugin, keep the general-use core untouched, wire the role specifics
  through each skill's `references/your-environment.md`.

---

## 9. Addendum (2026-08-17, from-scratch pass): substance, routing, and the standard itself

Sections 1–8 record four review passes. Every one of them was scoped and briefed by the same
coordinating agent, so any error in that framing propagated silently through all four. All four
checked **conformance** — frontmatter validity, worked-example arithmetic, link integrity, eval
parity. None asked the two questions that decide whether the library is any good:

1. **Is the advice correct?**
2. **Does the library actually route?**

This pass asked both, treated the earlier passes' output as suspect, and briefed domain experts to
verify claims *by execution and derivation* rather than by review. The results below include several
findings against this session's own earlier work.

### 9.1 The authoring standard had drifted from the library it governs

The most consequential finding, because `writing-agent-skills` is the reference every other skill
conforms to: **a conformance regime cannot audit its own reference.** No amount of checking skills
against the standard can detect a fault *in* the standard. Four faults were present:

- **A directive breach at the root.** §5's canonical tailoring exemplars were still Oracle OTBI
  reports, reconciliation, chart of accounts, and bank-statement formats — so every skill authored
  from the standard would inherit the exact framing the archive was created to retire.
- **The template contradicted the rules.** `frontmatter-rules.md` requires a `metadata:` block on new
  skills; `assets/SKILL.template.md` had none. Following step 1 of the standard — copy the template —
  produced a non-conforming skill.
- **The token math was internally inconsistent by an order of magnitude.** SKILL.md said Claude sees
  `name` + `description` at "~100 tokens each"; `frontmatter-rules.md` separately claimed the whole
  listing is budgeted to ~1% of context. Measured, the real figure is ~235 tokens per description and
  14.9% of a 200K window. Both published claims were wrong, in the same skill's own docs, in
  directions that cancel — which is why neither had ever been questioned.
- **The checklist omitted every guard this session had to learn the hard way.** No trigger-collision
  check, no catalog-regeneration step, no arithmetic-verification of worked examples, no reciprocal-
  link pass. Those lessons had been recorded in `MEMORY.md`, where only the coordinator reads them,
  rather than in the checklist, where authors work.

All four are fixed. The trigger-test item now also carries the four rules that decide whether a
result means anything.

### 9.2 The measurement bug that made an entire earlier pass counterproductive

`scripts/validate.sh` was counting description length with `wc -m`, which under a C locale counts
**bytes, not characters**. Every em dash was over-charged by two. **112 of 121 skills** were affected.

Acting on those inflated numbers, an earlier pass in this session trimmed **46 descriptions**.
Re-measured: **none of the 46 had ever exceeded the 1024-character cap**, and all sat in the
non-gating 973–1024 NOTE band. The trims bought nothing, and 12 of them removed real routing or
teaching signal — a mechanism, a provenance mark, a scope boundary. Those 12 are restored; trigger
lists were verified byte-identical across the revert, so no routing contract moved. The validator now
counts characters via `python3`, with a `LC_ALL=C.UTF-8` fallback.

The general lesson, now in `MEMORY.md`: **a measurement that drives edits gets verified before the
edits, not after.**

### 9.3 Routing viability — the verdict

**The full library does not fit comfortably, and description trimming was never the lever.**

Measured 2026-08-17: 121 skills' names + descriptions = **110,081 characters ≈ 29,750 tokens ≈ 14.9%
of a 200K context**, present before the user asks anything. Two consequences:

- **A full install is deep past the point where this starts, and the mechanism is worse than a
  count threshold.** *(Mechanism corrected 2026-08-19 — see
  `docs/live-routing-and-degradation-2026-08-18.md` §1–§2, which now carries the decompiled
  algorithm and retracts the account originally given here.)* The real gate is a **character
  budget**: `floor(context_tokens × 4 × skillListingBudgetFraction)`, i.e. **8,000 characters** at
  the 200K/1% defaults, against **113,677** needed to render all 121 descriptions. Skills start as
  bare names and are upgraded back to full text in **descending order of recent use**
  (`usageCount × max(0.5^(days/7), 0.1)`, unused = 0), greedily, skipping any that do not fit.
  Simulated against this library (`scripts/simulate-listing-budget.py`): **3 of 121 keep a
  description on a default 200K session; 118 route on their bare name** — silently, with no error,
  while `/plugin:skill` direct invocation keeps working. That is precisely the path an author uses
  to test their own skill, so the failure is invisible from the inside.
- **The lever is skills per install, not characters per description.** Trimming a description by 100
  characters saves ~27 tokens; not installing a 15-skill plugin saves ~3,900 — a 145× difference.
  This is the arithmetic the trimming pass of §9.2 should have run first.

`README.md` now carries a per-plugin cost table and recommends **three or four plugins (~35–50 skills,
5–7% of context)** as the working set. This is recorded as a **design constraint of the library, not a
footnote**: a 121-skill marketplace is a catalog to select from, not a manifest to install.

### 9.4 Trigger collisions: resolved at the string level, not at the routing level

An earlier pass reported "zero trigger collisions" and that claim is *literally* true — there are **0
exact duplicate trigger phrases** across all 121 skills. It is also misleading, and the correction
belongs in the record: **the router matches against whole descriptions, not against `Triggers:` lists.**
Measured now, **111 distinct trigger phrases still appear as whole words inside a different skill's
description** — `python` in 7 other descriptions, `pipeline` in 6, `code review` in 3.

> **Method, stated because the first published figure was wrong.** This counts, for each of the
> 1,328 trigger phrases, how many *other* skills' descriptions contain it as a whole word,
> searching the **entire** description including that skill's own `Triggers:` list — which is what
> the router actually sees. Excluding the other skill's `Triggers:` list gives 98 instead, but that
> narrower reading contradicts the three examples above (it yields `python` in 5 and `code review`
> in 1). An earlier version of this section published **85**, which came from an undisclosed
> minimum-length filter of 6 characters that silently dropped short phrases like `git` and `SQL`;
> it also described the method as searching "prose" when it did not. Corrected 2026-08-18.
`elite-python-engineer` yielded the trigger `code review` while continuing to advertise code review in
its prose. The collision was **renamed, not resolved.**

Two concrete defects followed from treating exact-duplicate elimination as the goal:

- **`standardize` now has no trigger owner at all.** Three skills each held the bare word; collision
  surgery qualified all three simultaneously (`standardize values`, `standardize features`,
  `standardize a process`), and nobody checked whether the bare phrase still landed anywhere. It is
  row B1 of the trigger test.
- **A routing regression in `exploratory-data-analysis`**, caused by this session: `mean`, `median`,
  `spread` and `summary statistics` were scrubbed from its prose to clear a collision, which made
  "summary statistics for this dataset" unable to reach the first-look skill at all. Prose restored;
  the boundary with `descriptive-statistics` is now stated on the **depth** axis (screening signal vs
  publishable summary) rather than by vocabulary ownership.

The standing rule adopted: **never resolve a collision by deleting the loser's trigger.** Name the
seam reciprocally in both skills instead.

### 9.5 Substance: what expert review found that four conformance passes could not

Domain experts were instructed to verify by running code and re-deriving results, not by reading.
That distinction produced the findings — and it also invalidated part of the coordinator's own brief:
**three of eight claims briefed to the data-layer reviewer did not survive contact with a real
install**, and the DOE reviewer caught an arithmetic inconsistency the coordinator had introduced.

Representative confirmed defects, all fixed:

| Skill | The claim as published | What is actually true |
|---|---|---|
| `model-evaluation` | A large negative class "inflates the true-negative rate", making AUC optimistic | False twice over. TNR = 1 − FPR is a within-negatives rate that does not move with class size, and AUC is an expectation over one draw from each class, so it has **no** dependence on prevalence. Verified: downsampling negatives 100× moved precision from 13.9% to 94.1% and left AUC identical. The published mechanism predicts the opposite of what happens. |
| `time-series-forecasting` | "MASE < 1 means you beat seasonal-naive — the cleanest single number" | A special case promoted to a rule. MASE divides out-of-sample h-step error by *in-sample one-step* naive error, so the bar tightens with horizon for reasons unrelated to model quality: on a random walk the optimal forecast scores MASE ≈ √13 ≈ 3.6 at h = 13, making the optimal model unreachable under a MASE < 1 policy. |
| `statistical-inference` | Rank tests as drop-in "nonparametric equivalents" for comparing means | Mann–Whitney's null is stochastic dominance, equivalent to a means test only under location shift. Verified construction: a zero-inflated arm with **twice** the mean revenue is declared *dominated* — the test points away from the money. The log transform is the same trap: it silently changes the estimand to the geometric mean. |
| `design-of-experiments` | 4–7 factors in 8–16 runs at "resolution IV+", mains clear of 2-factor interactions | Impossible. Defining subgroups derived by closing generators under symmetric difference: only k=4 in 8 runs reaches IV; k=5, 6, 7 in 8 runs are all resolution III. Also: A × ABCDE = BCDE, not BCD; and folding a resolution IV design leaves the alias structure **identical**, so the recommended fold-over bought nothing. |
| `reliability-engineering` | A Weibull β fitted to a repairable system's 9 repaired failures | Category error — Weibull describes time-to-first-failure of non-repairable units; a repairable system needs a point process. Refitted as a power-law NHPP: β = 0.858, CI [0.30, 1.42], i.e. **no detectable trend**, not the reliability growth claimed. The real signal was clustering, which a binomial test settles decisively (p = 6.0×10⁻⁵) with no Weibull at all. |
| `prompt-engineering` | Wording-based output contracts; "think step by step"; temperature as the flakiness fix | Superseded. Schema-constrained output makes non-conforming JSON impossible rather than merely unlikely; reasoning depth is configuration, not prose; and the Claude API **rejects** non-default `temperature`/`top_p`/`top_k` with a 400 on its 4.7-and-later generations, so the advice was unexecutable. Rated NET-NEGATIVE before the rewrite: an unaided current-generation assistant would have done better than the skill told it to. |
| `database-and-orm` | Money as `Numeric`; SQLAlchemy will warn on float conversion | The warning was removed in SQLAlchemy 2.0 — grepped the installed source, captured warnings with `simplefilter("always")`: zero. The conversion is now **silent**, which makes the defect worse. Measured: 1.005 → 1.00 through `Numeric(12,2)`. |
| `testing-strategy` | Set `join_transaction_mode="create_savepoint"` for test isolation | The prescribed fix is **harmful**. SQLAlchemy 2.0 already defaults to `conditional_savepoint`, which isolates correctly; `create_savepoint` on default pysqlite *leaks* — rows committed by the endpoint survived `tx.rollback()` and carried into later tests. |

**Provenance discipline held under pressure.** One reviewer initially marked new citations
`[snippet-only, cross-checked]`, which in that skill specifically asserts verification against the
research dossier. The citations were not in the dossier. Rather than let a false provenance claim
stand, it defined a new, weaker mark — `[canon attribution]`, meaning author/year named but not
independently re-verified — and applied it consistently. Another reviewer flagged three claims it
could **not** verify in this environment as `[unverified here]` instead of asserting them.

### 9.6 The value test — the finding worth reporting rather than burying

Reviewers were asked, per skill: **does invoking this beat an unaided competent assistant?** On a
14-skill sample: **3 NET-NEGATIVE, 6 MARGINAL.** Nearly two-thirds were marginal or worse — and four
conformance-focused passes had rated every one of them as passing, because every one *was* conformant.

This is the honest headline of the pass: **conformance and value are close to uncorrelated, and only
one of them had ever been measured.** A skill can carry perfect frontmatter, resolve every cross-link,
verify every worked example, and still teach a reader something false or tell a current-generation
model to do less than it would have done unaided. The NET-NEGATIVE cases were not sloppy; they were
*stale* — correct advice for an earlier generation of tooling, presented as current.

### 9.7 What remains unmet, stated plainly

- **The trigger test has never been run, for any skill.** `docs/trigger-test.md` now exists with 43
  risk-ranked rows, exact prompts, near-misses, and a pass/fail log. Executing it needs fresh
  interactive sessions, so the protocol is the deliverable and the compliance record is **empty**.
  Nothing in this library's history establishes that any skill routes.
- ~~**Only 14 of 121 skills received expert substance review.**~~ **CLOSED 2026-08-19 — the census
  ran. See §14.** All 121 were reviewed: **80 NET-POSITIVE, 41 MARGINAL, 0 NET-NEGATIVE.** The
  14-skill sample did not generalise, and it was right not to extrapolate it — in either direction.
- **111 whole-word description collisions remain.** They are recorded and measured, not fixed. Fixing them
  means naming seams reciprocally, one pair at a time, and the trigger test is what identifies which
  pairs actually mis-route.

---

## 10. Decision list for the owner (contested — not decided unilaterally)

Everything factually wrong was fixed directly. The items below are genuinely contested, or they are
scope calls that belong to the library's owner rather than to a reviewer. Each carries a
recommendation so it can be settled quickly.

**D1 — Should `design-of-experiments` keep teaching Taguchi's crossed arrays and S/N ratios as the
default?** *(raised by the DOE reviewer, explicitly deferred)*
The larger-is-better S/N formula in the skill is correct and is kept. But the mainstream position is
that Taguchi's *goals* were absorbed into standard practice while his *methods* largely were not:
crossed arrays multiply runs (9 × 4 = 36 before replication) where **combined arrays** estimate
control-by-noise interactions directly, and S/N confounds mean with variance behind a transformation
the analyst never chose. The skill now presents both sides. The open question is which one is taught as
the default path.
→ **Recommendation: teach combined arrays as the default and keep Taguchi as a named, contextualized
alternative.** It is the position most modern texts take, and it costs fewer runs. Say so explicitly
rather than presenting a balanced menu, because a skill that refuses to recommend leaves the reader
where they started.

**D2 — `chicken-little`'s Oracle content: already settled, with one factual correction to the stored
rationale.** *(not a new finding — see the correction below)*
This pass's residue sweep flagged `coding-agent-skills:chicken-little` as archived-domain content in an
active plugin. **That is a settled decision, not an open one**: `MEMORY.md` records it as an
owner-ratified exception (2026-08-11) with an explicit instruction not to re-flag it in future residue
sweeps, on the grounds that it is name-gated and is the only surviving copy of that commissioned depth.
The decision stands and nothing was changed.

One narrow correction to the *rationale* rather than the decision, because the stored reason contains a
measurable claim that does not hold: the exception is justified as "zero routing pollution" on the basis
of name-gating, but **3 of the skill's 7 trigger phrases are not the persona name** — `invoice black
hole`, `ghost receipts`, and `orphan distributions` are Oracle domain phrases that can route on their
own, and the description spends roughly a third of its always-loaded budget on Oracle Fusion specifics.
So the pollution is small and bounded, not zero.
→ **Recommendation: no action, and stop re-flagging it.** The cost is a few hundred tokens for anyone
who installs `coding-agent-skills`, which is a fair price for the only copy of commissioned depth, and
the three domain triggers are specific enough that they will not fire on unrelated work. The reason to
record the correction at all is that "zero" invites a future sweep to re-derive the same finding and
re-open the same decision — which is exactly what happened here. The residue-sweep note in `MEMORY.md`
has been amended to say *bounded and accepted* instead of *zero*.

**Superseded 2026-08-18 (owner directive).** The owner subsequently directed that *all* Oracle
skills be deleted. That directive overrides this exception: chicken-little's two Oracle reference
files (`oracle-fusion-data-model.md`, `sql-patterns.md`) were deleted, the Oracle Do-it step and
the named-Oracle-failure-modes section were removed, the three Oracle domain triggers
(`invoice black hole`, `ghost receipts`, `orphan distributions`) were dropped, and
`your-environment.md` was rewritten domain-neutral. The skill is now gated on the persona name
alone, so the routing cost analysed above is now zero as a matter of fact. The analysis is left in
place because it is the reason the "zero" claim was auditable at all — but the decision it
recommended (no action) no longer stands.

**D3 — `assertion-evidence-deck/references/oracle-cm-domain.md` (151 lines) is retained as an opt-in
legacy reference.** The skill itself was de-mounted earlier in this session; the description and body
are clean, and the reference is labeled "read only if you work that system," so it costs zero tokens
unless deliberately opened.
→ **Recommendation: leave it.** Lower stakes than D2 by a wide margin — it is outside the routing
payload entirely. Flagging it only so the archive's boundary is on the record as *deliberate* rather
than missed.

**D4 — `full-stack-dev-skills:elite-python-engineer` has an unresolved scope seam.** It yielded the
triggers `python`, `code review`, and `fastapi` to other skills on the theory that it is name-gated by
"Pythagoras" — but its description does **not** signal name-gating, and it still advertises "code
review" in prose. Its broadest surviving route is the bare word `refactor`. So it is neither cleanly
name-gated nor cleanly discoverable. (Note: the earlier suspicion that it had become *unreachable* is
**not** borne out — it retains `write python`, `refactor`, `production-grade python`, and `production
python`.)
→ **Recommendation: decide the identity, then make the description match.** Either (a) name-gate it
honestly — say "Use when the user asks for Pythagoras by name" as `chicken-little` does, and drop
`refactor` — or (b) treat it as the production-Python skill and restore qualified triggers
(`production python review`, `python code review`) while `git-and-code-review` keeps language-agnostic
review. Rows A1, A2, B5, B6 and C10 of the trigger test are designed to tell you which is happening
today; **run those five before choosing.**

**D5 — `standardize` has no trigger owner.** Three skills each qualified it away simultaneously. A user
typing "standardize this" now matches no trigger phrase, though whole-description matching may still
route them somewhere.
→ **Recommendation: leave it unowned and let the model ask.** A bare ambiguous verb spanning data
cleaning, feature scaling, and process documentation *should* produce a clarifying question, not a
confident guess. Row B1 tests exactly this; if it produces a confident wrong pick instead, revisit.

**D6 — Only 14 of 121 skills received expert substance review.** The 3 NET-NEGATIVE / 6 MARGINAL sample
suggests more stale advice exists, but the sample was drawn toward technical skills where staleness is
most likely, so it should not be extrapolated to the whole library.
→ **Recommendation: commission review by decay rate, not by breadth.** The skills most likely to have
gone stale are the ones describing fast-moving external tooling — `bespoke-llm-architect`,
`agentic-workflow-design`, `agent-harness-config`, `ml-in-production`, `frontend-modern-ui`,
`claude-api`-adjacent material. The method-and-reasoning skills (Lean, decision science, math
foundations, writing) rest on stable ground and are far lower risk. Roughly 15 skills, not 107.

**D7 — Method judgment calls the reviewers made, documented with both sides in-file.** No action needed
unless you disagree; recorded so the choices are visible rather than silent: the sharp null for a plain
permutation test (studentized version prescribed); freeze-then-backtest as a stated compromise against
nested selection; "CUPED routinely halves n" anchored to ρ ≈ 0.7 rather than asserted generally; the
FastAPI teardown boundary written as version-dependent with a runnable probe, because the review's
stated ≥0.106 rationale is **inverted** relative to FastAPI's own changelog even though its conclusion
holds.

**D8 — Three restored descriptions land at 1013–1016 characters**, over the 1010-character soft target
this session had been using, under the hard 1024 cap (`exploratory-data-analysis`, `the-challenger`,
`rebuild-rehearsal`).
→ **Recommendation: accept them.** Two were at that length before the unnecessary trims of §9.2;
restoring them returns to a state that never violated anything. The soft target was an artifact of the
byte-counting bug.

**D9 — `references/your-environment.md` lives in the plugin cache, which updates discard.** *(new,
2026-08-18; the one finding from the surfaces pass that is a design decision rather than a defect)*
All 121 skills tell the user to record their real specifics in `references/your-environment.md`. That
file sits inside the installed plugin, so `/plugin marketplace update` either refuses on the dirty
tree or overwrites it. The single persistent artifact the library asks a user to create is stored in
the least durable place available, and nothing warns them.
→ **Recommendation: change what the skills ask for, not where the file lives.** Keep
`your-environment.md` as the shipped *template* — it documents what to record — but have the Tailor
section tell the user to copy it into **their own project** (e.g. `.claude/skills-env/<skill>.md`) and
point the skill at that. It survives updates, it is theirs, and it keeps real data out of a directory
they may not realise is disposable. This is ~121 small edits to one section, so it wants your
go-ahead before it starts. The alternative — documenting the fragility in place — is cheaper but
leaves the user's work destructible by a routine update.

---

## 11. Addendum (2026-08-18, surfaces pass): everything that is not a SKILL.md

Sections 9–10 reviewed the 121 skill bodies. This pass reviewed the surfaces that review could not
see — the 22,604-line reference corpus, the 121 evals as deliverables, the docs layer, the two
scripts, and packaging/privacy — across 19 agents, with every finding attacked by an adversarial
verifier. 81 survived.

### 11.1 The headline: the repository is not the product

**Every quality gate in this library operates on the repository, and nothing had ever verified the
installed artifact.** `validate.sh` and `gen-catalog.py` walk `plugins/**` from the repo root and
cannot be run by an installed user at all. Once you look for that, several independently-reported
findings collapse into one cause:

- **`CLAUDE_PLUGIN_ROOT` appeared zero times across all 121 skills**, while every bundled-script
  invocation used a bare repo-relative path. The one command that produces the assertion-evidence
  deck, and all five citation-verification examples, were a guaranteed file-not-found after
  `/plugin install` — the skill runs from a plugin cache with the user's own project as cwd.
  **Fixed at 13 sites**, plus a new house-standard §4b, a checklist line, and a validator check.
- **`references/your-environment.md` lives inside the plugin cache.** All 121 skills instruct the
  user to write their environment there, where a `/plugin marketplace update` either aborts on the
  dirty tree or discards it. The one persistent thing the library asks a user to create is stored
  in the least durable place available. **Flagged, not fixed — this is a design decision (D9).**
- The `(archived: plugin:skill, restorable from archive/)` convention names a directory installed
  users do not have. Honest inside the repo; meaningless outside it.

### 11.2 The artifacts are sound; the statements about themselves were not

The largest category was false self-description, and the worst instance was this review's own:

| Claim | Reality |
|---|---|
| "85 distinct trigger phrases appear inside another skill's description" | **111.** The 85 came from an undisclosed ≥6-char filter, and the method was described as searching "prose" when it searched whole descriptions (prose-only gives 98 and contradicts the paragraph's own three examples). It had propagated to seven sites including `MEMORY.md`. |
| Authoring standard: 107,700 chars / 29,000 tokens / 14.6% | README said 110,081 / 29,750 / 14.9% for the *same* measurement, and §9 had declared that discrepancy fixed. Both now regenerate from measurement, and `scripts/measure-listing-cost.py` prints both tables so neither can drift again: **109,662 / 29,638 / 14.82%** as of 2026-08-18. |
| Token counts throughout | Derived from a 3.7 chars/token divisor **disclosed nowhere**. Now stated at every site — an undisclosed divisor is exactly how the two figures above diverged. |
| README "sweet spot: ~35–50 skills, 5–7%" | Contradicted by all four of its own bundles. Measured: **24–31 skills, 2.95–3.59%.** Guidance and a per-bundle table are now generated from one measurement. |
| `trigger-test.md`: "~35 rows means ~35 sessions" | 45 rows, **80 prompts**. The one instrument aimed at the installed product understated its own cost by more than 2× — a plausible reason it has never been run. |
| Install command in the published catalog | Still named the pre-rename GitHub owner, disagreeing with README and the marketplace manifest, and re-emitted on every regeneration. Fixed at the generator. |

### 11.3 Tooling that reported green while not looking

Four defects in the gate itself, each reproduced before fixing:

- **A missing closing `---` fence passed as OK** — the whole file became "frontmatter" and its
  mangled description flowed into both catalogs.
- **One non-UTF-8 byte anywhere silently disabled the entire cross-link check.** Reproduced: a
  planted broken link reported 1 error clean, **0 errors** with one bad byte elsewhere.
- **The body-line counter stopped at the first bare `---`**, so the 500-line cap was bypassable by
  any skill using a horizontal rule. A 168-line file counted as 30.
- **`gen-catalog.py`'s lead-clause splitter was bracket-blind** (its fourth bug), emitting three
  unbalanced cells in the committed `INDEX.md`.
- **Manifests were checked only for JSON validity.** Adding coherence checks immediately found that
  **all eight skills added this session were missing from their plugin descriptions** — the strings
  `/plugin` shows pre-install — and that **11 of 14 marketplace entries had drifted** from their
  plugin manifests, so neither file was authoritative.

### 11.4 Two more false claims in skill content

- **`agent-harness-config` inverted the settings-precedence order**, placing enterprise/managed
  settings lowest — i.e. telling readers a git-ignored `settings.local.json` overrides
  administrator policy. Security-relevant and wrong in all three places it appeared.
- **`design-of-experiments` claimed "nine aliased pairs"** for the 16-run 2^(6−2) design. Six
  factors have only C(6,2) = 15 two-factor interactions; nine pairs would need 18. The real
  structure, derived from I = ABCE = BCDF = ADEF, is seven groups — six pairs and one triple.

### 11.5 What was good, stated plainly

The eval corpus is 121:1 complete with zero orphans; every archived pointer resolves; the
generated catalogs are byte-identical to a fresh regeneration; and **no secrets, credentials, or
client data exist anywhere in the tree**. The `executive-briefing → briefing-method.md` path is
complete end to end — template, worked memo, and checklist produce a signable deliverable without
leaving the skill. That is the model the analytical and engineering paths should copy.

### 11.6 A trap caught in this pass's own deliverable

`docs/trigger-test.md`'s Tier D asked whether a "generic prompt" fails to load each persona skill.
Checked against the skills' actual trigger lists, **six of its eight generic prompts were
paraphrases of phrases those skills deliberately own** (`is this ready to build on`, `simpler
solution`, `will it hold at real volumes`, `future outcomes`, `how good is this`, `refactor`). Run
as written, the compliance record would have scored six correct routes as failures and invited
deleting real trigger phrases — the exact move the protocol forbids elsewhere. Tier D now asks its
three questions as three columns, and the in-scope column makes a load a **PASS**.

## 12. Addendum (2026-08-18, comprehensive from-scratch pass): consolidation verdict

Owner instruction: *"do a comprehensive review from scratch… delete all Oracle skills. Review all
others for substance and effectiveness, and optimize where appropriate. Feel free to delete and
merge when appropriate."* The Oracle deletion is §12.1. The consolidation verdict is §12.3, and it
is a negative result, which is the part worth reading carefully: **no merge and no deletion is
warranted on the current tree**, and the evidence for that is stronger than the evidence any
previous pass produced for its positive findings.

### 12.1 Oracle deletion (done)

17 skills across `oracle-fusion-finance-skills` and `oracle-otbi-skills`, 70 files, removed from
`archive/plugins/` entirely rather than left archived. The archived-plugin count therefore falls
from 9 to 7. Three follow-on removals were needed because the directive reaches further than the
plugins themselves:

- `coding-agent-skills:chicken-little` lost two reference files, one Do-it step, three trigger
  phrases, its named-Oracle-failure-modes section, and its Oracle-shaped `your-environment.md`.
  This **retires the owner-ratified exception** recorded in `MEMORY.md` on 2026-08-11 and analysed
  at §10; the later directive supersedes the earlier exception, and the analysis at §10 is left in
  place only because it is why the exception's stated reason was checkable at all.
- `coding-agent-skills:soviet-space-graphite` had an OTBI-specific worked verdict citing a "library
  fact" about a skill that no longer exists. Rewritten to carry the same lesson without the vendor.
- `decision-science-skills:reference-class-forecasting` named an OTBI export in its environment
  template. Generalized.

What remains and is *not* residue: Oracle as a SQL dialect in `sql-for-analysts` (portability is
the point), Oracle OTBI as one of five named BI products in `dashboard-design`, and "oracle" as the
testing term in `lean-six-sigma-for-software`. Those are the word, not the domain.

### 12.2 What was checked, and how to re-check it

Everything below is a command, not a judgement, so the next pass can reproduce it rather than
re-derive it:

| Check | Result |
|---|---|
| `bash scripts/validate.sh` | 0 errors, 0 warnings, 28 notes |
| `python3 scripts/check-arithmetic.py` (new) | 0 disagreeing chains across 410 files |
| `python3 scripts/gen-catalog.py` | 121 skills / 14 plugins, catalogs byte-identical on regeneration |
| Runnable-code sweep (191 blocks) | 84 PASS, 0 FAIL, 107 not independently runnable |
| Eval parity | 121 skills : 121 evals, 0 orphans either way |
| Eval asset references | 0 pointing at a `references/` or `scripts/` file that does not exist |
| Cross-links | 0 unresolved; 15 distinct archived targets across 37 pointers, all marked |
| Relative markdown links | 0 broken |
| Exact trigger collisions | 0 |
| Inbound-citation graph | 0 skills with zero inbound citations |
| Description promises vs content | 0 capabilities advertised in a description and absent from the skill |
| Pairwise description overlap | max Jaccard **0.168**, on the two Chicken Little autopsy editions |

Two of these are new instruments rather than new results. `check-arithmetic.py` closes the defect
class that appeared in *every* authoring wave and survived four hand passes;
`measure-listing-cost.py` closes the one where a number quoted in two documents drifts apart.

### 12.3 Consolidation verdict: nothing to merge, nothing to delete

The consolidation question was asked properly this time — by measurement first, then by reading the
candidates measurement produced — and it came back empty.

**Overlap.** The highest description overlap between any two of the 121 skills is 0.168 (Jaccard on
content words). For comparison, the pairs that *were* merged in earlier passes were obvious on
sight. Nothing in the current tree is a near-duplicate of anything else.

**The candidates measurement produced, and why each survives:**

- `chicken-little-executive-advisor` / `chicken-little-technical-compiler` (0.168) — two fixed
  autopsy protocols with different stages, different output structures, and different activation
  phrases (`deploy advisor` vs `deploy compiler`). Merging them yields one skill holding two
  mutually exclusive protocols behind two name-gates: strictly worse.
- `adams-plain-grade` / `adams-smart-brevity` (0.138) — the same Adams core aimed at opposite
  registers (5th-grade accessible vs professional-scanning). A merged skill would need a mode
  switch on the one axis that decides every sentence it writes.
- `full-stack-app-architecture` / `frontend-modern-ui` (0.148) — a stack-and-boundaries decision
  versus a layer's craft. Different questions, explicit seam in both.
- `extreme-ownership` / `stay-hard-accountability` (0.102) — leading a team versus driving
  yourself. The seam is stated in both descriptions and both bodies.
- `python-for-analysts` / `excel-automation-python` (0.124, cross-plugin) — overlap is the word
  "Python", not the work.

**Thinness is not redundancy.** The five thinnest skills (`reflective-learner` 148 lines,
`full-stack-app-architecture` 152, `supervised-modeling` 154, `lean-code-principles` 155,
`dmaic-problem-solving` 157) are all load-bearing: `dmaic-problem-solving` carries 14 inbound
citations, the second-most in its plugin, and `reflective-learner` carries 8. The honest finding is
the inverse of a deletion case — **the hub skills are the shallowest ones**, and the improvement
available is depth, not removal.

**The context-cost problem is not solved by deleting skills.** A full install costs ~19.4% of a
200K window by the harness's own real tokenizer (not the 14.8-14.9% this repo's char-based
estimate had reported — see `docs/live-routing-and-degradation-2026-08-18.md`), and the library
sits deep past the point where the listing silently degrades — at the default 200K/1% budget of
8,000 characters, only **3 of 121** skills keep a description (computed by
`scripts/simulate-listing-budget.py`; an earlier live-introspection figure of "101 of 121" is
withdrawn as unreproducible, and the mechanism account was corrected on 2026-08-19). Deleting the five
thinnest skills would recover about 1,200 tokens — 0.6% of a context — while removing genuinely
used content. Installing two plugins instead of fourteen recovers 11%.
The lever is skills *per install*; `README.md` carries the measured per-plugin and per-bundle
tables, and `scripts/measure-listing-cost.py` keeps them honest.

### 12.4 Substance fixes applied in this pass

Nine, each verified in place rather than merely changed:

1. **`fmea`** — the Action Priority table let a catastrophic-but-rare-and-detectable failure
   (S 9, O 2, D 3) rate **Low**, which is precisely the averaging-away the table replaced RPN to
   prevent. Rule 2 gained a severity ceiling. Swept all 1,000 (S, O, D) cells: 18 cells rated Low
   at S ≥ 9 before, 0 now (and 0 at S ≥ 7); 36 cells move, all Low → Medium; all five worked-example
   AP values unchanged.
2. **`rest-api-data-pulls`** — the pagination loop advanced `offset` by the requested page size, so
   a server returning a short page while `hasMore` stayed true silently skipped the rows it
   withheld. Now advances by `len(items)`.
3. **`pdf-data-extraction`** — `amount()` inverted the sign of a plain `-750.25`: the regex that
   strips parentheses also stripped the minus the negativity test never looked for. A sign
   inversion in a statement parser is the worst kind of quiet defect.
4. **`backend-api-development`** — the login snippet called `pwd.verify()`. `pwd` is a Python
   stdlib module with no such function, so the snippet shadows stdlib *and* does not run.
5. **`csv-and-flat-file-wrangling`** — `xxd` ships with vim; the POSIX `od` fallback is now given.
6. **`spaced-retrieval-learning`** — a "10–20% of the retention interval" rule contradicted the
   study it cited: Cepeda's own 70-day data point is ~21 days, where the rule yields 7–14. Replaced
   with the four reported intervals and a note that the proportion collapses at long delays.
7. **`anomaly-detection`** — step 6 attributed every alert by marginal robust z, which is blind by
   construction to the joint anomalies step 4's multivariate detectors exist to find. Added the
   branch, and the instruction to say plainly that no single value is out of range.
8. **`stakeholder-mapping`** — the worked example asserted that a re-map must reach both artifacts
   while showing artifacts that did not contain the change it described.
9. **`medical-research-detective`** — country inference resolved name-beats-city across a whole
   affiliation string rather than per segment, and carried a bare `wales` hint. Self-test 46/46
   with four regression cases added.

### 12.5 Privacy sweep

Two private project names remained in committed files (`adams-smart-brevity` ×3,
`weight-of-the-books`' environment template) after the `MEMORY.md` identity split. Both removed; a
token-level sweep of `MEMORY.private.md` against the whole committed tree now returns nothing but
ordinary vocabulary. One item is *not* removed and is a decision for the owner: see §12.6.

### 12.6 Open decisions from this pass

1. ~~**The `ut` brand pack in `assertion-evidence-deck`.**~~ **RESOLVED 2026-08-18** — the owner
   directed "genericize", overriding the recommendation to keep it unchanged. The palette and its
   WCAG analysis stay; the institution does not. `ut` → `warm-accent`, with the old name kept as a
   deprecated alias that resolves and prints a note, so no existing deck spec breaks. Doing the
   rename surfaced a real bug it would otherwise have hidden: the spec file's documented `"brand"`
   field was never read — `build()` took only the CLI flag — so a spec saying `"brand": "ut"` had
   been rendering neutral in silence. Now the flag overrides the spec and the spec is honoured when
   the flag is absent, which is what the schema always claimed.
2. **Depth for the five hub-but-thin skills** (§12.3). Not a defect; a ranked opportunity.
3. ~~**`docs/trigger-test.md` remains unrun.**~~ **SUPERSEDED — see §13.** It has since been run
   twice as a blind simulation and once live against the real harness.

## 13. Addendum (2026-08-18, later the same day): the live routing test, and two folklore corrections

Three follow-ups on the owner's earlier decisions: run the trigger test live against the real
harness rather than a simulation, re-measure the ~100-skill degradation claim properly, and check
whether the `script-wizard` guard pattern generalizes to a second skill.

### 13.1 The live test — real, not simulated

`claude plugin eval` and `claude plugin marketplace` are real shipped commands, gated behind a
per-organization early-access flag openable per-shell via `CLAUDE_CODE_WALNUT_SPIRE=1` (not
committed to any settings file). All 14 plugins were installed for real; seven live routing cases
were run as genuine agent turns graded on the actual `Skill`-tool transcript. Total real spend:
≈$0.93, disclosed because this mechanism spends real money per run.

**Headline finding: every PASS this protocol has ever recorded — including the freshly-repaired
D2/D9 seams — was measured against a full, undegraded listing. Run for real, both failed with
zero `Skill` calls**, because their target's description was, at the time, invisible in this
session's real listing. A routing fix verified by simulation is conditional on the description
being visible at all, and a realistic full install does not reliably provide that. Full method
and every case: `docs/live-routing-and-degradation-2026-08-18.md`.

### 13.2 The ~100-skill folklore, corrected

The standing `MEMORY.md` lesson ("~100 installed skills trims least-used descriptions to
name-only," one anecdotal 2026-07-18 observation from an unrelated project) is refined rather than
superseded.

> **This paragraph was itself wrong, and is corrected here (2026-08-19).** It originally declared
> the folklore "superseded, not merely caveated," and asserted the mechanism was a fill in listing
> order with a hard cutoff, "mechanistically different (order, not usage)." An independent audit —
> run by agents that did not write these documents — sent me back to the shipped binary, where the
> sort key turns out to be `usageCount × max(0.5^(daysSinceUse/7), 0.1)`. **The folklore named the
> right variable and this "correction" replaced it with a wrong one.** The install-order pattern
> that was observed is the degenerate all-zero-usage case: in a fresh session every score is 0, so
> the stable sort preserves listing order. There is also no cutoff — the fill skips oversized
> entries and continues. And the "101 of 121" figure came from a model introspecting its own
> system reminder, an instrument that did not reproduce on re-test; it is withdrawn in favour of
> `scripts/simulate-listing-budget.py`, which computes the answer from the algorithm.

What survives, with the corrected numbers: the severity finding, and it is worse than published.
At the genuine 200K default the budget is 8,000 characters against 113,677 needed, so **3 of 121
skills keep a description and 118 route on bare names**. The earlier "19 survivors ≈ 2.3% of 200K"
was measured in a session whose real budget was ~30,000 characters (a ~750K context) and then
reported as a fraction of 200K, which understated the problem. The one mitigation the real
mechanism supplies is that usage-weighting means a returning user's working set keeps its
descriptions — the arbitrary case is a first session on a fresh install, not the steady state.

Separately, `claude plugin details` gave a second, real-tokenizer-computed cost figure —
**≈38,800 tokens (≈19.4% of 200K)** — about 30% above this repo's own chars/3.7 estimate
(≈29,700 tokens, ≈14.9%). Both figures are now cited together wherever this repo quotes install
cost, with the real one primary.

### 13.3 `script-wizard`, checked for a sibling — none found

Before writing more Tier C guards on the pattern that caught `script-wizard`'s over-breadth, the
library was searched for a second skill carrying the same defect signature (an explicit,
unqualified breadth claim — "even when phrased casually" or equivalent). Only `script-wizard`
carries it. The next-broadest candidate, `sparring-partner` ("any work product"), was checked
against the same standard and found meaningfully different: two reciprocal seams already repaired
this session, and no narrower same-purpose sibling in this library for generic single-artifact
critique — unlike `script-wizard`, whose breadth competed directly with siblings owning more
precise vocabulary. **No second skill warrants a new guard row.** Recorded so this search is not
repeated.

---

## 14. Addendum (2026-08-19): the substance census, and a correction to this document

Two things happened in this pass. The census that §9.7 recorded as unmet was run to completion,
and an independent audit found that the *previous* pass's headline finding — published in this
document as verified fact — was wrong. The second is the more important result, so it comes first.

### 14.1 This document's own mechanism claim was wrong, and the folklore it "corrected" was right

§9.3, §12.3 and §13.2 asserted that the skill-listing degradation is "a character budget filled in
listing order with a hard cutoff … **not** a priority ordering by usage," and on that basis
declared a 2026-07-18 note ("trims least-used descriptions") superseded.

Read out of the shipped CLI binary (v2.1.235), the selection is:

```
budget   = SLASH_COMMAND_TOOL_CHAR_BUDGET, else floor(context_tokens × 4 × 0.01) = 8,000 chars
baseline = every non-bundled skill rendered "- name"      (bundled skills are protected)
order    = DESC by usageCount × max(0.5^(daysSinceUse/7), 0.1)     (never used ⇒ 0)
fill     = greedy upgrade to full text; if it does not fit, SKIP IT AND CONTINUE
```

It **is** usage-ordered, there is no cutoff, and the folklore named the right variable. The
install-order pattern the previous pass observed was real but was the degenerate all-zero-usage
case: in a fresh session every score is 0, so a stable sort preserves listing order. The pass
mistook the boundary condition for the mechanism.

The severity was also misreported. "19 FULL ≈ 2.3% of a 200K window" was measured in a session
whose real budget was ~30,000 characters (≈750K context) and then expressed as a fraction of 200K.
At the genuine default the library needs 113,677 characters against 8,000 available, and **3 of 121
skills keep a description**. The published figure understated the problem.

And the "101 of 121 NAMEONLY" figure came from asking a model to introspect its own system
reminder. It did not reproduce on re-test. It is withdrawn, and replaced by
`scripts/simulate-listing-budget.py`, which computes the answer from the algorithm and can be run
by anyone offline. Two further defects of the same family were found and fixed: a completeness
claim ("every place this repo quotes 14.8% is now corrected") that was false when written, and a
"proof" in `trigger-test.md` that both failing seam pairs "already carried reciprocal body seams" —
git shows one pair was one-directional and the other had no seam at all.

**The lesson worth keeping** is not "check your numbers." It is that the word *live* did the
damage: a real measurement, honestly obtained, licensed a generalisation the measurement could not
support, and the provenance made it feel unfalsifiable. An observation of behaviour is not a
mechanism. And when you overturn a prior claim, you owe an account of why the old claim produced
the evidence it did — here that account was missing, which is exactly where the error hid.

The auditors were wrong in places too, which is part of the record: one asserted
`skillListingBudgetFraction` does not exist in the CLI (it occurs four times, and the CLI's own
warning names it), and two auditors gave contradictory accounts of the algorithm. Adversarial
review manufactures confident false findings alongside true ones. The primary source settles it.

### 14.2 The census: 121 of 121, closing D6

Run in two phases — 83 quantitative skills verified by executing code, 38 qualitative skills judged
against a strong unaided baseline — with every finding adversarially refuted by a second expert and
every value verdict independently re-formed.

| | Reviewed | NET-POSITIVE | MARGINAL | NET-NEGATIVE |
|---|---:|---:|---:|---:|
| Phase 1 (quantitative) | 83 | 59 | 24 | 0 |
| Phase 2 (qualitative) | 38 | 21 | 17 | 0 |
| **Total** | **121** | **80** | **41** | **0** |

Findings: **134 raised → 69 confirmed** (22 major, 47 minor), **65 refuted**, and **131 claims
recorded as "could not verify in this environment"** rather than asserted — that last number being
the one that most distinguishes this pass from the four that preceded it.

**The 14-skill sample did not generalise.** It returned 3 NET-NEGATIVE and 6 MARGINAL — nearly
two-thirds marginal-or-worse — and the census returns **zero** NET-NEGATIVE across 121. §9.7 was
right to refuse to extrapolate it, and right that assuming the unreviewed 107 were better was not
warranted either. Both cautions held; the answer simply came out better than the sample implied.
Part of that is real improvement (the NET-NEGATIVE cases in the sample were *fixed* in that pass),
and part is that the sample was deliberately drawn toward fast-decaying technical skills.

The honest caveat: **41 MARGINAL is a third of the library**, and that is the number to act on. A
MARGINAL verdict means the skill mostly restates what a competent current-generation assistant
already does. It is not a defect, and the owner has already declined a trim — but it is the
strongest available signal about where depth would pay.

### 14.3 What the census found that conformance could not

The high-severity defects were, without exception, invisible to every previous pass because they
required *running something*:

- **`dmaic-problem-solving`** computed a combined false-alarm rate by adding four per-rule rates.
  The rules overlap, so union ≠ sum: true ARL₀ ≈ 92 points, not 52 — the published rate was ~75%
  too high. Confirmed by a Markov chain and an independent 40,000-run Monte Carlo (91.58 ± 0.43),
  both calibrated against the known closed forms 370.4 and 255.
- **`realtime-and-dynamic-features`** shipped an optimistic-mutation recipe that throws on a cache
  miss *inside* `onMutate`, so the mutation is rejected and `mutationFn` never runs — the server
  write silently does not happen while the UI shows the click as accepted. Verified against
  `@tanstack/query-core@5.101.4`.
- **`full-stack-app-architecture`** shipped an import-boundary test with a false negative: built on
  a real tree, it reported zero violations while one feature genuinely imported and read another's
  private module. `from pkg import name` binds a submodule when the name is one.
- **`medical-research-detective`** flagged ordinary papers as retracted by unanchored substring
  match — and the caller turns any signal into "do not use as support," i.e. it told researchers to
  discard valid evidence.
- **`git-and-code-review`** taught `git merge main`, which merges a stale local ref and prints
  "Already up to date." with exit 0 while the real `origin/main` has moved.
- **`adams-smart-brevity`** told the assistant to rewrite litigated phrasing wherever it appears,
  with no carve-out for language a rule requires verbatim — where clarity can void a safe harbour.

Cross-plugin coherence was swept separately, because batching by domain makes a defect spanning two
plugins invisible to every batch: 41 alleged contradictions, **1 upheld** (`pre-mortem` multiplying
risk dimensions in the exact way `fmea`'s reference generalises a prohibition against — the defect
already fixed in `fmea` and never swept to its sibling), plus five under-specification seams worth
fixing.

**A defect class worth naming: fixes do not propagate to siblings.** `pre-mortem` carried the
arithmetic `fmea` had already been repaired for. Whatever is fixed in one skill should be grepped
for across the others that share the technique.
