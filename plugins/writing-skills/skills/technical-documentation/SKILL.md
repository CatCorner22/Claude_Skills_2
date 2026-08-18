---
name: technical-documentation
description: >-
  Structures technical documentation as typed artifacts, not prose: routes docs through
  Procida's Diátaxis framework (tutorial, how-to, reference, explanation — forms that
  fail when blended), shapes the README around a newcomer's first screen, records decisions as
  Nygard-style ADRs (context/decision/consequences, superseded never
  edited), keeps a human-readable changelog keyed to SemVer, and holds API and
  reference docs to examples-first, versioned, generated-vs-hand-written discipline. Owns the
  document types; register stays with writing-skills:adams-smart-brevity,
  explanation craft with writing-skills:explanation-design. Gives every page an owner, a cadence,
  and a last-verified date. Use when writing or restructuring
  docs for a project, method, or process. Triggers: technical documentation, write the README,
  ADR, architecture decision record, changelog, Diátaxis, how-to guide, tutorial vs reference,
  API docs, docs as code, semantic versioning, our docs are out of date.
metadata:
  version: "1.2.1"
  source: >-
    Built from the general-use expansion research dossier
    (docs/research/general-use-expansion-research.md, §5 technical-documentation).
    Provenance legend: [snippet-only] = verified via cross-checked WebSearch result
    blocks; direct fetches of diataxis.fr and keepachangelog.com were egress-blocked,
    so all Diátaxis and Keep-a-Changelog claims carry that mark.
---

# Technical documentation (typed artifacts, not prose)

Most documentation fails by type confusion, not bad sentences: a how-to buried in an
essay, a reference page that teaches, a README that philosophizes before it installs.
The fix is a small set of named document types, each with one job. Daniele Procida's
Diátaxis framework supplies the router — four forms derived from two axes
(action/cognition × acquisition/application): **tutorials** (learning-oriented),
**how-to guides** (task-oriented), **reference** (information-oriented), and
**explanation** (understanding-oriented); ideas he crystallized at Divio and presented
in "What nobody tells you about documentation" (PyCon Australia 2017), later named at
diataxis.fr [snippet-only]. Michael Nygard's "Documenting Architecture Decisions"
(2011) supplies the decision record [snippet-only]; Olivier Lacan's Keep a Changelog
(2014) — "Don't let your friends dump git logs into changelogs" — supplies the change
record, keyed to Tom Preston-Werner's Semantic Versioning [snippet-only]. One honesty
rule up front: Diátaxis is a named author's framework that *systematized existing
practice* — Django's similar four-part docs structure predates it, so never claim
"Django adopted Diátaxis"; the Python project publicly *discussed* adopting it, which
is not "restructured wholesale" [snippet-only].

## When to use
- Writing or restructuring a project's docs: README, docs site or wiki, ADRs, a
  changelog, a data dictionary, an API reference, a routine procedure doc.
- Auditing docs nobody uses — sorting existing pages by type usually exposes why.
- Documenting a recurring method (an analysis, a matter workflow, an ops process) so a
  successor inherits both the steps and the *why*.
- Not for: sentence-level clarity and register → `writing-skills:adams-smart-brevity`
  (it owns documentation *writing* — the two compose: this skill decides which document
  exists and its architecture; that one tightens every sentence in it).
- Not for: the craft of making one concept land with a newcomer →
  `writing-skills:explanation-design` (audience model, analogy with marked breaks) —
  it is the content method for the explanation quadrant; this skill owns the shelf.
- Not for: crisis playbooks with tripwires and sealed authority →
  `safety-and-reliability-skills:break-glass-playbooks` (it owns "runbook"); a full
  method doc with sequence, timing, and key points →
  `continuous-improvement-skills:standard-work`; the checklist card itself →
  `safety-and-reliability-skills:checklist-design`.
- Not for: authoring Agent Skills → `coding-agent-skills:writing-agent-skills`.
- Not for: commit-message and PR prose → `coding-agent-skills:git-and-code-review`.

## Do it
Templates, the quadrant audit protocol, worked examples, and per-type rules are in
`references/document-types.md`.

1. **Route the request through Diátaxis before writing a word.** Ask what the reader
   is doing (acquiring skill vs applying it) and what they need (action vs
   understanding): learning by doing → **tutorial** (a lesson that must work
   end-to-end); getting a job done → **how-to guide** (goal-named steps, competence
   assumed); looking something up → **reference** (complete, dry, structured like the
   thing it describes); wanting the why → **explanation** (context, alternatives,
   trade-offs). One document, one form. In an audit, sort every existing section into
   a quadrant — the misfiled ones are one fix list, and **form is only the first of three axes**:
   record each page's owner and last-verified date too, because a page can be perfectly filed and
   quietly wrong, and a form-only audit is blind to exactly that page (step 8).
2. **Shape the README around the newcomer's first screen.** In order: what this is
   (one sentence), who it is for, proof it works (a minimal example or output), how to
   install/run it, and where to go next — links out to the four forms. Preston-Werner's
   Readme Driven Development argument: "Until you've written about your software, you
   have no idea what you'll be coding" [snippet-only] — the README is cheapest to write
   *first*.
3. **Record each significant decision as an ADR.** Nygard's template: Title, Status,
   Context, Decision, Consequences [snippet-only]. Number them, keep them with the
   project, and treat accepted ADRs as immutable — a reversed decision gets a *new* ADR
   that supersedes the old, never an edit. Context is the payload: it is what stops
   successors from re-litigating a decision whose constraints they can't see.
4. **Keep the changelog for humans, keyed to versions.** Keep a Changelog categories —
   Added / Changed / Deprecated / Removed / Fixed / Security — newest first, ISO dates,
   an Unreleased section on top [snippet-only]. File by what happened to the *name*, not by the
   story: something that used to work and now doesn't goes under **Removed**, even when a
   replacement arrived — a substitution earns two entries (Changed for the new behaviour, Removed
   for the retired input), because consumers scan `### Removed` for what will break them. Connect
   it to SemVer (MAJOR.MINOR.PATCH = breaking/feature/fix): drafting the entry forces the version
   question — a Changed or Removed line that breaks users *is* the argument for a major bump.
5. **Write routine procedure docs — and hand off at the seams.** A run sheet for a
   recurring task is a how-to guide: trigger, numbered steps, expected result, what to
   check. If it is crisis-shaped (tripwire, pre-granted authority, sealed moves) it is
   a break-glass playbook, not a procedure doc; if it needs timing and key-point
   discipline it is standard work; if it needs a 5–9-item card it is checklist design.
6. **Hold reference and API docs to the discipline.** Examples first: every entry
   shows a runnable example before the prose. Versioned with what they document — docs
   for one version claiming to describe another are worse than none. Generate what is
   derivable from the source (signatures, schemas, parameter lists — generated docs
   can't drift) and hand-write what is not (semantics, examples, pitfalls — meaning
   doesn't autogenerate). Mark which is which so maintainers know where edits survive.
7. **Treat the docs as code.** Same repo as the thing documented, changed in the same
   review as the behavior change, built and link-checked automatically — Anne Gentle's
   *Docs Like Code* and the Write the Docs community practice [snippet-only]. A doc
   that lives where the change happens has a chance of staying true. Know the limit: this is
   *change-triggered* review, so it only protects docs coupled to a change someone is already
   making. It is why step 8 exists.
8. **Give every page an owner and a review cadence, and stamp what was verified — the
   time-triggered half.** The docs people call out of date are usually the ones no PR ever
   touches: the method note whose assumption stopped holding, the data dictionary an upstream
   team's schema change invalidated, the run sheet for a tool that shipped a new menu. No commit,
   no review, no signal. So: **one named person** per page (not "the team" — that means nobody);
   **a cadence set by how fast the page rots**, which its Diátaxis form predicts (run the tutorial
   each release on the path; verify the run sheet *on use*, which is free because the work happens
   anyway; diff the reference against its schema quarterly; re-ask the method note annually
   whether you would still choose this); and **a "last verified: date, by whom, how" stamp,
   distinct from last-edited** — git's modified date resets on a typo fix, so it flatters. Name the
   verification method, or the stamp becomes a signature ritual. Then make it mechanical: the build
   can warn on a page past its cadence exactly as it fails on a dead link. Every stale page resolves
   to **verify, fix, or retire** — deleting or deprecating-with-a-pointer is a legitimate and often
   correct answer, since an unowned unverified page is indistinguishable from a live one and so costs
   more than no page. **Exempt ADRs by name:** they are historical records whose value is their
   immutability, and a freshness sweep that "updates" them destroys the trail (step 3).

## Why / learn
The four forms exist because readers arrive in four different states, and a document
optimized for one state actively harms the others: the learner following a tutorial
needs a guaranteed path and no choices; the practitioner with a job needs choices and
no pedagogy; the looker-upper needs completeness and predictable structure; the person
asking "why is it like this?" needs the discussion every other form must exclude. Blend
them and each reader wades through the other three's material — which is why "we have
docs but nobody uses them" is usually a filing problem. Diátaxis matters as a *router*,
not a quota: you rarely need all four documents; you always need to know which one you
are writing. And teach it honestly — a framework with one named author, systematizing
practice that (as at Django) partly predates it, is more credible than a fake timeless
standard, and the attribution models the citation hygiene good reference docs need.

ADRs are Nygard's answer to a specific failure: "Large documents are never kept up to date.
Small, modular documents have at least a chance at being updated" [snippet-only]. An ADR records
*one* decision at the moment it was made, with the context that forced it. Immutability
is what makes the trail trustworthy — a superseded ADR still explains why the system
looked that way in its era, while an edited one erases the very history a successor
needs. The changelog earns its keep the same way: a git log records what changed for
the project's *developers*; a changelog triages what matters for the project's *users*
— curation, not transcription, is the value added. And the README-first argument
generalizes past software: writing the first screen forces you to know what the thing
is, who it serves, and how anyone proves it works — for a codebase, an analysis method,
or a practice playbook alike.

Type confusion explains why docs go *unread*. It does not explain why they go *wrong*, and that is
the more expensive failure, because a misfiled page merely wastes a reader's time while a confidently
wrong one costs a decision. Wrongness has a different cause and needs a different mechanism.
"Docs as code" is the standard answer and it is a **change-triggered** control: a behaviour change and
its doc change ride the same review, which works precisely to the extent that the doc sits next to
something a commit touches. Notice what that leaves uncovered — and notice that it is exactly the
list people complain about. A data dictionary goes wrong when an upstream team renames a column: no
commit in your repo, so no review fires. A method note goes wrong when the assumption underneath a
definition quietly stops holding: nothing textual changed at all, so no diff could see it. A run
sheet goes wrong when the tool it drives ships a new menu. Link-checkers, spell-checkers and
same-PR review are all blind to every one of these, and they are the mechanisms most teams believe
they have covered themselves with.

The complement is **time-triggered**, and it is unglamorous: a named owner, a cadence, and a
last-verified stamp. Each of the three fixes a distinct failure. Ownership fixes diffusion of
responsibility — a page owned by "the team" is owned by nobody, and the useful accountability is not
for writing the page but for answering whether it is still true. Cadence fixes the fact that rot
rates differ wildly, which is why a uniform "review everything annually" policy either wastes effort
on stable references or lets a fast-rotting tutorial break for eleven months; the Diátaxis form you
already assigned is a decent predictor of the rot rate, so the router does double duty. And the
last-verified stamp fixes the measurement: git's last-*modified* date is free and misleading, since
reflowing a paragraph makes a two-year-unchecked page look current. Recording *how* it was verified
— ran it, diffed it against the schema, re-asked whether the rejected alternatives are still the live
ones — is what keeps the stamp from degenerating into a signature. Once the date exists, staleness
becomes mechanically checkable, which is the honest completion of the docs-as-code idea rather than
a rejection of it. One exception, and it matters: ADRs are exempt, because their value *is* their
staleness — a superseded ADR correctly describes a world that no longer exists, and a well-meaning
freshness sweep is the most likely way that trail gets destroyed.

## Common mistakes
- Blending quadrants ("the tutorial also documents every option") → one form per
  document; cross-link to the reference instead of inlining it.
- Editing an accepted ADR to match the new decision → write a superseding ADR; the old
  one is history, not an error.
- Pasting the git log as the changelog → curate human-relevant entries into the six
  categories, newest first.
- Filing a removal under **Changed** because something replaced it ("Breaking: the old input is
  gone") → it goes under **Removed**; consumers scan that heading for what will break them. A
  substitution earns two entries.
- A page with no named owner → "the team owns it" means nobody answers for whether it is true. One
  name per page, accountable for accuracy rather than for authorship.
- Relying on docs-as-code alone → it is change-triggered, so it never fires on the data dictionary
  an upstream schema change broke or the method note whose assumption lapsed. Add owner, cadence,
  and a last-verified stamp.
- Treating git's last-modified date as freshness → a typo fix resets it. Stamp "last verified: date,
  by whom, *how*" separately, and let the build warn when it is past cadence.
- Running a staleness sweep over the ADRs → they are historical records; refreshing them destroys the
  trail. Exempt them by name and supersede instead.
- Auditing an unloved corpus by quadrant only → a correctly filed, confidently wrong page passes.
  Audit form, ownership, and freshness, and resolve every stale page to verify / fix / retire.
- README opening with badges, philosophy, or org history → first screen: what it is,
  who it's for, proof it works, how to run it.
- Claiming "Django adopted Diátaxis" or "Python restructured on it" → Django's
  structure predates the framework; Python discussed adoption [snippet-only].
- Hand-maintaining what the source could generate → it drifts silently; generate the
  derivable, hand-write the meaning.
- Writing a "runbook" for a foreseeable crisis here → that word and that job belong to
  `safety-and-reliability-skills:break-glass-playbooks`.
- Docs in a system nobody reviews → docs as code: same repo, same PR, same review.

## Tailor to your environment
Record your documentation terrain in `references/your-environment.md`: where each doc
type lives (repo, wiki, shared drive), your ADR numbering and location, changelog and
versioning conventions, the document types your role actually produces (method notes,
data dictionaries, matter playbooks, run sheets) **with an owner, a review cadence, and a
last-verified date for each**, and the audiences each serves. Keep
the committed file structural — client names, internal system details, or anything
sensitive goes in `your-environment.private.md` (git-ignored), never in a committed
file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/technical-documentation.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/document-types.md — the Diátaxis router with the three-axis audit protocol
  (form / ownership / freshness) and the owner-cadence-last-verified mechanisms per form, README
  first-screen anatomy, ADR template with a worked example, Keep a Changelog + SemVer
  with a worked example and the Changed-vs-Removed filing rule, routine-procedure template with
  seam handoffs, API/reference discipline, and docs-as-code practice with its change-triggered
  limit, all with provenance marks
- references/your-environment.md — your doc locations, conventions, and recurring
  document types (fill in)
