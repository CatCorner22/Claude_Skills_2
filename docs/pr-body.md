# Library overhaul: re-aim to a career-portable general-use skills library

> **Status (2026-08-17): this is an in-repo narrative record, not a pending action.**
>
> It was written as the PR body for **#39** because the GitHub API could not reach the renamed
> `CatCorner22/Claude_Skills_2` at the time (git push worked — GitHub redirects — but API calls
> 403'd), so there was no way to post it. That has since resolved: the API reaches the repo again,
> **#39 is merged**, and the follow-on work has its own posted body on **#40**. Nothing here needs
> pasting anywhere.
>
> The file is kept because PR descriptions are easy to lose and this is the fullest single account
> of the overhaul. **Read §1–§5 as the record of #39** (archive, consolidation, the eight new
> skills, the four review passes) and **§6 onward as the from-scratch pass**, which lands in #40 and
> corrects several claims in §1–§5. Where the two disagree, the later section is right — the earlier
> text is deliberately left standing so the corrections are visible rather than quietly rewritten.

## What this does

Re-aims the library from a treasury/Oracle-centric catalog to a **career-portable,
general-use** one, then reviews and finalizes every skill in it.

**Before:** 181 skills / 24 plugins, mixed domain-specific and general.
**After:** **121 active skills / 14 plugins**, all domain-neutral and role-portable, with
68 domain skills preserved in `archive/` and every active skill line-reviewed.

Reviewing this diff: pass `-M` (detect renames) and hide whitespace. Of ~580 changed paths,
**~290 are pure directory moves** — the archive. Real content change is roughly 290 files.

## 1. Archive (delisted, preserved, restorable)

Nine plugins / 66 skills moved to `archive/plugins/` + `archive/evals/` with full git
history: `oracle-fusion-finance-skills`, `oracle-otbi-skills`, `sponsored-projects-ar-skills`,
`cash-management-skills`, `treasury-accounting-skills`, `public-sector-treasury-skills`,
`accounting-skills`, `banking-skills`, `finance-skills`.

Two dental-mounted skills archived at skill level to `archive/skills/`:
`curve-hero-design-language`, `chicken-little-college-kid`.

All 66 cross-references from active skills into archived plugins were rewritten — re-pointed
to a verified active sibling where a real seam exists, otherwise plain prose with an explicit
`(archived: plugin:skill, restorable from archive/)` pointer. **Locally installed copies of
archived plugins keep working** — installs are version-pinned snapshots; they simply stop
receiving updates and leave the marketplace listing. Manifest and restore procedure:
`archive/README.md`.

Also archived: two separate dental "notes standardizer" apps, their benchmark docs and
validation record, and an Oracle-era Python tool — all previously at the repo root or
`tools/`, none referenced by any skill. See `archive/apps/README.md`. The repo root is now
the marketplace only.

## 2. Consolidation

`board-of-advisors-skills` (1 skill + 6 subagents) **merged into `coding-agent-skills`** —
now `coding-agent-skills:board-review`, with the six specialist advisors at
`plugins/coding-agent-skills/agents/`. A one-skill plugin was pure install friction. It is
now the only plugin shipping subagents.

## 3. New skills (8)

Built from a research-verified dossier (`docs/research/general-use-expansion-research.md`)
with collision-scanned triggers and misattribution corrections carried as teaching content:

| Skill | Plugin | Verified anchor |
|---|---|---|
| `causal-inference` | data-analytics-bi | Pearl DAGs; DiD/IV/RDD; Hill's 1965 *viewpoints* (not criteria) |
| `ab-test-design` | data-analytics-bi | Kohavi canon; SRM, peeking, MDE; Twyman's law via Ehrenberg |
| `survey-and-sampling-design` | data-analytics-bi | Groves total survey error; Dillman; Literary Digest died of **nonresponse** (Squire 1988) |
| `bayesian-updating` | decision-science | Natural frequencies; Tetlock update discipline; honest Bayes/Price/Laplace history |
| `technical-documentation` | writing | Diátaxis; ADR (Nygard 2011); Django's docs **predate** Diátaxis |
| `executive-briefing` | collaboration | BLUF doctrine (DA Pam 600-67, 1986); Minto SCQA; completed staff work, dual attribution |
| `stakeholder-mapping` | collaboration | The power-interest grid is Johnson & Scholes / Eden & Ackermann — **not in Mendelow 1981** |
| `reproducible-analysis` | data-tools | Knuth; FAIR; the ACM used reproducible/replicable backwards 2013–2020 |

## 4. Review passes — what each one actually found

Every active skill was line-reviewed. Findings, not vibes:

**Mechanical audit** — came back clean: 181/181 skills had conforming evals, references,
names, descriptions, and section order. The defects were in the *tooling*: `gen-catalog.py`'s
frontmatter parser leaked bare `metadata:` keys into 33 catalog entries as fake triggers, and
`validate.sh` suppressed every per-skill OK line after the first error anywhere.

**Adversarial review** (15 agents: 7 reviewers → 7 skeptics → synthesis; 62 raw findings, 23
refuted, **39 confirmed → 30 work items, all executed**). The dominant defect class was
**worked-example arithmetic** — the part a reader lifts and reuses:
- `causal-inference`'s collider example taught the induced association **with the sign
  inverted**, and its two conclusion sentences contradicted each other.
- `spreadsheet-modeling`'s cross-foot "check" was an algebraic tautology that could not fire
  on the error the narrative claimed it caught; its breakeven was 7 points off its own inputs.
- `excel-automation-python`'s verification assertion ended in `or True` — dead code, in the
  block the skill stakes its trust argument on.
- `ml-project-framing`'s leakage remedy did not fix the leak it named.
- `ab-test-design`'s A/A guidance recreated the peeking setup its own §5 condemns.
- `assertion-evidence-deck` was the last standing-directive breach: it named the former
  employer and an internal ERP nickname **in its published routing contract**, and its build
  script defaulted `--brand` to that employer's palette. De-mounted; the palette survives as
  an explicit non-default legacy option.

**Text optimization** (10 agents) — 19 skills optimized, **27 confirmed already at standard
and left untouched**. The recurring gap was a missing *deliverable contract*: 12 skills taught
a method but never stated what the finished artifact contains. Also activated
`ui-and-ux-inspection`'s Fitts/NASA-TLX instruments, which had sat in a reference file its
Do-it never invoked.

**Closing assessment** (9 agents, arithmetic-first) — 10 more worked-example defects, 31
skills confirmed at standard. `reliability-engineering` claimed "~one failure every four
months" where its own SLO gives ~5.5; `weight-of-the-books` projected 7-year retention at
~97M rows by ignoring the +12%/yr growth its own manifest states (~140M);
`exponential-growth-and-logs` — a skill that *teaches* this math — shipped a false same-CAGR
equation; `medical-research-detective` said "the relative risk is 100%" for a doubling,
readable as RR = 1.0.

**Finalization** — 9 trigger-phrase collisions resolved, 50 descriptions trimmed for headroom,
README and
CONTRIBUTING corrected (both still described the pre-archive library; CONTRIBUTING's "Next:"
section contradicted the repo's own standing directive), dated status stamps on all five
research docs, and the **first-ever coherence audit of the eval suite**: 95 of 121 coherent,
zero positive-prompt drift, 3 dead near-miss references fixed, 22 files cleared of
archived-domain scenarios.

> **Corrected by §6.** Two claims in this Finalization paragraph did not survive re-measurement, and
> are left above as written so the record shows what changed. (1) The **50 description trims were
> unnecessary** — the validator was counting bytes rather than characters, so none of those
> descriptions had ever exceeded the cap; 12 of the trims destroyed routing or teaching signal and
> have been reverted. (2) **"Zero collisions" means zero *exact duplicate strings*, not unambiguous
> routing** — the router matches whole descriptions, and 111 phrases still compete inside other
> skills' prose. The live phrase count is 1,328.

## 5. Tooling

- `scripts/gen-catalog.py` — parser bug fixed; refactored into `collect()` + emitters; now
  also generates **`docs/INDEX.md`**, a when-to-use / optimized-for / how-to-trigger router
  grouped by category with an archived-plugins manifest. Two lead-clause extraction bugs
  fixed along the way (the first truncated 86% of the capability column; the second returned
  fragments like "Turns any material" where an em-dash opened a paired appositive).
- `scripts/validate.sh` — per-skill error flag; non-gating NOTE tier at >973 chars. Two further
  changes from the from-scratch pass: description length is now counted in **characters** (it was
  counting bytes via `wc -m` under a C locale, over-charging every em dash by two across 112 of 121
  skills), and **cross-link resolution is now enforced** rather than eyeballed — every
  `plugin:skill` reference resolves against active skills, active subagents, and `archive/`, and
  errors if it resolves to none of them or points at an archived target without saying so.
- `scripts/gen-catalog.py` — a third lead-clause bug fixed: the capability clause could run past a
  sentence boundary and trail the next sentence's opening words into the INDEX cell. Verified by
  diffing all 121 generated rows; exactly the 2 intended rows changed.

## 6. From-scratch pass (2026-08-17) — substance and routing

Sections 1–5 describe passes that all checked **conformance**. This pass asked the two questions
none of them had: *is the advice correct?* and *does the library actually route?* It treated the
earlier work — including its own — as suspect, and briefed domain experts to verify by **executing
code and re-deriving results** rather than by reading.

- **The authoring standard had drifted from the library it governs.** `writing-agent-skills` is the
  reference every skill conforms to, so no conformance check can detect a fault *in it*. Four were
  present: an Oracle directive breach in its tailoring exemplars, a template that contradicted its
  own frontmatter rules, token math wrong by an order of magnitude in two directions that cancelled,
  and a checklist missing every guard this session had to learn the hard way. All fixed.
- **~45 substance defects fixed across 19 skills**, including six that taught something *false* and
  would have survived any conformance check: ROC AUC's prevalence mechanism (stated backwards —
  resampling does not move AUC), MASE < 1 as a ship/no-ship rule (unreachable at h=13 on a random
  walk), rank tests as drop-in tests of means (a verified case where the arm with twice the revenue
  is declared *dominated*), resolution IV promised for designs that are resolution III, a Weibull
  β fitted to a repairable system, and a test-isolation setting that actively leaks rows between
  tests.
- **Three of eight claims briefed to one reviewer did not survive contact with a real install** —
  including a SQLAlchemy warning that no longer fires, making a silent data-loss bug worse than
  documented. Reviewers were explicitly instructed to report defects *in the brief* as findings.
- **46 description trims from an earlier pass were unnecessary** — the byte-counting bug above meant
  none had ever exceeded the cap. 12 that destroyed routing or teaching signal are reverted, with
  trigger lists verified byte-identical so no routing contract moved.
- **Routing viability**: the full 121-skill library costs **14.9% of a 200K context** before anything
  is asked, and sits past the ~100-skill point where the listing silently trims descriptions to
  name-only. `README.md` now carries a per-plugin cost table and recommends three or four plugins.
  The corollary, stated plainly rather than defended: description trimming was never the lever —
  skills per install is, by a factor of ~145.
- **`docs/trigger-test.md` (new)**: 45 risk-ranked rows with exact prompts, expected skill,
  near-miss, and a pass/fail log — covering the skills that lost trigger phrases, the phrases that
  moved, over-broad single-word triggers, the persona-gated skills, and everything rewritten today.

Full narrative and an 8-item owner decision list: `docs/library-review-2026-08.md` §9–§10.

## Verification

```
bash scripts/validate.sh      # 0 errors, 0 warnings
python3 scripts/gen-catalog.py # 121 skills across 14 plugins (+9 archived)
```
- 121 skills ↔ 121 evals, no orphans.
- **0 exact duplicate trigger phrases** — but read that precisely: the router matches whole
  descriptions, not `Triggers:` lists, and **111 trigger phrases still appear as whole words inside a
  different skill's description prose** (`python` in 7 others). The earlier "0 collisions" headline
  was true at the string level and misleading at the routing level; the collision was renamed, not
  resolved. Those 85 are measured and recorded, not fixed.
- 0 unresolved cross-links — now **enforced by `validate.sh`**, not audited by hand.
- 14 marketplace entries ↔ 14 plugin directories, names and versions reconciled.
- All 14 plugins version-bumped — **installed copies only pick up changes on a bump**, so run
  `claude plugin update <plugin>@treasury-analyst-skills` for the ones you have installed.

**Two verifications this PR does not have, stated plainly:**

1. **The fresh-session trigger test has never been run, for any skill.** It is the only check that
   validates routing, and it cannot be run from a session that already knows the answer.
   `docs/trigger-test.md` now provides the runnable protocol; the compliance log is **empty**.
   Nothing in this library's history establishes that any skill routes.
2. **The evals have never been executed** — ~360 scenarios remain unrun. Their static coherence was
   audited (each eval tests the route its skill actually advertises), which is a different and much
   weaker claim.

**And one bound on scope:** only **14 of 121 skills** received expert substance review. On that
sample, 3 were NET-NEGATIVE and 6 MARGINAL against the test "does invoking this beat an unaided
competent assistant?" — every one of them conformant, and rated passing by four prior passes. The
sample was drawn toward technical skills where staleness is most likely, so it should not be
extrapolated to the whole library; neither should the unreviewed 107 be assumed better.

## Notes

- The marketplace ID stays **`treasury-analyst-skills`** deliberately, for install
  compatibility. Renaming it would break every existing `<plugin>@treasury-analyst-skills`
  reference. The name is stale; the breakage would be worse.
- `coding-agent-skills:chicken-little` keeps its Oracle Fusion data-model reference by
  ratified exception: it is name-gated and the only surviving copy of that commissioned depth.
  Recorded in `MEMORY.md` so future residue sweeps don't re-flag it. **Correction from this pass:**
  the original rationale said "zero routing pollution", which is not accurate — 3 of the skill's 7
  triggers are Oracle domain phrases rather than the persona name, and about a third of its
  always-loaded description is Oracle specifics. The exception is *bounded and accepted*, not zero.
  The decision is unchanged; only the reason is corrected, because a falsifiable justification
  invites the next audit to re-derive the finding and re-open a settled call — which is exactly what
  happened here.
- **Security housekeeping:** the deleted `GITHUB_SETUP.md` had committed an `ssh-ed25519`
  deploy **public** key and an expired device code. The public half discloses nothing on its
  own, but if that deploy key still exists on the repository, revoke it in GitHub settings —
  independently of this PR.
- Standing process rules adopted from what these passes found. The first two came from the earlier
  passes: **arithmetic-verify every worked example before ship** (it failed in every authoring wave),
  and **run a reciprocal-link pass on every new-skill wave** (six of eight new skills landed as
  citation sinks with zero inbound links). The from-scratch pass added, among others: **a conformance
  regime cannot audit its own reference**; **verify a measurement before acting on it** (the byte-vs-
  character bug drove 46 pointless edits); **never resolve a trigger collision by deleting the
  loser's phrase** (doing so left `standardize` with no owner at all and broke a live route in
  `exploratory-data-analysis`); and **put the guard where the author works** — rules that lived only
  in `MEMORY.md` were re-learned repeatedly, so each now lands in `review-checklist.md` too, and the
  automatable ones went into `validate.sh`.

Full narrative: `docs/library-review-2026-08.md`.
