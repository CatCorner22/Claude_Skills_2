# Evals — oracle-fusion-finance-skills:fusion-auto-reconciliation-design

## 1. Positive trigger (should load the skill)
> "Our card settlements land as one big ACH deposit net of processor fees and nothing
> auto-matches — should I just add a transaction creation rule and a wide amount tolerance
> to make them reconcile?"

Expected: skill loads; gently corrects the root cause (TCR + wide tolerance would compare
the statement with itself and invite false positives); designs the right pattern — match
the deposit to the AR remittance batch (or grouped receipts by settlement date + merchant
ID parsed from the 88-record/addenda), handle the processor fee as a bank-originated item;
asks for the raw BAI2 line and current rule config before finalizing; recommends measuring
match rate before/after in OTBI.

## 2. Near-miss (should NOT load this skill)
> "Auto-reconciliation matched fine in UAT but production dropped to 40% after go-live —
> what changed?"

Expected: a test-passes-prod-fails incident →
`oracle-fusion-finance-skills:fusion-cm-production-troubleshooting` (environment-parity
protocol). This skill designs and optimizes the engine; that one diagnoses production
divergence. If this loads alone, tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** applies the four principles by name where they bite; engineers
  matching from what the bank actually sends (parsing before tolerances); sequences rules
  by precision; scopes any TCR to bank-originated items; includes an OTBI measurement plan.
- **Teaches:** explains subledger supremacy (why a TCR patch destroys the control's
  independence) and the tolerance/false-positive trade.
- **Safe:** asks for the raw statement line and rule config instead of guessing; exact
  Oracle terminology and navigation paths; release-dependent field names flagged
  confirm-in-your-release.
