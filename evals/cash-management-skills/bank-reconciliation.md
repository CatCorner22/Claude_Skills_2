# Evals — cash-management-skills:bank-reconciliation

## 1. Positive trigger (should load the skill)
> "My bank statement shows $482,100 but the GL cash account says $479,650. Help me reconcile it
> and find what's making up the difference."

Expected: skill loads; frames bank vs. book; asks for/organizes both sides; classifies the
$2,450 difference into timing vs. bank-only vs. true differences; builds to zero.

## 2. Near-miss (should NOT load this skill)
> "Reconcile my prepaid insurance schedule to the GL balance for June."

Expected: this is a GL balance-sheet account reconciliation, not a bank rec. The
`accounting-skills:account-reconciliations` skill should handle it instead. If this skill loads,
tighten the description / cross-links.

## 3. Quality rubric
A good response:
- **Does the task:** separates the two balances, matches on amount + date + reference, classifies
  unmatched items into the three buckets, produces adjusted-bank = adjusted-book (to zero), and
  ages open items.
- **Teaches:** explains *why* timing and true differences are kept separate and why plugging a
  residual defeats the control — not just the mechanics.
- **Safe:** never plugs a residual to force zero; leaves bank errors as reconciling items rather
  than booking them.
