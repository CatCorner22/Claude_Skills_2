---
name: fusion-ar-and-collections
description: >-
  Runs Oracle Fusion Receivables — creating and importing AR transactions (invoices, credit
  memos), applying receipts manually and through lockbox/automatch, keeping unapplied and
  on-account cash honest, and working aging and the Advanced Collections dunning/strategy cycle.
  Use when booking or fixing an AR transaction in Fusion, applying or troubleshooting receipts,
  reconciling unapplied cash, or setting up aging and collections follow-up. Triggers: fusion AR,
  receivables invoice, apply receipt, unapplied receipt, on-account, lockbox, autoapply,
  credit memo fusion, AR aging, collections fusion, dunning, receipt application, customer
  balance.
---

# Fusion AR and collections

## When to use
- Creating, importing (AutoInvoice), crediting, or adjusting transactions in Oracle Fusion
  Receivables; applying or unapplying receipts; running lockbox.
- Investigating customer balances: unapplied/on-account cash, aging buckets, disputed items,
  and the collections workflow.
- Not for: cash-side bank reconciliation of the deposits → see
  `cash-management-skills:bank-reconciliation`. For working-capital strategy (DSO targets, terms)
  → see `finance-skills:working-capital-management`.

## Do it
1. **Anchor on the two ledgers inside AR.** Receivables tracks *transactions* (invoices, credit
   memos, debit memos, adjustments) and *receipts* (cash in), and every customer balance question
   is "which transactions remain open and which receipts aren't fully applied?" Start any
   investigation with the customer's open items and unapplied receipts, not the GL.
2. **Create transactions by the right door.** Manual UI for one-offs; **AutoInvoice** for volume
   (import lines from order management/billing feeds or FBDI, then run Import AutoInvoice and work
   the exceptions in the AutoInvoice workbook). Transaction type controls sign, accounting, and
   whether it posts to AR; terms drive due date and aging.
3. **Credit and adjust with the audit trail, not deletes.** Wrong invoice → **credit memo**
   (full or partial, applied to the invoice); small write-offs → **adjustment** with an approved
   reason/limit; never "fix" by editing a completed transaction.
4. **Apply receipts deliberately.** Manual receipts: enter, then apply to the customer's open
   items — oldest first unless remittance advice says otherwise. Volume: **lockbox** (bank file
   in, AutoMatch applies by invoice number/amount with configurable rules) or **AutoApply**.
   Whatever can't match cleanly lands as **unapplied** (money on the customer, no invoice) or
   **on-account** (deliberately parked) — both are real cash in GL but unresolved in AR.
5. **Work the unapplied queue weekly.** Every unapplied/on-account receipt is either missing
   remittance info (chase it), a short-pay/dispute (route to collections), or a duplicate/refund
   case. An aging unapplied balance is the #1 sign the application process is broken.
6. **Read aging the way collections does.** Aging buckets (current/1–30/31–60/61–90/90+) run off
   due date. In **Advanced Collections**, customers get scored, assigned strategies (sequences of
   tasks: dunning letter, call, escalate), and delinquencies drive the work queue. Disputes hold
   items out of dunning while they're researched.
7. **Close the loop to cash and GL.** Receipts tie to bank deposits (remittance batches →
   Cash Management for statement reconciliation), and Create Accounting posts AR activity to GL.
   Month-end: AR aging total reconciles to the AR control account —
   `references/ar-workflows.md` has the checklist.

## Why / learn
AR breaks in the *gaps between systems and intentions*: the invoice said one amount, the customer
paid another, the bank file truncated the reference — and every unmatched dollar has to park
somewhere visible (unapplied or on-account) rather than vanish. Fusion's design makes those
parking lots explicit precisely so you can manage them; a clean AR shop is defined by how fast
cash leaves them, not by never using them. The audit-trail rule (credit memos and adjustments,
never edits) exists because AR is a legal record of claims against customers — the correction
history *is* the defense in a dispute. And collections is just aging made actionable: buckets
sort by risk, strategies standardize the follow-up, and disputes formally separate "won't pay
yet" from "won't pay ever," which keeps dunning credible. When you see AR this way — claims,
cash, and the reconciliation of the two — every screen in the module maps to one of the three.

## Common mistakes
- Fixing a wrong invoice by editing it → credit memo + rebill; completed transactions are audit records.
- Letting unapplied receipts age → work the queue weekly; every one is missing info, a dispute, or a refund case.
- Applying receipts newest-first for convenience → distorts aging; oldest-first unless remittance says otherwise.
- Treating on-account as applied → it's parked cash, still unresolved against invoices.
- Dunning disputed items → log the dispute so the strategy skips them; dunning a disputed invoice burns goodwill.
- Skipping AutoInvoice exceptions → lines sit in the interface, revenue and AR both understated; work the exception workbook.
- Aging-to-GL mismatch ignored at close → reconcile AR subledger to the control account before signing off.

## Tailor to your environment
Describe your AR setup in `references/your-environment.md` (real customer data only in
`your-environment.private.md`, git-ignored): business units, transaction types and sources,
receipt methods and lockbox setup, AutoMatch rules, aging buckets, collections strategies, and
write-off limits. **Never commit customer names, balances, or bank references.**

## References
- references/ar-workflows.md — lockbox/AutoMatch flow, unapplied-cash triage, month-end AR checklist
- references/your-environment.md — your BUs, types, receipt methods, strategies (fill in)
