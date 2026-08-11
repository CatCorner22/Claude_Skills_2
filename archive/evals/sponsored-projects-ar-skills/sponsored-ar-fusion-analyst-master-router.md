# Evals — sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router

## 1. Positive trigger (should load the skill)
> "How healthy is our sponsored projects AR? Here's an export from our Fusion environment —
> tell me where we stand and what to do."

Expected: skill loads first; classifies this as a multi-part question (profile → recon + KPI →
reporting); confirms the award/bill-plan mix before any metric; validates the export (source,
as-of date, aging basis) before calculating; sequences the sub-skills and enforces the
five-part output structure.

## 2. Near-miss (should NOT load this skill)
> "Our regular customer invoices are aging badly — help me work the collections queue."

Expected: general (non-sponsored) AR — `oracle-fusion-finance-skills:fusion-ar-and-collections`.
If this skill loads, tighten the sponsored/grants framing in the description.

## 3. Quality rubric
A good response:
- **Does the task:** routes correctly, confirms award type, refuses to compute from assumed
  data (requests the extract or its precise description), and delivers in the standard
  structure (summary, validation, metrics, recommendations, edge cases).
- **Teaches:** why sponsored AR spans the PPM/Receivables seam, why award type changes every
  metric's meaning, and why validation-before-calculation is non-negotiable.
- **Safe:** public Oracle concepts only; flags implementation-specific config as questions;
  every number carries its as-of date.
