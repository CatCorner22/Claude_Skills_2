# WIP reconciliation worksheet (reference)

## Contents
- Pipeline cut format
- PPM-to-AR reconciliation worksheet
- Variance decomposition
- Exception queue format

## Pipeline cut format
As-of date prominent; amounts in reporting currency (state rate basis if converted).
| Segment | Ready to Bill | In Progress | Error | Total unbilled | Billed (open AR) |
|---|---|---|---|---|---|
| By sponsor / project / contract / award type | | | | | |
Add an age dimension to each unbilled bucket (0–30 / 31–60 / 61–90 / 90+ days since
transaction date): an aged Ready-to-Bill bucket is a process finding even when the total looks
healthy.

## PPM-to-AR reconciliation worksheet (per contract)
| Line | Source | Amount |
|---|---|---|
| PPM recognized revenue (inception-to-date or period) | Projects - Revenue Real Time | ... |
| − AR invoiced (accepted transactions, net of credits) | Receivables - Transactions Real Time | ... |
| **= Expected unbilled** | | ... |
| Measured pipeline (Ready + In Progress + Error) | Project Billing - Bill Transactions Real Time | ... |
| **= Residual variance** | expected − measured | ... |
Run cost-reimbursable contracts on cost too (incurred billable cost − invoiced): revenue- and
cost-based views can differ by indirect/fee mechanics — say which basis the deliverable uses.

## Variance decomposition
Work the residual in this order:
1. **Timing:** invoices generated but not yet accepted (in AutoInvoice or awaiting Confirm
   Invoice Acceptance) — legitimate, list them with age.
2. **Credits/rebills not netted:** linked credit memos and re-issued invoices double-counted
   on one side — net by linked transaction.
3. **Exceptions:** Error-status transactions and billing holds — belongs to the exception queue.
4. **Scope mismatch:** the two extracts filtered differently (date basis, BU, contract range)
   — fix the extracts, not the numbers.
5. **True data issues:** whatever survives 1–4; smallest bucket if the pipeline is healthy,
   and the one worth escalating.

## Exception queue format
| Reason | Count | Amount | Oldest (days) | Fix owner | Standard fix |
|---|---|---|---|---|---|
| AutoInvoice validation (customer/site/setup) | | | | AR / customer master | Complete setup, re-run |
| Funding exhausted / contract hard limit | | | | Grants accountant / PI | Funding amendment or cost transfer |
| Contract or billing hold | | | | Contract admin | Resolve hold reason, release |
| Missing burden/rate schedule | | | | Costing | Correct rates, reprocess |
Track queue total and oldest-item age over time — the queue's *trend* is the health metric.
