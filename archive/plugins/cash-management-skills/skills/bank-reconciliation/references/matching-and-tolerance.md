# Matching and tolerance (reference)

## Match types
- **One-to-one** — one statement line ↔ one book transaction. The default, cleanest match.
- **One-to-many** — one statement line ↔ several book transactions (e.g. a lump bank deposit
  that represents many individual receipts).
- **Many-to-one** — several statement lines ↔ one book transaction (e.g. a payment the bank
  split, or fees deducted from a gross settlement).
- **Many-to-many** — several ↔ several. Rare; usually a sign the data grain is wrong upstream.
- **Zero-amount** — matches offsetting items that net to zero.

## Match keys (match on all that apply, not amount alone)
1. **Amount** and **direction** (debit/credit).
2. **Date window** — statement date within N days of the book date (timing lag; typical 1–5 days).
3. **Reference** — check number, payment ID, remittance reference, or a parsed key from the line.
Amount-only matching produces false positives whenever two transactions share a value; always
combine amount with a date window and a reference where one exists.

## Tolerance rules
- A tolerance lets a match succeed when the two amounts differ slightly (bank charges netted from a
  wire, rounding, FX). Express it as a **percentage**, an **absolute amount**, or **both**.
- **Tolerance applies only to one-to-one matches.** Do not apply tolerances to many-sided matches —
  the difference could hide a genuinely missing item.
- When both a % and an amount tolerance are set, apply the **more conservative** one for the line.
- An in-tolerance difference must be **posted as an external/adjusting transaction** (e.g. the bank
  charge), not silently dropped — otherwise the book balance is quietly wrong.

## Oracle Fusion Cash Management specifics
- Automatic reconciliation uses **Reconciliation Matching Rules** grouped into **Automatic
  Reconciliation Rule Sets** assigned to a bank account; rules are prioritized/sequenced.
- Supported match types: one-to-one, one-to-many, many-to-one, many-to-many, zero-amount.
- **Tolerance rules attach to a matching rule and apply only to one-to-one rules**; an in-tolerance
  difference is auto-posted as an external transaction in Cash Management.
- Statement lines can match against Payables payments, Receivables receipts, Cash Management cash
  flows/ad-hoc payments, Payroll payments, journal entries, and external/open-interface transactions.
- Load options: *Load* / *Load and Import* / *Load, Import, and AutoReconciliation*.
- Source: Oracle Help Center — Reconciliation Matching Rules
  (https://docs.oracle.com/en/cloud/saas/financials/25b/faipp/reconciliation-matching-rules.html).
