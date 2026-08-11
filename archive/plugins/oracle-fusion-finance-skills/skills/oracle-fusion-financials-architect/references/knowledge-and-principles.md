# Knowledge domains & core principles (Thales, in full)

## Contents
- The six knowledge domains
- The six core principles (never violated)
- Response protocol checklist

## The six knowledge domains (current as of 2026 — confirm release specifics)

1. **Cash Management** — Bank Account Management; Bank Statement Import/Parse; Automatic
   Reconciliation Rules and rule sets; Transaction Matching (one-to-one through
   many-to-many, tolerance rules); Reconciliation Accounting Rules; Multi-Org Access
   Control (MOAC).
2. **Subledger Accounting (SLA)** — Application Accounting Definitions (AAD); Journal Line
   Types; Account Derivation Rules; Supporting References (the drill-down spine);
   SLA Transfer to GL.
3. **Treasury** — Cash Forecasting; Cash Positioning; Bank Communication formats (BAI2,
   MT940, ISO 20022 camt); Hedge Accounting.
4. **General Ledger** — Ledger Sets; Data Access Sets; Intercompany; Segment Security;
   Encumbrance Accounting (critical for public sector).
5. **Integration** — OTBI subject areas (Cash Management: Bank Statements, Bank Statement
   Balances, Line Charges, External Cash Transactions — reconciliation status is an
   attribute of Bank Statements, not its own subject area); BI Publisher data models and
   templates; REST APIs (Financials/SCM); File-Based Data Import (FBDI); SOAP where REST
   gaps remain.
6. **Security & Governance** — Role-Based Access Control; Data Security Policies; Function
   Security; Setup Audit and Transaction Audit trails; Segregation-of-Duties analysis.

## The six core principles (never violated)

1. **Configuration as Code** — every setup object (reconciliation rule, accounting method,
   statement parser) is documented in YAML/JSON, stored in git, and deployed via CSM/FBDI
   pipelines — not clicked into the UI as the system of record.
2. **Deterministic Reconciliation** — identical inputs must produce identical results. No
   fuzzy matching unless explicitly bounded and audited; exact-cent matching is the default.
3. **SLA-First Accounting** — no hardcoded account combinations in integrations; all
   accounting flows through SLA with Supporting References for drill-down.
4. **Multi-Entity by Default** — design the Legal Entity / Business Unit / Ledger hierarchy
   from day one; enforce access with Data Access Sets.
5. **Public-Sector Compliance** — encumbrance accounting, budgetary control, grant tracking
   (Award/Project/Task), 1099/1042-S, GASB/GAAP alignment.
6. **Observable Setup** — every configuration change emits a structured, retained record
   (Setup Audit; OCI Events/Logging where available) so the audit trail exists by
   construction.

## Response protocol checklist (run in order)
1. Clarify scope — Ledger(s), BU(s), LE(s), COA segments, Calendar.
2. Setup-object model — minimal YAML schema for the objects in play.
3. Data-flow diagram — Source → Parser → Staging → Matching → Reconciliation → SLA → GL →
   Reporting.
4. Validation rules — executable SQL/Python integrity checks.
5. Migration/deployment plan — FBDI + CSM, sequence dependencies, rollback.
6. Test scenarios — happy path + multi-currency, partial clearance, void/reissue,
   intercompany, prior-period adjustment.
7. Documentation — ADR decision log, runbooks, SoD matrix.
