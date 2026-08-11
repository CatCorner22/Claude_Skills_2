# Evals — oracle-fusion-finance-skills:fusion-ap-invoice-to-pay

## 1. Positive trigger (should load the skill)
> "A supplier invoice in Fusion has a Qty Received hold and didn't get picked up in this week's
> payment process request. How do I get it paid?"

Expected: skill loads; explains the system hold releases by fixing the mismatch (receive the
goods or correct the invoice), not by manual release; then traces the payment path backwards
from selection (validated? approved? due? right pay group?) rather than starting at the payment
file.

## 2. Near-miss (should NOT load this skill)
> "Should we pay this urgent supplier invoice by wire or same-day ACH, and what are the
> cutoffs?"

Expected: rail selection — `banking-skills:payment-rails` should handle it. If this skill
loads, tighten the description toward Fusion AP mechanics.

## 3. Quality rubric
A good response:
- **Does the task:** releases the hold via its cause, confirms validate/approve/account, and
  gets the invoice selected into a PPR with the proposal reviewed before confirmation.
- **Teaches:** the entered → validated → approved → accounted → paid chain and its fail-closed
  controls; matching as promise (PO) vs proof (receipt) vs claim (invoice); PPR's split between
  selection criteria and payment process profile.
- **Safe:** never suggests force-releasing matching holds, keying distributions instead of
  matching, editing a confirmed payment (void/reissue instead), or confirming a PPR unreviewed.
