# Sponsored-AR anomaly playbook (reference)

## Contents
- Exception queue formats
- Anomaly thresholds and formulas
- Cross-pillar worksheet
- Risk-register template

## Exception queue formats
One block per queue, always with age and trend:
| Queue | Count | Amount | Oldest (days) | 3-month trend | Owner |
|---|---|---|---|---|---|
| Billing exceptions / Error status | | | | ↑/→/↓ | |
| Contract/billing holds | | | | | |
| Unapplied receipts | | | | | |
| At-risk receipts (disputed/collections-flagged) | | | | | |
Escalate any queue whose *trend* is up two consecutive reviews, regardless of size.

## Anomaly thresholds and formulas
Starting points — tune to your volumes in the environment file:
- **Outlier aging:** account/award weighted-average days vs its sponsor-category mean;
  flag |z| ≥ 2 (z = (x − μ_segment) / σ_segment), or > p95 of the segment.
- **DSO spike:** current DSO vs trailing-6-period mean; flag moves > 2σ or > 20% —
  then run mix-vs-behavior decomposition (KPI skill) before labeling it behavior.
- **Adjustment/credit-memo volume:** count and amount per period by preparer/project/sponsor;
  flag > 2σ vs trailing 6 periods, and any single item above your materiality line.
- **Overdue-beyond-terms:** days past *sponsor-specific* terms; flag > 1.5× terms, escalate
  > 2×.
- **Funding proximity:** billed + pipeline ≥ 90% of award funding → watch; > 100% → immediate.
Keep it rules-and-z-scores here; persistent/subtle patterns (fraud-like sequences,
multi-variable drift) → `machine-learning-skills:anomaly-detection`.

## Cross-pillar worksheet (per award)
| Line | Source |
|---|---|
| Costs incurred by category (ITD) | PPM cost/expenditure data |
| Billable base (after allowability screens) | PPM + policy |
| Billed by category (ITD) | AR transactions (or PPM invoice detail) |
| **Gap: billed − billable base** | positive = over-billing risk; negative = leakage |
| Category mismatches | billed categories with no corresponding cost |
Route: over-billing on federal awards → `federal-sponsored-ar-compliance-risk`; leakage →
`unbilled-billed-ar-wip-recon`; item verdicts → `federal-cost-allowability`.

## Risk-register template
| # | Risk / finding | Category | Awards/sponsors affected | Exposure $ | Likelihood | Age/trend | Condition or indicator | Owner | Mitigation | Review date |
|---|---|---|---|---|---|---|---|---|---|---|
Categories: exception / sponsored-specific / anomaly / cross-pillar.
Prioritization score: exposure × likelihood × documentation-weakness (1–3 each).
Register hygiene: every row has an owner and a review date; closed rows keep their history;
the register is reviewed on a cadence (monthly during close, quarterly minimum).
