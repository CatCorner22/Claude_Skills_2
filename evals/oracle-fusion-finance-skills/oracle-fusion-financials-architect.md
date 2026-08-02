# Evals — oracle-fusion-finance-skills:oracle-fusion-financials-architect

## 1. Positive trigger (should load the skill)
> "Design the reconciliation configuration for our two new bank accounts in Fusion Cash
> Management — matching rules, accounting rules, and how we deploy it to PROD safely.
> Treat the setup as code; I want validation checks and a rollback plan."

Expected: skill loads; adopts the Thales persona; clarifies ledger/BU/LE/COA scope first;
delivers the setup-object YAML, data flow, executable validation rules, a phased
migration playbook with rollback, test scenarios (incl. partial clearance and
void/reissue), and ADRs — deterministic matching with bounded tolerances only.

## 2. Near-miss (should NOT load this skill)
> "Quick question — what's the exact FSM task name to create a bank branch, and where is
> it in the Redwood UI?"

Expected: a configuration-specific Q&A → `oracle-fusion-finance-skills:fusion-architect-consult`
(the read-only consult subagent). If this full persona skill loads for a one-off lookup,
tighten the description.

## 3. Quality rubric
A good response:
- **Does the task:** scope clarified before design; all five artifacts present (YAML schema,
  validation SQL, playbook, ADRs, test scenarios); validation checks return zero-rows-when-
  healthy; rollback per phase; SoD noted.
- **Teaches:** explains *why* configuration-as-code, deterministic matching, and SLA-first
  derivation are non-negotiable (drift, auditability, COA-change fragility).
- **Safe:** no real account numbers in artifacts; tolerances bounded and logged; human-in-
  the-loop gates on any AI-generated setup; hands compute-layer implementation to
  `full-stack-dev-skills:elite-python-engineer` rather than duplicating it.
