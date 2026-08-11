# Evals — oracle-otbi-skills:otbi-report-building

## 1. Positive trigger (should load the skill)
> "I need to build an OTBI analysis in Fusion that lists bank statement lines with a couple of
> calculated columns, then put it on a dashboard. Walk me through it."

Expected: skill loads; opens Reports and Analytics → Create → Analysis; confirms a single subject
area; builds Criteria (columns, aggregation, formula), filters, Results views + compound layout;
saves under /Shared Folders/Custom; adds a dashboard and dashboard prompt; verifies totals.

## 2. Near-miss (should NOT load this skill)
> "Which OTBI subject area should I use to report on bank charges by charge type?"

Expected: this is a subject-area choice, not a build walkthrough —
`oracle-otbi-skills:otbi-subject-area-selection` should handle it. If this skill loads instead,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** gives the concrete Create-Analysis path, enforces one subject area, builds
  Criteria → Filters → Results in order, saves under /Custom (copy-before-edit), and adds a dashboard
  prompt bound to "is prompted" filters.
- **Teaches:** explains that OTBI queries live data through one subject area's fact/dimension
  folders, and why separating the query (Criteria/Filters) from presentation (Results) lets one
  analysis feed several views and a shared prompt.
- **Safe:** never edits a delivered object in place; filters early to protect the live database.
