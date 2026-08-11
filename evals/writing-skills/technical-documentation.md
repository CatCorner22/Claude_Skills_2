# Evals — writing-skills:technical-documentation

## 1. Positive trigger (should load the skill)
> "Our project's README is a wall of text, the wiki mixes setup steps with design
> essays, and we just picked a new storage format with zero record of why. Restructure
> the docs — and write the ADR for the storage decision."

Expected: skill loads; runs the quadrant audit — every wiki section sorted into
tutorial / how-to / reference / explanation, misfiled sections (setup steps inside
essays) becoming the fix list; rebuilds the README first screen in order (what it is,
who it's for, proof it works, how to run, where to go next); writes ADR-000N in
Nygard's Context/Decision/Consequences form with honest downsides in Consequences,
numbered and stored with the project, immutable once accepted; proposes a
`CHANGELOG.md` (Keep a Changelog categories, newest first, ISO dates) keyed to the
project's versioning; routes sentence-level tightening to
`writing-skills:adams-smart-brevity` rather than doing register work as the deliverable.

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
  Context/Decision/Consequences with Status, one decision each, superseded never
  edited; changelog in the six categories, newest first, ISO dates, connected to the
  versioning scheme; reference/API entries examples-first, versioned with the
  artifact, generated-vs-hand-written marked; routine procedure docs with trigger,
  steps, verification, escalation — and hands off crisis runbooks, standard work, and
  checklist cards at the named seams.
- **Teaches**: why the four forms fail when blended (four reader states, one document
  can't serve them all); why ADRs are small and immutable (Nygard: large documents are
  never kept up to date; an edited trail can't be trusted); why a changelog is
  curation for users, not a git-log dump for developers; why the README first screen
  is a design act (Readme Driven Development).
- **Stays honest**: presents Diátaxis as Procida's framework systematizing existing
  practice; never claims "Django adopted Diátaxis" (Django's structure predates it)
  and says Python only *discussed* adoption; [snippet-only] provenance marks preserved
  on Diátaxis, Nygard, Keep a Changelog, SemVer, and docs-as-code claims; no invented
  adoption statistics; no time-anchored claims about what is "current practice."
