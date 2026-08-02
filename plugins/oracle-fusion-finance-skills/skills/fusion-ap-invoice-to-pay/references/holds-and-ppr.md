# AP holds and Payment Process Request stages (reference)

## Contents
- Common holds → how they release
- PPR stages and where payments fall out
- Payment file and post-confirmation issues

## Common holds → how they release
| Hold | Type | Cause | Release |
|---|---|---|---|
| Price | System (matching) | Invoice unit price exceeds PO price beyond tolerance | Correct invoice price, update PO, or adjust tolerance policy |
| Qty Ordered | System (matching) | Billed quantity > ordered | Correct invoice or amend PO |
| Qty Received | System (matching, 3-way) | Billed quantity > received | Receive the goods, or correct the invoice |
| Distribution variance | System | Distribution total ≠ invoice total | Fix distribution amounts |
| Tax variance | System | Calculated vs entered tax mismatch | Recalculate/correct tax lines |
| No rate | System | Foreign-currency invoice without a conversion rate | Supply the rate or run rate updates |
| Supplier site on hold | Manual/config | Site flagged (dispute, compliance) | Authorized release at the supplier site level |
| Manual hold (user-defined) | Manual | Deliberate stop (quality, dispute) | Authorized person releases with a reason — audit-trailed |

System holds re-derive at validation: fix the cause, revalidate, and the hold clears. Manual
holds persist until an authorized release.

## PPR stages and where payments fall out
1. **Selection** — criteria: BU, payment business function, pay group, payment method, due date
   window, currency. Invoices missing here are unvalidated, unapproved, held, not yet due, or
   outside the criteria. Fix the invoice or widen criteria deliberately (not casually).
2. **Proposed payments review** — grouped by supplier/site/method. Check count, total, discounts
   taken/lost, and anything unexpectedly *absent*.
3. **Build** — creates payment documents. Falls out here: missing/invalid supplier bank account,
   payment method vs profile mismatch, currency the profile can't handle.
4. **Format** — the payment process profile renders the bank file (ISO 20022 pain.001, NACHA,
   positional formats). Failures here are profile/template issues, not invoice issues.
5. **Transmit/confirm** — file goes to the bank (or print); confirming marks payments Negotiable
   and invoices Paid.

## Payment file and post-confirmation issues
- Bank rejects the file → compare the file against the bank's spec version; the fix lives in the
  payment process profile/format template.
- One payment in a confirmed run is wrong → **void** that payment (reopens the invoice) and
  reissue; never edit the payment record.
- Duplicate payment risk after re-running → check invoice status is Paid before any manual
  one-off; duplicate-invoice checks key on supplier + invoice number.
