# Library overhaul: re-aim to a career-portable general-use skills library

> **This file is the PR description for PR #39.** Paste its contents into the PR body on
> GitHub. It lives in the repo because this session's GitHub API cannot reach the renamed
> `CatCorner22/Claude_Skills_2` (git push works — GitHub redirects — but API calls 403).

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

**Finalization** — 9 trigger-phrase collisions resolved (now **1298 phrases, zero
collisions**), 50 descriptions trimmed for headroom (validator notes 57 → 19), README and
CONTRIBUTING corrected (both still described the pre-archive library; CONTRIBUTING's "Next:"
section contradicted the repo's own standing directive), dated status stamps on all five
research docs, and the **first-ever coherence audit of the eval suite**: 95 of 121 coherent,
zero positive-prompt drift, 3 dead near-miss references fixed, 22 files cleared of
archived-domain scenarios.

## 5. Tooling

- `scripts/gen-catalog.py` — parser bug fixed; refactored into `collect()` + emitters; now
  also generates **`docs/INDEX.md`**, a when-to-use / optimized-for / how-to-trigger router
  grouped by category with an archived-plugins manifest. Two lead-clause extraction bugs
  fixed along the way (the first truncated 86% of the capability column; the second returned
  fragments like "Turns any material" where an em-dash opened a paired appositive).
- `scripts/validate.sh` — per-skill error flag; non-gating NOTE tier at >973 chars.

## Verification

```
bash scripts/validate.sh      # 0 errors, 0 warnings
python3 scripts/gen-catalog.py # 121 skills across 14 plugins (+9 archived)
```
- 121 skills ↔ 121 evals, no orphans.
- 1298 trigger phrases, **0 collisions**.
- 0 unresolved cross-links; 0 `board-of-advisors-skills` references in the active tree.
- 14 marketplace entries ↔ 14 plugin directories, names and versions reconciled.
- All 14 plugins version-bumped — **installed copies only pick up changes on a bump**, so run
  `claude plugin update <plugin>@treasury-analyst-skills` for the ones you have installed.

**Not covered by any automated pass:** the evals have never been *executed*. Real trigger
testing needs fresh interactive sessions, which no agent in this work could do cleanly. The
audit verified their static coherence — that each eval tests the route its skill actually
advertises — but the ~360 scenarios remain unrun.

## Notes

- The marketplace ID stays **`treasury-analyst-skills`** deliberately, for install
  compatibility. Renaming it would break every existing `<plugin>@treasury-analyst-skills`
  reference. The name is stale; the breakage would be worse.
- `coding-agent-skills:chicken-little` keeps its Oracle Fusion data-model reference by
  ratified exception: it is name-gated (zero routing pollution) and the only surviving copy of
  that commissioned depth. Recorded in `MEMORY.md` so future residue sweeps don't re-flag it.
- **Security housekeeping:** the deleted `GITHUB_SETUP.md` had committed an `ssh-ed25519`
  deploy **public** key and an expired device code. The public half discloses nothing on its
  own, but if that deploy key still exists on the repository, revoke it in GitHub settings —
  independently of this PR.
- Two standing process rules were adopted from what these passes found, and are now in
  `MEMORY.md`: **arithmetic-verify every worked example before ship** (it failed in every
  authoring wave), and **run a reciprocal-link pass on every new-skill wave** (six of eight
  new skills landed as citation sinks with zero inbound links).

Full narrative: `docs/library-review-2026-08.md`.
