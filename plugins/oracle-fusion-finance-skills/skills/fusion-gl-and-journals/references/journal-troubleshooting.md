# Fusion GL journal troubleshooting (reference)

Common reasons a journal won't save, won't get approved, or won't post — and what to do.

## Contents
- Entry-time errors (won't save)
- Approval stage (saved but stuck)
- Posting errors (approved but unposted)
- Verifying the result

## Entry-time errors (won't save)
| Symptom / message | Cause | Fix |
|---|---|---|
| "Invalid account combination" | Combination never created and dynamic insertion is off, or a segment value is wrong | Check each segment against the value set; ask GL setup whether dynamic combination creation is enabled |
| Cross-validation rule violation (message cites a rule name) | The combination breaks a CVR (e.g. balance-sheet account + operational cost center) | Change the offending segment to a permitted value; if the business case is real, request a CVR review — don't work around it |
| "Value is not enabled/active" or end-dated value | Segment value disabled or past its end date | Use the replacement value; finance master data owns re-enabling |
| Period list doesn't show your period | Period is Closed or Never Opened for that ledger | Ask GL close owner to open it, or book into the current open period with the right accounting date |
| ADFdi upload marks rows failed | Same validation as UI, batched | Read the row-level status column; fix flagged rows and re-submit only those |

## Approval stage (saved but stuck)
- Status **Pending approval**: find it in the approver's BPM worklist; approval rules usually route
  by amount, category, or source. Don't re-enter the journal — you'll create a duplicate.
- Rejected: the journal returns to the preparer with the rejection comment; edit and resubmit.
- Approval bypassed unexpectedly: some sources/categories are excluded from approval by rule —
  that's configuration, not an error.

## Posting errors (approved but unposted)
| Symptom | Cause | Fix |
|---|---|---|
| "The period is not open" | Period closed between entry and posting | Reopen (with authorization) or change the period/accounting date |
| "Unbalanced journal" | Debits ≠ credits, or suspense posting disabled and lines don't balance by balancing segment | Correct amounts; check whether the ledger allows suspense posting (booking the difference to a suspense account) |
| Posts but creates extra lines | Intercompany balancing generated offset lines across balancing segment values | Expected behavior — verify the intercompany accounts used |
| AutoPost didn't pick it up | Journal's source/category outside the AutoPost criteria set | Post manually or ask for the AutoPost criteria to be reviewed |
| "Funds check failed" (budgetary control) | Budgetary control enabled and the entry exceeds budget | Needs a budget adjustment or override approval — a control, not a defect |

## Verifying the result
- Journal status shows **Posted** and a posting date.
- Account Inspector / trial balance reflects the movement in the right period and ledger.
- For multi-entity entries, confirm each balancing segment value nets to zero including the
  auto-generated intercompany lines.
