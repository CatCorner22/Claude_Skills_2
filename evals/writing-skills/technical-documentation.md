# Evals — writing-skills:technical-documentation

## 1. Positive trigger (should load the skill)
> "Our project's README is a wall of text, the wiki mixes setup steps with design
> essays, and we just picked a new storage format with zero record of why. Restructure
> the docs — and write the ADR for the storage decision."

Expected: skill loads; runs the audit on **three axes, not one** — every wiki section sorted into
tutorial / how-to / reference / explanation *and* given an owner and a last-verified date, so the
output is two fix lists (misfiled sections such as setup steps inside essays; unowned or unverified
pages) rather than one; rebuilds the README first screen in order (what it is,
who it's for, proof it works, how to run, where to go next); writes ADR-000N in
Nygard's Context/Decision/Consequences form with honest downsides in Consequences,
numbered and stored with the project, immutable once accepted; proposes a
`CHANGELOG.md` (Keep a Changelog categories, newest first, ISO dates) keyed to the
project's versioning, filing a retired input under **Removed** rather than as a "Breaking:" clause
inside a Changed line; routes sentence-level tightening to
`writing-skills:adams-smart-brevity` rather than doing register work as the deliverable.

## 1b. Positive trigger (staleness — owner and cadence)
> "Half our docs are out of date and nobody notices until someone gets burned. The data dictionary
> still lists columns the warehouse team renamed months ago, and the method note describes an
> assumption we stopped making last year. We already do docs-as-code — same repo, same PR,
> link-checking in CI. What else is there?"

Expected: skill loads and identifies the real gap: **docs-as-code is change-triggered**, so it only
fires on docs coupled to a change someone is already making in this repo — and both examples named
are precisely the decoupled case (an upstream schema rename produces no commit here; a lapsed
assumption produces no textual diff at all), which is why link-checking and same-PR review were never
going to catch them. Prescribes the **time-triggered** complement: **one named person per page**
(not "the team"), accountable for accuracy rather than authorship; **a cadence set by the page's rot
rate**, with the Diátaxis form as the predictor (run the tutorial each release on the path; verify the
run sheet *on use*, which is free; diff the data dictionary's generated regions against the schema
quarterly and on upstream change; re-ask the method note annually whether the choice and its rejected
alternatives still hold); and **a "last verified: date, by whom, how" stamp distinct from
last-edited**, because git's modified date resets on a typo fix and so flatters. Makes it mechanical —
the build warns on a page past its cadence, the same class of check as a dead link. Resolves every
stale page to **verify, fix, or retire**, treating deletion or deprecate-with-a-pointer as a
legitimate outcome. And **exempts ADRs by name** from freshness review, since their value is their
immutability and a well-meaning sweep would destroy the trail.

## 2. Near-miss (register/clarity guard — should NOT load)
> "This design doc is wordy and passive and nobody finishes it. Edit it for clarity
> and brevity — tighten every section."

Expected: `writing-skills:adams-smart-brevity` territory — sentence-level meaning and
document-level attention on an *existing* document, no new document types, no
restructuring by form. This skill decides which documents exist and their architecture;
that one tightens the prose. A pure "edit for clarity / tighten this" ask routes there.

## 2b. Near-miss (crisis-runbook guard — should NOT load)
> "Write a runbook for when the payment provider goes down at 2 a.m. — who gets paged,
> what access they'll need, and the first steps before the on-call lead wakes up."

Expected: `safety-and-reliability-skills:break-glass-playbooks` territory — it owns
"runbook," and the ask is crisis-shaped: a tripwire someone watches, pre-granted
emergency access, sealed first moves at calm-headed quality. This skill covers routine
operational procedure docs and hands off anything crisis-shaped.

## 3. Quality rubric
- **Does**: routes content through Diátaxis before writing (one form per document,
  misfits split or moved); README first screen in the five-part order; ADRs in
  Context/Decision/Consequences with Status, one decision each, and a superseded ADR whose
  *body* is never rewritten — its Status line is updated to point at the successor, which is the
  one edit a superseded ADR does receive; changelog in the six categories, newest first, ISO dates, connected to the
  versioning scheme, **with removals filed under Removed even when something replaced them** (a
  substitution earns two entries) and deprecations carrying a removal date; reference/API entries
  examples-first, versioned with the
  artifact, generated-vs-hand-written marked; routine procedure docs with trigger,
  steps, verification, escalation — and hands off crisis runbooks, standard work, and
  checklist cards at the named seams; **every page gets a named owner, a review cadence matched to
  its rot rate, and a last-verified stamp naming the verification method**, with ADRs explicitly
  exempted and stale pages resolved to verify / fix / retire.
- **Teaches**: why the four forms fail when blended (four reader states, one document
  can't serve them all); why ADRs are small and immutable (Nygard: large documents are
  never kept up to date; an edited trail can't be trusted); why a changelog is
  curation for users, not a git-log dump for developers, and why its categories are a
  contract a consumer reads selectively (a removal hidden in a Changed line is invisible to the
  reader it was written for); why the README first screen
  is a design act (Readme Driven Development); **why type confusion explains unread docs but not
  wrong ones** — docs-as-code is change-triggered and structurally blind to pages whose subject moves
  without a commit here, so ownership, cadence, and a last-verified date (distinct from
  last-modified, which a typo fix resets) are the time-triggered complement rather than extra
  process.
- **Stays honest**: presents Diátaxis as Procida's framework systematizing existing
  practice; never claims "Django adopted Diátaxis" (Django's structure predates it)
  and says Python only *discussed* adoption; [snippet-only] provenance marks preserved
  on Diátaxis, Nygard, Keep a Changelog, SemVer, and docs-as-code claims; no invented
  adoption statistics; no time-anchored claims about what is "current practice."
