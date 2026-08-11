# Sponsored-AR subject-area map (reference)

Public, documented Oracle Fusion OTBI concepts. Names drift slightly across releases — confirm
in your instance's subject-area list; the shape below is stable.

## Contents
- Subject areas by question
- The integration status flow
- Data-profile table format
- Glossary starter

## Subject areas by question
| Question | Subject area (side) | Typical columns |
|---|---|---|
| What invoices/credit memos exist for sponsor X? | Receivables - Transactions Real Time (AR) | Transaction number/date/type, customer (sponsor), amounts, status |
| What's due, overdue, aging? | Receivables - Payment Schedules Real Time (AR) | Due date, balance due, days overdue, dispute |
| AR-side revenue recognized | Receivables - Revenue Real Time (AR) | Revenue amounts, accounting periods |
| Draft/approved project invoices before AR | Projects - Invoices Real Time (PPM) | Invoice status, contract, project, amounts |
| Project revenue recognized | Projects - Revenue Real Time (PPM) | Revenue events/amounts by project/contract |
| Award/contract funding and remaining | Projects - Funding Real Time (PPM) | Funding amount, allocated, by award/contract |
| Unbilled/WIP and pipeline status | Project Billing - Bill Transactions Real Time (bridge) | Billing status (Ready to Bill / In Progress / Billed / Error), transaction amounts, project/contract |
| Billing exceptions/holds | Project billing exceptions patterns (bridge) | Exception type, transaction, reason |
One subject area per analysis (the standing OTBI rule); joins across the seam happen in your
analysis layer (exports joined on contract/project/invoice number), not inside one OTBI query.

## The integration status flow
```
PPM bill plan → Generate Invoice (PPM: Draft → Submitted → Approved/Released)
   → AutoInvoice interface → Receivables transaction created
   → Confirm Invoice Acceptance → PPM invoice status reflects AR acceptance
Unbilled AR = incurred cost / recognized revenue (PPM) not yet through this flow
Billed AR   = Receivables transaction exists; now ages via payment schedules
```
Failure modes to know: AutoInvoice validation errors park lines in the interface (billing
status Error); unaccepted invoices sit "in AR" but unconfirmed in PPM; credit/rebill cycles
create linked transactions that must be netted in any balance view.

## Data-profile table format
| Column (as received) | Mapped Fusion concept | Side (PPM/AR/bridge) | Nulls % | Notes |
|---|---|---|---|---|
Plus: row count, date range (min/max of each date column), as-of date, extraction filters
stated by the provider, currency/currencies present.

## Glossary starter
- **Award / contract:** the funded agreement (Grants: award; billing runs on the contract).
- **Bill plan:** the contract's billing method — cost-reimbursable or amount/event-based.
- **Unbilled AR (WIP):** PPM-side value not yet invoiced through AutoInvoice.
- **Billed AR:** invoiced, now living in Receivables payment schedules until paid.
- **Billing status:** bridge attribute — Ready to Bill, In Progress, Billed, Error.
- **Confirm Invoice Acceptance:** the step that syncs AR acceptance back to PPM.
- **LOC billing:** letter-of-credit awards — drawn against the LOC rather than invoiced
  conventionally; treat as its own segment.
