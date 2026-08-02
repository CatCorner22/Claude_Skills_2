# Debit/credit rules, T-accounts, and the accounting cycle (reference)

## Contents
- The accounting equation, extended
- Normal balance by account type
- Contra accounts
- Worked example: posting to T-accounts
- Trial balance
- The accounting cycle

## The accounting equation, extended
Base identity (always true):

```
Assets = Liabilities + Equity
```

Revenue, expenses, and owner draws/dividends are movements inside equity, so during a period the working form is:

```
Assets = Liabilities + Equity + (Revenue − Expenses − Draws/Dividends)
```

Revenue increases equity; expenses and draws/dividends decrease it. At period end, revenues and expenses close
into equity (retained earnings), collapsing the working form back to A = L + E.

## Normal balance by account type
| Account type | Normal balance | Increases with | Decreases with |
|---|---|---|---|
| Asset | Debit | Debit | Credit |
| Liability | Credit | Credit | Debit |
| Equity | Credit | Credit | Debit |
| Revenue | Credit | Credit | Debit |
| Expense | Debit | Debit | Credit |
| Draws / Dividends (contra-equity) | Debit | Debit | Credit |

Rule of thumb: **debits raise the left side of the equation (assets, expenses); credits raise the right side
(liabilities, equity, revenue).**

## Contra accounts
A contra account sits against a parent and carries the **opposite** normal balance, netting the parent down:
- **Accumulated depreciation** — contra-asset, credit-normal; nets down PP&E.
- **Allowance for doubtful accounts** — contra-asset, credit-normal; nets down accounts receivable.
- **Sales returns & allowances (contra-revenue)** — debit-normal; nets down gross revenue.
- **Treasury stock** — contra-equity, debit-normal; nets down equity.

## Worked example: posting to T-accounts
Three transactions for a new business (illustrative amounts):
1. Owner invests 50,000 cash. `Dr Cash 50,000 / Cr Owner's equity 50,000`
2. Buy equipment for 20,000 cash. `Dr Equipment 20,000 / Cr Cash 20,000`
3. Provide services for 8,000 on account. `Dr Accounts receivable 8,000 / Cr Service revenue 8,000`

Posted to T-accounts (debits left, credits right):

```
        Cash                     Equipment              Accounts receivable
  Dr        |   Cr          Dr        |   Cr          Dr        |   Cr
 50,000     | 20,000       20,000     |               8,000     |
 ---------- | --------     --------   |               ------    |
 Bal 30,000 |              Bal 20,000 |               Bal 8,000 |

     Owner's equity             Service revenue
  Dr    |   Cr              Dr    |   Cr
        | 50,000                  | 8,000
        | ---------               | ------
        | Bal 50,000              | Bal 8,000
```

Check the equation: Assets (30,000 + 20,000 + 8,000 = 58,000) = Liabilities (0) + Equity (50,000 + 8,000 revenue = 58,000). Balanced.

## Trial balance
List each account's ending balance under Debit or Credit and total the columns — they must be equal.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 30,000 | |
| Accounts receivable | 8,000 | |
| Equipment | 20,000 | |
| Owner's equity | | 50,000 |
| Service revenue | | 8,000 |
| **Totals** | **58,000** | **58,000** |

Equal totals confirm the arithmetic. They do **not** prove correctness: an omitted entry, a posting to the wrong
account, or two offsetting errors all leave the trial balance in balance.

## The accounting cycle
The repeating sequence each period:

1. **Analyze** the transaction (which accounts, which direction).
2. **Journalize** — record the debit/credit entry in the journal.
3. **Post** the entry to the ledger (T-accounts).
4. **Unadjusted trial balance** — prove debits = credits.
5. **Adjusting entries** — accruals, deferrals, depreciation, estimates (see `accounting-skills:journal-entries`).
6. **Adjusted trial balance**.
7. **Financial statements** — income statement, balance sheet, cash flow (see `accounting-skills:financial-statements`).
8. **Closing entries** — zero out revenue, expense, and draw/dividend accounts into retained earnings.
9. **Post-closing trial balance** — only permanent (balance-sheet) accounts remain.
