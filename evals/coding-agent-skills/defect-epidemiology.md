# Evals — coding-agent-skills:defect-epidemiology

## 1. Positive trigger (should load the skill)
> "We just fixed an off-by-one in the pagination helper — the last row of every page was
> being dropped. I'm almost certain this helper got copy-pasted around before it was
> extracted. Where else does this appear? Find patient zero."

Expected: skill loads; treats the fixed bug as the index case; writes a two-part
fingerprint (semantic signature — "iterates to length minus one, so the final element is
skipped whenever the page is full" — plus the minimal wrong shape) and tests it against
both the buggy and fixed versions; runs the three passes in order — literal grep on
distinctive tokens, LLM semantic sweep over candidate regions (same subsystem, same
author cluster, similarly structured files) for Type 3–4 mutations, then the
version-history transmission tree; produces a contact-disposition table where every row
ends patched, not-applicable (with the reason), or accepted-with-reason (with owner and
revisit date); traces patient zero and runs the infectious-source checklist (is the
snippet still on the wiki? in the scaffold?); reads each source's out-degree off the tree;
quarantines the highest out-degree source (fix the origin, lint/CI rule carrying the outbreak-report
ID, in-situ warning); closes only when the table has no blank dispositions, and files the
outbreak report.

## 2. Near-miss (single-bug guard — should NOT load)
> "Checkout is throwing a 500 for one user when they apply a discount code — help me
> debug it."

Expected: ordinary debugging — no confirmed pattern exists yet, so there is nothing to
trace. This skill begins after a defect is confirmed (and typically fixed once); it is
the step that follows debugging, not a way to do it.

## 2b. Near-miss (prospective guard — should NOT load)
> "Before we launch the new import pipeline, rank everything that could go wrong with it
> so we know what to test hardest."

Expected: `continuous-improvement-skills:fmea` — prospective failure-mode analysis of a
design before anything has failed. Defect epidemiology is retrospective population-level
spread control triggered by a confirmed index case.

## 3. Quality rubric
- **Does**: fingerprint with both semantic signature and minimal wrong shape, validated
  against buggy and fixed versions; all three passes run with coverage recorded (regions
  cleared listed alongside hits); a complete disposition table with no blank rows and no
  unreasoned not-applicables; patient-zero identified with the infectious-source
  checklist answered; source out-degrees read from the transmission tree, not asserted; quarantine
  that acts on sources (origin fix + mechanical lint/CI rule + in-situ warning), not just
  cases; an outbreak report filed.
- **Teaches**: why patches do not propagate on their own (the ReDeBug finding) and why
  inconsistent clone evolution is how fixed bugs return (Juergens); why the unit of work
  is the pattern, not the failure; why the fingerprint must be semantic (Type 1–4
  mutation vs. which pass still catches it); why mechanism (lint rule) outlives memo.
- **Stays honest**: provenance marks (`[snippet-only]`) preserved on ReDeBug, VUDDY,
  Juergens (~107 faults), and clone-genealogy claims; spread presented as the tree's
  branching rate, never as an invented statistic; accepted-with-reason rows carry a named
  owner and revisit date, not a shrug; near-miss boundaries respected (no RCA or FMEA
  work smuggled in).
