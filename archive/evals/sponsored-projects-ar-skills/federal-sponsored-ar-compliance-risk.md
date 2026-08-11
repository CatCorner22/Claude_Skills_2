# Evals — sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk

## 1. Positive trigger (should load the skill)
> "Here's our AR aging with a proposed write-off list — several items are on NIH and DOE
> awards. Assess our compliance exposure before we book anything, including what this means
> for our Single Audit."

Expected: skill loads; isolates the federal population (incl. pass-throughs); blocks the
federal write-offs per §200.426 (move to institutional funds, treat as process finding);
scans the remaining patterns (aged AR by payment method, adjustment churn, unbilled vs
expenditures); sizes exposure with the full multiplier; maps the SEFA/Single Audit surface;
grades documentation readiness; delivers prioritized flags with the not-an-audit-opinion
disclaimer.

## 2. Near-miss (should NOT load this skill)
> "What's the current Single Audit threshold and what does 2 CFR 200 say about the de minimis
> rate?"

Expected: the rules themselves — `sponsored-projects-ar-skills:uniform-guidance-federal-core`.
If this skill loads instead, sharpen the risk-assessment-vs-reference split.

## 3. Quality rubric
A good response:
- **Does the task:** federal population isolated, pattern scan run with the
  exposure/likelihood/documentation prioritization, write-off rule applied exactly, SEFA
  tie-out checked, edge cases (cost sharing, program income, closeout, subrecipients) covered.
- **Teaches:** the time-asymmetry of federal AR risk (collected ≠ closed), patterns as the
  exhaust of tested processes, and why the government never absorbs collection failures.
- **Safe:** never approves a federal-award write-off, sizes exposure beyond direct cost,
  includes the disclaimer verbatim, keeps findings/award data out of committed files.
