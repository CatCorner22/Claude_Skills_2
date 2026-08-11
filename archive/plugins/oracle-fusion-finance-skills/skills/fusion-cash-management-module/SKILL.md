---
name: fusion-cash-management-module
description: >-
  Operates the Oracle Fusion Cash Management module — bank, branch, and account setup; loading
  and troubleshooting electronic bank statements (BAI2, camt.053); tuning automatic
  reconciliation matching rules and rule sets; handling external cash transactions; and reading
  the module's reconciliation statuses. Use when setting up bank accounts in Fusion, loading
  bank statements, configuring or debugging auto-reconciliation, or clearing unreconciled
  statement lines in the Fusion CE module. Triggers: fusion cash management, bank statement
  load, camt.053 fusion, BAI2 import, auto reconciliation fusion, matching rules, reconcile in
  fusion, external cash transaction, bank account setup fusion, unreconciled statement lines.
---

# Fusion Cash Management module

## When to use
- Setting up banks, branches, and bank accounts in Oracle Fusion Cash Management, or wiring a new
  account into statement loading and reconciliation.
- Loading electronic bank statements and fixing loads that fail or leave lines unmatched;
  tuning automatic reconciliation rules; creating external cash transactions.
- Not for: the reconciliation *method* itself (matching discipline, classifying breaks) → see
  `cash-management-skills:bank-reconciliation`. For OTBI reporting on this data → see
  `oracle-otbi-skills:otbi-cash-management-reports`. For raw statement formats → see
  `banking-skills:bank-statement-parsing`.

## Do it
1. **Set up the hierarchy in order: bank → branch → account.** The bank and branch are shared
   reference data; the **bank account** carries the working config — currency, legal entity that
   owns it, GL cash (and cash-clearing) account combination, IBAN/account number, and which
   modules may use it (Payables, Receivables, Payroll, Cash Management). An account invisible to
   a module is almost always missing that module's use flag or the user's data-security access.
2. **Wire statement loading.** Electronic statements arrive as **BAI2, camt.053 (ISO 20022), EDIFACT
   FINSTA, or SWIFT MT940**; the load runs through the **Load and Import Bank Statements** process
   (file via UCM, or straight from bank connectivity/H2H). The parsing contract is the format +
   the bank's dialect of it — when a load fails, compare the file against the bank's spec before
   suspecting Fusion. Intraday (camt.052/BAI2 intraday) and prior-day statements load separately.
3. **Know what a statement line must match against.** Reconciliation in the module means pairing
   **statement lines** with **system transactions**: AP payments, AR receipts (via remittance
   batches), payroll payments, and **external cash transactions** (fees, interest, transfers that
   no subledger created — enter them manually, via REST, or let **bank statement transaction
   creation rules** generate them from statement lines).
4. **Tune automatic reconciliation as rules in a rule set.** Each matching rule pairs
   one-to-one/one-to-many/many-to-one lines and transactions on criteria (amount exact or within
   tolerance, date window, reference/transaction number, transaction codes). Rules run in
   sequence — put the strictest (exact reference + amount) first, looser amount+date rules later,
   and set tolerances deliberately. The **transaction-code mapping** (BAI/camt codes → transaction
   types) is what lets rules discriminate wires from fees; keep it current when the bank adds codes.
5. **Run and read reconciliation.** Autoreconciliation runs after statement load (or scheduled).
   Lines end **reconciled** or stay **unreconciled**; review the unmatched by reason: missing
   system transaction (create the external transaction or chase the subledger), reference mangled
   by the bank (loosen/repair the rule or match manually), amount split across transactions
   (needs a many-to-one rule), or true exceptions for investigation.
6. **Reconcile manually what rules shouldn't touch.** One-off oddities get manual matching in the
   Reconcile Bank Statements work area; don't write a permanent rule for a one-time event.
7. **Verify the cash accounting.** Reconciliation can drive accounting (cash vs cash-clearing
   movements via SLA). Month-end, the bank statement balance, the module's reconciled position,
   and the GL cash account tie out — `references/statement-recon-setup.md` holds the checklist
   and rule-design patterns.

## Why / learn
The module is a *matching machine between two independent records of the same cash*: the bank's
statement and your subledgers. Everything in the setup exists to make that pairing decidable —
the account config declares who owns which record, transaction-code mappings translate the
bank's language, external transactions fill the gaps subledgers don't cover, and matching rules
encode how much fuzziness you'll tolerate before a human looks. Rule ordering matters because
every match a strict rule makes is one a loose rule can't get wrong; running loose rules first
is how false matches (the worst outcome — a wrong reconciliation looks *done*) sneak in. And the
reason unreconciled lines deserve triage rather than brute-force matching is that each unmatched
line is evidence: of a missing accounting entry, a bank data-quality issue, or fraud. The module
surfaces the evidence; the reconciliation method (see `cash-management-skills:bank-reconciliation`)
tells you what it means.

## Common mistakes
- Loose amount-only rules early in the rule set → false matches that hide real breaks; strictest rules first.
- Missing transaction-code mapping for a new bank code → those lines never auto-match; maintain the map.
- Creating external transactions for items AP/AR should own → duplicates when the subledger entry arrives; check the source first.
- Blaming Fusion for a load failure without reading the file → compare against the bank's format spec (dialects differ).
- Account not visible to Payables/Payroll → the account-use flags or data access, not a bug.
- Writing a permanent rule for a one-off event → rule sprawl; match it manually.
- Skipping the GL tie-out → module says reconciled, GL cash disagrees; close isn't done until they tie.

## Tailor to your environment
Record your cash setup in `references/your-environment.md` (real account numbers/IBANs only in
`your-environment.private.md`, git-ignored): banks and accounts (sanitized), statement formats
per bank, transaction-code maps, your rule set order and tolerances, and external-transaction
conventions. **Never commit real account numbers, IBANs, or statement files.**

## References
- references/statement-recon-setup.md — format notes, rule-design patterns, month-end tie-out checklist
- references/your-environment.md — your banks, formats, code maps, rule sets (fill in)
