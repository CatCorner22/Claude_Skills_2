# Cash Management OTBI subject areas (reference)

The four stable Cash Management subject areas, their key columns, and the reports each supports.
Companion to `otbi-subject-area-selection`. There is **no standalone reconciliation subject area** —
reconciliation status is an attribute inside Bank Statements Real Time (header and line level).
Confirm exact column names in your release; some flexfield/DFF columns may not be exposed.

## Contents
- 1. Bank Statements Real Time
- 2. Bank Statement Balances Real Time
- 3. Bank Statement Line Charges Real Time
- 4. External Cash Transactions Real Time
- 5. Common dimensions
- 6. Single-area limit and workarounds
- 7. Security and performance
- 8. Sources

## 1. Cash Management - Bank Statements Real Time
- **Grain:** bank statement lines (with header context).
- **Holds:** statement lines, bank account, and **reconciliation status at header and line level**.
- **Use for:** unreconciled lines, reconciliation exceptions, unreconciled **aging** (via a CASE
  column formula), reconciliation **status summary**, and statement-line detail / drill.
- The **primary area** for anything reconciliation- or statement-line-oriented.

## 2. Cash Management - Bank Statement Balances Real Time
- **Grain:** balances by bank account and date.
- **Holds:** opening/closing **booked and available** balances, balance code, credit/debit indicator.
- **Use for:** daily/period bank statement balances by account, **cash-position-style** snapshots by
  bank/currency/LE (prompt-driven), and **missing/late statement** monitoring.
- Note: a true dynamic multi-source cash position is the **Essbase Cash Position Worksheet**; OTBI
  only *approximates* position off statement balances.

## 3. Cash Management - Bank Statement Line Charges Real Time
- **Grain:** bank charges on statement lines.
- **Holds:** **Charge Code, Charge Type, Charge Amount, Charge Rate, Tax ID, Tax Rate**, plus bank
  account (IBAN, branch) and reconciliation status.
- **Use for:** bank **charges by code/type/bank** and **charge-tax breakdowns** (bank-fee analysis).

## 4. Cash Management - External Cash Transactions Real Time
- **Grain:** external cash transactions.
- **Holds:** external cash transactions created from statement upload, reconciliation tolerance
  differences, or manual entry (fees, interest); time linked to **External Cash Transaction Date**.
- **Use for:** external cash transaction **audits** and analysis of tolerance/manual items.

## 5. Common dimensions
- **Bank Account:** bank name, branch, IBAN, account number, currency, legal entity.
- **Bank Statement:** sequence, statement date, reconciliation status.
- **Cash / External Transaction:** date, amount, reference.
- Pick the **date column that matches the question** — statement date vs. external-transaction date.

## 6. Single-area limit and workarounds
- One analysis queries one subject area; no native cross-subject-area joins.
- Reports needing cleared **AP-payment / AR-receipt transaction-level joins** (outstanding checks,
  deposits in transit) are **not** doable in one Cash Management area. Options:
  - **Payables / Receivables subject areas** for the sub-ledger side.
  - **BI Publisher SQL data model** to join across tables/pillars in one report.
  - **Side-by-side analyses on a dashboard** sharing a prompt (queried separately, shown together).
  - **Fusion Data Intelligence (FDI) / OAC** for cross-pillar and historical reporting.
  - Oracle's **predefined Cash Management reports** for standard outputs.

## 7. Security and performance
- To even see these areas a user needs the **Cash Management Transaction Analysis Duty** (typically
  via the **Cash Manager** job role); data security still limits rows by bank account / BU / LE.
- Real-time queries hit the live DB — filter on bank account + date early, avoid pulling every
  column, and expect degradation during period close.
- Confirm the **CAMT.053 version** supported for the customer's release rather than hard-coding one.
- Some flexfield/DFF columns may not be exposed — check the folders before promising a column.

## 8. Sources
- Cash Management subject areas, folders, and attributes —
  https://docs.oracle.com/en/cloud/saas/financials/25c/fappp/cash-management-subject-areas-folders-and-attributes.html
- Create your first analysis —
  https://docs.oracle.com/en/cloud/saas/otbi/otbi-user/create-your-first-analysis.html
