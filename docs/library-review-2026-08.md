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
  that commissioned depth in the repo.

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

- **A full install is past the observed degradation threshold.** At roughly 100 installed skills the
  listing begins trimming the least-used skills' descriptions to **name-only** — silently, with no
  error, while `/plugin:skill` direct invocation keeps working. That is precisely the path an author
  uses to test their own skill, so the failure is invisible from the inside.
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
Measured now, **85 distinct trigger phrases still appear as whole words inside a different skill's
description prose** — `python` in 7 other descriptions, `pipeline` in 6, `code review` in 3.
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
- **Only 14 of 121 skills received expert substance review.** The value-test verdicts above are a
  sample, not a census. Extrapolating them is not warranted; neither is assuming the unreviewed 107
  are better.
- **85 whole-word prose collisions remain.** They are recorded and measured, not fixed. Fixing them
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

**D2 — `coding-agent-skills:chicken-little` is still mounted on the archived Oracle domain.** *(found
in this pass; the sharpest tension with your archive directive)*
This is the one place where archived-domain content sits in the **always-loaded routing payload**, not
behind an opt-in reference. The skill's description advertises "deep Oracle Cloud Fusion Financials
data-model knowledge (AP, AR, CoA/GL, XLA tables and statuses)" and "named Oracle failure modes"; **3
of its 7 trigger phrases** are Oracle-specific (`invoice black hole`, `ghost receipts`, `orphan
distributions`); and `references/oracle-fusion-data-model.md` (144 lines) is listed as a live
reference. Your directive was to archive all Oracle/Fusion/OTBI/treasury skills, but this is a
*multi-domain persona you drafted* that happens to include Oracle among Python, Lean Six Sigma, and
project management — so archiving it wholesale is not obviously what you asked for.
→ **Recommendation: de-mount rather than archive.** Move `oracle-fusion-data-model.md` to `archive/`,
strip the Oracle clauses and the three Oracle triggers from the description, and keep the persona's
portable layers. That is the pattern already applied to `assertion-evidence-deck` and
`rest-api-data-pulls` in this session. **Not done pending your call**, because it materially changes a
persona you authored.

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
