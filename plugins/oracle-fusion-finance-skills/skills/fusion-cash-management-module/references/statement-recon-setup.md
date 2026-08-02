# Fusion CE statement loading and reconciliation setup (reference)

## Contents
- Statement formats
- Matching-rule design patterns
- Transaction-code mapping
- Month-end tie-out checklist

## Statement formats
| Format | Notes |
|---|---|
| BAI2 | US-centric positional format; type codes (e.g. 3xx credits, 4xx-5xx debits by family) drive line classification; banks vary in how they populate reference/text fields |
| camt.053 (ISO 20022) | XML end-of-day statement; richer, structured references (EndToEndId, remittance info); confirm which camt.053 version your Fusion release and your bank both support |
| camt.052 / BAI2 intraday | Intraday positions; loaded separately from prior-day |
| MT940 / EDIFACT FINSTA | Legacy formats still common outside the US |
Load path: file → UCM (or H2H/connectivity) → **Load and Import Bank Statements** ESS job →
parse per format mapping → statement header/lines. Load failures: wrong format chosen, bank
dialect deviating from spec, duplicate statement (same account+date), or truncated file.

## Matching-rule design patterns
Order rules strict → loose within the rule set:
1. **Exact reference + exact amount** (1:1) — payment/receipt number in the statement reference.
   Highest confidence; put first.
2. **Exact amount + date window** (1:1, e.g. ±2 business days) — for banks that mangle references.
3. **Many-to-one / one-to-many** — batched receipts vs one deposit line; one payment settling as
   several lines. Constrain by date and total-amount tolerance.
4. **Tolerance rules** (amount within X or X%) — last, small tolerances only; every tolerance is
   reconciliation error you've pre-approved. Pair with an accounting policy for the difference.
Test a rule change against a month of history before trusting it: measure auto-match rate *and*
inspect a sample of new matches for false positives — the match rate going up is not by itself
good news.

## Transaction-code mapping
Map each bank transaction code (BAI type code / camt bank transaction code) to a transaction
type the rules can use (wire in/out, ACH, fee, interest, transfer). Unmapped codes leave lines
generic and unmatched. Review the map when: a new bank/account onboards, the bank migrates to
ISO 20022, or a new fee/product appears. Bank statement transaction creation rules can
auto-create external transactions (fees, interest) keyed on these codes — scope them tightly so
they never fabricate what a subledger will also book.

## Month-end tie-out checklist
1. All statements for the period loaded (no missing days) — check statement continuity.
2. Autoreconciliation run; unreconciled lines triaged (missing transaction / bad reference /
   split / true exception) with owners.
3. External transactions created for bank-only items (fees, interest) and accounted.
4. Reconciled-through date per account = period end.
5. **Bank statement closing balance = module reconciled position = GL cash account** (via
   cash/cash-clearing). Differences are unposted accounting, in-transit items, or unreconciled
   lines — name each dollar.
