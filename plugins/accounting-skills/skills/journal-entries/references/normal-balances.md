# Normal balances and worked entries (reference)

## Normal balance by account type
| Account type | Normal balance | Increases with | Decreases with |
|---|---|---|---|
| Asset | Debit | Debit | Credit |
| Liability | Credit | Credit | Debit |
| Equity | Credit | Credit | Debit |
| Revenue | Credit | Credit | Debit |
| Expense | Debit | Debit | Credit |

Rule of thumb: **debits raise assets and expenses; credits raise liabilities, equity, and revenue.** This falls
out of Assets = Liabilities + Equity + (Revenue − Expenses).

## Contra accounts (they sit against a parent and carry the opposite normal balance)
- **Accumulated depreciation** — contra-asset, credit-normal; nets down PP&E.
- **Allowance for doubtful accounts** — contra-asset, credit-normal; nets down accounts receivable.
- **Sales returns & allowances / contra-revenue** — debit-normal; nets down gross revenue.
- **Treasury stock** — contra-equity, debit-normal; nets down equity.

## Worked entries (illustrative amounts)

### Accrual — expense incurred, not yet invoiced
Accrue June cloud usage of 12,000 expected to be invoiced in July.
```
Dr  Cloud hosting expense        12,000
    Cr  Accrued liabilities            12,000
```
Reverse on July 1 (mirror image) so the vendor invoice posts normally without double-counting.

### Deferral — cash paid in advance (prepaid)
Pay 24,000 for a 12-month insurance policy on July 1.
```
Dr  Prepaid insurance (asset)    24,000
    Cr  Cash                            24,000
```
Then amortize 2,000/month: `Dr Insurance expense 2,000 / Cr Prepaid insurance 2,000`.

### Deferral — cash received in advance (deferred revenue)
Receive 36,000 for a 12-month subscription.
```
Dr  Cash                         36,000
    Cr  Deferred revenue (liability)    36,000
```
Recognize 3,000/month: `Dr Deferred revenue 3,000 / Cr Subscription revenue 3,000`.

### Reversing entry — clearing a prior accrual
On the first day of the next period, reverse last period's accrual:
```
Dr  Accrued liabilities          12,000
    Cr  Cloud hosting expense           12,000
```
When the real invoice arrives (`Dr Cloud hosting expense / Cr Accounts payable`), the reversal's credit offsets it.

### Reclass — moving a misclassified balance
Marketing spend of 5,000 was booked to office supplies.
```
Dr  Marketing expense             5,000
    Cr  Office supplies expense          5,000
```
Total debits and credits are unchanged; only the classification moves. Net income is unchanged here because both
lines are expenses; the effect is on department/account detail, not the bottom line.

### Adjusting entry — depreciation
Monthly straight-line depreciation of 1,500 on equipment.
```
Dr  Depreciation expense          1,500
    Cr  Accumulated depreciation        1,500
```
No cash moves — this is why adjusting entries typically do not touch a cash account.
