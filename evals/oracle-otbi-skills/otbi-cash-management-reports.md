# Evals — oracle-otbi-skills:otbi-cash-management-reports

## 1. Positive trigger (should load the skill)
> "Build me an OTBI report in Oracle Cash Management that shows unreconciled bank statement lines
> aged into 0-30/31-60/61-90/90+ buckets by bank account."

Expected: skill loads; puts it on **Bank Statements RT** (reconciliation status is an attribute
there); filters unreconciled + bank account + date; adds a CASE aging bucket; checks the Cash Manager
duty role; hands off build/filter mechanics to the other OTBI skills.

## 2. Near-miss (should NOT load this skill)
> "Walk me through actually matching my bank statement to the ledger and classifying the outstanding
> checks and deposits in transit."

Expected: this is the reconciliation process, not an OTBI report —
`cash-management-skills:bank-reconciliation` should handle it. If this skill loads instead, tighten
the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** maps the report to the correct one of the four Cash Management subject areas,
  builds it there, and names the required duty role.
- **Teaches:** explains that reconciliation status is an attribute inside Bank Statements RT (no
  separate area), and where the single-subject-area boundary forces a different tool (outstanding
  checks / deposits in transit; true cash position).
- **Safe:** doesn't invent a reconciliation subject area; doesn't present an OTBI balance snapshot as
  a true multi-source cash position; flags the Cash Manager duty and data-security row limits.
