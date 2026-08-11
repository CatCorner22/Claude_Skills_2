# Fusion AR working references

## Contents
- Lockbox / AutoMatch flow
- Unapplied-cash triage
- Month-end AR checklist

## Lockbox / AutoMatch flow
1. Bank produces a lockbox file (BAI2 lockbox or bank-specific format) with payer, amount, and
   remittance references.
2. Load via the lockbox import (transmission format maps the file's fields).
3. Validation pass: payer identified? invoice references parse? amounts consistent?
4. **AutoMatch** applies receipts using match rules — exact invoice number, then fuzzy/reference
   heuristics, within configured thresholds. Tune thresholds conservatively: a false match is
   worse than an unapplied receipt (you'd be misstating *which* customer/invoice is paid).
5. Exceptions land unidentified (payer unknown) or unapplied (payer known, items unclear).
   Unidentified → research payer via bank details/remitter name; unapplied → triage below.

## Unapplied-cash triage
For each unapplied or on-account receipt, classify and act:
| Pattern | Likely cause | Action |
|---|---|---|
| Amount matches one open invoice ± small tolerance | Reference missing/garbled | Apply; note tolerance write-off if policy allows |
| Round amount, no invoice match | Prepayment or deposit | Park on-account deliberately; tie to order/contract |
| Payment = several invoices minus a deduction | Short pay / dispute | Apply to invoices, create dispute/deduction case for the gap |
| Duplicate of a recent payment | Customer error | Contact customer: apply forward or refund |
| Payer unknown entirely | Missing remitter data | Bank trace; if unresolved past policy window, escalate per unclaimed-funds policy |
Track the queue by age; unapplied older than ~30 days signals a process gap (bad remittance
channels, references dropped by the bank file, or AutoMatch rules too tight).

## Month-end AR checklist
1. AutoInvoice interface clear (no stuck lines) — exceptions worked or documented.
2. All receipt batches for the period entered and remitted.
3. Unapplied/on-account reviewed; material items explained.
4. Adjustments and credit memos approved within limits.
5. Create Accounting final for Receivables; transfer to GL complete.
6. **AR aging total = AR control account balance in GL** — investigate any gap (usually unposted
   activity, manual JEs against the control account, or period-cutoff receipts).
7. Reserve review: aged buckets feed the allowance for doubtful accounts.
