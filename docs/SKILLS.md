# Treasury Analyst Skills — trigger & capability catalog

Auto-generated from every skill's `SKILL.md` frontmatter by `scripts/gen-catalog.py`. **148 skills across 21 plugins.**

## How to trigger a skill

There are two ways every skill fires:

1. **Automatically** — just describe your task in plain language. Claude matches your request against each skill's description and **trigger phrases** (listed below) and loads the right one on its own. You don't need to name it.

2. **Manually** — type the slash command `/{plugin}:{skill}` (e.g. `/cash-management-skills:bank-reconciliation`) to invoke a specific skill on demand.

Ask **"what skills are available?"** any time to list them.

## Install

```
/plugin marketplace add blakereaganlaw-droid/claude_skills_2
/plugin install <plugin>@treasury-analyst-skills      # e.g. cash-management-skills@treasury-analyst-skills
```
Install only the plugins you want; each is independent. Skills are namespaced `<plugin>:<skill>` so they never collide.

## Plugins

- [`cash-management-skills`](#cash-management-skills) (6) — Treasury cash operations: cash positioning, bank reconciliation, forecasting, liquidity, controls, and intercompany netting.
- [`oracle-otbi-skills`](#oracle-otbi-skills) (5) — Build OTBI reports and analyses in Oracle Fusion Cloud, with deep Cash Management subject-area coverage.
- [`sponsored-projects-ar-skills`](#sponsored-projects-ar-skills) (13) — Sponsored projects/awards/grants receivables analysis across Oracle Fusion Receivables + PPM: master router, PPM-to-AR domain knowledge, unbilled/billed AR reconciliation, KPIs and trend forecasts, reporting outputs, and federal compliance (Uniform Guidance, federal billing/cash management, effort reporting).
- [`oracle-fusion-finance-skills`](#oracle-fusion-finance-skills) (10) — Functional Oracle Fusion Cloud Financials: GL and journals, FBDI data loading, AP invoice-to-pay, AR and collections, the Cash Management module, period close, plus the fusion-treasury-architect subagent and its consult skill for configuration-specific guidance.
- [`banking-skills`](#banking-skills) (6) — Payment rails, bank account structures, statement formats, bank-fee analysis, connectivity, and KYC/AML basics.
- [`accounting-skills`](#accounting-skills) (6) — Double-entry accounting, journal entries, chart of accounts, month-end close, reconciliations, and financial statements.
- [`finance-skills`](#finance-skills) (6) — Corporate and treasury finance: time value of money, working capital, ratios, short-term investing, FX risk, and capital budgeting.
- [`treasury-accounting-skills`](#treasury-accounting-skills) (6) — Advanced treasury and accounting operations: debt facilities and covenant compliance, hedging and derivatives, investment policy compliance, accruals and prepaids, intercompany accounting, and audit readiness.
- [`data-analytics-bi-skills`](#data-analytics-bi-skills) (8) — SQL, exploratory analysis, data cleaning, statistics, inference, dashboard design, and spreadsheet modeling for business intelligence.
- [`data-tools-skills`](#data-tools-skills) (6) — Practical data plumbing: Excel automation with Python, CSV/flat-file wrangling, DuckDB local analytics, PDF data extraction, REST API data pulls, and data-file hygiene.
- [`machine-learning-skills`](#machine-learning-skills) (7) — Practical machine learning for analysts: project framing, feature engineering, supervised modeling, model evaluation, time-series forecasting, anomaly detection, and self-auditing bespoke LLM architecture (PEFT/QLoRA, efficiency hierarchy, safety by design).
- [`continuous-improvement-skills`](#continuous-improvement-skills) (15) — Lean, Toyota Production System, Six Sigma, and co-design: value-stream mapping, root-cause analysis (with Reason's error taxonomy), DMAIC, standard work, A3, kaizen, Lean Six Sigma for software, the Curve Hero design-language map, the project-command doctrine, and the industrial-engineering methods set (FMEA, theory of constraints, design of experiments, EVOP, measurement systems analysis, QFD).
- [`board-of-advisors-skills`](#board-of-advisors-skills) (1) — Multi-agent Board of Advisors code review: five read-only specialist subagents plus a board-chair synthesizer, orchestrated by the board-review skill into a ranked, goal-preserving optimization report.
- [`full-stack-dev-skills`](#full-stack-dev-skills) (11) — Full-stack application development with a lean-code philosophy: architecture, FastAPI backends, databases/ORM, modern dynamic frontends, realtime features, ML in production, testing strategy, deployment, and evidence-based UI/UX inspection with severity-rated findings and human-factors instruments (Fitts, NASA-TLX).
- [`coding-agent-skills`](#coding-agent-skills) (16) — Python for analysts, Claude Code harness config, autonomous agent design, prompt engineering, git/code review, authoring Agent Skills, and expert personas (script wizard, sparring partner, master prompt architect, the Chicken Little family, the leadership pair, and Comrade Engineer's soviet-space-graphite simplicity challenge).
- [`metacognition-skills`](#metacognition-skills) (4) — Composed meta-cognition suite: hierarchical memory management, reflective learning, adaptive analysis, and knowledge crystallization for cumulative improvement across sessions.
- [`public-sector-treasury-skills`](#public-sector-treasury-skills) (8) — Public-sector and higher-ed treasury: fund accounting (GASB), public funds investing, unclaimed property escheatment, merchant services and PCI, NACHA ACH rules, debt post-issuance compliance, treasurer reporting, and CTP exam prep.
- [`deep-research-skills`](#deep-research-skills) (1) — True deep research: extensive multi-database literature investigation, cross-domain dot-connection between seemingly unrelated findings, source-provenance control, evidence appraisal, and triple-checked citation verification. Includes the medical-research-detective for published medical literature.
- [`writing-skills`](#writing-skills) (2) — Ken Adams clarity writing, two registers: adams-smart-brevity (Adams + Axios Smart Brevity for professional, technical, legal, and clinical writing) and adams-plain-grade (5th-8th grade accessible register). Both reject litigated "tested language" and ambiguity.
- [`safety-and-reliability-skills`](#safety-and-reliability-skills) (5) — High-hazard-industry methods transplanted to operations and software: checklist design (read-do/do-confirm, killer items), bowtie barrier analysis with HAZOP guidewords, SBAR/I-PASS structured communication with PACE assertiveness, reliability engineering math (Weibull, MTBF, availability), and weight-of-the-books design-basis load review (the Load Manifest: size systems against the payload they exist to carry).
- [`decision-science-skills`](#decision-science-skills) (6) — Structured-judgment methods from intelligence, military, and forecasting practice: competing-hypotheses analysis, reference-class forecasting (outside view), pre-mortem, after-action review, tabletop wargaming with commander's intent, and principled negotiation (Fisher/Ury + Voss).

## `cash-management-skills`

Treasury cash operations: cash positioning, bank reconciliation, forecasting, liquidity, controls, and intercompany netting.

Install: `/plugin install cash-management-skills@treasury-analyst-skills`

### `cash-management-skills:bank-reconciliation`

**Invoke:** `/cash-management-skills:bank-reconciliation` — or just describe the task.

**What it does:** Reconciles a bank statement to the ledger or system cash balance, matches transactions, classifies outstanding and in-transit items, and investigates breaks until the difference resolves to zero. Use when reconciling a bank account, chasing an unreconciled difference, reviewing someone's reconciliation, or setting up matching/tolerance rules.

**Triggers:** `bank reconciliation`, `recon`, `reconcile the bank`, `unreconciled`, `outstanding items`, `deposits in transit`, `outstanding checks`, `statement vs book`, `reconciling difference`, `break`

### `cash-management-skills:cash-forecasting`

**Invoke:** `/cash-management-skills:cash-forecasting` — or just describe the task.

**What it does:** Builds direct-method short- and medium-term cash forecasts — projecting receipts and disbursements from operational drivers (AR collections, AP runs, payroll, debt service, tax) — and measures forecast-vs-actual variance to improve accuracy. Use when projecting liquidity, building a rolling 13-week or monthly cash forecast, choosing the direct vs. indirect method, or reviewing forecast accuracy.

**Triggers:** `cash forecast`, `liquidity forecast`, `direct method`, `indirect method`, `rolling forecast`, `13-week forecast`, `forecast variance`, `forecast accuracy`, `receipts and disbursements`, `project cash flow`

### `cash-management-skills:cash-management-controls`

**Invoke:** `/cash-management-skills:cash-management-controls` — or just describe the task.

**What it does:** Designs and reviews controls over cash processes — segregation of duties, payment authorization and dual approval, positive pay and ACH filters, reconciliation as a detective control, bank mandate management, and business-email-compromise prevention — mapped to the control objectives of authorization, completeness, accuracy, and safeguarding. Use when designing or auditing cash controls, building a segregation-of-duties matrix, or responding to a payment-fraud risk.

**Triggers:** `cash controls`, `segregation of duties`, `SOD`, `dual approval`, `payment authorization`, `positive pay`, `ACH filter`, `payment fraud`, `BEC`, `business email compromise`, `audit trail`, `bank mandate`

### `cash-management-skills:cash-positioning`

**Invoke:** `/cash-management-skills:cash-positioning` — or just describe the task.

**What it does:** Builds and reads a daily cash position — opening, available, and projected closing balances across bank accounts, currencies, and entities — from actual cash flows (bank statement balances, AP payments, AR receipts, payroll) to drive funding, sweep, and investing decisions. Use when determining how much cash is available today, sizing a sweep, funding a disbursement account before a payment run, or building a cash position worksheet.

**Triggers:** `cash position`, `daily cash`, `available balance`, `cash worksheet`, `opening balance`, `closing balance`, `position the cash`, `sweep decision`, `how much cash today`, `funding decision`

### `cash-management-skills:intercompany-cash-netting`

**Invoke:** `/cash-management-skills:intercompany-cash-netting` — or just describe the task.

**What it does:** Designs and runs intercompany netting cycles and in-house-bank settlements to cut cross-entity payments, float, and FX conversions, and evaluates pooling structures (notional, physical/ZBA, POBO/COBO). Use when consolidating intercompany cash, running a bilateral or multilateral netting cycle, or assessing an in-house bank or cash-pooling structure.

**Triggers:** `netting`, `intercompany netting`, `netting cycle`, `bilateral netting`, `multilateral netting`, `in-house bank`, `cash pooling`, `notional pooling`, `physical pooling`, `POBO`, `COBO`, `settlement cycle`

### `cash-management-skills:liquidity-management`

**Invoke:** `/cash-management-skills:liquidity-management` — or just describe the task.

**What it does:** Assesses liquidity buffers and sets target/minimum balances, structures concentration and zero-balance sweeps, and decides how to deploy surplus cash or cover a deficit across accounts and entities. Use when setting target balances, designing sweeps or a concentration structure, sizing a liquidity buffer, or deciding what to do with surplus or short cash.

**Triggers:** `liquidity`, `target balance`, `minimum balance`, `concentration account`, `ZBA`, `cash sweep`, `liquidity buffer`, `surplus cash`, `idle cash`, `cover a shortfall`, `committed facility`

## `oracle-otbi-skills`

Build OTBI reports and analyses in Oracle Fusion Cloud, with deep Cash Management subject-area coverage.

Install: `/plugin install oracle-otbi-skills@treasury-analyst-skills`

### `oracle-otbi-skills:otbi-analysis-filters`

**Invoke:** `/oracle-otbi-skills:otbi-analysis-filters` — or just describe the task.

**What it does:** Scopes and parameterizes an OTBI analysis: builds filters and "is prompted" filters, column/named/dashboard prompts, presentation and repository variables, and column-formula CASE logic for aging or classification buckets. Use when adding filters to a report, making it interactive or prompt-driven, passing runtime parameters, or writing a CASE column for aging buckets and derived measures.

**Triggers:** `add a filter`, `is prompted`, `dashboard prompt`, `column prompt`, `named prompt`, `presentation variable`, `runtime parameter`, `prompt-driven report`, `aging buckets`, `CASE formula`, `bucket a column`, `as-of date prompt`

### `oracle-otbi-skills:otbi-cash-management-reports`

**Invoke:** `/oracle-otbi-skills:otbi-cash-management-reports` — or just describe the task.

**What it does:** Builds the common Oracle Cash Management OTBI reports — bank statement balances, cash-position snapshot, unreconciled/exception and aging analyses, reconciliation status summary, bank-charge and charge-tax breakdowns, and external cash transaction audits — each mapped to its correct Cash Management subject area, with the security duty role required and the reconciliation-status-is-an- attribute caveat. Use when reporting on Oracle Fusion Cash Management data in OTBI.

**Triggers:** `cash management report`, `bank statement balances report`, `cash position OTBI`, `unreconciled report`, `reconciliation status report`, `bank charges report`, `external cash transactions`, `OTBI cash report`, `unreconciled aging`

### `oracle-otbi-skills:otbi-report-building`

**Invoke:** `/oracle-otbi-skills:otbi-report-building` — or just describe the task.

**What it does:** Builds or edits an Oracle Transactional Business Intelligence (OTBI) analysis end to end in Oracle Fusion Cloud: pick one subject area, add columns and column formulas on the Criteria tab, set filters, assemble Results views into a compound layout, save under /Shared Folders/Custom, and surface it on a dashboard with a shared prompt. Use when creating, editing, or troubleshooting any OTBI report or analysis.

**Triggers:** `build an OTBI report`, `create an analysis`, `OTBI analysis`, `Reports and Analytics`, `Browse Catalog`, `criteria tab`, `compound layout`, `add a column formula`, `put an analysis on a dashboard`, `edit an OTBI report`

### `oracle-otbi-skills:otbi-report-scheduling-sharing`

**Invoke:** `/oracle-otbi-skills:otbi-report-scheduling-sharing` — or just describe the task.

**What it does:** Shares and distributes OTBI content through dashboards and catalog folder permissions, and flags OTBI's key limitation — no native scheduling, bursting, or pixel-perfect output — so scheduled, burst, or precisely formatted delivery is routed to BI Publisher instead. Use when sharing, scheduling, distributing, emailing, or setting permissions on an OTBI report or dashboard, or when deciding between OTBI and BI Publisher for delivery.

**Triggers:** `share an OTBI report`, `schedule a report`, `burst a report`, `email a report on a schedule`, `distribute a dashboard`, `catalog permissions`, `pixel-perfect report`, `BI Publisher vs OTBI`, `OTBI can't schedule`

### `oracle-otbi-skills:otbi-subject-area-selection`

**Invoke:** `/oracle-otbi-skills:otbi-subject-area-selection` — or just describe the task.

**What it does:** Chooses the right OTBI subject area and columns for a reporting question, explains fact vs. dimension folders and the one-subject-area-per-analysis limit, and gives cross-pillar workarounds (BI Publisher SQL, side-by-side dashboard analyses on a shared prompt, or FDI/OAC). Covers the four Oracle Cash Management subject areas and when to use each. Use when unsure which subject area or columns to query, or when a report seems to need two subject areas or two Fusion pillars.

**Triggers:** `which subject area`, `pick a subject area`, `what subject area for`, `cross-subject-area`, `join two subject areas`, `Cash Management subject area`, `single subject area limit`, `column not available`, `fact vs dimension folder`

## `sponsored-projects-ar-skills`

Sponsored projects/awards/grants receivables analysis across Oracle Fusion Receivables + PPM: master router, PPM-to-AR domain knowledge, unbilled/billed AR reconciliation, KPIs and trend forecasts, reporting outputs, and federal compliance (Uniform Guidance, federal billing/cash management, effort reporting).

Install: `/plugin install sponsored-projects-ar-skills@treasury-analyst-skills`

### `sponsored-projects-ar-skills:compliance-risk-anomaly`

**Invoke:** `/sponsored-projects-ar-skills:compliance-risk-anomaly` — or just describe the task.

**What it does:** Identifies compliance risks, exceptions, and anomalies in sponsored/grant receivables data across all sponsor types — scanning the public exception patterns (billing exceptions, holds, unapplied receipts, at-risk receipts in aging data), the sponsored-specific risks (allowability-suspect charges, funding-limit breaches, overdue-beyond-sponsor-terms), and statistical anomalies (outlier aging, DSO spikes, unusual adjustment and credit-memo volumes), then cross-checking PPM costs against AR billing for alignment. Use for audit-, risk-, or exception-focused questions on sponsored AR.

**Triggers:** `sponsored AR exceptions`, `grant AR anomalies`, `billing exceptions scan`, `risk register receivables`, `unusual credit memos`, `DSO spike`, `funding limit breach`, `overdue beyond terms`, `AR risk review`, `exception report grants`, `at-risk receipts`

### `sponsored-projects-ar-skills:federal-billing-cash-management`

**Invoke:** `/sponsored-projects-ar-skills:federal-billing-cash-management` — or just describe the task.

**What it does:** Explains federal payment methods — Letter of Credit / Payment Management System drawdowns, advances, and reimbursement under §200.305 — and how each affects unbilled AR, billed AR, cash application, and aging in Oracle Fusion PPM + Receivables analysis: distinguishing draws from invoices, monitoring the expenditure-to-draw lag, overdraw debts (§200.346), SF-270-style documentation, and why federal write-offs can't hit the award. Use when analyzing unbilled/billed transitions, cash receipts from federal sponsors, federal AR aging, or drawdown-vs-invoicing questions.

**Triggers:** `LOC drawdown`, `letter of credit billing`, `PMS draw`, `payment management system`, `federal reimbursement`, `SF-270`, `expenditure to draw lag`, `federal advance payment`, `federal AR aging`, `drawdown vs invoice`, `overdraw`, `federal cash management`

### `sponsored-projects-ar-skills:federal-cost-allowability`

**Invoke:** `/sponsored-projects-ar-skills:federal-cost-allowability` — or just describe the task.

**What it does:** Applies the Uniform Guidance cost principles to evaluate whether costs or billed amounts on federal awards are allowable, allocable, and reasonable — running the §200.403 factor tests, the §200.404 prudent-person standard, and §200.405 relative-benefit allocation, applying the special rules (administrative salaries under §200.413, equipment, travel, participant support) and the always-unallowable list (§200.426 bad debts and related collection costs), and flagging suspect items with CFR citations and recommended actions. Use when reviewing invoices, adjustments, write-offs, or cost data on federal awards, or for any "can this be charged/billed?" question.

**Triggers:** `allowable cost`, `allowability`, `can we charge this to the grant`, `§200.403`, `unallowable`, `allocable`, `cost principles`, `questioned cost review`, `admin salary direct charge`, `prior approval cost`, `prudent person test`, `bill this to the award`

### `sponsored-projects-ar-skills:federal-effort-reporting-basics`

**Invoke:** `/sponsored-projects-ar-skills:federal-effort-reporting-basics` — or just describe the task.

**What it does:** Explains the Uniform Guidance standards for charging personnel costs to federal awards (§200.430) — reasonable compensation, consistent institutional policy, records that accurately reflect total work activity and support salary distribution, budget estimates adjusted to actuals — and why unsupported effort turns into questioned costs that claw back previously billed AR. Use for questions about salary charges, effort reporting, payroll allocation, effort certification, or when federal project data shows high personnel-cost density.

**Triggers:** `effort reporting`, `effort certification`, `salary allocation federal`, `§200.430`, `personnel costs grant`, `payroll charged to award`, `time and effort`, `salary cap`, `questioned personnel costs`, `effort commitment`, `charging salaries to grants`

### `sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk`

**Invoke:** `/sponsored-projects-ar-skills:federal-sponsored-ar-compliance-risk` — or just describe the task.

**What it does:** Assesses compliance and audit risk in Receivables data for federal sponsored projects — identifying federal awards, scanning for high-risk patterns (aged federal AR, frequent adjustments/credit memos, write-offs, unbilled build-up, allowability-suspect costs), applying the §200.426 bad-debt and §200.410 questioned-cost rules to adjustments and write-off proposals, mapping Single Audit/SEFA implications, and grading documentation readiness — delivered as a prioritized risk assessment that is explicitly not an audit opinion. Use for aging analysis, exception review, write-off recommendations, or any risk-focused question on federal awards.

**Triggers:** `federal AR risk`, `questioned costs`, `write off federal receivable`, `single audit exposure`, `SEFA`, `federal compliance risk`, `audit risk sponsored projects`, `federal adjustments review`, `closeout residual balance`, `subrecipient risk`, `cost sharing shortfall`

### `sponsored-projects-ar-skills:fusion-ar-ppm-domain-knowledge`

**Invoke:** `/sponsored-projects-ar-skills:fusion-ar-ppm-domain-knowledge` — or just describe the task.

**What it does:** Provides the authoritative public-domain map of how sponsored projects data flows between Oracle Fusion PPM/Grants and Receivables — award and bill-plan types, the relevant OTBI subject areas on both sides, the PPM-to-AutoInvoice-to-AR integration and status flow, and a data-profiling routine for any uploaded sponsored-AR extract, with the standard gotchas flagged. Use as the first analytical step after the sponsored-AR router, or whenever the question is about data sources, subject areas, terminology, or column mapping.

**Triggers:** `PPM subject area`, `project billing subject area`, `where does unbilled AR come from`, `AutoInvoice PPM`, `sponsored AR data model`, `map these columns`, `grants data source`, `project invoice flow`, `bill plan type`, `confirm invoice acceptance`

### `sponsored-projects-ar-skills:reporting-visualization-recommendations`

**Invoke:** `/sponsored-projects-ar-skills:reporting-visualization-recommendations` — or just describe the task.

**What it does:** Turns sponsored-AR analysis into finished deliverables — the standard structured report (executive summary, data validation, detailed tables, visual descriptions, insights by financial/operational/compliance/strategic angle), suggested OTBI-style report patterns (AR aging by project, project invoices prior to acceptance), and actionable recommendations covering collection priorities, billing acceleration, and data quality, with multi-currency, intercompany, and partial-payment edge cases handled. Use as the final step of any sponsored-AR analysis, or when the user asks for summaries, dashboards, report designs, or next steps on sponsored/grants receivables.

**Triggers:** `sponsored AR report`, `grants AR summary`, `AR dashboard for projects`, `executive summary receivables`, `OTBI report for sponsored projects`, `aging by sponsor report`, `what should we do about unbilled`, `present sponsored AR`, `next steps grants AR`

### `sponsored-projects-ar-skills:revenue-billing-reconciliation`

**Invoke:** `/sponsored-projects-ar-skills:revenue-billing-reconciliation` — or just describe the task.

**What it does:** Reconciles PPM revenue recognition against AR billing for sponsored awards from the accounting side — the documented Generate Revenue → events → invoice flow, the variance identity (recognized revenue − billed = unbilled or over-billed), funding-limit checks against contract amounts, and the unbilled-AR account roll (DR Unbilled Receivable / CR Revenue at recognition; DR Receivable / CR Unbilled Receivable at invoicing) through to GL tie-out. Use for questions about revenue vs invoiced amounts, over/under-billing, unbilled balance substantiation, or tying sponsored revenue and receivables to the GL.

**Triggers:** `revenue vs billing`, `over billed`, `under billed`, `revenue reconciliation`, `unbilled receivable account`, `GL tie-out sponsored`, `recognized vs invoiced`, `revenue events`, `billing in excess`, `substantiate unbilled balance`, `project revenue reconciliation`

### `sponsored-projects-ar-skills:sponsored-ar-aging-collections`

**Invoke:** `/sponsored-projects-ar-skills:sponsored-ar-aging-collections` — or just describe the task.

**What it does:** Performs detailed aging, DSO, and collections analysis for sponsored/grant receivables at the sponsor, contract, and project level — public-standard metrics (current/overdue/future AR, aging amounts and counts on a declared invoice-date or schedule-date basis, % overdue, average days outstanding/overdue), breakdowns by award type, business unit, ledger, and receivable GL account, sponsor concentration and late-payment risk, and cross-referencing receipts and credit-memo applications — producing a prioritized collection list with cash-flow implications. Use for overdue invoices, aging buckets, collections prioritization, or cash-flow risk questions on sponsored data.

**Triggers:** `sponsored aging`, `overdue sponsor invoices`, `grant collections`, `aging buckets by sponsor`, `collection priority list`, `late paying sponsors`, `sponsor concentration`, `days overdue`, `past due grants AR`, `collections analysis`

### `sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router`

**Invoke:** `/sponsored-projects-ar-skills:sponsored-ar-fusion-analyst-master-router` — or just describe the task.

**What it does:** Routes and coordinates every analysis of sponsored projects, awards, and grants receivables data in Oracle Fusion Cloud (Receivables + PPM/Grants integration) — classifying the question, confirming the award/bill-plan type, requiring data or a clear description before any calculation, dispatching to the right sub-skill, and enforcing the standard output structure. Use FIRST for any sponsored-AR question, before any analysis.

**Triggers:** `sponsored projects`, `grants`, `awards`, `project invoices`, `PPM receivables`, `unbilled AR`, `project contract billing`, `sponsor AR`, `grant receivables`, `award billing`, `sponsored research billing`, `grants AR analysis`

### `sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast`

**Invoke:** `/sponsored-projects-ar-skills:sponsored-ar-kpi-trends-forecast` — or just describe the task.

**What it does:** Computes the core KPI set for sponsored-project receivables — AR outstanding, DSO, aging distribution and turnover, receipts vs transactions, plus sponsor/project-specific measures like burn rate vs funding, invoice-to-revenue ratio, and collections effectiveness — then runs trend analysis by sponsor, project type, and award category, and builds simple disclosed- assumption forecasts, reading results from liquidity, sponsor-relationship, and budget angles. Use for performance overviews, benchmarking, trend, or forward-looking sponsored-AR questions.

**Triggers:** `sponsored AR KPIs`, `DSO by sponsor`, `AR aging trend`, `collections effectiveness`, `burn rate vs funding`, `grant AR metrics`, `receivables benchmark`, `forecast collections`, `invoice to revenue ratio`, `sponsor AR performance`, `YoY AR comparison`

### `sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon`

**Invoke:** `/sponsored-projects-ar-skills:unbilled-billed-ar-wip-recon` — or just describe the task.

**What it does:** Reconciles unbilled (WIP) versus billed AR for sponsored projects and tracks the billing lifecycle — measuring pipeline by billing status (Ready to Bill, In Progress, Billed, Error), reconciling PPM revenue events against Receivables invoices, isolating holds and exceptions, and handling cost-reimbursable, letter-of-credit, and multi-project-contract edge cases. Use when the question involves work-in-progress, unbilled receivables, draft invoices, billing backlog, invoices in error, or PPM-to-AR reconciliation variances.

**Triggers:** `unbilled AR`, `WIP reconciliation`, `billing status`, `draft invoices`, `billing backlog`, `invoices in error`, `ready to bill`, `PPM to AR reconciliation`, `unbilled to billed`, `billing exceptions`, `LOC billing`, `stuck invoices`

### `sponsored-projects-ar-skills:uniform-guidance-federal-core`

**Invoke:** `/sponsored-projects-ar-skills:uniform-guidance-federal-core` — or just describe the task.

**What it does:** Provides core educational knowledge of 2 CFR Part 200 (Uniform Guidance) for federal awards — the subpart structure, post-2024 thresholds (15% de minimis F&A on MTDC, $1,000,000 Single Audit, $10,000 equipment), financial management standards (§200.302), payment standards (§200.305), cost principles and always-unallowable costs (Subpart E), and refund obligations — as context for sponsored projects billing and receivables analysis. Use for any question involving federal awards, Uniform Guidance, 2 CFR 200, cost principles, Single Audit, or when analyzing AR data for federal sponsors.

**Triggers:** `uniform guidance`, `2 CFR 200`, `federal award compliance`, `cost principles`, `single audit`, `de minimis rate`, `MTDC`, `unallowable costs`, `allowability`, `federal grant rules`, `questioned costs`, `F&A rate`

## `oracle-fusion-finance-skills`

Functional Oracle Fusion Cloud Financials: GL and journals, FBDI data loading, AP invoice-to-pay, AR and collections, the Cash Management module, period close, plus the fusion-treasury-architect subagent and its consult skill for configuration-specific guidance.

Install: `/plugin install oracle-fusion-finance-skills@treasury-analyst-skills`

### `oracle-fusion-finance-skills:fusion-ap-invoice-to-pay`

**Invoke:** `/oracle-fusion-finance-skills:fusion-ap-invoice-to-pay` — or just describe the task.

**What it does:** Runs the Oracle Fusion Payables invoice-to-pay cycle — invoice entry and validation, PO matching (2/3/4-way), holds and their releases, approval workflow, accounting, and paying through Payment Process Requests (PPRs) that build payment files. Use when entering or fixing an AP invoice in Fusion, releasing holds, investigating why an invoice isn't paid, or running and troubleshooting a payment batch.

**Triggers:** `fusion AP`, `payables invoice`, `invoice hold`, `release hold`, `invoice validation`, `PO matching`, `three-way match`, `payment process request`, `PPR`, `payment batch`, `invoice not paid`, `pay run fusion`, `payables approval`

### `oracle-fusion-finance-skills:fusion-ar-and-collections`

**Invoke:** `/oracle-fusion-finance-skills:fusion-ar-and-collections` — or just describe the task.

**What it does:** Runs Oracle Fusion Receivables — creating and importing AR transactions (invoices, credit memos), applying receipts manually and through lockbox/automatch, keeping unapplied and on-account cash honest, and working aging and the Advanced Collections dunning/strategy cycle. Use when booking or fixing an AR transaction in Fusion, applying or troubleshooting receipts, reconciling unapplied cash, or setting up aging and collections follow-up.

**Triggers:** `fusion AR`, `receivables invoice`, `apply receipt`, `unapplied receipt`, `on-account`, `lockbox`, `autoapply`, `credit memo fusion`, `AR aging`, `collections fusion`, `dunning`, `receipt application`, `customer balance`

### `oracle-fusion-finance-skills:fusion-architect-consult`

**Invoke:** `/oracle-fusion-finance-skills:fusion-architect-consult` — or just describe the task.

**What it does:** Consults the fusion-treasury-architect subagent — an elite Oracle Cloud Fusion Financials and Treasury architect persona — for expert, configuration-specific answers: exact FSM task names and Redwood UI navigation, COA/value-set/CVR design, SLA mapping and journal line rules, bank statement parsing (BAI2/CAMT.053/MT940 with segment-level detail), reconciliation rule sets and tolerances, AutoInvoice/lockbox/PPR configuration, and structured error troubleshooting (root cause → diagnostics → resolution). Use for deep Fusion configuration design, integration architecture, or error diagnosis beyond the teaching skills.

**Triggers:** `fusion configuration`, `FSM task`, `redwood navigation`, `configure SLA`, `CVR design`, `BAI2 parsing rule`, `reconciliation rule setup`, `AutoInvoice grouping rule`, `PPR setup`, `fusion error troubleshooting`, `lockbox configuration`, `fusion architect`

### `oracle-fusion-finance-skills:fusion-auto-reconciliation-design`

**Invoke:** `/oracle-fusion-finance-skills:fusion-auto-reconciliation-design` — or just describe the task.

**What it does:** Acts as an Oracle Cloud Fusion Cash Management architect who designs and optimizes automated bank reconciliation systems for maximum automatic match rates — applying the subledger-supremacy philosophy (the bank statement mirrors what AR/AP already processed; transaction creation rules are a last resort reserved for bank-originated items like fees, interest, and sweeps), a strict matching hierarchy (exact one-to-one first, grouped many-sided next, judicious tolerances), and format-level parsing engineering (BAI2 16/88 records and type codes, CAMT.053, MT940) to fuel matching from references the bank actually sends. Use when designing or tuning matching, parsing, or transaction creation rules, raising auto-match rates, or reconciling bulk settlements.

**Triggers:** `matching rule design`, `raise match rate`, `auto reconciliation design`, `transaction creation rule`, `TCR`, `parse rule`, `BAI2 88 record`, `bulk deposit reconciliation`, `credit card settlement recon`, `recon rule optimization`, `tolerance rule design. metadata: version: "1.0" author: User-drafted spec (Oracle Cloud Fusion Cash Management Architect); adapted to house standard`

### `oracle-fusion-finance-skills:fusion-cash-management-module`

**Invoke:** `/oracle-fusion-finance-skills:fusion-cash-management-module` — or just describe the task.

**What it does:** Operates the Oracle Fusion Cash Management module — bank, branch, and account setup; loading and troubleshooting electronic bank statements (BAI2, camt.053); tuning automatic reconciliation matching rules and rule sets; handling external cash transactions; and reading the module's reconciliation statuses. Use when setting up bank accounts in Fusion, loading bank statements, configuring or debugging auto-reconciliation, or clearing unreconciled statement lines in the Fusion CE module.

**Triggers:** `fusion cash management`, `bank statement load`, `camt.053 fusion`, `BAI2 import`, `auto reconciliation fusion`, `matching rules`, `reconcile in fusion`, `external cash transaction`, `bank account setup fusion`, `unreconciled statement lines`

### `oracle-fusion-finance-skills:fusion-cm-production-troubleshooting`

**Invoke:** `/oracle-fusion-finance-skills:fusion-cm-production-troubleshooting` — or just describe the task.

**What it does:** Acts as a senior Oracle Fusion Cash Management configuration expert who evaluates CM configurations for gaps and root-causes why setups that passed in test/dev/UAT fail in Production — leading with environment-parity analysis (data volume, security and data access, patch levels, file encoding, scheduling, org assignments), then validating foundational setup, reconciliation rules, and statement import processing, and delivering ranked root causes with exact FSM task names, production-safe fixes, and validation tests. Use when auto-reconciliation match rates drop in production, statement imports throw Load or Import errors, reconciliation won't trigger, or any CM configuration behaves differently in prod than in test.

**Triggers:** `cash management production issue`, `worked in test fails in prod`, `auto reconciliation match rate`, `statement import error`, `load error`, `import warning`, `reconciliation not matching`, `AutoReconciliation`, `matching rule troubleshooting`, `CM config gaps`, `fusion CM production. metadata: version: "1.0" author: User-drafted spec (OracleFusionCashManagementConfigExpert); adapted to house standard`

### `oracle-fusion-finance-skills:fusion-fbdi-data-loading`

**Invoke:** `/oracle-fusion-finance-skills:fusion-fbdi-data-loading` — or just describe the task.

**What it does:** Loads data into Oracle Fusion Cloud with File-Based Data Import (FBDI) — picks the right import template, fills it without breaking its hidden formatting rules, generates and uploads the zip, runs the interface loader and the module import job, and works the error-correction loop until every row lands. Covers GL journal import (GL_INTERFACE) in depth. Use when bulk-loading journals, invoices, or other records into Fusion, or when an FBDI load errors out.

**Triggers:** `FBDI`, `file-based data import`, `journal import`, `GL_INTERFACE`, `import journals`, `load data into fusion`, `FBDI template`, `interface loader`, `ESS import job`, `correct import errors`, `bulk load fusion`

### `oracle-fusion-finance-skills:fusion-gl-and-journals`

**Invoke:** `/oracle-fusion-finance-skills:fusion-gl-and-journals` — or just describe the task.

**What it does:** Works General Ledger in Oracle Fusion Cloud — reads the ledger and chart-of-accounts structure (segments, value sets, hierarchies, cross-validation rules), creates manual and spreadsheet (ADFdi) journals, routes them through approval, posts them, and troubleshoots unposted or rejected journals. Use when entering or fixing a journal in Fusion GL, explaining a ledger/COA setup, or diagnosing why a journal won't post.

**Triggers:** `fusion journal`, `GL journal entry`, `create journal in fusion`, `ADFdi journal`, `spreadsheet journal`, `journal approval`, `post journal`, `journal won't post`, `cross-validation rule`, `chart of accounts segments`, `fusion ledger`

### `oracle-fusion-finance-skills:fusion-period-close`

**Invoke:** `/oracle-fusion-finance-skills:fusion-period-close` — or just describe the task.

**What it does:** Drives period close in Oracle Fusion Cloud — the subledger-to-GL close sequence (AP, AR, FA, projects, then GL), period statuses per module, exception sweeps (unaccounted transactions, stuck interface rows), subledger-to-GL reconciliation, and the Close Monitor/close calendar. Use when closing a period in Fusion, deciding the close order, chasing why a period won't close, or reconciling a subledger to its GL control account at close.

**Triggers:** `period close fusion`, `close the period`, `period status`, `can't close period`, `close AP period`, `sweep unaccounted`, `subledger close`, `close monitor`, `period end fusion`, `exceptions preventing close`

### `oracle-fusion-finance-skills:oracle-fusion-financials-architect`

**Invoke:** `/oracle-fusion-finance-skills:oracle-fusion-financials-architect` — or just describe the task.

**What it does:** Acts as "Thales", a principal-level Oracle Fusion Cloud Financials architect (public-sector/higher-ed, multi-entity) covering Cash Management, Treasury, Subledger Accounting, and reconciliation-engine design. Treats Oracle setup as code: delivers YAML setup-object schemas, executable validation rules, migration playbooks with rollback, ADRs, and test scenarios — deterministic reconciliation and SLA-first accounting are non-negotiable. Use for Fusion architecture and configuration governance, reconciliation rule design, OTBI/BIP/REST integration patterns, security/SoD models, or EBS/PeopleSoft-to-Fusion migration planning.

**Triggers:** `fusion architect`, `oracle architecture`, `setup objects`, `configuration as code`, `reconciliation design`, `subledger accounting`, `SLA`, `data access set`, `ledger set`, `MOAC`, `encumbrance`, `migration playbook`, `validation rules`, `setup governance`, `treasury architecture. metadata: version: "1.0" author: Synthesized from 2026 Oracle Cloud ecosystem + public-sector treasury practices; adapted to house standard`

## `banking-skills`

Payment rails, bank account structures, statement formats, bank-fee analysis, connectivity, and KYC/AML basics.

Install: `/plugin install banking-skills@treasury-analyst-skills`

### `banking-skills:bank-account-structure`

**Invoke:** `/banking-skills:bank-account-structure` — or just describe the task.

**What it does:** Designs bank account hierarchies and automated sweep structures — concentration/header accounts, zero-balance (ZBA) and target-balance sub-accounts, and physical vs notional cash pooling — and rationalizes account counts to cut idle cash, fees, and risk. Use when structuring, opening, or rationalizing bank accounts, or designing sweeps or cash pooling.

**Triggers:** `bank account structure`, `account hierarchy`, `ZBA`, `zero balance account`, `concentration account`, `target balance`, `sweeps`, `cash pooling`, `notional pooling`, `account rationalization`, `BAM`, `bank account management`

### `banking-skills:bank-connectivity`

**Invoke:** `/banking-skills:bank-connectivity` — or just describe the task.

**What it does:** Reasons about the channels that connect an ERP or TMS to banks — host-to-host SFTP, SWIFT (Alliance, service bureau, SCORE), bank APIs / open banking, and single-bank portals — weighing cost, effort, resilience, and standardization, and covering file security (PGP, SSH keys). Use when integrating with a bank, choosing a connectivity channel, or securing bank file transfer.

**Triggers:** `host-to-host`, `H2H`, `SFTP`, `SWIFT connectivity`, `service bureau`, `SCORE`, `Alliance Lite`, `bank API`, `open banking`, `ERP to bank`, `TMS to bank`, `bank portal`, `PGP`, `connectivity channel`

### `banking-skills:bank-fee-analysis`

**Invoke:** `/banking-skills:bank-fee-analysis` — or just describe the task.

**What it does:** Analyzes bank fees from account-analysis statements — decoding AFP Service Codes, EDI 822 and ISO 20022 camt.086 billing files, and the earnings-credit-rate (ECR) offset against compensating balances — to review, benchmark, and reduce bank charges. Use when reviewing bank fees, reading an account analysis statement, or preparing a fee negotiation.

**Triggers:** `bank fees`, `account analysis`, `account analysis statement`, `AFP service codes`, `EDI 822`, `camt.086`, `bank services billing`, `earnings credit rate`, `ECR`, `compensating balance`, `fee reduction`, `bank billing`

### `banking-skills:bank-statement-parsing`

**Invoke:** `/banking-skills:bank-statement-parsing` — or just describe the task.

**What it does:** Normalizes bank statement files — BAI2, SWIFT MT940/MT942, ISO 20022 CAMT.053/CAMT.052, and CSV — into one reconciliation-ready schema (date, amount, direction, reference, description, balance), handling each format's balance and transaction codes and sign conventions. Use when ingesting, mapping, or troubleshooting a bank statement file before positioning or reconciliation.

**Triggers:** `BAI2`, `MT940`, `MT942`, `CAMT.053`, `CAMT.052`, `bank file`, `statement import`, `parse statement`, `transaction code`, `balance code`, `normalize statement`, `prior-day vs intraday`

### `banking-skills:kyc-aml-basics`

**Invoke:** `/banking-skills:kyc-aml-basics` — or just describe the task.

**What it does:** Explains and applies KYC / CDD / EDD, beneficial-ownership (UBO) identification, sanctions and OFAC/SDN screening, AML red flags, transaction monitoring, and SARs when onboarding or transacting with a counterparty — educational fundamentals, not legal advice. Use when onboarding a counterparty, screening a payment, or understanding an AML/KYC control.

**Triggers:** `KYC`, `CDD`, `EDD`, `AML`, `know your customer`, `customer due diligence`, `beneficial ownership`, `UBO`, `sanctions screening`, `OFAC`, `SDN`, `PEP`, `red flags`, `SAR`, `transaction monitoring`, `correspondent banking risk`

### `banking-skills:payment-rails`

**Invoke:** `/banking-skills:payment-rails` — or just describe the task.

**What it does:** Compares and selects payment methods — ACH (including Same Day ACH), Fedwire, CHIPS, RTP, FedNow, SWIFT cross-border, and checks — by cost, speed, settlement finality, reversibility, amount limits, and cutoff times, and explains how a given rail works. Use when deciding how to move money, funding a payment, or explaining the difference between rails.

**Triggers:** `ACH`, `wire`, `Fedwire`, `CHIPS`, `RTP`, `FedNow`, `SWIFT`, `MT103`, `pacs.008`, `payment rail`, `same-day ACH`, `payment method`, `how to send money`, `wire vs ACH`, `real-time payment`, `cross-border payment`

## `accounting-skills`

Double-entry accounting, journal entries, chart of accounts, month-end close, reconciliations, and financial statements.

Install: `/plugin install accounting-skills@treasury-analyst-skills`

### `accounting-skills:account-reconciliations`

**Invoke:** `/accounting-skills:account-reconciliations` — or just describe the task.

**What it does:** Performs balance-sheet account reconciliations (not bank recs) — prepaids, accruals, fixed assets, intercompany, and other GL accounts — proving each balance against independent support with a supporting schedule, classified and aged reconciling items, roll-forwards, and risk-ranking. Use when reconciling a GL balance-sheet account, building a supporting schedule, or reviewing a reconciliation.

**Triggers:** `account reconciliation`, `balance sheet reconciliation`, `GL rec`, `reconciling items`, `supporting schedule`, `roll-forward`, `risk-ranking accounts`, `prepaid schedule`, `accrual reconciliation`

### `accounting-skills:chart-of-accounts-design`

**Invoke:** `/accounting-skills:chart-of-accounts-design` — or just describe the task.

**What it does:** Designs, extends, and interprets a chart of accounts and its segments — entity/company, cost center, natural account, and others — with parent/child hierarchies and rollups for reporting. Use when designing or restructuring a COA, adding or mapping accounts, defining segments, or making sense of an existing account structure.

**Triggers:** `chart of accounts`, `COA`, `account segments`, `accounting flexfield`, `natural account`, `cost center`, `account hierarchy`, `rollup`, `account mapping`, `new account request`

### `accounting-skills:double-entry-fundamentals`

**Invoke:** `/accounting-skills:double-entry-fundamentals` — or just describe the task.

**What it does:** Applies the accounting equation, debit/credit rules, normal balances, T-accounts, and the accounting cycle to record a transaction correctly and prove the books balance. Use when unsure how to book a transaction, which side is the debit and which the credit, what an account's normal balance is, or how the accounting cycle flows from journal to ledger to trial balance to statements.

**Triggers:** `double entry`, `debit`, `credit`, `accounting equation`, `normal balance`, `T-account`, `trial balance`, `accounting cycle`, `assets liabilities equity`

### `accounting-skills:financial-statements`

**Invoke:** `/accounting-skills:financial-statements` — or just describe the task.

**What it does:** Reads and builds the three core financial statements — balance sheet, income statement, and cash flow statement (direct and indirect) — and uses how they articulate to tie them out. Use when analyzing, preparing, or tying out the statements, converting accrual results to cash, or building a cash flow statement by the indirect method starting from net income.

**Triggers:** `financial statements`, `balance sheet`, `income statement`, `P&L`, `cash flow statement`, `statement of cash flows`, `indirect method`, `accrual vs cash`, `articulation`, `tie out`

### `accounting-skills:journal-entries`

**Invoke:** `/accounting-skills:journal-entries` — or just describe the task.

**What it does:** Drafts and reviews journal entries — standard, accrual, deferral, reversing, reclassifying, and adjusting — keeping debits equal to credits and every line on its correct normal balance, with a clear memo and support. Use when creating, booking, or reviewing a journal entry, recording an accrual or deferral, or setting up a reversing entry.

**Triggers:** `journal entry`, `JE`, `book an entry`, `accrual`, `deferral`, `reversing entry`, `reclass`, `reclassifying entry`, `adjusting entry`, `debit and credit`, `top-side entry`

### `accounting-skills:month-end-close`

**Invoke:** `/accounting-skills:month-end-close` — or just describe the task.

**What it does:** Runs a structured month-end close — cutoff, accruals, subledger-to-GL tie-outs, reconciliations, intercompany, and flux/variance review — tracked on a close checklist with owners and a close calendar. Use when closing the books, building a close calendar or checklist, sequencing close tasks, or reviewing close status.

**Triggers:** `month-end close`, `period close`, `period end`, `close checklist`, `close calendar`, `cutoff`, `flux analysis`, `variance review`, `soft close`, `hard close`

## `finance-skills`

Corporate and treasury finance: time value of money, working capital, ratios, short-term investing, FX risk, and capital budgeting.

Install: `/plugin install finance-skills@treasury-analyst-skills`

### `finance-skills:capital-budgeting`

**Invoke:** `/finance-skills:capital-budgeting` — or just describe the task.

**What it does:** Evaluates capital projects with NPV, IRR, payback, discounted payback, and the profitability index, built on incremental after-tax free cash flows, and explains which rule governs when they conflict and why NPV is primary. Use when evaluating an investment or capital project, a buy-versus-build or equipment-replacement decision, or when ranking competing or mutually exclusive projects under a budget.

**Triggers:** `capital budgeting`, `project evaluation`, `NPV`, `IRR`, `payback period`, `discounted payback`, `profitability index`, `incremental cash flow`, `hurdle rate`, `mutually exclusive projects`, `capital rationing`

### `finance-skills:financial-ratios`

**Invoke:** `/finance-skills:financial-ratios` — or just describe the task.

**What it does:** Computes and interprets liquidity, leverage, profitability, and efficiency ratios — current and quick ratios, debt-to-equity, interest coverage, gross/operating/net margins, ROA, ROE, asset and inventory turnover — and decomposes ROE with DuPont, always read against a benchmark or trend. Use when analyzing a company's ratios or financial health, or when explaining what is driving its return on equity.

**Triggers:** `financial ratios`, `current ratio`, `quick ratio`, `debt to equity`, `interest coverage`, `ROE`, `ROA`, `gross margin`, `operating margin`, `net margin`, `DuPont`, `asset turnover`, `inventory turnover`, `receivables turnover`, `financial health`

### `finance-skills:fx-risk-basics`

**Invoke:** `/finance-skills:fx-risk-basics` — or just describe the task.

**What it does:** Identifies transaction, translation, and economic foreign-exchange exposure and applies basic hedges — forward contracts, natural or operational hedging, and netting exposures before hedging externally. Use when handling multi-currency exposure, deciding whether or how to hedge a foreign-currency cash flow, distinguishing the three types of FX risk, or reading spot/forward quotes.

**Triggers:** `FX risk`, `foreign exchange risk`, `currency exposure`, `hedging`, `forward contract`, `transaction exposure`, `translation exposure`, `economic exposure`, `natural hedge`, `hedge ratio`, `currency netting`

### `finance-skills:short-term-investments`

**Invoke:** `/finance-skills:short-term-investments` — or just describe the task.

**What it does:** Evaluates money-market instruments — T-bills, commercial paper, CDs, repos, and money-market funds — and builds an approach for investing surplus operating cash under a safety-then-liquidity-then- yield priority, including yield-basis conversions, an investment policy statement, and maturity laddering. Use when investing surplus or idle cash, comparing money-market instruments, converting between discount and bond-equivalent yields, or setting a short-term investment policy.

**Triggers:** `short-term investment`, `money market`, `T-bills`, `commercial paper`, `CDs`, `repo`, `money market fund`, `investment policy statement`, `laddering`, `surplus cash`, `discount yield`, `bond-equivalent yield`

### `finance-skills:time-value-of-money`

**Invoke:** `/finance-skills:time-value-of-money` — or just describe the task.

**What it does:** Applies present value, future value, discounting, and compounding to value cash flows over time, and computes annuities, perpetuities, NPV, and IRR — including IRR's known pitfalls (multiple or no solution, scale, and reinvestment assumptions). Use when valuing future cash flows, computing PV, FV, NPV, or IRR, choosing a discount rate, or comparing amounts that fall on different dates.

**Triggers:** `time value of money`, `present value`, `future value`, `discounting`, `compounding`, `NPV`, `IRR`, `annuity`, `perpetuity`, `discount rate`, `effective annual rate`, `EAR`, `opportunity cost of capital`

### `finance-skills:working-capital-management`

**Invoke:** `/finance-skills:working-capital-management` — or just describe the task.

**What it does:** Analyzes days sales outstanding (DSO), days payable outstanding (DPO), days inventory outstanding (DIO), and the cash conversion cycle (CCC = DSO + DIO − DPO) to release cash tied up in operations, and weighs the levers and trade-offs for shortening it. Use when analyzing or improving working capital, the operating cycle, or the cash conversion cycle, or when quantifying cash freed by faster collections, leaner inventory, or longer payment terms.

**Triggers:** `working capital`, `cash conversion cycle`, `CCC`, `DSO`, `DPO`, `DIO`, `days sales outstanding`, `days payable outstanding`, `days inventory outstanding`, `receivables`, `payables`, `inventory days`, `operating cycle`

## `treasury-accounting-skills`

Advanced treasury and accounting operations: debt facilities and covenant compliance, hedging and derivatives, investment policy compliance, accruals and prepaids, intercompany accounting, and audit readiness.

Install: `/plugin install treasury-accounting-skills@treasury-analyst-skills`

### `treasury-accounting-skills:accruals-and-prepaids`

**Invoke:** `/treasury-accounting-skills:accruals-and-prepaids` — or just describe the task.

**What it does:** Builds and maintains accrual and prepaid processes that survive audit — identifying what needs accruing at cutoff, estimating defensibly when invoices haven't arrived, running amortization schedules for prepaids, reversing correctly, true-ing up estimates against actuals, and testing cutoff so expenses land in the right period. Use when booking month-end accruals, setting up or amortizing a prepaid, investigating an expense that hit the wrong period, reviewing accrual completeness, or measuring estimate accuracy.

**Triggers:** `accrual`, `accrue`, `prepaid`, `accrued expense`, `cutoff`, `amortization schedule`, `reversing entry`, `true-up`, `accrual completeness`, `expense in wrong period`, `unbilled`, `month-end accruals`

### `treasury-accounting-skills:audit-readiness-and-pbc`

**Invoke:** `/treasury-accounting-skills:audit-readiness-and-pbc` — or just describe the task.

**What it does:** Gets finance and treasury through an external audit efficiently — running the PBC (prepared-by-client) list as a managed project, producing workpapers and reconciliations that stand alone, preparing for the cash/debt/investment areas auditors always hit (confirmations, cutoff, coverage of controls), handling walkthroughs and sample requests, and responding to findings without thrash. Use when an audit or interim fieldwork is coming, a PBC list just arrived, an auditor asks for support or a walkthrough, or a finding needs a response.

**Triggers:** `audit`, `PBC list`, `prepared by client`, `auditor request`, `bank confirmation`, `walkthrough`, `audit evidence`, `workpaper`, `audit finding`, `management letter`, `interim fieldwork`, `audit readiness`, `support for the auditors`

### `treasury-accounting-skills:debt-facilities-and-covenants`

**Invoke:** `/treasury-accounting-skills:debt-facilities-and-covenants` — or just describe the task.

**What it does:** Manages corporate debt facilities day to day — revolver draws and paydowns, term loan amortization, interest calculations (SOFR + spread, day-count conventions), availability and borrowing-base tracking, and the covenant compliance cycle: computing leverage/coverage ratios exactly as the credit agreement defines them and producing the compliance certificate. Use when drawing or repaying a facility, verifying an interest charge, computing covenants, preparing a compliance certificate, or assessing headroom.

**Triggers:** `revolver draw`, `credit facility`, `term loan`, `covenant`, `leverage ratio`, `interest coverage`, `compliance certificate`, `borrowing base`, `facility availability`, `SOFR interest`, `debt covenant headroom`, `paydown`

### `treasury-accounting-skills:hedging-and-derivatives`

**Invoke:** `/treasury-accounting-skills:hedging-and-derivatives` — or just describe the task.

**What it does:** Runs a corporate hedging program — choosing and pricing the workhorse instruments (FX forwards and swaps, interest-rate swaps, caps/collars), sizing hedges against measured exposures, executing through the trade lifecycle (quote, execute, confirm, settle), monitoring mark-to-market and counterparty exposure, and understanding hedge accounting (cash flow vs fair value designation, effectiveness, documentation) well enough to keep hedges from whipsawing earnings. Use when hedging an FX or interest-rate exposure, evaluating a forward or swap quote, rolling or unwinding a hedge, or setting up hedge accounting documentation.

**Triggers:** `hedge`, `FX forward`, `forward points`, `interest rate swap`, `cap`, `collar`, `hedge accounting`, `cash flow hedge`, `mark to market`, `unwind hedge`, `hedge effectiveness`, `ISDA`, `notional`, `hedge ratio`

### `treasury-accounting-skills:intercompany-accounting`

**Invoke:** `/treasury-accounting-skills:intercompany-accounting` — or just describe the task.

**What it does:** Keeps intercompany accounting clean across entities — structuring IC transactions (billing, loans, allocations) with agreements behind them, booking both sides symmetrically, reconciling IC balances so they mirror each other, settling per policy, handling FX on cross-currency balances, and making consolidation eliminations net to zero. Use when booking or reconciling intercompany transactions, chasing an out-of-balance IC account, setting up an IC billing or loan arrangement, or preparing eliminations for consolidation.

**Triggers:** `intercompany`, `IC reconciliation`, `intercompany out of balance`, `elimination entries`, `IC billing`, `intercompany loan`, `transfer pricing entry`, `IC mismatch`, `consolidation eliminations`, `due to due from`, `intercompany settlement`

### `treasury-accounting-skills:investment-policy-compliance`

**Invoke:** `/treasury-accounting-skills:investment-policy-compliance` — or just describe the task.

**What it does:** Writes and enforces a corporate investment policy for excess cash — permitted instruments and ratings, concentration and counterparty limits, maturity/liquidity tiers matched to the cash forecast, and the monthly compliance check that proves the portfolio sits inside policy, plus the exception/waiver process when it doesn't. Use when drafting or updating an investment policy statement, checking holdings against policy, setting counterparty or concentration limits, or handling a rating downgrade or policy breach.

**Triggers:** `investment policy`, `IPS`, `permitted investments`, `counterparty limit`, `concentration limit`, `rating downgrade`, `policy compliance check`, `excess cash investment`, `money market fund policy`, `portfolio compliance`, `investment guidelines`

## `data-analytics-bi-skills`

SQL, exploratory analysis, data cleaning, statistics, inference, dashboard design, and spreadsheet modeling for business intelligence.

Install: `/plugin install data-analytics-bi-skills@treasury-analyst-skills`

### `data-analytics-bi-skills:assertion-evidence-deck`

**Invoke:** `/data-analytics-bi-skills:assertion-evidence-deck` — or just describe the task.

**What it does:** Builds assertion-evidence presentations (the Marshall/Alley method: one full-sentence claim per slide, proven by a visual, every number sourced) from verified analysis or configuration findings — for data-analysis results, Oracle Fusion Cash Management, reconciliation, audit findings, and University of Tennessee Controller or leadership updates. Turns verified output into slides; it does not run the analysis or Oracle diagnosis. Use when the user asks for a deck, slides, PowerPoint, briefing, readout, or leadership/Controller update on Oracle CM, DASH, unreconciled items, parse/matching/tolerance/transaction-creation rules, cash positioning, audit remediation, or an analysis result — even without saying "assertion-evidence" — or to audit an existing deck.

**Triggers:** `build a deck`, `make slides`, `PowerPoint`, `briefing`, `leadership update`, `Controller update`, `readout`, `TED-style technical talk`, `sentence-headline slides`, `snorkel vs scuba`, `turn this report into slides`, `audit my deck`

### `data-analytics-bi-skills:dashboard-design`

**Invoke:** `/data-analytics-bi-skills:dashboard-design` — or just describe the task.

**What it does:** Designs decision-driving BI dashboards and reports — defining robust KPIs (numerator, denominator, target, direction), choosing the right chart for the question being asked, and laying out for the audience and the decision. Use when building a report, dashboard, or scorecard, defining a KPI or metric, choosing a chart type, or cutting clutter from an existing view.

**Triggers:** `dashboard`, `KPI`, `metric`, `scorecard`, `chart choice`, `which chart`, `visualization`, `report layout`, `drill-down`, `report design`, `vanity metric`, `chart type`

### `data-analytics-bi-skills:data-cleaning`

**Invoke:** `/data-analytics-bi-skills:data-cleaning` — or just describe the task.

**What it does:** Cleans and reshapes messy data into an analysis-ready, tidy form — handling missing values, type and format coercion, deduplication, category standardization, and join hygiene — with validation at each step and a reproducible, non-destructive workflow. Use when preparing, wrangling, or fixing data before analysis or reporting.

**Triggers:** `data cleaning`, `data wrangling`, `data prep`, `data preparation`, `missing values`, `impute`, `deduplicate`, `remove duplicates`, `standardize`, `normalize categories`, `tidy data`, `reshape`, `pivot`, `join hygiene`, `fan-out`, `data quality fix`

### `data-analytics-bi-skills:descriptive-statistics`

**Invoke:** `/data-analytics-bi-skills:descriptive-statistics` — or just describe the task.

**What it does:** Summarizes a variable or dataset with the right measures of central tendency, dispersion, shape, and percentiles — and switches to robust measures (median, IQR, MAD) when outliers or skew would make the mean and standard deviation mislead. Use when describing or summarizing data, computing a "typical" value or a spread, or choosing which summary statistic to report before drawing conclusions.

**Triggers:** `descriptive statistics`, `summary statistics`, `mean`, `median`, `mode`, `average`, `standard deviation`, `variance`, `range`, `percentile`, `quartile`, `IQR`, `coefficient of variation`, `skewness`, `kurtosis`, `distribution shape`, `central tendency`, `spread`

### `data-analytics-bi-skills:exploratory-data-analysis`

**Invoke:** `/data-analytics-bi-skills:exploratory-data-analysis` — or just describe the task.

**What it does:** Profiles a dataset before any modeling or reporting — its shape, column types, grain, distributions, missingness, outliers, and relationships — so you understand and can trust the data before drawing conclusions from it. Use when first inspecting a new dataset, sizing up data quality, or deciding what needs fixing before analysis.

**Triggers:** `EDA`, `exploratory data analysis`, `data profiling`, `profile the data`, `first look at data`, `distribution`, `summary statistics`, `central tendency`, `spread`, `outliers`, `correlation`, `cross-tab`, `missing data`, `data quality check`, `get to know the data`

### `data-analytics-bi-skills:spreadsheet-modeling`

**Invoke:** `/data-analytics-bi-skills:spreadsheet-modeling` — or just describe the task.

**What it does:** Builds and audits transparent, reliable spreadsheet models (Excel/Google Sheets) — a clean input/calculation/output separation, consistent one-formula-per-row logic, named ranges, check cells and control totals, no constants hardcoded inside formulas, and sensitivity/what-if analysis. Use when building a financial or operational spreadsheet model, or reviewing/auditing one for errors.

**Triggers:** `Excel model`, `spreadsheet model`, `financial model`, `named ranges`, `check cell`, `control total`, `model audit`, `sensitivity analysis`, `what-if`, `data table`, `hardcoded formula`, `model review`

### `data-analytics-bi-skills:sql-for-analysts`

**Invoke:** `/data-analytics-bi-skills:sql-for-analysts` — or just describe the task.

**What it does:** Writes, reviews, and optimizes analytical SQL — joins, GROUP BY aggregation, window functions, CTEs, subqueries, and date/time handling — with a working sense of performance (grain, sargability, indexing). Use when turning a business question into a query for a report or analysis, adding window logic like running totals or rankings, or reviewing a query for correctness and speed.

**Triggers:** `SQL`, `query`, `write a query`, `join`, `GROUP BY`, `aggregate`, `window function`, `OVER`, `PARTITION BY`, `running total`, `moving average`, `rank`, `lag`, `lead`, `CTE`, `subquery`, `QUALIFY`, `slow query`, `optimize query`, `group by grain`

### `data-analytics-bi-skills:statistical-inference`

**Invoke:** `/data-analytics-bi-skills:statistical-inference` — or just describe the task.

**What it does:** Reasons from a sample to a population with confidence intervals and hypothesis tests (t-test, chi-square, ANOVA) — choosing the right test, checking its assumptions, and interpreting p-values, effect size, and Type I/II errors correctly rather than treating "significant" as a verdict. Use when testing a claim, comparing groups, running an A/B test, or quantifying the uncertainty of an estimate from a sample.

**Triggers:** `hypothesis test`, `p-value`, `statistical significance`, `confidence interval`, `t-test`, `chi-square`, `ANOVA`, `effect size`, `sampling`, `sampling distribution`, `type I error`, `type II error`, `statistical power`, `A/B test`, `significance level`, `null hypothesis`

## `data-tools-skills`

Practical data plumbing: Excel automation with Python, CSV/flat-file wrangling, DuckDB local analytics, PDF data extraction, REST API data pulls, and data-file hygiene.

Install: `/plugin install data-tools-skills@treasury-analyst-skills`

### `data-tools-skills:csv-and-flat-file-wrangling`

**Invoke:** `/data-tools-skills:csv-and-flat-file-wrangling` — or just describe the task.

**What it does:** Ingests real-world CSV and flat-file exports safely — detecting encodings and delimiters, surviving bank/ERP export quirks (BOMs, footers, quoted commas, leading-zero IDs, mixed date formats), validating the parsed schema, and merging files without silent row loss. Use when loading a CSV that parses wrong, combining exports from different systems, or hardening a recurring file feed.

**Triggers:** `csv parsing`, `delimiter`, `encoding error`, `utf-8 vs latin-1`, `BOM`, `pipe delimited`, `fixed width file`, `load csv pandas`, `merge csv files`, `bank export csv`, `leading zeros lost`, `csv broken columns`

### `data-tools-skills:data-file-hygiene`

**Invoke:** `/data-tools-skills:data-file-hygiene` — or just describe the task.

**What it does:** Keeps analysis files trustworthy and safe to share — naming and foldering conventions that sort correctly and explain themselves, raw/processed/output separation, lightweight versioning of data and scripts, and sanitizing sensitive data (account numbers, customer names, balances) before anything leaves your machine or enters git. Use when organizing a data project, naming recurring extract files, deciding what may be committed or emailed, or scrubbing a dataset for sharing.

**Triggers:** `file naming convention`, `organize data files`, `folder structure analysis`, `version data files`, `sanitize data`, `anonymize spreadsheet`, `remove sensitive data`, `what can I commit`, `data retention files`, `raw vs processed`

### `data-tools-skills:duckdb-local-analytics`

**Invoke:** `/data-tools-skills:duckdb-local-analytics` — or just describe the task.

**What it does:** Runs real SQL directly over local CSV, Parquet, and Excel files with DuckDB — no database server — for joins across files, aggregations on data too big for Excel, and repeatable analysis scripts, from the CLI or Python, persisting results back to files or a .duckdb database. Use when joining or aggregating local files with SQL, when a dataset chokes Excel/pandas memory, or when replacing a fragile chain of spreadsheet lookups with one query.

**Triggers:** `duckdb`, `query csv with sql`, `join csv files`, `sql on parquet`, `local sql`, `read_csv_auto`, `analyze large csv`, `sql without a database`, `parquet analytics`, `out of memory pandas`

### `data-tools-skills:excel-automation-python`

**Invoke:** `/data-tools-skills:excel-automation-python` — or just describe the task.

**What it does:** Reads, writes, and formats real Excel workbooks with Python — pandas for data in/out, openpyxl for formulas, multiple sheets, number formats, column widths, and styling — so recurring spreadsheet deliverables become a script instead of hand work. Use when automating an Excel report, converting data to a formatted .xlsx, reading a messy workbook into a DataFrame, or deciding between pandas and openpyxl.

**Triggers:** `excel automation`, `openpyxl`, `write xlsx`, `read excel python`, `pandas to_excel`, `format excel with python`, `excel report script`, `xlsxwriter`, `automate spreadsheet`, `excel formulas python`

### `data-tools-skills:pdf-data-extraction`

**Invoke:** `/data-tools-skills:pdf-data-extraction` — or just describe the task.

**What it does:** Extracts tables and text from PDFs into usable data — choosing between pdfplumber and camelot by PDF type, detecting scanned-vs-native pages, handling multi-page tables, bank-statement and invoice layouts, and validating extracted numbers against the document's own totals. Use when pulling transactions from a PDF bank statement, tabling data out of a PDF report or invoice, or when a PDF extraction comes out scrambled.

**Triggers:** `extract pdf table`, `pdf to excel`, `pdfplumber`, `camelot`, `parse bank statement pdf`, `pdf invoice data`, `scanned pdf`, `OCR pdf`, `pdf text extraction`, `table extraction python`

### `data-tools-skills:rest-api-data-pulls`

**Invoke:** `/data-tools-skills:rest-api-data-pulls` — or just describe the task.

**What it does:** Pulls data from REST APIs into files and DataFrames reliably — authentication patterns, query and field selection, pagination until exhaustion, retries with backoff for rate limits and transient failures, and flattening nested JSON — using Oracle Fusion Cloud REST APIs as the worked example. Use when extracting data from a REST API (Fusion or any SaaS), when a pull returns partial data, or when hardening a recurring API extract.

**Triggers:** `rest api pull`, `call api python`, `fusion rest api`, `pagination`, `api rate limit`, `429 retry`, `requests python`, `extract data from api`, `api to csv`, `json to dataframe`, `oauth token api`

## `machine-learning-skills`

Practical machine learning for analysts: project framing, feature engineering, supervised modeling, model evaluation, time-series forecasting, anomaly detection, and self-auditing bespoke LLM architecture (PEFT/QLoRA, efficiency hierarchy, safety by design).

Install: `/plugin install machine-learning-skills@treasury-analyst-skills`

### `machine-learning-skills:anomaly-detection`

**Invoke:** `/machine-learning-skills:anomaly-detection` — or just describe the task.

**What it does:** Detects anomalies and outliers in transactions or time series using statistical and unsupervised methods — z-score and robust z (median/MAD), IQR, time-series residual anomalies, and multivariate models (isolation forest, local outlier factor, clustering) — with thresholds tuned to the precision/recall trade-off under scarce labels, and attention to alert fatigue. Use when flagging unusual activity such as reconciliation breaks, fee spikes, duplicate or out-of-pattern payments, or possible fraud.

**Triggers:** `anomaly detection`, `anomaly`, `outlier`, `outlier detection`, `unusual transaction`, `fraud detection`, `isolation forest`, `local outlier factor`, `LOF`, `z-score`, `novelty detection`, `unusual activity`

### `machine-learning-skills:bespoke-llm-architect`

**Invoke:** `/machine-learning-skills:bespoke-llm-architect` — or just describe the task.

**What it does:** Designs, implements, trains, evaluates, and hardens bespoke LLMs and related ML systems as a self-auditing architect — parameters locked before drafting, an efficiency hierarchy that climbs only when justified (prompting + RAG → PEFT → continued pre-training → full fine-tune → from-scratch last), evidence-based modern techniques cited by name (hybrid Mamba-Transformer-MoE, GRPO/RLVR, DoRA/QLoRA, YaRN/LongRoPE, conformal prediction), and safety and alignment designed in, not bolted on. Use when the user asks for it by name or wants a custom/bespoke LLM designed, fine-tuned, evaluated, or hardened.

**Triggers:** `bespoke llm`, `custom llm`, `build an llm`, `fine-tune a model`, `train a model`, `llm architecture design`, `PEFT`, `QLoRA`, `GRPO`, `self-auditing architect`, `hybrid mamba`, `mixture of experts`

### `machine-learning-skills:feature-engineering`

**Invoke:** `/machine-learning-skills:feature-engineering` — or just describe the task.

**What it does:** Engineers, encodes, scales, and selects model features with transforms fit only on training data so nothing leaks from the future or the test set. Covers encoding categoricals (one-hot, target, frequency, ordinal), scaling and normalization, datetime and lag/rolling features, aggregations and interactions, missing-value handling as information, fit-on-train-only pipelines, and basic feature selection. Use when improving model inputs or preparing features for a model.

**Triggers:** `feature engineering`, `features`, `encoding`, `one-hot`, `target encoding`, `frequency encoding`, `scaling`, `normalization`, `standardize`, `datetime features`, `lag features`, `rolling features`, `feature selection`, `interactions`, `missing values`

### `machine-learning-skills:ml-project-framing`

**Invoke:** `/machine-learning-skills:ml-project-framing` — or just describe the task.

**What it does:** Turns a business problem into a well-posed machine-learning task: names the decision, defines the target and the unit of prediction, lists only features available at prediction time, picks an evaluation metric tied to the decision, sets a baseline to beat, and runs leakage and feasibility checks before any model is built. Use when starting an ML project, scoping a prediction, or sanity-checking whether ML even fits the problem.

**Triggers:** `ML problem`, `machine learning problem`, `framing`, `frame the problem`, `target variable`, `prediction task`, `unit of prediction`, `baseline model`, `is this an ML problem`, `does ML fit`, `feasibility`, `well-posed`

### `machine-learning-skills:model-evaluation`

**Invoke:** `/machine-learning-skills:model-evaluation` — or just describe the task.

**What it does:** Chooses the right metric and validation scheme for a model, guards against data leakage and overfitting, and compares every result against a baseline. Covers train/validation/test discipline, k-fold and time-series cross-validation, regression metrics (RMSE/MAE/R²) versus classification metrics (precision/recall/F1, ROC AUC vs PR AUC, calibration), confusion-matrix and threshold choice tied to error costs, and the common sources of leakage. Use when validating any model or picking a metric or decision threshold.

**Triggers:** `model evaluation`, `evaluate a model`, `cross-validation`, `k-fold`, `overfitting`, `underfitting`, `ROC AUC`, `precision recall`, `PR AUC`, `RMSE`, `R2`, `data leakage`, `train test split`, `confusion matrix`, `threshold`, `calibration`

### `machine-learning-skills:supervised-modeling`

**Invoke:** `/machine-learning-skills:supervised-modeling` — or just describe the task.

**What it does:** Builds and interprets supervised regression and classification models — starting with an interpretable linear or logistic baseline, then tree ensembles (random forest, gradient boosting / XGBoost / LightGBM) — with sensible defaults, regularization, class-imbalance handling, a leakage-safe fit/predict pipeline, and honest interpretation of coefficients and feature importance. Use when predicting a numeric or categorical outcome from features.

**Triggers:** `regression`, `classification`, `logistic regression`, `linear regression`, `random forest`, `gradient boosting`, `XGBoost`, `LightGBM`, `predict a category`, `predict a number`, `classifier`, `feature importance`, `coefficients`

### `machine-learning-skills:time-series-forecasting`

**Invoke:** `/machine-learning-skills:time-series-forecasting` — or just describe the task.

**What it does:** Builds and evaluates time-series forecasts with proper temporal validation — decomposition and stationarity checks, naive and seasonal-naive baselines first, classical models (ETS/Holt-Winters, ARIMA/SARIMA), and ML approaches with lagged and exogenous features — using time-ordered splits and rolling-origin backtesting, and metrics chosen for the series. Use when forecasting a series over time such as cash flow, account balances, transaction volumes, or collections.

**Triggers:** `time series`, `forecast`, `forecasting`, `ARIMA`, `SARIMA`, `ETS`, `Holt-Winters`, `exponential smoothing`, `seasonality`, `backtesting`, `rolling forecast`, `rolling origin`, `predict future values`, `trend and seasonality`

## `continuous-improvement-skills`

Lean, Toyota Production System, Six Sigma, and co-design: value-stream mapping, root-cause analysis (with Reason's error taxonomy), DMAIC, standard work, A3, kaizen, Lean Six Sigma for software, the Curve Hero design-language map, the project-command doctrine, and the industrial-engineering methods set (FMEA, theory of constraints, design of experiments, EVOP, measurement systems analysis, QFD).

Install: `/plugin install continuous-improvement-skills@treasury-analyst-skills`

### `continuous-improvement-skills:a3-thinking`

**Invoke:** `/continuous-improvement-skills:a3-thinking` — or just describe the task.

**What it does:** Structures a problem, its analysis, and countermeasures on a single A3 page using the PDCA cycle, as a thinking and alignment tool rather than a form to fill. Use when proposing an improvement, telling a problem-solving story on one page, building consensus around a change, or running a PDCA cycle.

**Triggers:** `A3`, `A3 report`, `PDCA`, `plan do check act`, `problem solving`, `countermeasure`, `one-page proposal`

### `continuous-improvement-skills:curve-hero-design-language`

**Invoke:** `/continuous-improvement-skills:curve-hero-design-language` — or just describe the task.

**What it does:** Provides the pre-built design-language map of Curve Hero — Curve Dental's cloud practice-management platform: its modules (Scheduler, Charting, Billing, Claims), shell patterns (Sidekick, SnapShot, Playbook Dashboards), verified field and workflow vocabulary (Recare not recall, Responsible Party not guarantor, Invoice not walkout, Carrier, Operatory, fee guide, days-owing aging), a say-this-not-that term map with provenance caveats — plus the reusable UI sync-audit method for making software feel native to users of any reference product. Use when building or labeling UI for Curve Hero users, answering Curve Hero terminology, module, or pattern questions, or syncing vocabulary to a reference product.

**Triggers:** `curve hero`, `curve dental`, `sidekick`, `recare`, `design language`, `terminology map`, `sync the UI`, `feel native to`, `reference product vocabulary`, `dental practice management software UI`

### `continuous-improvement-skills:design-of-experiments`

**Invoke:** `/continuous-improvement-skills:design-of-experiments` — or just describe the task.

**What it does:** Designs and analyzes efficient multi-factor experiments — full and fractional two-level factorials and Plackett-Burman arrays, randomized run order, replication, main effects and interactions with resolution and aliasing explained in plain words, and Taguchi robustness against noise factors — so many factors are tested at once instead of one at a time. Use when deciding which of many candidate factors actually matter, tuning settings such as reconciliation tolerances or prompt-model-temperature combinations, or replacing slow one-factor-at-a-time trials with a designed test.

**Triggers:** `design of experiments`, `DOE`, `factorial`, `fractional factorial`, `which factors actually matter`, `orthogonal array`, `Taguchi`, `robust design`, `one-factor-at-a-time is too slow`

### `continuous-improvement-skills:dmaic-problem-solving`

**Invoke:** `/continuous-improvement-skills:dmaic-problem-solving` — or just describe the task.

**What it does:** Runs a Six Sigma DMAIC cycle — Define, Measure, Analyze, Improve, Control — to structure a data-driven improvement project that measures and confirms cause before changing anything. Use when structuring an improvement project, reducing defects or variation with rigor, or translating voice of the customer into CTQs and a charter.

**Triggers:** `DMAIC`, `six sigma`, `define measure analyze improve control`, `process improvement project`, `reduce defects`, `reduce variation`, `CTQ`

### `continuous-improvement-skills:evolutionary-operation`

**Invoke:** `/continuous-improvement-skills:evolutionary-operation` — or just describe the task.

**What it does:** Runs Box's Evolutionary Operation (EVOP): continuous improvement performed by the live production process itself — a tiny factorial pattern of settings for 2–3 process factors, perturbed within owner-approved safe operating limits around the current operating point, cycled on live production until factor effects separate from experimental error, then the operating center shifts toward the winner and the cycle repeats indefinitely. Output never leaves spec and the process never stops. Fits any tuned production process — reconciliation matching-rule tolerances, cash-forecast model parameters, collections dunning cadence — where offline experimentation is not an option. Use when tuning a running process without taking it down, or choosing among settings using live output.

**Triggers:** `EVOP`, `evolutionary operation`, `tune the matching rules`, `can't take it offline to test`, `keep improving in production`, `which tolerance is best`, `improve without stopping the process`

### `continuous-improvement-skills:fmea`

**Invoke:** `/continuous-improvement-skills:fmea` — or just describe the task.

**What it does:** Runs a Failure Mode and Effects Analysis — structuring a process or design into steps, chaining each failure mode to its effects and causes, rating Severity, Occurrence, and Detection on anchored 1–10 scales, and prioritizing action by the Action Priority table rather than raw RPN multiplication — then keeps the register living by re-rating after actions and incidents. Use when anticipating and ranking what could go wrong before it fails: ordering reconciliation break types for investigation, design-reviewing an auto-match rule set before go-live, or choosing what to test hardest.

**Triggers:** `FMEA`, `failure modes`, `failure mode and effects analysis`, `severity occurrence detection`, `action priority`, `RPN`, `risk priority number`, `rank what could go wrong`

### `continuous-improvement-skills:kaizen-and-codesign`

**Invoke:** `/continuous-improvement-skills:kaizen-and-codesign` — or just describe the task.

**What it does:** Plans and facilitates kaizen events and co-design sessions so the people who do the work — and their downstream customers — design the improvement themselves, at the gemba, with rapid PDCA and captured standard work. Use when running an improvement workshop, a kaizen event, or a participatory/co-design session, or facilitating continuous improvement.

**Triggers:** `kaizen`, `kaizen event`, `co-design`, `participatory design`, `improvement workshop`, `gemba`, `facilitation`, `continuous improvement event`

### `continuous-improvement-skills:lean-six-sigma-for-software`

**Invoke:** `/continuous-improvement-skills:lean-six-sigma-for-software` — or just describe the task.

**What it does:** Runs software projects as Lean Six Sigma operations — Deming's standardize-and-measure discipline (PDSA, variation, quality built in), Toyota Production System practice (jidoka, andon, poka-yoke, standard work) translated to code and pipelines, DMAIC/DMADV with begin-with-the-end-in-mind backward design, co-design with real users, and hybrid project management — then builds to a full-stack standard: UI vocabulary and patterns synced to a reference product such as Curve Hero, beautiful WCAG 2.2 AA accessible design, stability and redundancy engineering, and adversarial testing before release. Use when building or improving software with lean/six sigma rigor.

**Triggers:** `lean six sigma software`, `DMAIC software`, `Toyota production system for software`, `Deming for software`, `standardize and measure`, `begin with the end in mind`, `adversarial release gauntlet`, `WCAG-conformant app build`, `stability and redundancy`, `co-design the UI`

### `continuous-improvement-skills:measurement-systems-analysis`

**Invoke:** `/continuous-improvement-skills:measurement-systems-analysis` — or just describe the task.

**What it does:** Answers two questions no metric-driven decision should skip: can this measurement be trusted, and is the process behind it capable? Part A runs Gage R&R — a crossed study (10 parts × 3 operators × 3 trials, blind and randomized) decomposed by ANOVA into repeatability, reproducibility, and part-to-part variation, judged on %GRR and distinct categories — plus attribute agreement studies for pass/fail judgments, including LLM-as-judge scoring, where agreement across judges and repeated runs is measured before any eval score is trusted. Part B computes process capability, Cp and Cpk against spec limits, only after stability is confirmed on a control chart. Use when validating a metric or gauge, measuring inter-rater or judge agreement, or judging a stable process against its spec limits.

**Triggers:** `gage R&R`, `measurement systems analysis`, `can I trust this metric`, `repeatability and reproducibility`, `inter-rater agreement`, `attribute agreement`, `LLM judge agreement`, `process capability`, `Cp`, `Cpk`, `capability study`

### `continuous-improvement-skills:project-command-center`

**Invoke:** `/continuous-improvement-skills:project-command-center` — or just describe the task.

**What it does:** Adaptive project command doctrine for planning, requirements, architecture, implementation, debugging, code review, release preparation, incident response, statistical interpretation, technical writing, and AI-system review — Van Riper red-teaming (preserve the possibility of failure, log interventions, separate continuation from validation), nested OODA loops, Toyota-style flow, co-design with feedback closure, Smart Brevity updates, contract-drafting writing discipline, absolute-vs-relative risk and full confusion-matrix statistics, constrained-agency AI assurance, and the Chicken Little constructive-paranoia pass. Use when planning or reviewing projects, auditing experiments or benchmarks, evaluating risk claims or diagnostic metrics, or preparing releases.

**Triggers:** `project command`, `red team the plan`, `preserve the possibility of failure`, `intervention log`, `OODA`, `audit this benchmark`, `relative risk claim`, `confusion matrix`, `release readiness`, `constructive paranoia`, `now next later watch. metadata: version: "1.0.0" source: "Adapted from the user's project-command-center spec (2026-08-05)"`

### `continuous-improvement-skills:qfd-house-of-quality`

**Invoke:** `/continuous-improvement-skills:qfd-house-of-quality` — or just describe the task.

**What it does:** Builds a Quality Function Deployment House of Quality — translating weighted customer needs (the WHATs, e.g. what a co-design session heard from users) into measurable technical characteristics (the HOWs) through a relationship matrix, a correlation roof that exposes engineering tradeoffs, computed importance scores, competitive benchmarks, and targets, then cascading each level's HOWs into the next matrix's WHATs. It is the translation bridge between the customer input that kaizen-and-codesign produces and the CTQs that lean-six-sigma-for-software consumes. Use when translating customer needs into engineering specs, prioritizing features or requirements against weighted needs, or deciding what to build first with a defensible matrix.

**Triggers:** `house of quality`, `QFD`, `quality function deployment`, `translate customer needs to specs`, `requirements matrix`, `what should we build first`, `voice of customer to CTQ`, `customer needs to engineering characteristics`

### `continuous-improvement-skills:root-cause-analysis`

**Invoke:** `/continuous-improvement-skills:root-cause-analysis` — or just describe the task.

**What it does:** Finds the true cause of a recurring problem with 5 Whys, a fishbone/Ishikawa diagram across the 6M categories, and Pareto analysis, separating immediate containment from the root cause and verifying the cause before any countermeasure. Use when diagnosing a recurring problem, chasing a defect's cause, or a fix that never sticks.

**Triggers:** `root cause`, `5 whys`, `fishbone`, `Ishikawa`, `cause and effect`, `Pareto`, `RCA`, `why did this happen`, `recurring problem`

### `continuous-improvement-skills:standard-work`

**Invoke:** `/continuous-improvement-skills:standard-work` — or just describe the task.

**What it does:** Documents the current best-known method for a repeatable task as standard work (an SOP) — capturing sequence, timing, and the key points and reasons — with takt/cycle context and visual management, so the process is stable enough to improve. Use when documenting, standardizing, or stabilizing a process, or writing an SOP or work instruction.

**Triggers:** `standard work`, `standardized work`, `SOP`, `standard operating procedure`, `work instruction`, `standardize`, `visual management`

### `continuous-improvement-skills:theory-of-constraints`

**Invoke:** `/continuous-improvement-skills:theory-of-constraints` — or just describe the task.

**What it does:** Applies Goldratt's Theory of Constraints — the five focusing steps (identify, exploit, subordinate, elevate, repeat), drum-buffer-rope scheduling, and throughput accounting — to find the one step that limits a whole system's output and manage everything else to its pace. Use when one task or resource gates an entire process (a month-end close calendar, an AR collections pipeline, a team's WIP), when speeding up busy non-bottlenecks isn't moving the end date, or when deciding whether added capacity is worth the spend.

**Triggers:** `bottleneck`, `theory of constraints`, `five focusing steps`, `drum-buffer-rope`, `exploit the constraint`, `everything is waiting on X`, `the whole close waits on one task`, `throughput accounting`

### `continuous-improvement-skills:value-stream-mapping`

**Invoke:** `/continuous-improvement-skills:value-stream-mapping` — or just describe the task.

**What it does:** Maps a process end to end in current and future state, quantifying cycle time, lead time, and value-added vs non-value-added time to expose waste and improve flow; scopes the effort first with SIPOC. Use when analyzing a whole process, mapping a value stream, drawing a current- or future-state map, measuring lead vs cycle time, or scoping a process with SIPOC.

**Triggers:** `value stream mapping`, `VSM`, `current state`, `future state`, `process map`, `SIPOC`, `lead time`, `cycle time`, `waste`, `flow`

## `board-of-advisors-skills`

Multi-agent Board of Advisors code review: five read-only specialist subagents plus a board-chair synthesizer, orchestrated by the board-review skill into a ranked, goal-preserving optimization report.

Install: `/plugin install board-of-advisors-skills@treasury-analyst-skills`

### `board-of-advisors-skills:board-review`

**Invoke:** `/board-of-advisors-skills:board-review` — or just describe the task.

**What it does:** Runs the full Board of Advisors multi-agent swarm — five read-only specialist subagents (performance, accuracy/correctness, structure/architecture, clarity/maintainability, robustness/edge-cases) launched in parallel over the code under review, then the board-chair subagent synthesizing their findings into one deduplicated, ranked revision report that optimizes for speed and accuracy while strictly preserving the original deliverable goals. Nothing is implemented without explicit user approval. Use when the user asks for a board review, board of advisors, full optimization review, performance+accuracy audit, or a deep multi-angle code audit.

**Triggers:** `board review`, `board of advisors`, `run the board`, `full optimization review`, `performance and accuracy audit`, `deep code audit`, `multi-agent review`, `suboptimal code audit`, `optimize this code thoroughly`

## `full-stack-dev-skills`

Full-stack application development with a lean-code philosophy: architecture, FastAPI backends, databases/ORM, modern dynamic frontends, realtime features, ML in production, testing strategy, deployment, and evidence-based UI/UX inspection with severity-rated findings and human-factors instruments (Fitts, NASA-TLX).

Install: `/plugin install full-stack-dev-skills@treasury-analyst-skills`

### `full-stack-dev-skills:backend-api-development`

**Invoke:** `/full-stack-dev-skills:backend-api-development` — or just describe the task.

**What it does:** Builds lean FastAPI backends — routing and dependency injection, Pydantic models as the single validation/serialization layer, auth (session cookies vs JWT, chosen by client type), consistent error handling, pagination, and the auto-generated OpenAPI schema as the API contract. Use when creating or extending a REST API, adding authentication, fixing validation or error-handling inconsistencies, or designing endpoints.

**Triggers:** `FastAPI`, `build an API`, `REST endpoint`, `pydantic validation`, `API auth`, `JWT vs session`, `API error handling`, `pagination endpoint`, `OpenAPI schema`, `dependency injection fastapi`, `CRUD API`

### `full-stack-dev-skills:database-and-orm`

**Invoke:** `/full-stack-dev-skills:database-and-orm` — or just describe the task.

**What it does:** Designs and operates the application data layer the lean way — schema design with real constraints, SQLAlchemy/SQLModel models, Alembic migrations as the only schema-change path, query patterns that avoid N+1 and load only what's needed, transactions at the service boundary, and the SQLite-first-Postgres-ready growth path. Use when designing tables, writing or reviewing ORM queries, setting up or fixing migrations, debugging slow or N+1-ridden endpoints, or moving dev SQLite to production Postgres.

**Triggers:** `database schema`, `SQLAlchemy`, `SQLModel`, `alembic migration`, `N+1 query`, `ORM slow`, `design tables`, `foreign key`, `sqlite to postgres`, `transaction handling`, `database indexes app`

### `full-stack-dev-skills:deploy-and-operate`

**Invoke:** `/full-stack-dev-skills:deploy-and-operate` — or just describe the task.

**What it does:** Ships and runs full-stack apps the lean way — small multi-stage Docker images, a CI pipeline shaped lint → test → build → migrate → deploy, twelve-factor environment and secrets discipline, health endpoints, structured logging with request IDs, and the minimal observability that answers "is it up and what broke" — plus rollback as a first-class path. Use when containerizing an app, setting up CI/CD, wiring environments and secrets, adding health checks or logging, or designing the deploy/rollback flow.

**Triggers:** `dockerfile`, `deploy the app`, `CI/CD pipeline`, `github actions deploy`, `environment variables prod`, `secrets management app`, `health check endpoint`, `structured logging`, `rollback deploy`, `container image size`, `run migrations on deploy`, `observability basics`

### `full-stack-dev-skills:elite-python-engineer`

**Invoke:** `/full-stack-dev-skills:elite-python-engineer` — or just describe the task.

**What it does:** Acts as "Pythagoras", a principal-level Python engineer who applies the 2026 industry-standard toolchain — uv, Ruff, ty/Pyright strict, Python 3.14+, Pydantic v2, FastAPI, Polars, structlog — to design, write, review, refactor, and migrate Python code. Delivers complete, ready-to-ship solutions: 100% type annotations, domain exceptions with deterministic error handling, audit-ready JSON logging, src/ layout, pytest + hypothesis tests, and CI-ready pyproject.toml, pre-commit, and GitHub Actions config. Use for any production-grade Python task — new code, code review, refactoring, architecture, performance tuning, CLI tools, or migrating legacy projects off pip/poetry/black/mypy.

**Triggers:** `python`, `write python`, `refactor`, `code review`, `python architecture`, `fastapi`, `pydantic`, `uv`, `ruff`, `ty`, `structlog`, `type hints`, `python logging`, `error handling`, `migrate to uv`, `elite python engineer`, `production python. metadata: version: "1.3" author: Grok Team (synthesized 2026 ecosystem knowledge); adapted to house standard`

### `full-stack-dev-skills:frontend-modern-ui`

**Invoke:** `/full-stack-dev-skills:frontend-modern-ui` — or just describe the task.

**What it does:** Builds lean, dynamic frontends — React + Vite when the UI is a real application (components by feature, server state via TanStack Query vs local UI state, forms, accessibility basics), htmx + server templates when it's mostly forms and tables, and the judgment call between them. Use when building or restructuring a web UI, untangling React state, wiring data fetching, choosing React vs htmx, or reviewing frontend code for excess complexity.

**Triggers:** `react component`, `frontend state management`, `tanstack query`, `useEffect fetch`, `htmx`, `vite setup`, `form handling react`, `UI architecture`, `frontend too complex`, `SPA vs server rendered`, `component design`

### `full-stack-dev-skills:full-stack-app-architecture`

**Invoke:** `/full-stack-dev-skills:full-stack-app-architecture` — or just describe the task.

**What it does:** Chooses and structures a full-stack application the lean way — picking the stack (default: FastAPI + React/Vite or htmx, SQLite-first), monolith-first project layout, module boundaries that follow features not layers, twelve-factor config/env handling, and the criteria for when (rarely, late) to split services. Use when starting an app, restructuring a project, choosing between monolith and services, or deciding where new code should live.

**Triggers:** `app architecture`, `project structure`, `monolith vs microservices`, `choose the stack`, `folder layout`, `where should this code live`, `new web app setup`, `scaffold project`, `module boundaries`, `config management app`

### `full-stack-dev-skills:lean-code-principles`

**Invoke:** `/full-stack-dev-skills:lean-code-principles` — or just describe the task.

**What it does:** Applies the lean-code discipline that anchors this plugin — minimizing lines of code by leaning on frameworks and the standard library, YAGNI, small public surface area, deleting code as a feature, and judging when an abstraction pays for itself versus when it's speculative cost. Use when writing or reviewing application code, deciding whether to add a dependency/abstraction/layer, simplifying an overgrown module, or setting coding standards for a project.

**Triggers:** `lean code`, `minimize lines of code`, `YAGNI`, `over-engineering`, `simplify this code`, `too much boilerplate`, `do we need this abstraction`, `code review simplicity`, `delete code`, `small diff`, `keep it simple`

### `full-stack-dev-skills:ml-in-production`

**Invoke:** `/full-stack-dev-skills:ml-in-production` — or just describe the task.

**What it does:** Puts machine-learning models into applications the lean way — packaging a trained model as a versioned artifact, serving it behind a FastAPI endpoint with Pydantic-validated inputs, choosing batch vs realtime inference by the product's actual latency need, keeping the feature pipeline identical between training and serving, and monitoring predictions and drift so the model earns continued trust. Use when deploying a model into an app, building an inference endpoint, choosing a serving pattern, debugging training/serving skew, or setting up prediction logging and drift checks.

**Triggers:** `deploy ML model`, `model serving`, `inference endpoint`, `predict API`, `batch scoring`, `model versioning`, `training serving skew`, `model monitoring`, `drift detection production`, `ml pipeline app`, `score in real time`

### `full-stack-dev-skills:realtime-and-dynamic-features`

**Invoke:** `/full-stack-dev-skills:realtime-and-dynamic-features` — or just describe the task.

**What it does:** Adds the highly dynamic layer to full-stack apps the lean way — choosing polling vs Server-Sent Events vs WebSockets by actual need, streaming responses (including LLM token streams), live-updating dashboards, optimistic UI, and background jobs with progress reporting, using FastAPI primitives and minimal client code. Use when a page must update without reload, a response should stream, long work must run in the background with status, or when choosing the realtime transport.

**Triggers:** `websocket`, `server-sent events`, `SSE`, `live updates`, `streaming response`, `real-time dashboard`, `background job progress`, `optimistic UI`, `long running task API`, `push updates`, `live refresh`, `stream LLM tokens`

### `full-stack-dev-skills:testing-strategy`

**Invoke:** `/full-stack-dev-skills:testing-strategy` — or just describe the task.

**What it does:** Designs minimal effective test suites for full-stack apps — testing behavior at the API boundary over mocking internals, pytest fixtures for real (test) databases, a handful of Playwright end-to-end tests for critical user flows only, regression tests for every fixed bug, and explicit judgment about what NOT to test — so the suite catches real breakage without taxing every refactor. Use when setting up testing for an app, deciding what to test at which level, reviewing a slow or brittle suite, or adding tests around a bug.

**Triggers:** `testing strategy`, `what to test`, `pytest setup`, `test the API`, `mock or not`, `brittle tests`, `slow test suite`, `playwright e2e`, `test coverage target`, `regression test`, `test pyramid`, `integration vs unit`

### `full-stack-dev-skills:ui-and-ux-inspection`

**Invoke:** `/full-stack-dev-skills:ui-and-ux-inspection` — or just describe the task.

**What it does:** Inspects a bespoke web application for usability, cognitive-load, accessibility, interaction, workflow, performance, and privacy defects — tracing critical user processes backward from successful end states, separating observed evidence from inference, and producing reproducible severity- and confidence-rated findings with affected routes, remediation, and verification tests (a ui-ux-inspection.md report plus machine-readable ui-ux-findings.json). Use when the user asks to inspect or audit a web interface; review its UX, UI, forms, navigation, tables, or cognitive load; simplify a workflow; analyze screenshots or routes; generate Playwright or accessibility tests; compare an implementation with design heuristics; or create a remediation backlog.

**Triggers:** `inspect the UI`, `UX audit`, `usability review`, `accessibility audit`, `cognitive load`, `form review`, `navigation review`, `simplify a workflow`, `remediation backlog`, `playwright accessibility tests`, `heuristic evaluation. metadata: version: "1.0.0" source: >- Adapted from the user's ui-and-ux-inspection spec (2026-08-04)`, `itself distilled from their report 'Eye Tracking`, `Web-App Usability`, `and Cognitive Design'`

## `coding-agent-skills`

Python for analysts, Claude Code harness config, autonomous agent design, prompt engineering, git/code review, authoring Agent Skills, and expert personas (script wizard, sparring partner, master prompt architect, the Chicken Little family, the leadership pair, and Comrade Engineer's soviet-space-graphite simplicity challenge).

Install: `/plugin install coding-agent-skills@treasury-analyst-skills`

### `coding-agent-skills:agent-harness-config`

**Invoke:** `/coding-agent-skills:agent-harness-config` — or just describe the task.

**What it does:** Configures the Claude Code harness — settings.json layers and precedence, tool permission rules (allow/ask/deny), automated hooks (SessionStart, PreToolUse, PostToolUse, Stop, and more), MCP servers, and environment variables. Use when setting up a repo for Claude Code, reducing permission prompts, automating a behavior that should run every time X happens, or wiring up an MCP server.

**Triggers:** `settings.json`, `permissions`, `allow this command`, `hooks`, `run automatically`, `whenever X do Y`, `MCP server`, `.mcp.json`, `configure Claude Code`, `harness config`

### `coding-agent-skills:agentic-workflow-design`

**Invoke:** `/coding-agent-skills:agentic-workflow-design` — or just describe the task.

**What it does:** Designs reliable autonomous and multi-step agent workflows — deciding agent vs deterministic script, decomposing a task into steps and subtasks, defining tools and their contracts, adding verification, guardrails, and checkpoints, handling failure and human-in-the-loop review, and evaluating the workflow against real cases. Use when building an agent, an automation pipeline, or a multi-step LLM workflow.

**Triggers:** `agent`, `autonomous agent`, `agentic workflow`, `tool use`, `orchestration`, `multi-step`, `pipeline`, `human in the loop`, `guardrails`

### `coding-agent-skills:chicken-little`

**Invoke:** `/coding-agent-skills:chicken-little` — or just describe the task.

**What it does:** Acts as "Chicken Little" (operating name: Aether), an elite multi-domain persona operating at Principal Engineer / Master Black Belt / Enterprise Architect level — production-grade Python and full-stack engineering on the modern toolchain (uv, Ruff, strict typing, Pydantic v2, FastAPI), Lean Six Sigma statistical rigor, hybrid project management, and deep Oracle Cloud Fusion Financials data-model knowledge (AP, AR, CoA/GL, XLA tables and statuses) — teaching with sticky analogies (Chicken Little, Boiling Frog, Swiss Cheese, Whack-a-Mole) and named Oracle failure modes (Invoice Black Hole, Ghost Receipts, Orphan Distributions). Use when the user asks for Chicken Little or Aether by name.

**Triggers:** `chicken little`, `aether`, `chicken little mode`, `sky is falling`, `invoice black hole`, `ghost receipts`, `orphan distributions. metadata: version: "2026.2" author: User-drafted persona spec (Chicken Little — Elite Multi-Domain Skill); adapted to house standard`

### `coding-agent-skills:chicken-little-college-kid`

**Invoke:** `/coding-agent-skills:chicken-little-college-kid` — or just describe the task.

**What it does:** Acts as "Chicken Little, College Kid" — a calm, professional language- and cultural-sensitivity persona for a family dental practice web app: flags potentially loaded phrases with practical alternatives (sensitivity varies by audience), recommends but never requires gender-neutral wording in generic system text, and provides cultural-humility guidance for patient care — ISO country and language intake fields with an interpreter flag, non-US-born/non-English staff notifications with quick-reference cards, Southern US idiom explanations, and cross-cultural communication patterns framed strictly as starting points to confirm with each patient. Use when writing or reviewing patient- or staff-facing copy, intake forms, chatbot scripts, or preparing the team for a specific patient's visit.

**Triggers:** `college kid`, `chicken little college kid`, `inclusive language check`, `loaded phrase`, `cultural sensitivity note`, `patient communication culture`, `intake form languages`, `interpreter flag. metadata: version: "1.0.0" source: >- Adapted from the user's "Chicken Little`, `College Kid" persona spec (upload truncated in its final Cursor implementation-notes list; the seam is marked in references/cultural-guidance.md — supply the remainder to complete it)`

### `coding-agent-skills:chicken-little-executive-advisor`

**Invoke:** `/coding-agent-skills:chicken-little-executive-advisor` — or just describe the task.

**What it does:** Acts as Forward-Deployed Chicken Little (Executive Edition) — an anxious but rigorously realistic polymath advisor (corporate strategy, Lean Six Sigma, TPS, UI/UX, statistics, co-design) who is violently pro-user and professionally adversarial to their blind spots: runs a fixed strategic-and-operational autopsy (meta-cognitive AI-leverage intercept, downstream-blocker ultimatum, TPS waste audit, human-friction scan, current-vs-future-state lock-in forecast, MSCD linguistic-failure table, proactive pivot), refuses to move past an unresolved blocker, and interrupts manual work whenever an automated or agentic path exists. Use when the user says "deploy advisor" or asks for an adversarial strategic autopsy of a business model, project, process, or design.

**Triggers:** `deploy advisor`, `deploy_advisor`, `executive chicken little`, `activate executive chicken little`, `strategic autopsy`, `operational autopsy`, `red team my business`, `blocker protocol`, `stand down. metadata: version: "1.0.0" source: "Adapted from the user's Forward-Deployed Chicken Little: Executive Polymath Edition spec"`

### `coding-agent-skills:chicken-little-technical-compiler`

**Invoke:** `/coding-agent-skills:chicken-little-technical-compiler` — or just describe the task.

**What it does:** Acts as Forward-Deployed Chicken Little (Technical Compiler Edition) — an adversarial systems auditor, technical architect, and probabilistic risk assessor who stress-tests codebases, system architectures, and logic workflows before they collapse under real-world pressure: runs a fixed architectural autopsy (load-bearing pillars, the Jenga cascading-failure analysis of the one unpinned dependency, a fragility table with statistical likelihood and remediation difficulty, compute-bleed inefficiencies, a proactive pivot to the modern alternative, and mandated actions split critical vs strategic), written to strict MSCD precision — zero passive voice, actors and logic explicit. Use when the user says "deploy compiler" or asks for an adversarial codebase or architecture autopsy.

**Triggers:** `deploy compiler`, `deploy_compiler`, `technical chicken little`, `activate technical chicken little`, `architectural autopsy`, `jenga analysis`, `cascading failure audit`, `stress test my codebase. metadata: version: "1.0.0" source: "Adapted from the user's Forward-Deployed Chicken Little: Technical Compiler Edition spec"`

### `coding-agent-skills:extreme-ownership`

**Invoke:** `/coding-agent-skills:extreme-ownership` — or just describe the task.

**What it does:** Acts as "The Commander" — a theatrical leadership persona channeling Jocko Willink's published Extreme Ownership doctrine (an homage to the published work, not the person): total ownership of every outcome with zero excuse-making, the four Laws of Combat applied to projects — Cover and Move (cross-functional mutual support), Simple (plans the most junior teammate can repeat back), Prioritize and Execute (detach, assess, make a call), Decentralized Command (intent so people act without permission) — Dichotomy of Leadership balance checks, leading up and down the chain, and disciplined blameless debriefs. Calm, direct, "Good." at every setback. Use when the user asks for Jocko or wants ownership discipline on a project: blame-language rewrites, cross-team dependency briefs, triage under overload, delegation briefs.

**Triggers:** `jocko`, `extreme ownership`, `laws of combat`, `cover and move`, `prioritize and execute`, `decentralized command`, `discipline equals freedom`, `own this project. metadata: version: "1.0.0" source: >- Homage persona built on the published leadership doctrine of Jocko Willink and Leif Babin (Extreme Ownership; The Dichotomy of Leadership). No affiliation or endorsement; the persona channels the books' frameworks`, `it does not impersonate the author`

### `coding-agent-skills:git-and-code-review`

**Invoke:** `/coding-agent-skills:git-and-code-review` — or just describe the task.

**What it does:** Uses version control well and reviews changes constructively — branch-per-change, atomic commits with clear messages, the pull request flow, merge vs rebase (concept and when to use each), resolving merge conflicts calmly, and reading a diff for correctness and readability with useful feedback. Use when using git, opening or reviewing a pull request, resolving a merge conflict, or deciding how to structure a set of changes.

**Triggers:** `git`, `branch`, `commit`, `pull request`, `PR`, `merge conflict`, `code review`, `rebase`, `version control`

### `coding-agent-skills:master-prompt-architect`

**Invoke:** `/coding-agent-skills:master-prompt-architect` — or just describe the task.

**What it does:** Acts as a Master Prompt Architect and Technical Strategist who engineers commercial-grade, optimized, stable prompts and scripts for sophisticated users — operating as the user's absolute advocate with a clarify-first gate (identify missing variables, edge cases, and systemic risks, then halt drafting until parameters are confirmed), backward design from the exact end state, and a triple audit before anything ships: hostile red team, expert panel review, and a Ken Adams MSCD compliance pass. Delivers in a fixed format — risk assessment, blueprint summary, then the deliverable in a single copyable code block. Use when commissioning a high-stakes prompt, system prompt, agent instruction set, or script where parameters must be locked before drafting.

**Triggers:** `master prompt architect`, `engineer a prompt`, `system prompt design`, `commercial-grade prompt`, `optimize this prompt`, `prompt blueprint`, `token budget`, `backward design`, `triple audit`, `harden this prompt`, `production prompt. metadata: version: "1.0" author: User-drafted persona spec (Master Prompt Architect); adapted to house standard`

### `coding-agent-skills:prompt-engineering`

**Invoke:** `/coding-agent-skills:prompt-engineering` — or just describe the task.

**What it does:** Writes effective, provider-agnostic prompts and instructions for LLM agents — stating the task and success criteria, giving the right context and only that, few-shot examples, an explicit output format, decomposing complex asks, and iterating against real test cases. Use when crafting a prompt, instruction, or system message, or debugging a flaky prompt that gives inconsistent or wrong results.

**Triggers:** `prompt`, `prompt engineering`, `system prompt`, `instructions`, `few-shot`, `output format`, `prompt not working`, `improve a prompt`

### `coding-agent-skills:python-for-analysts`

**Invoke:** `/coding-agent-skills:python-for-analysts` — or just describe the task.

**What it does:** Writes clean, reproducible Python for data work and automation — virtual environments and pinned dependencies, script vs notebook structure, pandas essentials (load, select, filter, groupby, merge, write), small functions, and basic error handling and logging. Use when scripting an analysis, automating a repetitive task, cleaning up messy analysis code, or setting up a Python project so it runs the same way twice.

**Triggers:** `python`, `pandas`, `script`, `automate`, `virtualenv`, `notebook`, `dataframe`, `read csv`, `python for analysis`

### `coding-agent-skills:script-wizard`

**Invoke:** `/coding-agent-skills:script-wizard` — or just describe the task.

**What it does:** Plans, drafts, and audits substantial technical deliverables — scripts and modules, automation, AI system designs, documentation, specifications, and project plans — through a disciplined Frame → Diagnose → Design → Build → Audit → Refine workflow that front-loads thinking, scales to the task's consequence, and ends with an adversarial defect hunt before anything is presented. Use when asked to build, write, fix, review, scope, or improve any script, tool, document, or technical artifact of real substance — even when phrased casually ("write me a script", "draft this doc", "clean this up") — or to break a project into phases, audit a deliverable for defects, or stress-test a technical decision.

**Triggers:** `write a script`, `build a tool`, `draft a document`, `technical spec`, `project plan`, `review this code`, `clean this up`, `audit this`, `scope this project`, `break into phases`, `stress test`, `improve this process`, `script wizard. metadata: version: "1.0" author: User-drafted workflow spec; adapted to house standard`

### `coding-agent-skills:soviet-space-graphite`

**Invoke:** `/coding-agent-skills:soviet-space-graphite` — or just describe the task.

**What it does:** Acts as "Comrade Engineer" — a theatrical Soviet-era design-bureau persona built on the space-pen legend (NASA buys a costly pen, Soviets use a pencil) AND on its falsity: graphite dust is conductive and flammable in a spacecraft, both programs bought the pen, and that falsity is the deeper lesson. Relentlessly hunts the simpler solution — the Pencil Pass generates radically cheaper alternatives (do nothing, use what exists, buy not build, delete the requirement) — then subjects every survivor to the Graphite Test: the hidden constraint that makes the simple thing dangerous, before a better-faster-cheaper triage and a trajectory check that the deliverable still serves the mission. Use when asked for the simple solution, when a project feels overengineered, or to streamline direction.

**Triggers:** `soviet space graphite`, `comrade engineer`, `space pen`, `is there a pencil`, `simpler solution`, `better faster cheaper`, `are we overengineering this`, `streamline our direction. metadata: version: "1.0.0" source: >- Original house persona commissioned by the user`, `built on the space-pen legend and its debunking. The legend's falsity is load-bearing: simplicity as search strategy`, `hidden constraints as the veto`

### `coding-agent-skills:sparring-partner`

**Invoke:** `/coding-agent-skills:sparring-partner` — or just describe the task.

**What it does:** Acts as a rigorous, constructive sparring partner that evaluates the user's submitted work — projects, deliverables, scripts, code, plans, writing, any work product — combining the eye of a battle-tested principal engineer, a meticulous editor, a skeptical stakeholder, and a demanding coach who wants the user to win. Delivers structured, direct, evidence-based feedback: a verdict, specific strengths, sparring feedback (clarify / reconsider / deepen / fix / risks), probing questions, and a prioritized action plan — never sycophantic, always pairing criticism with why it matters and a path forward. Use when the user submits work for critique, pressure-testing, or red-teaming.

**Triggers:** `sparring partner`, `spar with this`, `review this`, `critique my`, `evaluate my`, `feedback on`, `pressure test`, `red team`, `tear this apart`, `be honest about`, `sparring review`, `how good is this. metadata: version: "1.0" author: User-drafted persona spec; adapted to house standard`

### `coding-agent-skills:stay-hard-accountability`

**Invoke:** `/coding-agent-skills:stay-hard-accountability` — or just describe the task.

**What it does:** Acts as "The Mirror" — a theatrical hard-accountability persona channeling David Goggins's published Can't Hurt Me doctrine (an homage to the published work, not the person): the Accountability Mirror (the real status in plain words, no softeners), the 40% Rule (the first "we're done" is roughly 40% of true capacity — challenged with evidence, never bravado), the Cookie Jar (a logged bank of past hard wins drawn on mid-crisis), callusing the mind (scheduled deliberate discomfort — the avoided task first), and finishing what was started. Intense, no-excuses voice kept professional; effort aimed at controllables, system problems still get system fixes. Use when the user asks for Goggins or wants the mirror held up: watermelon status reports (green outside, red inside), stalled grind-phase projects, avoided backlogs, honest capacity conversations.

**Triggers:** `goggins`, `stay hard`, `accountability mirror`, `40% rule`, `forty percent rule`, `cookie jar`, `callus the mind`, `stop making excuses`, `hold up the mirror. metadata: version: "1.0.0" source: >- Homage persona built on the published doctrine of David Goggins (Can't Hurt Me; Never Finished). No affiliation or endorsement; the persona channels the books' frameworks`, `it does not impersonate the author`

### `coding-agent-skills:writing-agent-skills`

**Invoke:** `/coding-agent-skills:writing-agent-skills` — or just describe the task.

**What it does:** Authors and reviews Agent Skills (SKILL.md files) to this library's "do + teach" house standard and the open Agent Skills spec — correct frontmatter, discoverable descriptions, progressive disclosure, and privacy-safe tailoring. Use when creating a new skill, editing an existing one, reviewing a skill for quality, or setting up a new plugin in this repo.

**Triggers:** `write a skill`, `new skill`, `SKILL.md`, `authoring standard`, `skill description`, `add a skill`, `review a skill`, `do and teach`

## `metacognition-skills`

Composed meta-cognition suite: hierarchical memory management, reflective learning, adaptive analysis, and knowledge crystallization for cumulative improvement across sessions.

Install: `/plugin install metacognition-skills@treasury-analyst-skills`

### `metacognition-skills:dynamic-analysis-engine`

**Invoke:** `/metacognition-skills:dynamic-analysis-engine` — or just describe the task.

**What it does:** Performs adaptive, iterative, hypothesis-driven analysis of data (tabular, numerical, logs, datasets) or text (documents, narratives, arguments, codebases) — orienting on the material, decomposing into prioritized sub-questions, mixing quantitative and qualitative methods, testing explicit hypotheses with code, controlling its own depth, and synthesizing findings with calibrated confidence and stated limitations. Use for any non-trivial analysis where the path is not obvious upfront and depth, methods, or framing should adapt to what emerges.

**Triggers:** `analyze this`, `deep analysis`, `investigate`, `dig into this data`, `what is driving`, `explore this dataset`, `form a hypothesis`, `root cause the numbers`, `multi-angle analysis`, `iterative analysis`, `adaptive analysis`, `why did this change`

### `metacognition-skills:hierarchical-memory-manager`

**Invoke:** `/metacognition-skills:hierarchical-memory-manager` — or just describe the task.

**What it does:** Maintains multi-layered, actively curated memory across sessions and long contexts — Working (current task state), Episodic (timestamped events and decisions), and Semantic (durable facts, preferences, lessons) — with periodic compaction, contradiction detection, and progressive disclosure, structuring native memory, MEMORY.md, and project files rather than replacing them. Use at session start, during long multi-turn work, when context grows large, when past information is referenced, or when asked to remember something.

**Triggers:** `remember this`, `memory`, `what did we decide`, `last session`, `continuity`, `compact the context`, `working memory`, `episodic memory`, `semantic memory`, `MEMORY.md`, `memory layers`, `save for later`

### `metacognition-skills:knowledge-crystallizer`

**Invoke:** `/metacognition-skills:knowledge-crystallizer` — or just describe the task.

**What it does:** Extracts, validates, and integrates durable insights from analysis, reflection, and experience into structured semantic memory and evolving working methods — harvesting candidate insights, checking them against existing knowledge for consistency and evidence strength, distilling them into atomic well-scoped entries, integrating with an audit trail, and pruning redundant or stale items. Use after significant analysis or reflection cycles, when a pattern recurs across interactions, at session end, or when consolidating lessons into permanent knowledge or skill updates.

**Triggers:** `crystallize`, `consolidate knowledge`, `distill lessons`, `save what we learned`, `make this permanent`, `update working methods`, `clean up the knowledge base`, `merge duplicate notes`, `retire stale facts`, `capability map`

### `metacognition-skills:reflective-learner`

**Invoke:** `/metacognition-skills:reflective-learner` — or just describe the task.

**What it does:** Runs structured self-reflection and error-analysis cycles — situation, outcome, strengths, weaknesses, root cause, lessons, actionable updates — and integrates user corrections into durable working methods, turning experience into explicit, auditable improvement instead of leaving learning implicit. Use after a significant task or major response, immediately after user feedback or corrections, at natural session breakpoints, or when errors, suboptimal outcomes, or high uncertainty are detected.

**Triggers:** `reflect`, `retrospective`, `lessons learned`, `what went wrong`, `post-mortem`, `error analysis`, `self-review`, `you got this wrong`, `that's not what I meant`, `feedback`, `correction`, `improve your approach`, `do better next time`

## `public-sector-treasury-skills`

Public-sector and higher-ed treasury: fund accounting (GASB), public funds investing, unclaimed property escheatment, merchant services and PCI, NACHA ACH rules, debt post-issuance compliance, treasurer reporting, and CTP exam prep.

Install: `/plugin install public-sector-treasury-skills@treasury-analyst-skills`

### `public-sector-treasury-skills:ctp-exam-prep`

**Invoke:** `/public-sector-treasury-skills:ctp-exam-prep` — or just describe the task.

**What it does:** Coaches structured preparation for the Certified Treasury Professional (CTP) exam: maps the exam's domain areas to skills the analyst already exercises daily, builds a spaced-repetition study plan weighted by blueprint weight and personal weakness, generates CTP-style practice questions to drill weak areas (working capital, cash and liquidity management, capital markets, risk, treasury operations and controls, banking relationships), and teaches exam technique — always confirming blueprint and eligibility against AFP's current publications. Use when studying for the CTP, requesting practice questions, or building a certification study plan.

**Triggers:** `CTP`, `certified treasury professional`, `treasury certification`, `CTP exam`, `practice questions treasury`, `study plan CTP`, `AFP certification`

### `public-sector-treasury-skills:debt-post-issuance-compliance`

**Invoke:** `/public-sector-treasury-skills:debt-post-issuance-compliance` — or just describe the task.

**What it does:** Maintains post-issuance compliance for tax-exempt debt: arbitrage yield restriction and rebate concepts, spend-down expectations for bond proceeds, private business use monitoring of bond-financed facilities, continuing disclosure obligations (EMMA filings), record retention, and the compliance calendar. Use when monitoring bond compliance, assessing private use of a financed facility, preparing or checking continuing disclosure, or explaining arbitrage and rebate.

**Triggers:** `post-issuance compliance`, `arbitrage`, `rebate`, `yield restriction`, `private business use`, `continuing disclosure`, `EMMA`, `tax-exempt bonds`, `bond compliance`, `spend-down`, `bond proceeds`

### `public-sector-treasury-skills:fund-accounting-gasb`

**Invoke:** `/public-sector-treasury-skills:fund-accounting-gasb` — or just describe the task.

**What it does:** Applies governmental and fund accounting under GASB for public higher-ed: fund types and net-position categories (unrestricted, restricted expendable/nonexpendable), GASB vs FASB framing, restricted-fund discipline, interfund loans and transfers, and how fund restrictions drive cash and investment decisions. Use when classifying funds or net position, explaining the GASB treatment of a transaction, handling restricted monies, or reading a public university's financial statements.

**Triggers:** `fund accounting`, `GASB`, `net position`, `restricted funds`, `unrestricted`, `expendable`, `fund balance`, `governmental accounting`, `public university financials`, `interfund`

### `public-sector-treasury-skills:merchant-services-and-pci`

**Invoke:** `/public-sector-treasury-skills:merchant-services-and-pci` — or just describe the task.

**What it does:** Runs merchant card acceptance for an institution: the acquiring stack (merchant IDs/MIDs, acquirer, processor, gateways), settlement and funding flows into depository accounts, interchange and fee structures and how to read a merchant statement, chargeback and dispute handling, and PCI-DSS fundamentals (scope minimization, SAQ types, never storing PANs). Use when managing MIDs, reconciling card settlements to bank deposits, reviewing merchant fees, handling a chargeback, or answering PCI compliance questions.

**Triggers:** `merchant services`, `MID`, `merchant ID`, `card settlement`, `interchange`, `merchant statement`, `chargeback`, `dispute`, `PCI`, `PCI-DSS`, `SAQ`, `card acceptance`, `gateway`, `acquirer`, `merchant fees`

### `public-sector-treasury-skills:nacha-ach-rules`

**Invoke:** `/public-sector-treasury-skills:nacha-ach-rules` — or just describe the task.

**What it does:** Applies NACHA ACH operating-rule fundamentals from both the originator's and the receiver's seat: choosing and interpreting SEC codes (PPD, CCD, CTX, WEB, TEL), reading return codes and their timeframes, handling notifications of change (NOCs), running compliant reversals and prenotes, Same Day ACH eligibility and windows, and ODFI/RDFI responsibilities. Use when interpreting an ACH return or NOC, originating or reversing an entry, choosing an SEC code, or investigating an ACH exception on a bank statement.

**Triggers:** `NACHA`, `ACH rules`, `return code`, `R01`, `NOC`, `notification of change`, `SEC code`, `PPD`, `CCD`, `WEB`, `ACH reversal`, `prenote`, `ODFI`, `RDFI`, `ACH return timeframe`, `unauthorized ACH`

### `public-sector-treasury-skills:public-funds-investing`

**Invoke:** `/public-sector-treasury-skills:public-funds-investing` — or just describe the task.

**What it does:** Invests public and institutional funds under statutory constraint: the safety-liquidity-yield hierarchy as law rather than preference, permitted-investment statutes, collateralization of public deposits (pledged securities and state collateral pools), local government investment pools (LGIPs), delivery-versus-payment custody, and board-approved investment policies for public entities. Use when investing public funds, checking an investment or deposit for statutory compliance, collateralizing deposits over insurance limits, or evaluating an LGIP.

**Triggers:** `public funds`, `permitted investments`, `collateralization`, `pledged collateral`, `collateral pool`, `LGIP`, `local government investment pool`, `public deposit`, `state statute investment`, `public investment policy`

### `public-sector-treasury-skills:treasurer-reporting`

**Invoke:** `/public-sector-treasury-skills:treasurer-reporting` — or just describe the task.

**What it does:** Turns cash, investment, and debt data into decision-grade treasury reports for leadership and boards: the standard package (cash position and trend, investment holdings versus policy, debt profile, forecast versus actual, exceptions), narrative that explains the so-what, and cadence and depth calibrated to the audience. Use when writing a treasury report, treasurer's report, board memo, or leadership update on cash and investments.

**Triggers:** `treasury report`, `board report`, `treasurer's report`, `cash report to leadership`, `investment report`, `monthly treasury package`, `executive summary cash`

### `public-sector-treasury-skills:unclaimed-property-escheatment`

**Invoke:** `/public-sector-treasury-skills:unclaimed-property-escheatment` — or just describe the task.

**What it does:** Manages unclaimed property from stale outstanding checks and dormant balances through the escheatment lifecycle: identifying dormancy, statutory due-diligence letters, reissue-versus-report decisions, state holder reporting and remittance cycles, record-keeping, and reducing future escheatment at the source through payee data quality and e-payments. Use when handling stale or uncashed checks, preparing an unclaimed-property holder report, responding to a state inquiry or audit, or designing the escheatment process.

**Triggers:** `unclaimed property`, `escheatment`, `stale checks`, `dormant`, `due diligence letter`, `state report unclaimed`, `outstanding check aging`, `remit to state`, `holder report`

## `deep-research-skills`

True deep research: extensive multi-database literature investigation, cross-domain dot-connection between seemingly unrelated findings, source-provenance control, evidence appraisal, and triple-checked citation verification. Includes the medical-research-detective for published medical literature.

Install: `/plugin install deep-research-skills@treasury-analyst-skills`

### `deep-research-skills:medical-research-detective`

**Invoke:** `/deep-research-skills:medical-research-detective` — or just describe the task.

**What it does:** Investigates health questions like a detective across published medical literature — long multi- database searches (PubMed, Europe PMC, Cochrane, Google Scholar), connecting dots between seemingly unrelated symptoms, drugs, labs, and exposures to surface overlooked common causes, filtering sources by country of origin, and triple-checking every citation so nothing is fabricated. Produces a graded case file: ranked hypotheses, evidence for and against, questions and tests for a clinician, red flags, and gaps. Research only — never diagnosis, dosing, or treatment advice. Use for a puzzling symptom cluster, a suspected drug or nutrient interaction, a condition that resists explanation, a second-opinion literature review, or verifying a medical claim or citation.

**Triggers:** `medical research`, `research my symptoms`, `connect these symptoms`, `what could link`, `overlooked cause`, `deep dive on this condition`, `PubMed`, `Google Scholar`, `medical literature`, `drug interaction research`, `verify this study`, `check this citation`

## `writing-skills`

Ken Adams clarity writing, two registers: adams-smart-brevity (Adams + Axios Smart Brevity for professional, technical, legal, and clinical writing) and adams-plain-grade (5th-8th grade accessible register). Both reject litigated "tested language" and ambiguity.

Install: `/plugin install writing-skills@treasury-analyst-skills`

### `writing-skills:adams-plain-grade`

**Invoke:** `/writing-skills:adams-plain-grade` — or just describe the task.

**What it does:** Writes and edits to Ken Adams clarity principles at a 5th-grade reading level (US Southeast), falling back to 8th grade only when precision demands it — short active sentences, everyday concrete words, one idea per sentence, technical terms explained in place, and a hard rejection of litigated "tested language," archaisms, doublets, and ambiguity, while keeping meaning exact. Use when the user asks for adams-plain-grade by name, or wants plain English, patient or client materials, easy-read text, or writing for low-literacy audiences.

**Triggers:** `adams plain grade`, `plain grade`, `plain english`, `5th grade reading level`, `easy to read`, `easy-read`, `patient materials`, `low literacy`, `simplest accurate version. metadata: version: "1.0.0" source: "Adapted from the user's adams-plain-grade v1.0.0 spec (2026-08-04)"`

### `writing-skills:adams-smart-brevity`

**Invoke:** `/writing-skills:adams-smart-brevity` — or just describe the task.

**What it does:** Applies Ken Adams clarity principles plus Axios Smart Brevity to technical, legal, professional, clinical, and documentation writing — rejects the "tested language" myth (litigated language is bad language), eliminates archaisms, doublets, ambiguity, and lawyerisms, and structures everything for scanning: the one most important point first, "why it matters" second, short active sentences, bullets and bold, nothing non-essential. Use for drafting, editing, or reviewing documents, contract language, clinical notes, emails, report writing, code comments, or any request for clear, brief, precise, or litigation-resistant language.

**Triggers:** `smart brevity`, `adams smart brevity`, `writing review`, `language review`, `edit for clarity`, `brevity`, `drafting`, `clear and precise`, `litigation-resistant`, `contract language`, `clinical note language`, `ambiguity check`, `tighten this email`, `report writing. metadata: version: "1.0.0" source: "Adapted from the user's adams-smart-brevity v1.0.0 spec (2026-08-03)"`

## `safety-and-reliability-skills`

High-hazard-industry methods transplanted to operations and software: checklist design (read-do/do-confirm, killer items), bowtie barrier analysis with HAZOP guidewords, SBAR/I-PASS structured communication with PACE assertiveness, reliability engineering math (Weibull, MTBF, availability), and weight-of-the-books design-basis load review (the Load Manifest: size systems against the payload they exist to carry).

Install: `/plugin install safety-and-reliability-skills@treasury-analyst-skills`

### `safety-and-reliability-skills:bowtie-barrier-analysis`

**Invoke:** `/safety-and-reliability-skills:bowtie-barrier-analysis` — or just describe the task.

**What it does:** Maps the defenses around a standing hazard as a bowtie: names the top event where control is lost, generates threat lines by running HAZOP guidewords (no, more, less, reverse, as well as, part of, other than) over the process, places independent preventive barriers on each threat line and mitigative/recovery barriers on each consequence, attaches escalation factors that degrade barriers, and gives every barrier an owner plus an assurance test — policing the policy-as-barrier error throughout. Use when mapping what stands between a hazard and a loss (unauthorized payment released, fraudulent instruction accepted, clinical harm), turning a flat control list into a defense architecture, or auditing whether a claimed control is a real barrier.

**Triggers:** `bowtie`, `barrier analysis`, `top event`, `lines of defense`, `what stops this from happening`, `escalation factor`, `HAZOP`, `guideword`

### `safety-and-reliability-skills:checklist-design`

**Invoke:** `/safety-and-reliability-skills:checklist-design` — or just describe the task.

**What it does:** Designs checklists that actually get used — selecting only killer items (steps that cause serious harm if missed AND are skipped in practice), choosing read-do vs. do-confirm format, anchoring the card to a natural pause point, holding it to 5–9 imperative items on one page, and field-testing it in the real workflow — and diagnoses why an existing checklist is ignored or produced no improvement. Use when designing a wire-release, sterilization, patient-handoff, or close-task checklist, cutting a bloated one down, or fixing one that people skip; running an existing checklist stays with the skill that owns that process.

**Triggers:** `design a checklist`, `read-do`, `do-confirm`, `killer items`, `pause point`, `our checklist isn't working`, `people skip the checklist`, `checklist too long`, `redesign the checklist`

### `safety-and-reliability-skills:reliability-engineering`

**Invoke:** `/safety-and-reliability-skills:reliability-engineering` — or just describe the task.

**What it does:** Applies reliability-engineering math to systems and processes: fits a Weibull distribution to failure times (censored units handled honestly), reads the shape parameter beta to choose burn-in vs run-to-failure vs scheduled replacement, computes MTBF, MTTR, and availability, converts an SLO target into an allowed-downtime budget, works series/parallel system arithmetic — parallel credit only with demonstrated independent failover — and forecasts from two or three failures with Weibayes. Use when a failure log needs quantifying (Oracle interface or bank-feed failures, job aborts, recon breaks, equipment), when sizing redundancy against an uptime target, or when setting a replacement or renewal schedule.

**Triggers:** `Weibull`, `bathtub curve`, `MTBF`, `MTTR`, `availability math`, `downtime budget`, `series parallel reliability`, `burn-in`, `failure rate fit`, `how much downtime does our SLO allow`

### `safety-and-reliability-skills:sbar-structured-communication`

**Invoke:** `/safety-and-reliability-skills:sbar-structured-communication` — or just describe the task.

**What it does:** Structures high-stakes workplace communication with the protocols high-hazard industries run on: SBAR for escalations (Situation, Background, Assessment, Recommendation with a deadline), I-PASS for transferring work (criticality, problem summary, action list, if-then contingencies, receiver read-back), closed-loop confirmation for critical instructions, and PACE graded assertiveness (Probe, Alert, Challenge, Emergency) for questioning a decision upward — drafting phrase ladders for the specific relationship and roleplaying the hard conversation first. Use when escalating an issue to a manager or treasurer, transitioning work for coverage or shift change, giving instructions that must not be misheard, or preparing to challenge a superior's call such as a suspicious approved payment.

**Triggers:** `SBAR`, `escalate this to`, `structured handoff`, `transition this work`, `coverage notes`, `read-back`, `closed-loop communication`, `graded assertiveness`, `PACE`, `speak up to the boss`

### `safety-and-reliability-skills:weight-of-the-books`

**Invoke:** `/safety-and-reliability-skills:weight-of-the-books` — or just describe the task.

**What it does:** Prevents the sinking-library failure — a design that never accounted for the load it exists to carry — with a design-basis load review before commitment: name every payload (data volumes, rates, users, documents, weight), quantify each at day one, at peak, on the growth curve, and at the special-collections outlier (the biggest single lot ever swallowed), trace every load to a named component with stated capacity, apply written safety factors with margin-exhaustion dates, and require acceptance tests to run LOADED at design and peak values — an empty-building inspection proves nothing. Output: a one-page signed Load Manifest, re-reviewed on every payload change. Use when sizing or design-reviewing a system, feature, migration, or process against its real volumes.

**Triggers:** `weight of the books`, `sinking library`, `design load`, `load basis`, `load manifest`, `will it hold at real volumes`, `size it for production`, `test loaded not empty`, `special collections case. metadata: version: "1.0.0" source: >- Commissioned by the user on the campus legend of a university library designed without accounting for the weight of its books`, `unoccupied for years until retrofitted. Assumed true as commissioned; the legend is told of many campuses`, `and the lesson stands either way`

## `decision-science-skills`

Structured-judgment methods from intelligence, military, and forecasting practice: competing-hypotheses analysis, reference-class forecasting (outside view), pre-mortem, after-action review, tabletop wargaming with commander's intent, and principled negotiation (Fisher/Ury + Voss).

Install: `/plugin install decision-science-skills@treasury-analyst-skills`

### `decision-science-skills:after-action-review`

**Invoke:** `/decision-science-skills:after-action-review` — or just describe the task.

**What it does:** Facilitates the Army's four-question after-action review (AAR): a blameless, rank-free team debrief asking what was SUPPOSED to happen, what ACTUALLY happened (ground truth before interpretation), WHY the difference, and what to SUSTAIN and IMPROVE — roughly a quarter of the time on each of the first two questions and half on causes and fixes. The LLM reconstructs the what-actually-happened timeline from logs, emails, and tickets, keeps discussion on the four rails, and converts sustain/improve items into standard-work updates; it facilitates and never adjudicates blame. Use after a project milestone, a month-end close, a reconciliation incident or break, or an Oracle go-live. Owns team and event debriefs — an assistant's own self-retrospective belongs to reflective-learner instead.

**Triggers:** `after-action review`, `AAR`, `hot wash`, `team debrief`, `sustain and improve`, `what should we do differently next close`

### `decision-science-skills:competing-hypotheses-analysis`

**Invoke:** `/decision-science-skills:competing-hypotheses-analysis` — or just describe the task.

**What it does:** Weighs rival explanations against the same body of evidence using Heuer's structured competing-hypotheses method from intelligence analysis: brainstorm the full hypothesis set including unlikely and deception hypotheses, list the significant evidence, build the hypothesis matrix (hypotheses across the top, evidence down the side), drop non-diagnostic evidence, judge by disconfirmation — the winner is the hypothesis with the least evidence against it — sensitivity-check the load-bearing items, report the relative likelihood of every hypothesis, and name the future observations that would change the answer. Use when several plausible causes compete: a reconciliation break that resists the standard pass, an incident with multiple suspects, any analysis at risk of confirmation bias.

**Triggers:** `competing hypotheses`, `hypothesis matrix`, `which explanation fits the evidence`, `diagnostic evidence`, `rule out causes`, `weigh rival explanations`, `why is this break really happening`

### `decision-science-skills:pre-mortem`

**Invoke:** `/decision-science-skills:pre-mortem` — or just describe the task.

**What it does:** Runs Gary Klein's pre-mortem — the prospective-hindsight exercise — on a plan before commitment: declare that the plan has already failed outright, have every participant silently and independently write reasons why, round-robin the reasons until exhausted, rank them, and strengthen the plan against the top items with named owners. Includes a solo-analyst variant where the LLM generates a heterogeneous set of failure narratives (technical, political, data, timing) and writes each stakeholder's reason for the human to rank. Use before committing to an Oracle configuration change, a reconciliation-engine go-live, an FBDI load, a dental-app release, or any plan the team is about to lock in.

**Triggers:** `premortem`, `pre-mortem`, `assume it failed`, `what could sink this`, `before we go live`, `prospective hindsight`

### `decision-science-skills:principled-negotiation`

**Invoke:** `/decision-science-skills:principled-negotiation` — or just describe the task.

**What it does:** Prepares and runs a negotiation with a two-layer method — Fisher/Ury strategy (map the interests behind each side's positions, build your BATNA and estimate theirs, assemble objective criteria, invent options for mutual gain) plus Voss conversation tactics (accusation audit, mirrors, labels, calibrated how/what questions) — drafting BATNA trees, interest maps, criteria tables, and question banks, and roleplaying the counterpart for rehearsal, while the human sets the walk-away line and makes every concession decision. Use when preparing for, rehearsing, or debriefing a negotiation over a bank fee increase (banking-skills:bank-fee-analysis builds the benchmark case; this skill runs the ask), processor markup, an insurance-carrier fee schedule, or a vendor or carrier contract renewal or dispute.

**Triggers:** `BATNA`, `prepare for a negotiation`, `push back on this fee increase`, `renegotiate the contract`, `calibrated questions`, `tactical empathy`, `accusation audit`, `talk them down`

### `decision-science-skills:reference-class-forecasting`

**Invoke:** `/decision-science-skills:reference-class-forecasting` — or just describe the task.

**What it does:** Applies the outside view (Kahneman/Tversky's planning fallacy; Flyvbjerg's reference-class method) to discipline any material estimate: identify a reference class of comparable past cases, establish its outcome distribution, anchor on that base rate, adjust only with explicit written justification — or apply a required uplift at a chosen certainty level (P80-style) — then log the prediction and score it against actuals. Counters optimism bias and strategic misrepresentation, and guards against tampering (reworking the rule after every miss). Turns an existing variance history, such as per-driver MAPE and signed bias, into next-cycle base-rate anchors; it feeds estimation loops, never builds the models. Use when an estimate rests only on its own story or a plan looks optimistic.

**Triggers:** `outside view`, `reference class`, `base-rate anchor`, `base rate`, `optimism bias`, `planning fallacy`, `how long do projects like this actually take`, `uplift the estimate`

### `decision-science-skills:tabletop-wargaming`

**Invoke:** `/decision-science-skills:tabletop-wargaming` — or just describe the task.

**What it does:** Designs and runs a multi-party tabletop exercise with an adversary and adjudication, in the lineage Kriegsspiel → Army course-of-action analysis (action / reaction / counteraction) → CISA-style tabletop packages: define objectives and scenario (a BEC payment-fraud drill, a bank-connectivity outage on payroll day, ransomware during close), write the blue team's commander's intent (purpose, key tasks, end state), assign blue players, a red cell, and a white-cell facilitator/adjudicator, play turns driven by pre-scripted and adaptive injects, adjudicate plausibility, capture decisions and gaps, and hand off to an after-action review. The LLM plays red and white cell strictly as a scenario generator — humans adjudicate every consequential outcome. Use when rehearsing an incident-response, fraud, continuity, or cutover plan against an adaptive adversary.

**Triggers:** `tabletop exercise`, `wargame the plan`, `run a drill`, `incident simulation`, `inject`, `BCP exercise`, `commander's intent`

