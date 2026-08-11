---
name: federal-sponsored-ar-compliance-risk
description: >-
  Assesses compliance and audit risk in Receivables data for federal sponsored projects —
  identifying federal awards, scanning for high-risk patterns (aged federal AR, frequent
  adjustments/credit memos, write-offs, unbilled build-up, allowability-suspect costs),
  applying the §200.426 bad-debt and §200.410 questioned-cost rules to adjustments and
  write-off proposals, mapping Single Audit/SEFA implications, and grading documentation
  readiness — delivered as a prioritized risk assessment that is explicitly not an audit
  opinion. Use for aging analysis, exception review, write-off recommendations, or any
  risk-focused question on federal awards. Triggers: federal AR risk, questioned costs,
  write off federal receivable, single audit exposure, SEFA, federal compliance risk,
  audit risk sponsored projects, federal adjustments review, closeout residual balance,
  subrecipient risk, cost sharing shortfall.
---

# Federal sponsored-AR compliance and audit risk

## When to use
- Risk-reading federal receivables data: aging reviews, exception/adjustment analysis,
  write-off proposals, close-out exposure, or "how bad is this?" questions on federal awards.
- Pre-audit self-assessment of the AR-relevant Single Audit surface.
- Not for: the underlying rules themselves → see
  `sponsored-projects-ar-skills:uniform-guidance-federal-core` (frame/thresholds),
  `sponsored-projects-ar-skills:federal-billing-cash-management` (payment mechanics), and
  `sponsored-projects-ar-skills:federal-effort-reporting-basics` (personnel costs). Enter via
  the router (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Isolate the federal population first.** Identify federal awards by user flag, sponsor
   attributes (agency customers, pass-through entities), or award metadata — and separate
   **direct federal** from **pass-through** (federal money via a prime; still federal for
   compliance and SEFA). Everything after this step applies only to that population; blending
   federal and non-federal risk profiles produces noise in both.
2. **Scan for the high-risk patterns**, each of which maps to a specific compliance exposure:
   - **Large or aged federal AR** — on reimbursement awards, usually an improper/late request
     (fix the request); on draw-based awards, an aging *undrawn* balance (working capital +
     close-out risk).
   - **Frequent adjustments or credit memos** — churn suggests billing quality problems;
     auditors read adjustment patterns as control weakness.
   - **Write-offs against federal awards** — see step 3; this is the brightest line.
   - **High unbilled relative to expenditures** — value earned but unclaimed; expires at
     close-out (tie to `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`).
   - **Allowability-suspect costs in the billed base** — entertainment-like charges, over-cap
     salaries, unallocated lump sums; each is a future questioned cost already billed.
   `references/risk-scan-checklist.md` has the full pattern → exposure → action table.
3. **Apply the write-off rule exactly.** Per **§200.426, bad debts are unallowable** — an
   uncollectible federal receivable is generally **moved to non-sponsored (institutional)
   funds**, never written off against the award. Any write-off recommendation in the data set
   gets checked: if it touched a federal award, it's a finding to remediate, not history.
4. **Trace the questioned-cost mechanics.** Costs later determined unallowable **must be
   refunded, often with interest (§200.410)** — which can *reverse prior AR and revenue
   recognition*: billed and even collected federal AR is contingent until the allowability
   tail expires. Quantify exposure with the full multiplier (direct + fringe + F&A — see the
   effort skill's math) rather than the direct cost alone.
5. **Map the Single Audit surface (Subpart F).** Entities expending **≥ $1,000,000 in federal
   awards in a fiscal year** get a Single Audit; expenditure (and by extension billing/AR)
   data feeds the **SEFA (Schedule of Expenditures of Federal Awards)** and drives major-
   program determination and compliance testing. The AR analyst's contribution: expenditure
   and billing data that reconcile to the SEFA, and clean adjustment trails on anything an
   auditor will sample.
6. **Grade documentation readiness.** For each risk flag, ask whether the records demonstrate
   **allowability, allocability, and internal controls** (§200.302/§200.403 standards): the
   support behind billed costs, draw packages, adjustment justifications, and write-off
   approvals. A risk with strong documentation is a finding avoided; the same risk without it
   is a finding written. (Client-side audit craft:
   `treasury-accounting-skills:audit-readiness-and-pbc`.)
7. **Check the edge cases that hide risk:** **cost-sharing shortfalls** (unmet committed match
   → potential award reduction/refund), **program income** treatment (offsets billable costs
   under most methods), **residual balances at closeout** (unbilled expires; unspent advances
   return), **multi-year awards** (thresholds and terms can differ by award year), and
   **subrecipient pass-throughs** (the prime owns subrecipient monitoring; their
   noncompliance can become your questioned cost).
8. **Deliver:** risk assessment summary → prioritized flags (exposure-weighted, with the
   dollar math shown) → recommended documentation/process improvements per flag → **explicit
   disclaimer that this is an analytical risk assessment, not an audit opinion or legal
   advice** — in the router's standard output structure.

## Why / learn
Federal AR risk is *asymmetric in time*: commercial AR risk mostly resolves at collection
(paid or not), while federal AR stays contingent long after cash arrives, because allowability
review, effort certification cycles, and the Single Audit all run behind billing — a dollar
collected in year one can become a refund with interest in year three. That's why this skill
reads AR data for *patterns* rather than balances: adjustments, write-offs, and unbilled
build-ups are the visible exhaust of the processes auditors actually test, and each pattern
points at a specific rule (§200.426 for write-offs, §200.410 for questioned costs, Subpart F
for the testing machinery). The moved-to-institutional-funds rule for uncollectibles is the
signature example of federal logic: the government has pre-declared that its awards never
absorb collection failures, so the institution's only real defenses are upstream — bill
timely, bill allowable, document everything. And the disclaimer isn't humility theater:
risk-scanning is an analyst inferring exposure from data patterns, while an audit opinion is
a regulated attestation with defined procedures — conflating them misleads exactly the
audience (leadership, auditors) this deliverable serves.

## Common mistakes
- Scanning federal and non-federal AR as one population → the rules differ categorically; isolate first, including pass-throughs.
- Approving a "normal" write-off on a federal award → §200.426; move the loss to institutional funds and treat the event as a process finding.
- Sizing questioned-cost exposure at direct cost only → fringe and F&A unwind too; use the full multiplier.
- Treating collected federal AR as closed risk → contingent until the allowability/audit tail passes; age the tail, not just the balance.
- Reading frequent credit memos as tidy housekeeping → auditors read churn as billing control weakness; find the root cause.
- Ignoring cost-sharing and program income in an AR review → both quietly change what was billable; check commitments and income method.
- Forgetting pass-through obligations → subrecipient noncompliance rolls up to the prime; monitoring evidence belongs in the readiness grade.
- Presenting the assessment as an audit conclusion → it's analytics; the disclaimer is part of the deliverable.

## Tailor to your environment
Record your risk posture in `references/your-environment.md` (findings and award specifics in
`your-environment.private.md`, git-ignored): how federal awards are flagged in your data,
your Single Audit history and major programs, write-off policy and the institutional fund
used, cost-sharing tracking, and subrecipient monitoring ownership. **Never commit real
findings, award numbers, or balances.**

## References
- references/risk-scan-checklist.md — pattern → exposure → action table, SEFA tie-out, edge-case checks, disclaimer language
- references/your-environment.md — your flags, audit history, policies, owners (fill in)
