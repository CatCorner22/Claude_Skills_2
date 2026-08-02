# Federal AR risk scan (reference)

Educational tool built on public 2 CFR 200 text. Deliverables using it carry the standing
disclaimer: analytical risk assessment, **not an audit opinion or legal advice**; the
regulation, award terms, and institutional policy govern.

## Contents
- Pattern → exposure → action table
- Exposure math
- SEFA tie-out
- Edge-case checks
- Disclaimer language

## Pattern → exposure → action table
| Pattern in the data | Compliance exposure | First action |
|---|---|---|
| Aged federal AR (reimbursement awards) | Improper/late requests; 30-day clock never started | Review request quality; refile properly (see federal-billing-cash-management) |
| Aged undrawn balance (LOC/PMS awards) | Working capital loss; close-out expiry | Draw promptly; check award end dates |
| Write-off posted against a federal award | §200.426 violation | Reclassify to institutional funds; document; fix the policy gate |
| Frequent credit memos/adjustments on federal invoices | Billing control weakness (audit optics + real errors) | Root-cause the churn; tighten pre-billing review |
| Unbilled high vs expenditures | Unclaimed earned value; expires at closeout | Pipeline recon; accelerate billing (unbilled-billed-ar-wip-recon) |
| Allowability-suspect line items in billed base | Future questioned costs, refund + interest | Allowability screen; correct before the auditor finds it |
| Salary-heavy awards, weak certification status | Effort questioned costs (with multiplier) | Effort red-flag scan (federal-effort-reporting-basics) |
| Draws exceeding expenditures | §200.346 debt + interest | Immediate reconciliation and remediation |
| Missing subrecipient monitoring evidence | Pass-through liability for sub noncompliance | Monitoring file review before audit |
Prioritize flags by exposure dollars × likelihood × documentation weakness.

## Exposure math
```
Questioned direct cost                 D
+ Fringe on salary portion             F
+ F&A on (D + F) at applied rate       I
= Gross exposure                       D + F + I    (+ interest per §200.410 where applicable)
```
Report per flag and in total; separate "billed but at risk" from "collected but contingent."

## SEFA tie-out
- Federal expenditures by award (CFDA/ALN) in the ledger = SEFA totals.
- Billing/draw records reconcile to expenditures claimed.
- ≥ $1,000,000 total federal expenditures in the fiscal year → Single Audit applies
  (post-Oct-2024 threshold; award terms and fiscal year determine which regime).
- Pass-through amounts identified with the prime's identifying numbers.
Discrepancies between AR/billing data and the SEFA are audit findings in waiting — reconcile
before fieldwork.

## Edge-case checks
- [ ] **Cost sharing:** committed match tracked and met? Shortfall → potential proportional
      refund/award reduction.
- [ ] **Program income:** method (deductive/additive/matching) identified? Income offsets
      billable costs under the default deductive method.
- [ ] **Closeout:** awards ending ≤120 days with unbilled or undrawn balances (the money that
      expires); final reports calendared.
- [ ] **Multi-year awards:** which UG revision applies per award year; threshold drift.
- [ ] **Subrecipients:** risk assessments, monitoring evidence, sub SEFA/audit results
      reviewed.

## Disclaimer language (attach to every deliverable)
> This assessment is an analytical review of receivables data patterns against public
> Uniform Guidance provisions. It is not an audit, an audit opinion, or legal advice; it does
> not replace the award terms, 2 CFR 200, agency policy, or your institution's compliance
> office. Findings are indicators for management follow-up, not determinations.
