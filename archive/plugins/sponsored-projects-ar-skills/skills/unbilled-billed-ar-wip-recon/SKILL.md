---
name: unbilled-billed-ar-wip-recon
description: >-
  Reconciles unbilled (WIP) versus billed AR for sponsored projects and tracks the billing
  lifecycle — measuring pipeline by billing status (Ready to Bill, In Progress, Billed, Error),
  reconciling PPM revenue events against Receivables invoices, isolating holds and exceptions,
  and handling cost-reimbursable, letter-of-credit, and multi-project-contract edge cases. Use
  when the question involves work-in-progress, unbilled receivables, draft invoices, billing
  backlog, invoices in error, or PPM-to-AR reconciliation variances. Triggers: unbilled AR,
  WIP reconciliation, billing status, draft invoices, billing backlog, invoices in error,
  ready to bill, PPM to AR reconciliation, unbilled to billed, billing exceptions, LOC billing,
  stuck invoices.
---

# Unbilled/billed AR and WIP reconciliation

## When to use
- Measuring how much sponsored-project value is unbilled, where it sits in the billing
  pipeline, and what's stuck.
- Reconciling PPM-side revenue/costs against Receivables-side invoices, and explaining the
  variance.
- Not for: aging and collections of *already-billed* AR → see
  `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast` (metrics) and
  `oracle-fusion-finance-skills:fusion-ar-and-collections` (working it). For the accounting
  view — substantiating the unbilled GL balance and revenue-vs-billed variance → see
  `sponsored-projects-ar-skills:revenue-billing-reconciliation`. Come here via the
  router (`sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`).

## Do it
1. **Anchor on the billing-status pipeline.** From Project Billing - Bill Transactions Real
   Time concepts, every billable transaction carries a status: **Ready to Bill** (eligible,
   awaiting generation), **In Progress** (invoice being generated/in draft/in transfer),
   **Billed** (through AutoInvoice into Receivables), **Error** (failed validation — the
   stuck queue). The first deliverable is always the pipeline cut: amount and count by status,
   by project/contract/sponsor.
2. **Compute the three balances and the flow between them:**
   - **Unbilled AR** = incurred cost (cost-reimbursable) or earned/recognized amounts
     (milestone) not yet invoiced — Ready to Bill + In Progress + Error.
   - **Billed AR** = invoiced but uncollected — lives in Receivables payment schedules.
   - **Transition flow** = what moved unbilled → billed in the period (invoices generated and
     accepted). A healthy pipeline moves; a growing Error or aged Ready-to-Bill bucket is the
     finding.
3. **Reconcile PPM revenue to AR invoices.** Using public areas (Projects - Revenue Real Time
   vs Receivables - Revenue/Transactions): by contract, PPM recognized revenue −
   AR invoiced amounts = expected unbilled. Compare that *expected* unbilled to the *measured*
   pipeline from step 2; the residual decomposes into timing (generated not accepted),
   errors/exceptions, credits/rebills not netted, or genuine data issues.
   `references/wip-recon-worksheet.md` has the worksheet and variance decomposition.
4. **Work the exception queue explicitly.** Error-status transactions and billing holds each
   have a reason (missing customer setup, AutoInvoice validation, funding exhausted,
   contract hold). List them with age and amount — the fix owner differs by reason (grants
   accountant vs AR vs contract admin), so the deliverable names the queue per owner.
5. **Handle the edge cases as segments, not noise:**
   - **Cost-reimbursable awards:** unbilled grows with expense collection; check expenditure
     cutoff vs billing cycle (a "spike" after month-end cost collection is normal rhythm).
   - **LOC (letter-of-credit) billing:** drawn, not conventionally invoiced — exclude from
     standard invoice pipeline metrics and report the LOC draw status separately.
   - **Multi-project contracts:** billing happens at the contract; project-level unbilled
     needs the contract-to-project allocation — don't double count across projects.
6. **Deliver:** WIP summary by status/project + the reconciliation variance table + specific
   recommendations to accelerate billing (clear the error queue by owner, tighten the
   generate-to-accept cycle, align billing calendar to cost collection), in the router's
   standard output structure with the as-of date prominent.

## Why / learn
Unbilled AR is where sponsored-project cash goes to wait, and the reason it deserves its own
reconciliation is that *nobody owns it by default*: PPM thinks its job ended at revenue
recognition, Receivables hasn't heard of the money yet, and the balance sits on the seam
between them. The billing-status pipeline turns that seam into something manageable — a queue
with stages, ages, and owners, exactly like any operations backlog. The
PPM-revenue-minus-AR-invoices reconciliation is the completeness check on the queue itself: the
pipeline shows what the system *knows* is unbilled, while the revenue-vs-invoice gap shows what
*should* be unbilled, and the difference between those two is where silent leakage lives
(transactions that never became billable, credits nobody netted, conversion artifacts). The
edge cases matter because they break the mental model quietly: LOC awards make "no invoices"
normal, cost-reimbursable awards make lumpy unbilled normal, and multi-project contracts make
project-level sums wrong — segment first and each segment behaves sensibly again. For a
university or research institution, this pipeline *is* working capital: every day value sits in
Ready to Bill is an interest-free loan to the sponsor.

## Common mistakes
- Reporting one unbilled number with no status breakdown → the pipeline cut (Ready/In Progress/Error, with ages) is the analysis.
- Ignoring the Error queue because it's small this month → it compounds; list by reason with an owner per queue.
- Comparing PPM revenue directly to AR collections → the middle terms (invoiced, accepted) are where the story is; reconcile stepwise.
- Counting LOC awards in invoice-pipeline metrics → separate segment; they draw, not invoice.
- Summing project-level unbilled across a multi-project contract → allocation double-counts; reconcile at contract, then allocate.
- Reading a post-close unbilled spike as a problem on cost-reimbursable awards → it's the cost-collection rhythm; compare to the billing calendar.
- Omitting the as-of date → pipeline snapshots decay in days; date every number.

## Tailor to your environment
Record your billing operation in `references/your-environment.md` (award-level specifics in
`your-environment.private.md`, git-ignored): billing calendar vs cost-collection schedule,
your exception reasons and fix owners, LOC award list handling, and normal pipeline benchmarks
(so anomalies stand out). **Never commit real award numbers, sponsor names, or balances.**

## References
- references/wip-recon-worksheet.md — pipeline cut format, reconciliation worksheet, variance decomposition, exception queue format
- references/your-environment.md — your calendar, owners, benchmarks (fill in)
