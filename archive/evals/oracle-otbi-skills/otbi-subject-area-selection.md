# Evals — oracle-otbi-skills:otbi-subject-area-selection

## 1. Positive trigger (should load the skill)
> "I want to report unreconciled bank statement lines with an aging bucket in OTBI, but I'm not sure
> which subject area has reconciliation status. Which one do I use?"

Expected: skill loads; frames measure/grain/filters; selects **Cash Management - Bank Statements
Real Time** (reconciliation status is an attribute there, not a separate area); confirms the aging
can be a CASE column formula; hands off to report-building.

## 2. Near-miss (should NOT load this skill)
> "Save my finished analysis into the Custom folder and add a table and a bar chart to it."

Expected: this is build mechanics, not subject-area choice —
`oracle-otbi-skills:otbi-report-building` should handle it. If this skill loads instead, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** maps the question to exactly one subject area by checking fact/dimension
  folders, and names a workaround (BIP SQL, shared-prompt dashboard, or FDI/OAC) when it spans two.
- **Teaches:** explains that a subject area is a single trusted join model, which is why one analysis
  = one area, and why cross-pillar joins need a different tool.
- **Safe:** does not claim a reconciliation subject area exists; does not promise unverified
  flexfield columns.
