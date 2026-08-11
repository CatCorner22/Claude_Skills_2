# Cash Management report recipes (reference)

Companion to `otbi-cash-management-reports`. For each common report: its subject area, the key
columns, the leading filters, and suggested views. Column names are illustrative — confirm exact
names in your subject area's folders (they vary by release). Reconciliation status is an attribute
inside **Bank Statements RT**, not a separate area.

## Contents
- 1. Bank statement balances (daily/period)
- 2. Cash position snapshot (approximation)
- 3. Unreconciled lines / exceptions
- 4. Unreconciled aging
- 5. Reconciliation status summary
- 6. Bank charges by code/type/bank
- 7. Charge-tax breakdown
- 8. External cash transactions audit
- 9. Statement line detail / drill
- 10. Missing / late statement monitor
- 11. What to route off OTBI
- 12. Sources

## 1. Bank statement balances (daily/period)
- **Area:** Bank Statement Balances RT.
- **Columns:** Bank Account (name, number, currency, LE), Statement Date, opening/closing **booked**
  and **available** balances, balance code, credit/debit indicator.
- **Filters:** bank account, date range (prompted).
- **Views:** pivot (account x date), table.

## 2. Cash position snapshot (approximation)
- **Area:** Bank Statement Balances RT.
- **Columns:** Bank Account, Currency, Legal Entity, closing available balance, As-of Date.
- **Filters:** As-of Date, Bank Account, Currency, LE — all prompted (dashboard prompt).
- **Views:** pivot by bank/currency/LE, gauge for a total.
- **Caveat:** approximation off statement balances; the true dynamic multi-source position is the
  **Essbase Cash Position Worksheet**.

## 3. Unreconciled lines / exceptions
- **Area:** Bank Statements RT.
- **Columns:** Bank Account, Statement Date, statement line amount, reference, **Reconciliation
  Status** (line level).
- **Filters:** Reconciliation Status <> Reconciled; bank account; date.
- **Views:** table of exceptions, count by account.

## 4. Unreconciled aging
- **Area:** Bank Statements RT.
- **Columns:** as above plus a **CASE aging bucket** on days between statement date and As-of Date.
- **Filters:** unreconciled; bank account; date.
- **Views:** pivot (bucket x account), bar chart.
- Formula and band ordering: `otbi-analysis-filters` (references/prompts-and-formulas.md).

## 5. Reconciliation status summary
- **Area:** Bank Statements RT.
- **Columns:** Bank Account, **Reconciliation Status**, count/amount of lines.
- **Filters:** bank account; date.
- **Views:** pivot (status x account), pie/bar.

## 6. Bank charges by code/type/bank
- **Area:** Bank Statement Line Charges RT.
- **Columns:** Bank Account (name, branch, IBAN), **Charge Code, Charge Type, Charge Amount, Charge
  Rate**.
- **Filters:** bank account; date; charge type.
- **Views:** pivot (charge type x bank), bar chart of amount.

## 7. Charge-tax breakdown
- **Area:** Bank Statement Line Charges RT.
- **Columns:** Charge Code/Type, Charge Amount, **Tax ID, Tax Rate**, computed tax amount.
- **Filters:** bank account; date.
- **Views:** table, pivot by tax rate.

## 8. External cash transactions audit
- **Area:** External Cash Transactions RT.
- **Columns:** Bank Account, **External Cash Transaction Date**, amount, reference, type (fee,
  interest, manual).
- **Filters:** external-transaction date; bank account; type.
- **Views:** table, count by type.

## 9. Statement line detail / drill
- **Area:** Bank Statements RT.
- **Columns:** full line attributes — account, statement sequence, statement date, amount, reference,
  reconciliation status.
- **Filters:** bank account; statement/date (prompted).
- **Views:** detail table; use as a drill target from a summary.

## 10. Missing / late statement monitor
- **Area:** Bank Statement Balances RT.
- **Columns:** Bank Account, latest Statement Date, gap to expected date.
- **Filters:** date range; bank account.
- **Views:** table sorted by staleness; conditional formatting on overdue.

## 11. What to route off OTBI
- **Outstanding checks / deposits in transit** — need cleared AP-payment / AR-receipt
  transaction-level joins; not doable in one Cash Management area. Use Payables/Receivables subject
  areas, a **BI Publisher SQL data model**, or Oracle's predefined Cash Management reports.
- **True dynamic cash position** — the **Essbase Cash Position Worksheet**.
- **Scheduled / burst / pixel-perfect delivery** — **BI Publisher** (see
  `otbi-report-scheduling-sharing`).

## 12. Sources
- Cash Management subject areas, folders, and attributes —
  https://docs.oracle.com/en/cloud/saas/financials/25c/fappp/cash-management-subject-areas-folders-and-attributes.html
- Create your first analysis —
  https://docs.oracle.com/en/cloud/saas/otbi/otbi-user/create-your-first-analysis.html
