# Artifact templates (the five standard deliverables)

## Contents
- setup-objects.yaml
- validation-rules.sql
- migration-playbook.md
- adr/ (decision records)
- test-scenarios.yaml

## setup-objects.yaml — canonical configuration schema
```yaml
# One file = one governed unit of Fusion setup. Everything reviewable in git.
meta:
  instance: <env name>            # e.g. TEST / PROD pod
  release: <e.g. 25C — confirm>
  owner: <team/person>
  adr_refs: [ADR-001]
ledger:
  name: <primary ledger>
  coa_segments: [entity, fund, natural_account, department, ...]
bank_accounts:
  - name: <structural name only — never a real account number>
    legal_entity: <LE>
    use: [payables, receivables]
    cash_gl: <segment string pattern>
    cash_clearing_gl: <pattern>
transaction_codes:
  - code: "142"
    meaning: ACH credit
    flow: inbound
matching_rules:
  - name: p1_exact_reference
    sequence: 10
    type: one_to_one
    keys: [amount_cents, date_window_3d, reference]
    tolerance: none            # deterministic default; any tolerance must be bounded+logged
accounting_rules:
  - event_class: <e.g. bank_statement_line>
    journal_line_type: <JLT>
    derivation: <SLA rule name>   # never a hardcoded combination
    supporting_refs: [statement_line_id]
```

## validation-rules.sql — integrity checks (OTBI/ADW-runnable)
```sql
-- V1: no orphan parsers (every parser attached to >=1 bank account)
-- V2: every transaction code observed in statements is mapped
SELECT code FROM observed_stmt_codes
MINUS
SELECT code FROM configured_transaction_codes;
-- V3: every event class has an accounting rule (no unaccounted events)
-- V4: no matching rule with unbounded tolerance
SELECT rule_name FROM matching_rules
WHERE tolerance_type IS NOT NULL AND (tolerance_bound IS NULL OR audited_flag = 'N');
```
Convention: each check returns **zero rows when healthy**; any row is a named violation.

## migration-playbook.md — phased deployment skeleton
```markdown
# Migration: <scope>
Phase 0  Baseline export (CSM) + snapshot of validation-rules results
Phase 1  Reference data (codes, formats, parsers)     [rollback: re-import Phase-0 export]
Phase 2  Bank accounts + uses                          [depends: Phase 1]
Phase 3  Matching rules + rule sets                    [depends: Phase 2]
Phase 4  SLA (AAD, JLTs, derivations)                  [depends: Phase 2]
Phase 5  Validation-rules pass MUST return zero rows before cutover
Phase 6  Cutover + hypercare; rollback = Phase-0 import, documented per phase
```
Every phase names its FBDI/CSM vehicle, its dependency, and its rollback.

## adr/ — Architecture Decision Record format
```markdown
# ADR-<n>: <decision title>
Status: proposed | accepted | superseded by ADR-<m>
Context: <the forces — requirement, constraint, release limitation>
Decision: <what we chose>
Consequences: <what this makes easier/harder; what it forecloses>
```
One decision per record; never edit an accepted ADR — supersede it.

## test-scenarios.yaml — executable cases
```yaml
- id: T01_happy_path
  given: {statement_line: {amount: 150.00, code: "142", ref: R1}, open_st: {amount: 150.00, ref: R1}}
  expect: {status: matched, rule: p1_exact_reference}
- id: T02_partial_clearance
  given: {statement_line: {amount: 100.00}, open_st: {amount: 150.00}}
  expect: {status: review, reason: no_exact_candidate}
- id: T03_multi_currency
- id: T04_void_reissue
- id: T05_intercompany
- id: T06_prior_period_adjustment
```
Edge cases are first-class: a rule set ships only with its failing-path expectations.
