# Oracle Cloud Fusion Financials data model (AP · AR · CoA/GL · XLA)

Preserved near-verbatim from the source spec (Chicken Little v2026.2). Scope: current releases
in the 25x/26x range, schema FUSION. Rare statuses and newer features are version-specific —
verify against the instance or the current "Tables and Views for Financials" documentation
before relying on them.

Contents: §1 Architecture & nomenclature · §2 CoA & GL · §3 Payables · §4 Receivables ·
§5 Subledger Accounting (XLA) · §6 Behavioral guidelines

## §1 General architecture & nomenclature

- Transactions originate in subledgers (AP, AR, FA, Cash Management, Expenses…). **Subledger
  Accounting (XLA/SLA)** creates accounting events and journal entries (`XLA_EVENTS`,
  `XLA_AE_HEADERS`, `XLA_AE_LINES`, `XLA_TRANSACTION_ENTITIES`, `XLA_DISTRIBUTION_LINKS`), which
  transfer to General Ledger (`GL_JE_BATCHES`, `GL_JE_HEADERS`, `GL_JE_LINES`, `GL_BALANCES`).
- Drill-down linkage often uses `GL_IMPORT_REFERENCES` (via `GL_SL_LINK_ID` / `GL_SL_LINK_TABLE`).
- Shared foundation: Ledgers, Chart of Accounts, Legal Entities, Business Units, the TCA party
  model (`HZ_*` tables).
- Naming conventions:
  - Module prefixes: `GL_`, `AP_`, `AR_`/`RA_`, `XLA_`, `HZ_`, `CE_`, `FUN_`, `FND_`, `POZ_`.
  - `_ALL` tables hold multi-organization data — always filter by `ORG_ID`/business unit and/or
    ledger.
  - `_B` / `_TL` / `_VL`: base, translation, language-filtered view.
  - Common shape: Header → Lines (1:M) → Distributions.
- Critical shared identifiers: `LEDGER_ID`, `CODE_COMBINATION_ID` (CCID), `PARTY_ID`,
  `CUST_ACCOUNT_ID`, `VENDOR_ID`, `ORG_ID`, `INVOICE_ID`, `CUSTOMER_TRX_ID`, `JE_HEADER_ID`,
  `AE_HEADER_ID`, and `APPLICATION_ID` (**200 = Payables, 222 = Receivables, 101 = General
  Ledger**) — application IDs are essential for scoping XLA data.

## §2 Chart of Accounts (CoA) & General Ledger (GL)

- **CoA structure**: Value Sets → CoA Structure (segments + segment labels) → Structure
  Instance. Required labels typically include Primary Balancing Segment (often Company), Natural
  Account, and frequently Cost Center / Intercompany.
- **Key tables**:
  - `GL_CODE_COMBINATIONS` — account combinations. PK `CODE_COMBINATION_ID`. Notable:
    `SEGMENT1`…`SEGMENTn`, `CHART_OF_ACCOUNTS_ID`, `ENABLED_FLAG`, `SUMMARY_FLAG`,
    `CONCATENATED_SEGMENTS`, `ACCOUNT_TYPE`.
  - `GL_LEDGERS` — ledger definitions (Primary, Secondary, Reporting): currency, calendar, CoA.
  - `GL_JE_BATCHES` — journal batches; status commonly `U` (Unposted), `P` (Posted), plus
    process/error states.
  - `GL_JE_HEADERS` — journal headers (PK `JE_HEADER_ID`): `JE_BATCH_ID`, `LEDGER_ID`, `NAME`,
    `PERIOD_NAME`, `STATUS`, `JE_SOURCE`, `JE_CATEGORY`, `ACTUAL_FLAG`, `CURRENCY_CODE`.
    **STATUS**: `U` = Unposted, `P` = Posted; error/validation statuses include numeric and
    letter codes (e.g. 1 = invalid currency, A = code combination does not exist, L = unbalanced
    journal, C = detail posting not allowed, F = code combination not enabled) — verify exact
    codes in your release.
  - `GL_JE_LINES` — lines by `JE_HEADER_ID` + `JE_LINE_NUM`: `CODE_COMBINATION_ID`,
    entered/accounted amounts, debits/credits.
  - `GL_BALANCES` — period balances by CCID, ledger, currency, actual/budget/encumbrance flags.
    Prefer this for balance/trial-balance queries over aggregating lines.
  - Supporting: `GL_PERIODS`, `GL_PERIOD_STATUSES`, `GL_JE_SOURCES_B`, `GL_JE_CATEGORIES_B`.
- Always respect period open/close status and multi-ledger / multi-currency implications.

## §3 Payables (AP)

- **Core tables**:
  - `AP_INVOICES_ALL` (PK `INVOICE_ID`) — invoice headers: `INVOICE_NUM`, `VENDOR_ID`,
    `INVOICE_AMOUNT`, `INVOICE_TYPE_LOOKUP_CODE` (STANDARD, CREDIT, PREPAYMENT, DEBIT…),
    `ORG_ID`, `GL_DATE`, `INVOICE_DATE`. Status/flag columns:
    - `PAYMENT_STATUS_FLAG`: `Y` fully paid · `N` unpaid · `P` partially paid.
    - `WFAPPROVAL_STATUS` (approval workflow), `APPROVAL_STATUS`, `APPROVAL_READY_FLAG`,
      `APPROVAL_ITERATION`.
    - Cancellation via `CANCELLED_DATE` and related flags.
  - `AP_INVOICE_LINES_ALL` — lines: `LINE_NUMBER`, `LINE_TYPE_LOOKUP_CODE`, amounts, PO refs.
  - `AP_INVOICE_DISTRIBUTIONS_ALL` — accounting distributions; **the reliable place to read
    validation**: `MATCH_STATUS_FLAG` commonly `A` = validated/approved, `N`/NULL = never
    validated, `T` = needs revalidation, `S` = stopped. Plus `DIST_CODE_COMBINATION_ID`,
    amounts, accounting date.
  - `AP_PAYMENT_SCHEDULES_ALL` — scheduled payments: due dates, `AMOUNT_REMAINING`,
    `PAYMENT_STATUS_FLAG` (Y/N/P), hold flags.
  - `AP_INVOICE_PAYMENTS_ALL` — invoice↔payment links; `AP_CHECKS_ALL` — payment instruments.
  - `AP_HOLDS_ALL` — holds; an unreleased hold has `RELEASE_LOOKUP_CODE IS NULL`.
- **Suppliers**: modern tables are `POZ_SUPPLIERS` (linked to `HZ_PARTIES`) and site tables;
  legacy `AP_SUPPLIERS` references still appear in some contexts.
- **Interfaces**: `AP_INVOICES_INTERFACE`, `AP_INVOICE_LINES_INTERFACE` (open interface import).
- **Typical flow**: Entry → Validation (distribution match status) → Approval workflow →
  Accounting via XLA (`APPLICATION_ID` = 200) → Payment → Transfer/post to GL.
- An invoice cannot be paid until distributions validate and approval completes — read
  validation at distribution level, not from the header alone.

## §4 Receivables (AR)

- **Core tables**:
  - `RA_CUSTOMER_TRX_ALL` (PK `CUSTOMER_TRX_ID`) — transaction headers (invoices, credit/debit
    memos, bills receivable): `TRX_NUMBER`, `TRX_DATE`, bill-to references, `CUST_TRX_TYPE_ID`,
    `COMPLETE_FLAG`, `STATUS_TRX`, `DOCUMENT_STATUS_CODE`.
  - `RA_CUSTOMER_TRX_LINES_ALL` — lines; `LINE_TYPE` typically LINE, TAX, FREIGHT, CHARGES.
  - `AR_PAYMENT_SCHEDULES_ALL` — open items. **STATUS**: `OP` open · `CL` closed. `CLASS`: INV,
    DM, CM, CB, PMT…; `AMOUNT_DUE_REMAINING`, `AMOUNT_DUE_ORIGINAL`, due dates. Open vs closed
    is best read here (status + remaining amount).
  - `AR_CASH_RECEIPTS_ALL` (PK `CASH_RECEIPT_ID`) — receipts. **STATUS**: `APP` applied ·
    `UNAPP` unapplied · `UNID` unidentified · `REV` reversed · `NSF` non-sufficient funds ·
    `STOP` stop payment.
  - `AR_RECEIVABLE_APPLICATIONS_ALL` — applications of receipts/credit memos (status codes
    include APP, UNAPP, ACC, UNID…).
  - `AR_CASH_RECEIPT_HISTORY_ALL` — receipt lifecycle: APPROVED, CONFIRMED, REMITTED, CLEARED,
    REVERSED.
  - `AR_ADJUSTMENTS_ALL` — adjustments.
- **Customers (TCA)**: `HZ_PARTIES`, `HZ_CUST_ACCOUNTS`, `HZ_CUST_ACCT_SITES_ALL`,
  `HZ_CUST_SITE_USES_ALL`, plus site/contact tables.
- **Typical flow**: Transaction creation → AutoAccounting/distributions → Completion → Receipt
  application → Accounting via XLA (`APPLICATION_ID` = 222) → GL.

## §5 Subledger Accounting (XLA) & cross-module patterns

- `XLA_AE_HEADERS` — subledger journal headers: `ACCOUNTING_ENTRY_STATUS_CODE` (Draft, Final,
  Incomplete, Invalid…) and `GL_TRANSFER_STATUS_CODE` (Not transferred, Selected, Transferred).
- `XLA_AE_LINES` — accounting lines: `CODE_COMBINATION_ID`, accounted amounts/currency.
- Linkage: subledger document → XLA transaction entity/event → AE header/lines → (optionally)
  GL import references → GL journals/balances.
- Always scope XLA queries by `APPLICATION_ID`.
- Common integrity checks: balanced accounted DR/CR within headers; period status; open vs
  closed items; validation flags before payment or transfer. Failures here are where **Orphan
  Distributions** live.

## §6 Behavioral guidelines for Oracle responses

- Prefer exact table and column names; when discussing statuses, list the common coded values
  *and* their business meaning.
- Provide join paths and filters (`ORG_ID`, `LEDGER_ID`, period, status flags) for both
  performance and multi-org correctness.
- Give process context with data answers (e.g. "not payable until distributions validate and
  approval completes").
- Integrate LSS: quantify waste around status transitions (cycle time per state, defect rates);
  watch for Invoice Black Holes and Ghost Receipts; analyze extracts with Polars/DuckDB +
  statistics.
- Integrate PM: implementations, migrations, and remediations get phases, risks, RACI, and
  success criteria.
- **SaaS access reality**: direct SQL to base tables is frequently restricted in pure SaaS
  Fusion. Prefer OTBI subject areas (Payables Invoices – Transactions Real Time, Receivables –
  Transactions Real Time, General Ledger – Journals / Account Balance Real Time…), BI Publisher,
  REST APIs, FBDI, or extracts / Autonomous Data Platform — while keeping base-table knowledge
  for understanding, troubleshooting, custom extensions, and reconciliation logic
  (→ `oracle-otbi-skills:otbi-report-building`).
- If a rare status, newer feature, or instance-specific configuration is involved: state the
  assumption, recommend verification in the current environment or official docs.
