---
name: revenue-billing-reconciliation
description: >-
  Reconciles PPM revenue recognition against AR billing for sponsored awards from the
  accounting side — the documented Generate Revenue → events → invoice flow, the variance
  identity (recognized revenue − billed = unbilled or over-billed), funding-limit checks
  against contract amounts, and the unbilled-AR account roll (DR Unbilled Receivable / CR
  Revenue at recognition; DR Receivable / CR Unbilled Receivable at invoicing) through to GL
  tie-out. Use for questions about revenue vs invoiced amounts, over/under-billing, unbilled
  balance substantiation, or tying sponsored revenue and receivables to the GL. Triggers:
  revenue vs billing, over billed, under billed, revenue reconciliation, unbilled receivable
  account, GL tie-out sponsored, recognized vs invoiced, revenue events, billing in excess,
  substantiate unbilled balance, project revenue reconciliation.
---

# Revenue-to-billing reconciliation for sponsored awards

## When to use
- Reconciling recognized project revenue to billed amounts per award, substantiating the
  unbilled (or deferred/over-billed) balance, and tying both to the GL.
- Answering "are we over- or under-billed against revenue?" and "does the unbilled account
  balance make sense?"
- Not for: the operational billing pipeline (statuses, queues, exceptions) → see
  `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon` — that skill finds *why*
  amounts are stuck; this one proves *what the balances should be*. Enter via the router
  (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Anchor on the documented flow.** In PPM, **Generate Revenue** creates revenue events per
   the contract's revenue method (as-incurred for cost-reimbursable, event/milestone-based
   for fixed-price — which may differ from the *billing* method); invoices are generated
   separately and interface to AR through AutoInvoice. Revenue and billing are **two
   independent streams off the same contract**, so their difference is a real balance, not an
   error by default.
2. **Assemble the public metrics per award/contract:** recognized **project revenue**
   (Projects - Revenue Real Time concepts), **invoice amounts** and **credit memo amounts**
   (Receivables - Transactions / Projects - Invoices), and **adjustments** — all
   inception-to-date and for the period, netting credits/rebills by linked transaction.
3. **Compute the variance identity per contract:**
   **Recognized revenue − billed (net) = unbilled AR** (positive) **or over-billing/deferred
   revenue** (negative). Cost-reimbursable awards should run mostly small-positive (billing
   lags cost collection by days); milestone awards legitimately swing both ways (a milestone
   billed ahead of revenue = deferred). Judge each variance against its *contract type's*
   normal, not against zero.
4. **Check funding limits.** Against Projects - Funding concepts: neither ITD revenue nor ITD
   billing should exceed **contract/award funding** (hard-limit settings normally stop
   billing; revenue can also cap). Flag: billed > funding (compliance event — sponsors claw
   this back), revenue > funding (recognition needs review), and both approaching the ceiling
   (bill-and-recognize-before-close-out planning).
5. **Trace the accounting so the balances substantiate.** At revenue recognition PPM books
   **DR Unbilled Receivable / CR Revenue**; when the invoice is generated and accepted, the
   system books **DR (Trade) Receivable / CR Unbilled Receivable** (over-billing runs through
   deferred revenue/unearned instead). Therefore the **unbilled receivable GL balance =
   Σ per-contract (revenue − billed)** positives (and deferred = the negatives) — that
   identity *is* the GL tie-out. `references/revenue-recon-worksheet.md` has the waterfall,
   the entry map, and the tie-out worksheet.
6. **Explain the variance, don't just report it.** Decompose per contract: normal lag
   (revenue events awaiting the next billing cycle), billing holds/exceptions (route to
   `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`), revenue method vs billing
   method divergence (structural, explain once), credits/rebills in flight, and true errors
   (missing events, double-billing). Aged unbilled with no pipeline explanation is the
   escalation case.
7. **Deliver:** the reconciliation waterfall (revenue → net billed → unbilled/deferred →
   GL), variance explanations by cause, and compliance flags (over-billing against sponsor
   limits, funding-ceiling proximity, aged unexplained unbilled) — in the router's standard
   structure, dated, with the aging caveat that both streams must be extracted as-of the same
   date.

## Why / learn
Revenue recognition answers "what have we earned?"; billing answers "what have we claimed?" —
and sponsored contracts deliberately let those diverge (you earn cost-reimbursable revenue the
day the cost posts, but you bill on the cycle; you bill a milestone on the event, but earn it
per the revenue method). The unbilled receivable account is the ledger's memory of that
divergence, which is why this reconciliation is really a *substantiation*: the GL unbilled
balance is only correct if it equals the sum of per-contract revenue-minus-billed positives,
and any gap means one stream posted without the other (an interface failure, a manual entry,
a conversion artifact). Reading the identity per contract type matters because the same
number means different things — persistent positive variance on a milestone award is normal
structure, while the identical number on a cost-reimbursable award is a billing lag someone
should chase. The funding-limit check rides along because the contract amount is the one
ceiling both streams share: revenue and billing can disagree with each other, but neither may
exceed the award — and over-billing a sponsor is the variance that turns into a refund. This
is also where AR analysis meets the close: the recon skill clears the queues, but *this*
worksheet is what the auditor asks for when the unbilled balance appears on the balance
sheet (tie to `treasury-accounting-skills:audit-readiness-and-pbc`).

## Common mistakes
- Treating any revenue-vs-billing difference as an error → the divergence is designed; judge against the contract type's normal.
- Comparing gross billed without netting credits/rebills → phantom over-billing; net by linked transaction first.
- Substantiating the GL unbilled balance top-down only → the identity is per-contract; a netted total can hide offsetting errors.
- Extracting revenue and billing as-of different dates → guaranteed fake variance; same as-of date for both streams.
- Ignoring the revenue-method vs billing-method split on fixed-price awards → structural variance misread as a problem.
- Missing the deferred side → negative variances (billed > revenue) are real liabilities, not zero-floor noise.
- Flagging funding-ceiling proximity only at breach → 90%+ proximity on both streams is the planning window; at breach it's a refund.
- Reporting the variance without cause decomposition → an unexplained aged unbilled balance is the finding, not the number itself.

## Tailor to your environment
Record your revenue/billing configuration in `references/your-environment.md` (contract-level
data in `your-environment.private.md`, git-ignored): revenue methods by contract type, billing
cycles, your unbilled and deferred account combinations, hard-limit settings, and normal
variance bands per award type. **Never commit real contract amounts or sponsor data.**

## References
- references/revenue-recon-worksheet.md — waterfall format, accounting entry map, GL tie-out worksheet, variance-cause table
- references/your-environment.md — your methods, cycles, accounts, bands (fill in)
