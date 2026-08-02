# RCA tools and templates (reference)

Worksheets for the three core tools, plus the verification step. Applied to finance/accounting.

## Contents
- Problem statement template
- 5 Whys worksheet
- Fishbone (Ishikawa) 6M prompts
- Pareto tally
- Cause verification test
- Countermeasure record

## Problem statement template
> **What** is wrong: <the defect/deviation> · **Where**: <process/account/entity> · **When**:
> <started / how often> · **How big**: <magnitude, frequency, $> · **How we know**: <evidence/source>.

No cause, no solution, no blame. Example: "12 supplier invoices were paid twice in Q2 (vs. 2 in Q1),
totaling $84k, identified in the duplicate-payment report."

## 5 Whys worksheet
Follow one causal thread; each answer becomes the next "why". Read it back with "therefore" to check.
```
Problem: <statement>
Why 1? ________________________  →
Why 2? ________________________  →
Why 3? ________________________  →
Why 4? ________________________  →
Why 5? ________________________  → Root cause (a process/system condition you can change)
```
Stop when the answer is (a) actionable and (b) whose removal prevents recurrence — 5 is a guide, not a
quota. Branch into a fishbone if a "why" has several parallel causes.

## Fishbone (Ishikawa) 6M prompts
Spine = the effect (your problem statement). Brainstorm causes into six bones:
- **Man / People** — skills, training, staffing, handoffs, unclear ownership.
- **Method / Process** — steps, sequence, approvals, missing/ambiguous procedure.
- **Machine / Systems** — ERP config, interfaces, tooling, automation gaps.
- **Material / Inputs** — source data quality, master data, upstream document accuracy.
- **Measurement** — metric definitions, thresholds, how/when data is captured, wrong report.
- **Environment / Mother-nature** — deadlines, policy, period-end crunch, org changes.

Most durable causes live in Method, Measurement, or Machine — not "Man". Note the "Man" box invites
blame; convert it to *what let the person err*.

## Pareto tally
Count occurrences by category; sort descending; look for the ~vital few driving most of the total.
```
Category            | Count | %    | Cumulative %
Duplicate vendor ID |   6   | 43%  | 43%
Manual re-key       |   4   | 29%  | 72%   ← cumulative crosses ~70–80% here: attack these first
Timing / batch      |   2   | 14%  | 86%
Other               |   2   | 14%  | 100%
```
Fix the tallest bars first; don't spread effort evenly.

## Cause verification test
Before countermeasuring, prove it: "If <cause> is real, then toggling/removing it should change the
effect." Confirm with historical data, a controlled test, or turning the condition off and watching.
An unverified cause is a hypothesis, not a finding.

## Countermeasure record
| Root cause (verified) | Countermeasure (prefer error-proofing) | Owner | Date | Recurrence check |
|-----------------------|----------------------------------------|-------|------|------------------|
Only close the problem after the recurrence check confirms it held — then remove temporary containment.
