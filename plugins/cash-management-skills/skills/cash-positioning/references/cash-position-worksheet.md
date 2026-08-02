# Cash position worksheet (reference)

## Balance types (get these right first)
- **Ledger / booked balance** — all posted items, including funds not yet collected. Do **not**
  position against this when float or holds exist.
- **Available / collected balance** — ledger balance minus uncollected funds, holds, and float. This
  is the spendable number; position against it.
- **Opening balance** — the prior business day's **closing** balance from the final prior-day
  statement. It seeds today's worksheet.
- **Projected closing balance** — opening + today's inflows − today's outflows. The end-of-day number
  you steer toward the target.
- **Value date vs. posting date** — a flow belongs to the position on its **value date** (when funds
  are good), which can differ from when it posts.

## Worksheet layout (one per account/currency, then roll up)
| Line | Source | Actual/Proj |
|------|--------|-------------|
| Opening available balance | Prior-day statement | Actual |
| + Confirmed receipts today | Intraday statement, wires in | Actual |
| + Expected receipts today | Lockbox, card settlement, AR direct debits | Projected |
| − Scheduled disbursements | AP payment run, payroll, tax, debt service | Mixed |
| − Confirmed outflows today | Wires released, intraday debits | Actual |
| = Projected closing / available | Computed | Projected |
| Target / minimum balance | Policy | — |
| **Gap to target (sweep/fund)** | Closing − target | — |

## Statement / flow feeds
- **Prior-day statements** — BAI2, SWIFT MT940, ISO 20022 CAMT.053. Final, reconciled; source of the
  opening balance.
- **Intraday statements** — SWIFT MT942, BAI2 intraday. Show current-day activity as it posts; source
  of confirmed same-day flows.
- **Internal flows** — AP payments (from Payables), AR receipts (Receivables / lockbox), payroll runs,
  treasury deals (investments maturing, debt draws), tax and debt-service calendars.

## Multi-currency and multi-entity
- Hold a **position per currency**; manage each currency's liquidity on its own. A consolidated view
  requires an FX conversion at a stated rate and is for visibility, not for funding one currency from
  another.
- Hold a **position per legal entity/account**; cash moves between entities only via a real
  transaction (intercompany loan, dividend, POBO). See `cash-management-skills:intercompany-cash-netting`.

## Oracle Fusion Cash Management specifics
- The **Cash Positioning and Forecasting** work area builds **Cash Position Worksheets** backed by a
  multidimensional **Essbase cube**; dimensions include reporting period, currency, legal entity, and
  bank account.
- Cube sources: **bank statements** (prior-day and intraday), **external transactions**, **AP
  payments**, **AR receipts**, **payroll payments**, and **cash flows**.
- Positioning is **actuals-heavy and short-horizon**; Oracle keeps it distinct from **cash
  forecasting**, which extends the horizon with projected sources. Refresh the cube to reflect new
  statements and transactions before reading the position.
- Source: Oracle Help Center — *Cash Positioning and Forecasting* / *Overview of Cash Positioning*
  (https://docs.oracle.com/en/cloud/saas/financials/25b/faucm/).
