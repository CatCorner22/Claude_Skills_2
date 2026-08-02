# Evals — oracle-otbi-skills:otbi-report-scheduling-sharing

## 1. Positive trigger (should load the skill)
> "I built a bank-charges analysis in OTBI. Now I need it emailed to three regional controllers every
> month-end, each seeing only their own region. How do I schedule that?"

Expected: skill loads; explains OTBI has no native scheduling/bursting; routes the scheduled,
per-recipient (bursting) delivery to **BI Publisher**; covers sharing the interactive version via a
Shared folder / dashboard with role-based permissions in the meantime.

## 2. Near-miss (should NOT load this skill)
> "Add a pivot table and a bar chart to my analysis and arrange them in the compound layout."

Expected: this is building/authoring, not sharing or scheduling —
`oracle-otbi-skills:otbi-report-building` should handle it. If this skill loads instead, tighten the
description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** shares via Shared folder + dashboard + role-based catalog permissions, and
  correctly routes scheduling/bursting/pixel-perfect delivery to BI Publisher.
- **Teaches:** explains that OTBI is for interactive real-time exploration while BIP owns scheduled,
  burst, and pixel-perfect delivery — and how to tell which side a request is on.
- **Safe:** doesn't promise OTBI scheduling/bursting it can't do; notes data security still limits
  rows per user regardless of catalog permissions.
