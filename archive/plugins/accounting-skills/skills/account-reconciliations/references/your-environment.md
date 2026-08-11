# Your account-reconciliation environment (sanitized template)

Fill in your real setup. If it names real accounts or balances, keep it in `your-environment.private.md` instead —
that suffix is git-ignored, so raw data never gets committed. Commit only sanitized, structural examples.

## Accounts you reconcile
| Account | Risk (H/M/L) | Frequency | Independent support source | Preparer | Reviewer |
|---|---|---|---|---|---|
| <Prepaid expenses> | <M> | <monthly> | <amortization schedule> | | |
| <Accrued liabilities> | <H> | <monthly> | <accrual detail / invoices> | | |
| <Fixed assets / accum. depr.> | <M> | <monthly> | <FA register> | | |
| <Intercompany> | <H> | <monthly> | <counterparty confirmation> | | |
| <Clearing / suspense> | <H> | <monthly> | <should clear to zero> | | |

## Reconciling-item policy
- **Aging thresholds / escalation:** <e.g. > 60 days escalates to controller; 90+ requires write-off approval>
- **Materiality for investigation:** <threshold below which small items are aggregated>
- **Write-off approval:** <who approves clearing an aged/unsupported item>

## Roll-forward vs point-in-time
- Roll-forward accounts: <fixed assets, prepaids, accruals, debt>
- Point-in-time accounts: <which>

## Controls & tooling
- **Preparer/reviewer rule:** <segregation; no self-review>
- **Reconciliation tool:** <e.g. BlackLine, FloQast, spreadsheet + shared drive>
- **Retention / audit trail:** <where recs, schedules, and support are stored>
