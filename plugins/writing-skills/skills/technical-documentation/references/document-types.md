# Document types — the full method

Provenance legend: **[snippet-only]** = verified via cross-checked WebSearch result
blocks (per the general-use expansion dossier, §5); direct fetches of diataxis.fr and
keepachangelog.com were egress-blocked, so every Diátaxis and Keep-a-Changelog claim
below carries that mark. Re-verify against the primary sites before quoting externally.

## Contents
1. [The Diátaxis router](#1-the-diátaxis-router)
2. [The quadrant audit protocol](#2-the-quadrant-audit-protocol)
2a. [Owner, cadence, and "last verified" — the time-triggered half](#2a-owner-cadence-and-last-verified--the-time-triggered-half)
3. [README anatomy — the first screen](#3-readme-anatomy--the-first-screen)
4. [Architecture Decision Records](#4-architecture-decision-records)
5. [Changelog + semantic versioning](#5-changelog--semantic-versioning)
6. [Routine procedure docs and their seams](#6-routine-procedure-docs-and-their-seams)
7. [API and reference-doc discipline](#7-api-and-reference-doc-discipline)
8. [Docs as code](#8-docs-as-code)
9. [Worked example: one recurring analysis, four documents](#9-worked-example-one-recurring-analysis-four-documents)

## 1. The Diátaxis router

Daniele Procida derived four documentation forms from two axes — what the reader is
doing (acquisition of skill vs application of skill) and what they need (practical
action vs theoretical cognition) [snippet-only]:

| Form | Reader's state | Job | Voice | Cardinal sin |
|---|---|---|---|---|
| **Tutorial** | Learning, no context yet | A lesson that works end-to-end | "We will…" (teacher leads) | Offering choices; steps that can fail |
| **How-to guide** | Working, has a goal | Get one job done | "Do X, then Y" (recipe) | Teaching concepts mid-task |
| **Reference** | Working, needs a fact | Complete, accurate lookup | Dry, uniform, structured like the machinery | Narrative; persuasion; gaps |
| **Explanation** | Reflecting, wants the why | Understanding, context, trade-offs | Discursive, admits alternatives | Step-by-step instructions |

Routing questions, in order:
- Is the reader *acquiring* skill or *applying* it? (acquiring → tutorial/explanation;
  applying → how-to/reference)
- Do they need *action* or *understanding*? (action → tutorial/how-to; understanding →
  explanation/reference)

Honesty notes carried from the dossier [snippet-only]:
- Attribute the framework to Procida (presented at conferences from 2017, including
  "What nobody tells you about documentation," PyCon Australia 2017; earlier written up
  as "the Divio documentation system," later named Diátaxis at diataxis.fr).
- Adoption is commonly cited at Canonical/Ubuntu (where Procida later directed
  documentation practice), Cloudflare, and Gatsby. Django's four-part docs structure
  *predates* the framework — Procida is a long-time Django community figure and the
  framework systematized existing practice; never claim "Django adopted Diátaxis."
- The Python project ran a public discussion about adopting it (discuss.python.org) —
  "considered/partially applied," never "restructured wholesale."

## 2. The quadrant audit protocol

For an existing docs corpus that "nobody uses". **Audit on three axes, not one** — form (is it
filed right?), ownership (does anyone answer for it?), and freshness (is it still true?). A page
can be perfectly filed, beautifully written, and quietly wrong, and a form-only audit is blind to
exactly that page.

1. List every page/section as a row: title, current location, one-line summary, **owner (a person's
   name), last-verified date, review cadence**.
2. Assign each row a quadrant (T / H / R / E). Force a single choice; "both" means the
   section blends forms and gets split.
3. Flag the misfits: how-to steps buried in explanations, reference tables inside
   tutorials, why-discussions inside how-tos. Each misfit is one fix-list item: move,
   split, or rewrite in the target form.
4. **Flag the unowned and the unverified — the second fix list.** Any row with a blank owner, a blank
   last-verified date, or a last-verified date older than its cadence is a finding, independent of how
   well it is filed. This list is usually longer than the misfiled one and is the reason the corpus
   is distrusted.
5. Check coverage *against need*, not symmetry: a library needs a strong reference and
   a first tutorial; an internal process needs how-tos and one explanation. Empty
   quadrants are only gaps if a real reader arrives in that state.
6. Wire the navigation so each form links sideways (tutorial → reference for details,
   how-to → explanation for the why) instead of inlining the other form.
7. **Resolve every unverified row one of three ways — and "leave it" is not one of them:**
   **verify** it (do the specific check, stamp the date), **fix** it, or **retire** it (delete, or
   mark deprecated with a date and a pointer to what replaced it). An unowned, unverified page costs
   more than no page, because a reader cannot tell it from a live one; deletion is a legitimate and
   often correct outcome. Without a retirement path a staleness audit produces guilt instead of a
   cleaner corpus.

Row template that makes the three axes visible:

| Page | Form | Owner | Last verified | How verified | Cadence | Verdict |
|---|---|---|---|---|---|---|
| Run sheet: monthly extract | H | <name> | 2026-08-04 | ran it | on each use | current |
| Data dictionary | R | <name> | 2025-11-12 | diffed vs schema | quarterly | **stale — verify** |
| Utilization method note | E | *(blank)* | *(never)* | — | annual | **unowned + unverified** |

## 2a. Owner, cadence, and "last verified" — the time-triggered half

Docs-as-code (§8) is **change-triggered**: a behaviour change and its doc change ride the same PR,
so review catches drift at the cheapest moment. That works beautifully for a doc sitting beside the
code it describes, and does nothing at all for the docs people actually complain about — the method
note, the data dictionary, the run sheet. Those rot without anyone's PR ever touching them: the
upstream team renames a column, the assumption behind a definition stops holding, the tool the run
sheet drives ships a new menu. No commit in your repo, no review, no signal. The complement is
**time-triggered** review, and it needs three cheap mechanisms.

**1. A named owner — one person, in the page.** "The team owns it" means nobody does. The owner's job
is *not* to write the page; it is to answer for whether it is still true, and to be the name a reader
can ask. Where a page has genuinely no owner, that is the finding: either someone adopts it or it
gets retired.

**2. A review cadence set by the page's rot rate**, not by a uniform policy — and Diátaxis form is a
good predictor of rot rate, so the router does double duty:

| Form | How it rots | Cheapest verification | Cadence |
|---|---|---|---|
| **Tutorial** | Fastest and most visibly — it must run end to end, so any change on the path breaks it | **Run it.** Mechanical, and automatable in CI where the path allows | Every release touching the path, plus a scheduled run |
| **How-to / run sheet** | When the system or tool it drives changes | The operator verifies **on use** and stamps the date — the cheapest cadence there is, because it rides work already happening | On each use (flag if unused for a period — an unused run sheet may be a dead process) |
| **Reference / data dictionary** | Silently, and worst — nobody notices a wrong column until a decision rests on it | **Diff the generated regions against the source** (§7); the hand-written residue needs a read | Quarterly, or on any upstream schema change |
| **Explanation / method note** | By *assumption* drift rather than fact drift — which is exactly why link-checking and same-PR review never catch it | Ask the specific question: "would we still choose this, and are the alternatives we rejected still the live alternatives?" | Annual, plus whenever the thing it explains changes materially |
| **ADR** | **It doesn't — by design** | n/a | **Never. Exempt explicitly** (see below) |

**3. A "last verified" stamp, distinct from "last edited."** Git hands you last-*modified* for free
and it is the misleading number: a typo fix resets it, so a page nobody has checked in two years
reads as fresh the day someone reflows a paragraph. Record instead:

    Owner: <name> · Last verified: 2026-08-04 by <name> — ran the tutorial end-to-end on a clean
    machine · Review: quarterly

Naming *how* it was verified is what stops the stamp from becoming a signature ritual: "read it and
it looked fine" is not a verification, and writing the method down makes that obvious. Then make it
mechanical, which is the honest completion of docs-as-code: **the build can warn or fail on any page
whose last-verified date is past its cadence**, exactly as it already fails on a broken link. Render
the stamp visibly in the page so a reader can price the page's trustworthiness themselves.

**The ADR exemption is load-bearing — state it wherever the cadence policy lives.** ADRs are
historical records; their value comes from being immutable (§4). A staleness sweep that "refreshes"
old ADRs to match current reality destroys the exact trail a successor needs, and a review bot that
flags them as stale will eventually persuade someone to do it. Exempt them by name. Their update
mechanism is supersession, not verification.

## 3. README anatomy — the first screen

The first screen (what fits before any scrolling) answers, in order:
1. **What this is** — one sentence, no adjectives doing load-bearing work.
2. **Who it is for** — the reader can self-select out in seconds.
3. **Proof it works** — a minimal runnable example, real output, or a screenshot.
4. **How to run it** — install/setup commands that actually work on a clean machine.
5. **Where to go next** — links routed by Diátaxis form (first tutorial, how-to index,
   reference, design notes).

Below the fold: project status, contribution pointers, license, credits. The order is
Preston-Werner's Readme Driven Development argument operationalized: "Until you've
written about your software, you have no idea what you'll be coding" [snippet-only] —
writing the first screen first is a design act, not an afterthought.

## 4. Architecture Decision Records

Nygard's template ("Documenting Architecture Decisions," 2011), in Alexandrian-pattern
style [snippet-only]:

```markdown
# ADR-0007: Store analysis outputs as Parquet, not workbook tabs

Status: Accepted          <!-- Proposed | Accepted | Deprecated | Superseded by ADR-00NN -->
Date: <decision date>

## Context
Monthly outputs were accumulating as tabs in one shared workbook. Two corruption
incidents; no diffability; the review step cannot see what changed. Team is
spreadsheet-fluent, not database-fluent — the fix must keep an Excel export path.

## Decision
Each run writes immutable, dated Parquet files to `derived/`; a small script exports
any run to .xlsx on demand. The workbook becomes a view, never the store.

## Consequences
Diffable, scriptable history; review sees changes. Costs: a conversion step for
spreadsheet users; Parquet tooling becomes a hiring assumption. Revisit if the
Excel-export path goes unused for two consecutive quarters.
```

Rules that make ADRs work:
- **One decision per record.** An ADR is not a design doc and not an RFC — it records
  one decision and its consequences, briefly.
- **Immutable once accepted.** Reversals get a new ADR marked "Supersedes ADR-0007";
  the old record's status becomes "Superseded by ADR-0012." Nygard's rationale: large
  documents are never kept up to date; small modular documents have at least a chance
  [snippet-only] — and an unedited trail is the only trustworthy one.
- **Context is the payload.** Consequences state costs honestly, including what would
  trigger revisiting. A consequences section with no downsides is advocacy, not record.
- Numbered sequentially, stored with the project (`docs/adr/` or equivalent).
- The form is portable: a legal team's decision memos and an ops team's process
  decisions fit the same Context/Decision/Consequences skeleton.

## 5. Changelog + semantic versioning

Keep a Changelog (Olivier Lacan, published 2014) [snippet-only]:
- File named `CHANGELOG.md`, newest release first, ISO-8601 dates (`2026-08-11`).
- An `[Unreleased]` section on top collects entries as changes land, so release day is
  a rename, not an archaeology dig.
- Six categories, used only when non-empty: **Added, Changed, Deprecated, Removed,
  Fixed, Security**.
- The tagline is the discipline: "Don't let your friends dump git logs into
  changelogs" [snippet-only] — commits are for the project's developers; the changelog
  is curated for its users.

Semantic Versioning (Tom Preston-Werner, semver.org) [snippet-only]: `MAJOR.MINOR.PATCH`
where MAJOR = breaking change, MINOR = backward-compatible feature, PATCH =
backward-compatible fix. The two specs interlock: writing the changelog entry forces
the version question — an entry under **Changed** or **Removed** that breaks a consumer
*is* the case for a MAJOR bump, and a version bump with an empty changelog entry is a
claim with no evidence. Worked example:

```markdown
## [Unreleased]

## [2.0.0] - 2026-08-01
### Changed
- Quarterly capacity model now reads calendars from the HR feed instead of the
  manual tab.
### Removed
- The `manual_calendar` input. **Breaking** — supply calendars through the HR
  feed instead (hence 2.0.0).
### Fixed
- Weekend shifts no longer double-counted in utilization (#41).

## [1.3.0] - 2026-05-02
### Added
- Per-team drill-down sheet in the output workbook.
```

**Note the split, because it is the category rule most often broken.** One substitution generates
*two* entries: **Changed** for the behaviour that now works differently, **Removed** for the thing
that no longer exists. It is tempting to write the removal as a "Breaking:" clause inside the Changed
line — and that is a filing error, because the categories are a contract a consumer reads
selectively. Someone upgrading scans `### Removed` for everything that will break them; a removal
buried in a Changed sentence is invisible to exactly the reader it was written for. Rule of thumb:
**if a name that used to work no longer works, it goes under Removed**, whatever replaced it.
(Same discipline: an input that still works but is on notice goes under **Deprecated**, with the
removal date — that is the entry that gives consumers time.)

Version *methods and models* too, not just software: an analysis whose assumptions
change is a MINOR bump; one whose outputs stop being comparable to last quarter's is a
MAJOR bump, and the changelog entry says why.

## 6. Routine procedure docs and their seams

A routine procedure doc is a how-to guide for an operational task: **trigger** (what
event starts it), **preconditions** (access, inputs on hand), **numbered steps** (one
action each, expected result stated), **verification** (how you know it worked),
**escalation** (who to call when it doesn't). Keep it goal-named ("Close the monthly
extract," not "Extract procedures").

Route away what only looks like a procedure doc:
- Crisis-shaped — a tripwire someone watches, pre-granted authority, sealed first
  moves → `safety-and-reliability-skills:break-glass-playbooks` (that skill owns the
  word "runbook").
- A full method with sequence, timing, key points and reasons, trained and reviewed →
  `continuous-improvement-skills:standard-work`.
- A 5–9-item card at a pause point guarding killer items →
  `safety-and-reliability-skills:checklist-design`.

## 7. API and reference-doc discipline

- **Examples first.** Every entry leads with a minimal runnable example (or a filled
  template, for non-code references like a data dictionary), then the prose. Readers
  copy examples; they only read prose when the example surprises them.
- **Versioned with the thing documented.** Docs claiming version N while describing
  version N−1 are worse than absent — they spend the reader's trust. Keep docs in the
  same repo and release train as the artifact.
- **Generated vs hand-written, marked.** Generate what the source can derive:
  signatures, parameters, schemas, column lists — generated docs cannot drift.
  Hand-write what it cannot: semantics, examples, pitfalls, cross-references. Mark
  which regions are generated so nobody hand-edits text the next build overwrites.
- **Uniform entry shape.** Same fields, same order, every entry — reference readers
  navigate by pattern, and a missing field should read as "verified absent," not
  "maybe forgot."

## 8. Docs as code

Documentation in version control, reviewed and built like software — Anne Gentle's
*Docs Like Code* and the Write the Docs community guide [snippet-only]:
- Docs live in the same repo as what they document; a behavior change and its doc
  change ride the same PR, so review catches drift at the cheapest moment.
- Builds check what can be checked mechanically: links, spelling, example code that
  actually runs, **and the last-verified date against each page's cadence** (§2a) — a date past its
  review interval is as mechanically checkable as a dead link.
- **Know the boundary of this practice.** Same-PR review is *change-triggered*: it catches drift only
  in docs coupled to a change someone is already making. Docs whose subject moves without any commit
  in this repo — the data dictionary an upstream team's schema change invalidates, the method note
  whose assumption stopped holding — are invisible to it. Those need the time-triggered half:
  owner, cadence, last-verified stamp (§2a). Claiming docs-as-code as the whole answer is how a
  well-run repo ends up with a confidently wrong data dictionary.
- Prose quality in that review is `writing-skills:adams-smart-brevity`'s job;
  commit/PR prose is `coding-agent-skills:git-and-code-review`'s.

## 9. Worked example: one recurring analysis, four documents

An analyst owns a quarterly capacity study (the same skeleton fits an attorney's
matter playbook, an ops process, or a developer's service). The docs sort like this:

| Artifact | Diátaxis form | Content | Owner · verification · cadence |
|---|---|---|---|
| First-time walkthrough | Tutorial | A new teammate runs last quarter's study end-to-end on frozen sample data; every step guaranteed to work | Study owner · run it on a clean machine · each release touching the path + quarterly |
| Run sheet | How-to guide | Trigger (day 3 after quarter close), steps, expected outputs, verification totals, escalation | The operator on rotation · verified on use, date stamped · every use |
| Data dictionary | Reference | Every input column and derived field: source, type, allowed values, owner — uniform entries, generated from the schema where possible | Data steward · diff generated regions vs schema · quarterly + on upstream change |
| Method note | Explanation | Why utilization is defined this way, alternatives rejected, known limits — written per `writing-skills:explanation-design` | Analyst who owns the method · "would we still choose this?" · annual + on material change |
| ADRs | (record, not a quadrant) | One decision each, Context/Decision/Consequences | Author, permanently · **exempt from freshness review** · never |

Note which page in that table docs-as-code protects and which it doesn't. The tutorial and run sheet
sit on paths a change usually touches, so a same-PR review has a chance at them. The **data
dictionary** breaks when an upstream team renames a column — no commit here — and the **method note**
breaks when an assumption quietly stops holding, which no diff can see. Those two are why the
owner/cadence/last-verified columns exist, and they are reliably the two pages a team describes as
"out of date" years before anyone fixes them.

Decisions and change history attach to the same corpus: ADR-0001 records why the HR
feed replaced the manual calendar (context: two silent staleness incidents;
consequences: feed dependency, breaking input change), and the changelog's 2.0.0 entry
in §5 announces that same break to the study's consumers — the ADR explains *why*, the
changelog announces *that*, and neither document tries to do the other's job. The
audit protocol (§2) is how this table gets built from an existing pile: the old wiki
page that mixed the run sheet with the method essay splits into two rows, and the
"quick reference" that taught concepts becomes the tutorial.
