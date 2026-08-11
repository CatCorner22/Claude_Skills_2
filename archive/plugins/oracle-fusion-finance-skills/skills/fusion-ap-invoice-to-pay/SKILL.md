---
name: fusion-ap-invoice-to-pay
description: >-
  Runs the Oracle Fusion Payables invoice-to-pay cycle — invoice entry and validation, PO
  matching (2/3/4-way), holds and their releases, approval workflow, accounting, and paying
  through Payment Process Requests (PPRs) that build payment files. Use when entering or fixing
  an AP invoice in Fusion, releasing holds, investigating why an invoice isn't paid, or running
  and troubleshooting a payment batch. Triggers: fusion AP, payables invoice, invoice hold,
  release hold, invoice validation, PO matching, three-way match, payment process request, PPR,
  payment batch, invoice not paid, pay run fusion, payables approval.
---

# Fusion AP invoice-to-pay

## When to use
- Entering, validating, approving, or accounting an invoice in Oracle Fusion Payables, or
  diagnosing why one is stuck (holds, matching, approval).
- Running a Payment Process Request (pay run) and troubleshooting payments that didn't select,
  didn't build, or produced a bad payment file.
- Not for: which payment rail to use and its cutoffs → see `banking-skills:payment-rails`. For
  payment fraud controls (positive pay, dual approval) → see
  `cash-management-skills:cash-management-controls`.

## Do it
1. **Place the invoice in the lifecycle before touching it.** Every Fusion invoice walks
   **entered → validated → approved → accounted → paid**, and each stage has its own blocker
   (holds block validation, workflow blocks approval, period status blocks accounting, selection
   criteria block payment). Read the invoice's status fields first — they tell you which stage
   you're actually debugging.
2. **Enter by the right door.** Manual UI for one-offs; **Import Payables Invoices** (FBDI) for
   batches (see `oracle-fusion-finance-skills:fusion-fbdi-data-loading`); scanned/IDR or supplier
   portal where implemented. For PO-based invoices, always **match to the PO** rather than keying
   distributions — matching copies the account and creates the control linkage.
3. **Understand the match level you're under.** 2-way = invoice vs PO (price/quantity ordered);
   3-way adds receipt (quantity received); 4-way adds inspection. Match failures create
   **system holds** (price, quantity ordered/received) that you *cannot* release by hand-waving —
   they release when the mismatch is fixed (correct the invoice, receive the goods, or adjust the
   PO within tolerance).
4. **Validate, then read the holds.** Run Validate (or let the batch job do it). Holds split into
   **system holds** (matching, distribution variance, tax) released by fixing the cause, and
   **manual holds** released by an authorized person with a reason.
   `references/holds-and-ppr.md` maps common holds to releases.
5. **Approval and accounting.** If invoice approval workflow is on, the validated invoice routes
   by amount/BU rules; then **Create Accounting** (draft to preview, final to post to GL via
   SLA). An invoice must be validated, approved, and accounted before it's payable.
6. **Pay through a Payment Process Request.** A PPR selects due invoices by criteria (BU, pay
   group, due date, payment method), builds proposed payments, applies the **payment process
   profile** (which formats the payment file for the bank), and confirms. Review the selected
   set — especially *missing* invoices — before submitting.
7. **Troubleshoot non-payment from selection backwards:** not selected (due date after the pay
   run window, wrong pay group, holds, unvalidated) → selected but rejected in build (missing
   supplier bank account, currency/profile mismatch) → built but file failed (profile/format
   issue). Each stage logs its own rejection reason.
8. **Verify the run:** payment count and total match the reviewed proposal, the file transmitted,
   payments show Negotiable, and the invoices flip to Paid. Void/reissue handles mistakes —
   never edit a confirmed payment.

## Why / learn
AP in Fusion is a chain of *controls*, and the design principle is that each control fails
closed: an invoice that can't prove it matches its PO gets a hold, an unapproved invoice can't
account, an unaccounted invoice can't pay. Reading a stuck invoice therefore means walking the
chain backwards and asking "which proof is missing?" — not searching for a magic release button.
Matching is the heart of it: the PO is a promise of price, the receipt a proof of delivery, and
the invoice a claim; 3-way matching just refuses to pay a claim that exceeds the promise or the
proof. On the payment side, the PPR separates *what to pay* (selection criteria — a treasury
decision) from *how to pay it* (payment process profile — a formatting/banking decision), which
is why cash-flow problems get fixed in selection criteria and bank-file problems get fixed in the
profile. Understanding that split turns pay-run firefighting into two small, separate problems.

## Common mistakes
- Keying distributions on a PO invoice instead of matching → loses the control linkage and invites duplicates; always match.
- Trying to manually release a system (matching) hold → fix the mismatch (invoice, receipt, or PO); the hold releases itself.
- Chasing "why wasn't it paid" in the payment file → start at selection: due date, pay group, holds, validation status.
- Missing supplier bank account discovered at build time → maintain payment attributes on the supplier before the run.
- Confirming a PPR without reviewing proposed payments → review totals and missing invoices first; confirmation is the point of no return.
- Editing a confirmed payment → void and reissue; payments are immutable records.

## Tailor to your environment
Capture your AP configuration in `references/your-environment.md` (sensitive detail in
`your-environment.private.md`, git-ignored): business units, match level by PO type, tolerance
settings, approval thresholds, pay groups, PPR templates and schedule, payment process profiles
per bank, and who owns hold release. **Never commit supplier names, bank details, or real
invoice data.**

## References
- references/holds-and-ppr.md — common holds → releases; PPR stages and rejection reasons
- references/your-environment.md — your BUs, tolerances, pay groups, profiles (fill in)
