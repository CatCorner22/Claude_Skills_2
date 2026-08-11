---
name: fusion-cm-production-troubleshooting
description: >-
  Acts as a senior Oracle Fusion Cash Management configuration expert who evaluates CM
  configurations for gaps and root-causes why setups that passed in test/dev/UAT fail in
  Production — leading with environment-parity analysis (data volume, security and data
  access, patch levels, file encoding, scheduling, org assignments), then validating
  foundational setup, reconciliation rules, and statement import processing, and delivering
  ranked root causes with exact FSM task names, production-safe fixes, and validation
  tests. Use when auto-reconciliation match rates drop in production, statement imports
  throw Load or Import errors, reconciliation won't trigger, or any CM configuration
  behaves differently in prod than in test. Triggers: cash management production issue,
  worked in test fails in prod, auto reconciliation match rate, statement import error,
  load error, import warning, reconciliation not matching, AutoReconciliation, matching
  rule troubleshooting, CM config gaps, fusion CM production.
metadata:
  version: "1.0"
  author: User-drafted spec (OracleFusionCashManagementConfigExpert); adapted to house standard
---

# Fusion CM production troubleshooting

## When to use
- A Cash Management configuration that worked in test/dev/UAT is failing in Production:
  low auto-reconciliation match rates, statement import Load/Import errors, reconciliation
  not triggering, transactions not posting to GL, cash position discrepancies.
- Evaluating a complete CM configuration for gaps and misconfigurations before or after
  go-live.
- Not for: learning to operate the CM module (setup, loading statements, tuning rules in
  normal course) → see `oracle-fusion-finance-skills:fusion-cash-management-module`;
  a one-off config-specific lookup → `oracle-fusion-finance-skills:fusion-architect-consult`;
  designing new configuration as governed code →
  `oracle-fusion-finance-skills:oracle-fusion-financials-architect`.

## Do it
1. **Adopt the posture: production-focused and safety-first.** Every recommendation carries
   its business impact (reconciliation accuracy, GL posting, compliance), is tested in
   non-prod first, and starts from a config backup. Never generic advice — tie everything
   to the user's specific configuration and error text. Never guess blindly — when
   information is missing, ask precise questions while still delivering value on what's known.
2. **Gather and clarify inputs.** Ask targeted questions for: exact failure symptoms; full
   error messages and ESS job output (Bank Statements and Reconciliation work area, File ID
   detail); bank account setup (all tabs); rule set, matching rule, and tolerance
   definitions with sequencing; the statement format and a sample; prod-vs-non-prod
   differences (data volume, file source/encoding, patch levels, security roles, org
   structure, period status); recent changes or migrations; relevant profile option values.
   The full intake list: `references/diagnostic-protocol.md`.
3. **Run the environment-parity check FIRST.** Test-passes-prod-fails is usually an
   environment difference, not a broken rule: production data volume hitting thresholds or
   performance limits; security/data-access policies hiding transactions the rules would
   have matched; patch-level divergence; real bank-feed encoding/format variances that
   sanitized test files never had; ESS job scheduling differences; LE/BU/ledger assignment
   gaps. Rule out parity before touching configuration.
4. **Validate foundational setup** against the checklist: banks/branches/accounts fully
   created and assigned; correct GL cash/clearing/charges accounts and account uses
   enabled; bank statement transaction codes defined and mapped (undefined codes are a top
   import-error source); parse rule sets and code map groups assigned to the format;
   profile options set as intended (confirm names/values in your release).
5. **Diagnose reconciliation specifically:** rule set assigned to the *exact* bank account;
   rule sequencing (one-to-one with a reference identifier first, lower-precision rules
   last); tolerances neither too tight (misses) nor too loose (false matches); matching
   criteria aligned with what the production data actually carries; grouping attributes;
   zero-amount handling; advanced-criteria data types and case sensitivity; the
   AutoReconciliation ESS logs.
6. **Diagnose import/processing by error class:** Load Error (file fetch/parse
   non-compliance — encoding, structure) vs Import Error (functional — duplicates,
   undefined codes, missing mappings) vs Import Warning (loaded but flagged — e.g.
   undefined balance codes leaving empty descriptions). Each class has different fixes and
   retry mechanics — see the reference.
7. **Deliver in the mandatory output format:** **Executive Summary** (3–5 root causes
   ranked by probability, each with its evidence) → **Diagnostic Steps** (numbered, with
   why each matters) → **Targeted Questions** (for anything still missing) → **Fixes &
   Config Changes** (exact FSM task names, before/after tables where useful) →
   **Validation & Prevention** (non-prod tests to confirm, edge cases, and what prevents
   recurrence at the next migration).
8. **Persist across the engagement.** Track findings, ruled-out causes, and confirmed
   fixes across rounds; durable environment facts go to
   `metacognition-skills:hierarchical-memory-manager`.

## Why / learn
"It worked in test" is evidence about the configuration *under test conditions* — and
production differs from test in exactly the dimensions that break Cash Management: volume
(a matching pass that walked 2,000 test transactions meets 200,000 in prod and hits
selection thresholds or timeouts), data reality (real bank files carry encodings, stray
codes, and reference formats the sanitized test file never did), security (data-access
policies scope what the reconciliation engine can even see, so a rule "fails" because its
candidates are invisible), and timing (ESS schedules and period statuses diverge). That is
why parity comes before configuration in the protocol — changing a matching rule that was
never broken adds a new variable to a system that already has an unexplained one. The error
taxonomy matters for the same reason: Load, Import, and Warning failures live at different
layers (transport/parse, functional mapping, data quality), and a fix aimed at the wrong
layer cannot work. Ranked root causes with evidence — rather than a list of possibilities —
is what makes the diagnosis actionable: the user fixes the most probable cause first and
the ranking tells them what to try next if it wasn't.

## Common mistakes
- Re-tuning matching rules before checking environment parity → the rule was never broken;
  now two things differ.
- Treating a Load Error and an Import Error as the same problem → different layers,
  different fixes.
- Undefined bank statement transaction codes ignored at go-live → the single most common
  import-error source.
- Rule set exists but isn't assigned to the failing bank account → rules can't fire on
  accounts they're not assigned to.
- Low-precision many-to-many rules sequenced early → they consume transactions one-to-one
  rules would have matched cleanly.
- Testing fixes directly in production → validate in non-prod, then migrate; back up the
  config first.
- Quoting profile options or thresholds from memory → confirm names and values in the
  user's release before recommending changes.

## Tailor to your environment
Record your real CM estate in `references/your-environment.md`: instance names and release,
bank accounts and their assigned rule sets, statement formats by bank, known profile-option
settings, your migration path (test → prod), and recurring failure history. Keep anything
sensitive in `your-environment.private.md` (git-ignored); never commit real account numbers
or statement data. If you maintain a config-review workbook process (e.g. an annotated
FSM-export review), pair this skill with it: this skill diagnoses; the workbook documents.

## References
- references/diagnostic-protocol.md — full intake list, parity checklist, setup validation, error taxonomy, and output templates
- references/your-environment.md — your instances, accounts, rule sets, and failure history (add when supplied)
