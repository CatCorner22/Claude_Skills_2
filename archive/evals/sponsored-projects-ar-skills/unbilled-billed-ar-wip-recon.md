# Evals — sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon

## 1. Positive trigger (should load the skill)
> "Our unbilled AR on sponsored projects jumped 40% this quarter and I think invoices are
> stuck somewhere — figure out what's in the pipeline and reconcile it against what PPM says
> we've earned."

Expected: skill loads; cuts the pipeline by billing status with ages; runs the PPM-revenue-
minus-AR-invoices reconciliation to expected unbilled; decomposes the variance (timing →
credits → exceptions → scope → data); works the error queue by reason with fix owners;
segments cost-reimbursable/LOC/multi-project cases before concluding.

## 2. Near-miss (should NOT load this skill)
> "Which sponsors are slowest to pay their invoices and what's our DSO trend?"

Expected: billed-AR performance — `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast`.
If this skill loads, tighten the WIP/pipeline framing.

## 3. Quality rubric
A good response:
- **Does the task:** status cut with ages, stepwise reconciliation with decomposed variance,
  exception queue by owner, and billing-acceleration recommendations, all dated.
- **Teaches:** unbilled as a queue on the PPM/AR seam that nobody owns by default, the
  expected-vs-measured completeness check, and why the edge cases must be segments.
- **Safe:** doesn't net away the error queue, doesn't count LOC awards in invoice metrics,
  doesn't double-count multi-project contracts, and reads cost-collection rhythm before
  declaring a spike a problem.
