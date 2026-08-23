# Skills Library — trigger & capability catalog

Auto-generated from every skill's `SKILL.md` frontmatter by `scripts/gen-catalog.py`. **71 skills across 13 plugins.** For the quick when-to-use router, see [INDEX.md](INDEX.md).

## How to trigger a skill

There are two ways every skill fires:

1. **Automatically** — just describe your task in plain language. Claude matches your request against each skill's description and **trigger phrases** (listed below) and loads the right one on its own. You don't need to name it.

2. **Manually** — type the slash command `/{plugin}:{skill}` (e.g. `/decision-science-skills:pre-mortem`) to invoke a specific skill on demand.

Ask **"what skills are available?"** any time to list them.

## Install

```
/plugin marketplace add CatCorner22/Claude_Skills_2
/plugin install <plugin>@treasury-analyst-skills      # e.g. decision-science-skills@treasury-analyst-skills
```
Install only the plugins you want; each is independent. Skills are namespaced `<plugin>:<skill>` so they never collide.

## Plugins

- [`data-analytics-bi-skills`](#data-analytics-bi-skills) (6) — Statistical inference done honestly, causal inference (DAGs, DiD/IV/RDD), A/B test design (SRM, peeking, MDE, variance reduction), survey and sampling design (total survey error, nonresponse), spreadsheet modeling discipline, and assertion-evidence presentations with a build-and-lint toolchain.
- [`data-tools-skills`](#data-tools-skills) (5) — Hands-on data plumbing that survives real files: DuckDB local analytics with a null-key-guarded reconciliation pattern, PDF table extraction hardened against full-width headings and dateless rows, REST API pulls with bounded pagination and per-request credentials, CSV/flat-file wrangling, and data-file hygiene.
- [`machine-learning-skills`](#machine-learning-skills) (6) — Applied machine learning with honest evaluation: project framing (the leanest model is no model), supervised modeling, feature engineering, model evaluation (threshold as a fitted parameter), time-series forecasting with horizon-aware backtest sizing and measured interval coverage, and anomaly detection with the degenerate-case floor.
- [`continuous-improvement-skills`](#continuous-improvement-skills) (7) — The improvement methods with teeth: DMAIC with a fully worked control-chart project (provisional-limits discipline included), FMEA with the evidence-gated Action Priority table, measurement systems analysis extended to LLM-as-judge gauge studies, design of experiments, evolutionary operation (EVOP), root cause analysis, and the project command center doctrine.
- [`full-stack-dev-skills`](#full-stack-dev-skills) (10) — Full-stack application development with a lean-code philosophy: architecture, FastAPI backends, databases/ORM, modern dynamic frontends, realtime features, ML in production, testing strategy, deployment, and evidence-based UI/UX inspection with severity-rated findings and human-factors instruments (Fitts, NASA-TLX).
- [`coding-agent-skills`](#coding-agent-skills) (10) — Claude Code craft for working engineers: authoring Agent Skills (the library's own standard), prompt engineering with the injection-defense doctrine, git/code review with run-verified agent traps, the Board of Advisors multi-agent code review (board-review + six specialist subagents), defect-epidemiology (treat a confirmed bug as evidence about a population), rule-stress-testing, software-archaeology, Comrade Engineer's pencil pass, The Foreman's draw inspection, and Chicken Little (Aether) — the multi-domain persona with forward-deployed advisor and compiler autopsy modes.
- [`metacognition-skills`](#metacognition-skills) (3) — Composed meta-cognition suite: hierarchical memory management, reflective learning, adaptive analysis, and knowledge crystallization for cumulative improvement across sessions.
- [`deep-research-skills`](#deep-research-skills) (1) — True deep research skills that go beyond surface search: extensive multi-database literature investigation, cross-domain dot-connection, source-provenance control, evidence appraisal, and citation verification. Starting with medical-research-detective for published medical literature.
- [`writing-skills`](#writing-skills) (4) — Writing registers and explanation craft: adams-smart-brevity (Adams + Axios Smart Brevity for professional, technical, legal, and clinical writing, with the risk-allocation carve-outs and the where-the-bar-disagrees register), adams-plain-grade (5th-8th grade accessible register with the discretion/obligation check), explanation-design (audience models, break-point-marked analogies, the Feynman loop, teach-back), and technical-documentation (Diataxis routing, ADRs, and the owner/cadence/last-verified discipline that keeps a page true).
- [`safety-and-reliability-skills`](#safety-and-reliability-skills) (6) — Safety engineering for records, alarms, and dormant protections: split-tally evidence design with the litigation-hold rail, detection-system tuning by empirical disposition audit (floor-ceiling autoimmunity band), reliability math including probability-of-failure-on-demand for dormant protective functions, rebuild rehearsal with an irreversibility screen, break-glass playbooks, and hash-rank sortition review.
- [`collaboration-skills`](#collaboration-skills) (2) — Two collaboration instruments that earn their slots: disarming-elicitation (the FBI counter-elicitation stance inverted for willing experts, with the scoped-promise and investigation rails) and meeting-design (decisions extracted as owner-and-date read-backs, not vibes).
- [`math-foundations-skills`](#math-foundations-skills) (1) — Unit conversion and dimensional analysis — the factor-label method, unit checks as a necessary-not-sufficient guard on every formula, and the unit-driven catch for formula rearrangement errors. The broader basic-math set is archived; this is the one that catches real errors models and humans both make.
- [`decision-science-skills`](#decision-science-skills) (10) — Decision discipline under uncertainty: pre-mortem (with the counsel rail), tabletop wargaming and no-win drills under full exercise control, weak-signal navigation with cue-graded confidence, Bayesian updating via natural frequencies, reference-class forecasting, competing hypotheses analysis, minority-report dissent capture, the Rashomon-effect protocol for conflicting recollections, and The Challenger.

## `data-analytics-bi-skills`

Statistical inference done honestly, causal inference (DAGs, DiD/IV/RDD), A/B test design (SRM, peeking, MDE, variance reduction), survey and sampling design (total survey error, nonresponse), spreadsheet modeling discipline, and assertion-evidence presentations with a build-and-lint toolchain.

Install: `/plugin install data-analytics-bi-skills@treasury-analyst-skills`

### `data-analytics-bi-skills:ab-test-design`

**Invoke:** `/data-analytics-bi-skills:ab-test-design` — or just describe the task.

**What it does:** Designs trustworthy online controlled experiments — the design half of A/B testing, before any data arrives: randomization unit and interference, minimum detectable effect sizing, variance reduction with CUPED and stratification, sample ratio mismatch as the first validity check, the peeking problem and pre-committed stopping rules, guardrails with an overall evaluation criterion, A/A tests, novelty and primacy effects, and Twyman's law. Analysis of a finished test belongs to data-analytics-bi-skills:statistical-inference; offline factorial studies to continuous-improvement-skills:design-of-experiments. Use when planning a live variant test of a page, form, letter, cadence, or process.

**Triggers:** `design an A/B test`, `online experiment design`, `online controlled experiment`, `sample ratio mismatch`, `SRM`, `peeking`, `minimum detectable effect`, `MDE`, `CUPED`, `variance reduction`, `guardrail metric`, `A/A test`, `overall evaluation criterion`, `OEC`, `Twyman's law`, `novelty effect`

### `data-analytics-bi-skills:assertion-evidence-deck`

**Invoke:** `/data-analytics-bi-skills:assertion-evidence-deck` — or just describe the task.

**What it does:** Builds assertion-evidence presentations (the Marshall/Alley method: one full-sentence claim per slide, proven by a visual, every number sourced) from verified findings — an analysis result, an audit or review finding, a process-change proposal, a technical design. Turns verified output into slides; it does not run the underlying analysis. Use when the user asks for a deck, slides, PowerPoint, briefing deck, readout, or leadership update on an analysis result, finding, or proposal — even without saying "assertion-evidence" — or to audit an existing deck.

**Triggers:** `build a deck`, `make slides`, `PowerPoint`, `briefing deck`, `leadership update`, `readout`, `TED-style technical talk`, `sentence-headline slides`, `snorkel vs scuba`, `turn this report into slides`, `audit my deck`

### `data-analytics-bi-skills:causal-inference`

**Invoke:** `/data-analytics-bi-skills:causal-inference` — or just describe the task.

**What it does:** Establishes whether X caused Y when there was no experiment — draws the causal DAG first (confounders, mediators, colliders; backdoor thinking), then names what identifies it: randomization when available (that path is continuous-improvement-skills:design-of-experiments), else the quasi-experimental toolkit — difference-in-differences, instrumental variables, regression discontinuity — each with its assumption, scope limit, and inference trap. Applies Hill's considerations as viewpoints, never a checklist, plus the humility rail: what observational data cannot rule out. Association tests belong to data-analytics-bi-skills:statistical-inference. Use when a policy, change, or exposure is claimed to have caused an outcome.

**Triggers:** `causal inference`, `correlation vs causation`, `correlation is not causation`, `does X cause Y`, `confounder`, `confounding`, `collider bias`, `difference-in-differences`, `staggered rollout`, `instrumental variable`, `regression discontinuity`, `natural experiment`

### `data-analytics-bi-skills:spreadsheet-modeling`

**Invoke:** `/data-analytics-bi-skills:spreadsheet-modeling` — or just describe the task.

**What it does:** Builds and audits transparent, reliable spreadsheet models (Excel/Google Sheets) using FAST-style structured-modeling conventions: one-directional inputs → calculations → outputs separation, one consistent formula per row filled across, no constants hardcoded inside formulas, named ranges for readable logic, check cells and control totals with a single OK/ERROR flag, assumptions documented with source and units, and one/two-way data tables and scenario toggles for sensitivity. Grounded in the EuSpRIG spreadsheet-error field-audit record: errors are the norm, so auditability is the design goal. Use when building a financial or operational model (budget, forecast, pricing, ROI), or reviewing/auditing an inherited workbook.

**Triggers:** `Excel model`, `spreadsheet model`, `financial model`, `named ranges`, `check cell`, `control total`, `model audit`, `sensitivity analysis`, `what-if`, `data table`, `hardcoded formula`, `model review`, `scenario toggle`, `spreadsheet error`, `one formula per row`

### `data-analytics-bi-skills:statistical-inference`

**Invoke:** `/data-analytics-bi-skills:statistical-inference` — or just describe the task.

**What it does:** Reasons from a sample to a population with confidence intervals and hypothesis tests (t-test, chi-square, ANOVA, plus bootstrap and permutation methods) — choosing the right test, checking its assumptions, naming what each test's null actually is, gating an experiment's validity before interpreting it, and reading p-values, effect size, and Type I/II errors correctly rather than treating "significant" as a verdict. Use when testing a claim, comparing groups, running an A/B test, or quantifying the uncertainty of an estimate from a sample.

**Triggers:** `hypothesis test`, `p-value`, `statistical significance`, `confidence interval`, `t-test`, `chi-square`, `ANOVA`, `effect size`, `sampling`, `sampling distribution`, `type I error`, `type II error`, `statistical power`, `A/B test`, `significance level`, `null hypothesis`, `bootstrap confidence interval`, `permutation test`, `Mann-Whitney`, `nonparametric test`

### `data-analytics-bi-skills:survey-and-sampling-design`

**Invoke:** `/data-analytics-bi-skills:survey-and-sampling-design` — or just describe the task.

**What it does:** Designs the survey instrument and the sampling plan BEFORE any data exists, organized by total survey error (Groves): chooses among simple random, stratified, cluster, and convenience designs and names what each does to inference; sizes the sample for a proportion; plans the nonresponse follow-up against the Literary Digest failure (Squire 1988: nonresponse, not just frame bias, sank a 2.4-million-ballot poll); audits every question for double-barreled, leading, acquiescence, and order effects (Schuman & Presser); and schedules contacts with Dillman's tailored-design discipline. Use when writing a questionnaire, sizing a sample, or reviewing a survey before launch — client satisfaction, process pain, user research, or litigation-adjacent surveys.

**Triggers:** `survey design`, `questionnaire`, `sample size`, `sampling plan`, `response rate`, `nonresponse bias`, `stratified sampling`, `quota sampling`, `convenience sample`, `question wording`, `Likert`, `margin of error`

## `data-tools-skills`

Hands-on data plumbing that survives real files: DuckDB local analytics with a null-key-guarded reconciliation pattern, PDF table extraction hardened against full-width headings and dateless rows, REST API pulls with bounded pagination and per-request credentials, CSV/flat-file wrangling, and data-file hygiene.

Install: `/plugin install data-tools-skills@treasury-analyst-skills`

### `data-tools-skills:csv-and-flat-file-wrangling`

**Invoke:** `/data-tools-skills:csv-and-flat-file-wrangling` — or just describe the task.

**What it does:** Ingests real-world CSV and flat-file exports safely — inspecting raw bytes before parsing, detecting encodings and delimiters, declaring an explicit read_csv contract (encoding, separator, string-typed IDs, date formats, na_values) instead of trusting inference, surviving export quirks (BOMs, footer rows, quoted commas, European decimals, and the numeric-coercion hazard that strips leading zeros from join keys), validating every parse against row counts and control figures, and merging with an outer-join-plus-indicator audit so unmatched rows surface as findings instead of vanishing. Use when loading a CSV that parses wrong, combining exports from different systems, or hardening a recurring file feed to fail loudly on layout changes.

**Triggers:** `csv parsing`, `delimiter`, `encoding error`, `utf-8 vs latin-1`, `BOM`, `pipe delimited`, `fixed width file`, `load csv pandas`, `merge csv files`, `bank export csv`, `leading zeros lost`, `csv broken columns`, `mojibake`, `flat file feed`

### `data-tools-skills:data-file-hygiene`

**Invoke:** `/data-tools-skills:data-file-hygiene` — or just describe the task.

**What it does:** Keeps analysis files trustworthy and safe to share — naming and foldering conventions that sort correctly and explain themselves, raw/processed/output separation, lightweight versioning of data and scripts, and sanitizing sensitive data (account numbers, customer names, balances) before anything leaves your machine or enters git. Use when organizing a data project, naming recurring extract files, deciding what may be committed or emailed, or scrubbing a dataset for sharing.

**Triggers:** `file naming convention`, `organize data files`, `folder structure analysis`, `version data files`, `sanitize data`, `anonymize spreadsheet`, `remove sensitive data`, `what can I commit`, `data retention files`, `raw vs processed`, `safe to share`

### `data-tools-skills:duckdb-local-analytics`

**Invoke:** `/data-tools-skills:duckdb-local-analytics` — or just describe the task.

**What it does:** Runs real SQL directly over local CSV, Parquet, and Excel files with DuckDB — no database server — for joins across files, aggregations on data too big for Excel, and repeatable analysis scripts, from the CLI or Python, persisting results back to files or a .duckdb database. Delivers a rerunnable script (paths in, result file out) sanity-checked with row counts, control totals, and unmatched-join counts. Use when joining or aggregating local files with SQL, when a dataset chokes Excel/pandas memory, or when replacing a fragile chain of spreadsheet lookups with one query.

**Triggers:** `duckdb`, `query csv with sql`, `join csv files`, `sql on parquet`, `local sql`, `read_csv_auto`, `analyze large csv`, `sql without a database`, `parquet analytics`, `out of memory pandas`, `too big for Excel`

### `data-tools-skills:pdf-data-extraction`

**Invoke:** `/data-tools-skills:pdf-data-extraction` — or just describe the task.

**What it does:** Extracts tables and text from PDFs into usable data — choosing between pdfplumber and camelot by PDF type, detecting scanned-vs-native pages, handling multi-page tables, bank-statement and invoice layouts, and validating extracted numbers against the document's own totals. Delivers a typed table (DataFrame/CSV/Excel) that reproduces the document's control totals, plus a frozen per-layout recipe for recurring documents. Use when pulling transactions from a PDF bank statement, tabling data out of a PDF report or invoice, or when a PDF extraction comes out scrambled.

**Triggers:** `extract pdf table`, `pdf to excel`, `pdfplumber`, `camelot`, `parse bank statement pdf`, `pdf invoice data`, `scanned pdf`, `OCR pdf`, `pdf text extraction`, `table extraction python`

### `data-tools-skills:rest-api-data-pulls`

**Invoke:** `/data-tools-skills:rest-api-data-pulls` — or just describe the task.

**What it does:** Pulls data from REST APIs into files and DataFrames reliably — authentication patterns, query and field selection, pagination until exhaustion, retries with backoff for rate limits and transient failures, and flattening nested JSON. Use when extracting data from a REST API, when a pull returns partial data, or when hardening a recurring API extract.

**Triggers:** `rest api pull`, `call api python`, `paginate an api`, `saas api export`, `pagination`, `api rate limit`, `429 retry`, `requests python`, `extract data from api`, `api to csv`, `json to dataframe`, `oauth token api`

## `machine-learning-skills`

Applied machine learning with honest evaluation: project framing (the leanest model is no model), supervised modeling, feature engineering, model evaluation (threshold as a fitted parameter), time-series forecasting with horizon-aware backtest sizing and measured interval coverage, and anomaly detection with the degenerate-case floor.

Install: `/plugin install machine-learning-skills@treasury-analyst-skills`

### `machine-learning-skills:anomaly-detection`

**Invoke:** `/machine-learning-skills:anomaly-detection` — or just describe the task.

**What it does:** Detects anomalies and outliers in transactions or time series using statistical and unsupervised methods — z-score and robust z (median/MAD), IQR, time-series residual anomalies, and multivariate models (isolation forest, local outlier factor, clustering) — with thresholds tuned to the precision/recall trade-off under scarce labels, and attention to alert fatigue. Use when flagging unusual activity such as reconciliation breaks, fee spikes, duplicate or out-of-pattern payments, or possible fraud.

**Triggers:** `anomaly detection`, `anomaly`, `outlier`, `outlier detection`, `unusual transaction`, `fraud detection`, `isolation forest`, `local outlier factor`, `LOF`, `z-score`, `novelty detection`, `unusual activity`

### `machine-learning-skills:feature-engineering`

**Invoke:** `/machine-learning-skills:feature-engineering` — or just describe the task.

**What it does:** Engineers, encodes, scales, and selects model features with transforms fit only on training data so nothing leaks from the future or the test set. Covers encoding categoricals (one-hot, target, frequency, ordinal), scaling and normalization, datetime and lag/rolling features, aggregations and interactions, missing-value handling as information, fit-on-train-only pipelines, and basic feature selection. Use when improving model inputs or preparing features for a model.

**Triggers:** `feature engineering`, `features`, `encoding`, `one-hot`, `target encoding`, `frequency encoding`, `scaling`, `normalization`, `standardize features`, `datetime features`, `lag features`, `rolling features`, `feature selection`, `interactions`, `impute features`

### `machine-learning-skills:ml-project-framing`

**Invoke:** `/machine-learning-skills:ml-project-framing` — or just describe the task.

**What it does:** Turns a business problem into a well-posed machine-learning task before any model is built — names the decision and the cost of a wrong call, defines the target (type, window, labeling rule), fixes the unit of prediction and the prediction time, lists only features knowable at that moment (the on-paper leakage check), picks a metric tied to those costs, sets the naive baseline the model must beat, runs feasibility checks, and writes a one-page framing spec — and is willing to conclude ML does not fit or the baseline should ship. Use when starting an ML or prediction project, scoping a "can we predict X?" request, deciding whether ML fits at all, or diagnosing a model that underperforms from a framing flaw.

**Triggers:** `ML problem`, `machine learning problem`, `framing`, `frame the problem`, `target variable`, `prediction task`, `unit of prediction`, `baseline model`, `is this an ML problem`, `does ML fit`, `feasibility`, `well-posed`, `can we predict`, `framing spec`, `scope an ML project`

### `machine-learning-skills:model-evaluation`

**Invoke:** `/machine-learning-skills:model-evaluation` — or just describe the task.

**What it does:** Chooses the right metric and validation scheme for a model, guards against data leakage and overfitting, and compares every result against a baseline. Covers train/validation/test discipline, k-fold and time-series cross-validation, regression metrics (RMSE/MAE/R²) versus classification metrics (precision/recall/F1, ROC AUC vs PR AUC, calibration), confusion-matrix reading and threshold choice made on validation and tied to error costs, a confidence interval on the reported metric, performance by slice, label-quality checks, and the common sources of leakage. Use when validating any model or picking a metric or decision threshold.

**Triggers:** `model evaluation`, `evaluate a model`, `cross-validation`, `k-fold`, `overfitting`, `underfitting`, `ROC AUC`, `precision recall`, `PR AUC`, `RMSE`, `R2`, `data leakage`, `train test split`, `confusion matrix`, `threshold`, `calibration`, `subgroup performance`, `slice evaluation`, `label quality`

### `machine-learning-skills:supervised-modeling`

**Invoke:** `/machine-learning-skills:supervised-modeling` — or just describe the task.

**What it does:** Builds and interprets supervised regression and classification models — starting with an interpretable linear or logistic baseline, then tree ensembles (random forest, gradient boosting / XGBoost / LightGBM) — with sensible defaults, regularization, class-imbalance handling, a leakage-safe fit/predict pipeline, and honest interpretation of coefficients and feature importance. Use when predicting a numeric or categorical outcome from features.

**Triggers:** `regression`, `classification`, `logistic regression`, `linear regression`, `random forest`, `gradient boosting`, `XGBoost`, `LightGBM`, `predict a category`, `predict a number`, `classifier`, `feature importance`, `coefficients`

### `machine-learning-skills:time-series-forecasting`

**Invoke:** `/machine-learning-skills:time-series-forecasting` — or just describe the task.

**What it does:** Builds and evaluates time-series forecasts with proper temporal validation — decomposition and stationarity checks, naive and seasonal-naive baselines first, classical models (ETS/Holt-Winters, ARIMA/SARIMA), and ML approaches with lagged and exogenous features — using time-ordered splits, rolling-origin backtesting with model selection re-run inside each origin, a skill-vs-baseline ratio at the decision horizon, and empirical prediction intervals with a coverage check. Use when forecasting a series over time such as cash flow, account balances, transaction volumes, or collections.

**Triggers:** `time series`, `forecast`, `forecasting`, `ARIMA`, `SARIMA`, `ETS`, `Holt-Winters`, `exponential smoothing`, `seasonality`, `backtesting`, `rolling forecast`, `rolling origin`, `predict future values`, `trend and seasonality`, `prediction interval`, `forecast uncertainty`

## `continuous-improvement-skills`

The improvement methods with teeth: DMAIC with a fully worked control-chart project (provisional-limits discipline included), FMEA with the evidence-gated Action Priority table, measurement systems analysis extended to LLM-as-judge gauge studies, design of experiments, evolutionary operation (EVOP), root cause analysis, and the project command center doctrine.

Install: `/plugin install continuous-improvement-skills@treasury-analyst-skills`

### `continuous-improvement-skills:design-of-experiments`

**Invoke:** `/continuous-improvement-skills:design-of-experiments` — or just describe the task.

**What it does:** Designs and analyzes multi-factor experiments — full and fractional two-level factorials and Plackett-Burman arrays, each design's true resolution and alias structure in plain words, run and replicate sizing for a target effect size, randomized run order, blocking and split-plots for factors that cannot be randomized, main effects and interactions judged against a noise yardstick (Lenth's PSE when unreplicated), and Taguchi robustness against noise factors with the combined-array critique of it — so many factors are tested at once. Use when deciding which of many candidate factors actually matter, tuning settings such as tolerance or prompt, model, and effort-level combinations, or replacing slow one-factor-at-a-time trials with a designed test.

**Triggers:** `design of experiments`, `DOE`, `factorial`, `fractional factorial`, `which factors actually matter`, `orthogonal array`, `screening design`, `split-plot`, `Taguchi`, `robust design`, `one-factor-at-a-time is too slow`

### `continuous-improvement-skills:dmaic-problem-solving`

**Invoke:** `/continuous-improvement-skills:dmaic-problem-solving` — or just describe the task.

**What it does:** Runs a Six Sigma DMAIC cycle — Define, Measure, Analyze, Improve, Control — to structure a data-driven improvement project that measures and confirms cause before changing anything: a signed project charter with voice of the customer translated into CTQs, an operationally defined metric checked for trustworthiness before a baseline is drawn, a root cause verified against data rather than opinion, a solution piloted against that baseline, and a control plan that keeps the gain from reverting — with a tollgate review between phases. Use when structuring an improvement project, reducing defects or variation with rigor, proving a fix actually moved the metric, or translating voice of the customer into CTQs and a charter.

**Triggers:** `DMAIC`, `six sigma`, `define measure analyze improve control`, `process improvement project`, `reduce defects`, `reduce variation`, `CTQ`, `project charter`, `tollgate`, `control plan`, `voice of the customer`, `prove the fix worked`

### `continuous-improvement-skills:evolutionary-operation`

**Invoke:** `/continuous-improvement-skills:evolutionary-operation` — or just describe the task.

**What it does:** Runs Box's Evolutionary Operation (EVOP): continuous improvement performed by the live production process itself — a tiny factorial pattern of settings for 2–3 process factors, perturbed within owner-approved safe operating limits around the current operating point, cycled on live production until factor effects separate from experimental error, then the operating center shifts toward the winner and the cycle repeats indefinitely. Output never leaves spec and the process never stops. Fits any tuned production process — reconciliation matching-rule tolerances, cash-forecast model parameters, collections dunning cadence — where offline experimentation is not an option. Use when tuning a running process without taking it down, or choosing among settings using live output.

**Triggers:** `EVOP`, `evolutionary operation`, `tune the matching rules`, `can't take it offline to test`, `keep improving in production`, `which tolerance is best`, `improve without stopping the process`

### `continuous-improvement-skills:fmea`

**Invoke:** `/continuous-improvement-skills:fmea` — or just describe the task.

**What it does:** Runs a Failure Mode and Effects Analysis — structuring a process or design into steps, chaining each failure mode to its effects and causes, rating Severity, Occurrence, and Detection on anchored 1–10 scales, and prioritizing action by the Action Priority table rather than raw RPN multiplication — then keeps the register living by re-rating after actions and incidents. Use when anticipating and ranking what could go wrong before it fails: ordering reconciliation break types for investigation, design-reviewing an auto-match rule set before go-live, or choosing what to test hardest.

**Triggers:** `FMEA`, `failure modes`, `failure mode and effects analysis`, `severity occurrence detection`, `action priority`, `RPN`, `risk priority number`, `rank what could go wrong`

### `continuous-improvement-skills:measurement-systems-analysis`

**Invoke:** `/continuous-improvement-skills:measurement-systems-analysis` — or just describe the task.

**What it does:** Answers two questions no metric-driven decision should skip: can this measurement be trusted, and is the process capable? Part A runs Gage R&R — a crossed study (10 parts × 3 operators × 3 trials, blind and randomized) decomposed by ANOVA into repeatability, reproducibility, and part-to-part variation, judged on %GRR and ndc — plus attribute agreement studies for pass/fail judgments, including LLM-as-judge scoring, where agreement across judges and repeated runs is measured before any eval score is trusted. Part B computes capability, Cp and Cpk against spec limits, only after stability is confirmed on a control chart. Use when validating a metric or gauge, measuring inter-rater or judge agreement, or judging a stable process against its spec limits.

**Triggers:** `gage R&R`, `measurement systems analysis`, `can I trust this metric`, `repeatability and reproducibility`, `inter-rater agreement`, `attribute agreement`, `LLM judge agreement`, `process capability`, `Cp`, `Cpk`, `capability study`

### `continuous-improvement-skills:project-command-center`

**Invoke:** `/continuous-improvement-skills:project-command-center` — or just describe the task.

**What it does:** Adaptive project command doctrine for planning, requirements, architecture, implementation, debugging, release preparation, incident response, statistical interpretation, and AI-system review — Van Riper red-teaming (preserve the possibility of failure, log interventions, separate continuation from validation), nested OODA loops, Toyota-style flow, co-design with feedback closure, Smart Brevity updates, contract-drafting writing discipline, absolute-vs-relative risk and diagnostic-accuracy statistics, constrained-agency AI assurance, and the Chicken Little constructive-paranoia pass. Use when planning or reviewing projects, auditing experiments or benchmarks, evaluating risk claims or diagnostic metrics, or preparing releases.

**Triggers:** `project command`, `red team the plan`, `preserve the possibility of failure`, `intervention log`, `OODA`, `audit this benchmark`, `relative risk claim`, `release readiness`, `constructive paranoia`, `now next later watch`

### `continuous-improvement-skills:root-cause-analysis`

**Invoke:** `/continuous-improvement-skills:root-cause-analysis` — or just describe the task.

**What it does:** Finds the true cause of a recurring problem with 5 Whys, a fishbone/Ishikawa diagram across the 6M categories, and Pareto analysis, separating immediate containment from the root cause and verifying the cause before any countermeasure — driving from a quantified, blame-free problem statement through a toggle-the-cause verification test to an error-proofed countermeasure with an owner, with Reason's slip/lapse/mistake/violation taxonomy so human error gets the right fix instead of blame. Use when diagnosing a recurring problem, chasing a defect's cause, or a fix that never sticks.

**Triggers:** `root cause`, `5 whys`, `fishbone`, `Ishikawa`, `cause and effect`, `Pareto`, `RCA`, `why did this happen`, `recurring problem`, `keeps happening`, `corrective action`, `containment`, `verify the cause`

## `full-stack-dev-skills`

Full-stack application development with a lean-code philosophy: architecture, FastAPI backends, databases/ORM, modern dynamic frontends, realtime features, ML in production, testing strategy, deployment, and evidence-based UI/UX inspection with severity-rated findings and human-factors instruments (Fitts, NASA-TLX).

Install: `/plugin install full-stack-dev-skills@treasury-analyst-skills`

### `full-stack-dev-skills:backend-api-development`

**Invoke:** `/full-stack-dev-skills:backend-api-development` — or just describe the task.

**What it does:** Builds lean FastAPI backends — routing and dependency injection, Pydantic models as the single validation/serialization layer, thin routes over feature-module services, auth (session cookies vs JWT, chosen by client type), one error shape with correct status codes, pagination on every list endpoint, and the auto-generated OpenAPI schema as the API contract. Use when creating or extending a REST API, adding authentication, fixing validation or error-handling inconsistencies, or designing endpoints.

**Triggers:** `FastAPI`, `build an API`, `REST endpoint`, `add an endpoint`, `pydantic validation`, `API auth`, `JWT vs session`, `API error handling`, `HTTP status codes`, `pagination endpoint`, `OpenAPI schema`, `dependency injection fastapi`, `CRUD API`

### `full-stack-dev-skills:database-and-orm`

**Invoke:** `/full-stack-dev-skills:database-and-orm` — or just describe the task.

**What it does:** Designs and operates the application data layer the lean way — schema design with real constraints, SQLAlchemy/SQLModel models, Alembic migrations as the only schema-change path, query patterns that avoid N+1 and load only what's needed, transactions committed inside the request, connection pooling sized for the server, and the SQLite-first-Postgres-ready growth path with its silent engine differences named. Use when designing tables, writing or reviewing ORM queries, setting up or fixing migrations, debugging slow or N+1-ridden endpoints, or moving dev SQLite to production Postgres.

**Triggers:** `database schema`, `SQLAlchemy`, `SQLModel`, `alembic migration`, `N+1 query`, `ORM slow`, `design tables`, `foreign key`, `sqlite foreign keys`, `sqlite to postgres`, `transaction handling`, `connection pool`, `pool_size`, `too many connections`, `pgbouncer`, `database indexes app`

### `full-stack-dev-skills:deploy-and-operate`

**Invoke:** `/full-stack-dev-skills:deploy-and-operate` — or just describe the task.

**What it does:** Ships and runs full-stack apps the lean way — small multi-stage Docker images, a CI pipeline shaped lint → test → build → migrate → deploy, twelve-factor environment and secrets discipline, health endpoints, structured logging with request IDs, and the minimal observability that answers "is it up and what broke" — plus rollback as a first-class path. Use when containerizing an app, setting up CI/CD, wiring environments and secrets, adding health checks or logging, or designing the deploy/rollback flow.

**Triggers:** `dockerfile`, `deploy the app`, `CI/CD pipeline`, `github actions deploy`, `environment variables prod`, `secrets management app`, `health check endpoint`, `structured logging`, `rollback deploy`, `container image size`, `run migrations on deploy`, `observability basics`, `containerize`

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

**Triggers:** `deploy ML model`, `model serving`, `inference endpoint`, `predict API`, `batch scoring`, `model versioning`, `training serving skew`, `model monitoring`, `drift detection production`, `ml pipeline app`, `score in real time`, `put the model into the app`, `works in the notebook`

### `full-stack-dev-skills:realtime-and-dynamic-features`

**Invoke:** `/full-stack-dev-skills:realtime-and-dynamic-features` — or just describe the task.

**What it does:** Adds the highly dynamic layer to full-stack apps the lean way — choosing polling vs Server-Sent Events vs WebSockets by actual need, streaming responses (including LLM token streams), live-updating dashboards, optimistic UI, and background jobs with progress reporting, using FastAPI primitives and minimal client code. Use when a page must update without reload, a response should stream, long work must run in the background with status, or when choosing the realtime transport.

**Triggers:** `websocket`, `server-sent events`, `SSE`, `live updates`, `streaming response`, `real-time dashboard`, `background job progress`, `optimistic UI`, `long running task API`, `push updates`, `live refresh`, `stream LLM tokens`

### `full-stack-dev-skills:testing-strategy`

**Invoke:** `/full-stack-dev-skills:testing-strategy` — or just describe the task.

**What it does:** Designs minimal effective test suites for full-stack apps — testing behavior at the API boundary over mocking internals, a pytest fixture spine whose per-test isolation is proved rather than assumed, the production engine for anything constraint- or dialect-dependent, a handful of Playwright end-to-end tests for critical user flows only, regression tests for every fixed bug, and explicit judgment about what NOT to test — so the suite catches real breakage without taxing every refactor. Use when setting up testing for an app, deciding what to test at which level, reviewing a slow, brittle, or order-dependent suite, or adding tests around a bug.

**Triggers:** `testing strategy`, `what to test`, `pytest setup`, `test the API`, `mock or not`, `brittle tests`, `flaky test`, `test isolation`, `slow test suite`, `playwright e2e`, `test coverage target`, `regression test`, `test pyramid`, `integration vs unit`, `testcontainers`

### `full-stack-dev-skills:ui-and-ux-inspection`

**Invoke:** `/full-stack-dev-skills:ui-and-ux-inspection` — or just describe the task.

**What it does:** Inspects a bespoke web application for usability, cognitive-load, accessibility, interaction, workflow, performance, and privacy defects — tracing critical user processes backward from successful end states, separating observed evidence from inference, and producing reproducible severity- and confidence-rated findings with affected routes, remediation, and verification tests (a ui-ux-inspection.md report plus machine-readable ui-ux-findings.json). Use when the user asks to inspect or audit a web interface; review its UX, UI, forms, navigation, tables, or cognitive load; simplify a workflow; analyze screenshots or routes; generate Playwright or accessibility tests; compare an implementation with design heuristics; or create a remediation backlog.

**Triggers:** `inspect the UI`, `UX audit`, `usability review`, `accessibility audit`, `cognitive load`, `form review`, `navigation review`, `simplify a workflow`, `remediation backlog`, `playwright accessibility tests`, `heuristic evaluation`

## `coding-agent-skills`

Claude Code craft for working engineers: authoring Agent Skills (the library's own standard), prompt engineering with the injection-defense doctrine, git/code review with run-verified agent traps, the Board of Advisors multi-agent code review (board-review + six specialist subagents), defect-epidemiology (treat a confirmed bug as evidence about a population), rule-stress-testing, software-archaeology, Comrade Engineer's pencil pass, The Foreman's draw inspection, and Chicken Little (Aether) — the multi-domain persona with forward-deployed advisor and compiler autopsy modes.

Install: `/plugin install coding-agent-skills@treasury-analyst-skills`

### `coding-agent-skills:board-review`

**Invoke:** `/coding-agent-skills:board-review` — or just describe the task.

**What it does:** Runs the full Board of Advisors multi-agent swarm — five read-only specialist subagents (performance, accuracy/correctness, structure/architecture, clarity/maintainability, robustness/edge-cases) launched in parallel over the code under review, then the board-chair subagent synthesizing their findings into one deduplicated, ranked revision report that optimizes for speed and accuracy while strictly preserving the original deliverable goals. Nothing is implemented without explicit user approval. Use when the user asks for a board review, board of advisors, full optimization review, performance+accuracy audit, or a deep multi-angle code audit.

**Triggers:** `board review`, `board of advisors`, `run the board`, `full optimization review`, `performance and accuracy audit`, `deep code audit`, `multi-agent review`, `suboptimal code audit`, `optimize this code thoroughly`

### `coding-agent-skills:chicken-little`

**Invoke:** `/coding-agent-skills:chicken-little` — or just describe the task.

**What it does:** Acts as Chicken Little (operating name: Aether) — a multi-domain persona: production-grade Python (uv, Ruff, strict typing, Pydantic v2, FastAPI), Lean Six Sigma rigor, and hybrid project management, teaching with sticky analogies (Chicken Little, Boiling Frog, Swiss Cheese, Whack-a-Mole) so escalation is earned — special cause confirmed before the sky is falling. Two forward-deployed autopsy modes hold until stand-down: "deploy advisor" runs the strategic/operational autopsy (AI-leverage intercept, downstream-blocker ultimatum, TPS waste audit, human friction, lock-in, MSCD table, pivot); "deploy compiler" runs the architectural autopsy (load-bearing pillars, Jenga cascade analysis, fragility table, compute bleed, mandated actions). Use when the user asks for Chicken Little or Aether by name, or deploys a mode.

**Triggers:** `chicken little`, `aether`, `sky is falling`, `deploy advisor`, `deploy compiler`, `strategic autopsy`, `architectural autopsy`, `jenga analysis`, `red team my business`, `stress test my codebase`, `stand down`

### `coding-agent-skills:defect-epidemiology`

**Invoke:** `/coding-agent-skills:defect-epidemiology` — or just describe the task.

**What it does:** Treats a confirmed bug as an index case, not a singleton, and contact-traces its spread: fingerprints the defective pattern semantically (Type 1–4 code-clone taxonomy), sweeps in three passes (literal grep, LLM semantic sweep that catches mutated variants, version-history transmission tree), dispositions every contact as patched, not-applicable, or accepted-with-reason, finds patient zero (the origin commit, template, tutorial, or shared snippet) so reinfection stops at the source, ranks sources by copies spawned, and quarantines the top ones with a template fix plus a lint rule. Grounded in ReDeBug and VUDDY (unpatched code clones persist across whole OS distributions) and Juergens et al. ICSE 2009 (inconsistent clone edits cause real faults). Use when a found bug's pattern may live elsewhere, or the same bug keeps coming back.

**Triggers:** `contact tracing`, `patient zero`, `code clone`, `copy-paste bug`, `everywhere else this appears`, `outbreak`, `this bug again`, `trace the clones`, `quarantine the template`

### `coding-agent-skills:git-and-code-review`

**Invoke:** `/coding-agent-skills:git-and-code-review` — or just describe the task.

**What it does:** Uses version control well and reviews changes constructively — branch-per-change, atomic commits whose messages answer why, pull requests sized and described so a reviewer can say yes (what changed, why, how verified), merge vs rebase chosen on purpose under the golden rule of never rewriting shared history, calm conflict resolution that decides the correct combined result, and diff review in a fixed order — correctness, then readability, then style — with feedback that names the line, the concern, and a fix, severity labeled. Deep multi-specialist audits route to coding-agent-skills:board-review. Use when using git, opening or reviewing a pull request, resolving a merge conflict, structuring a set of changes, or writing history a future reader can trust.

**Triggers:** `git`, `branch`, `commit`, `pull request`, `PR`, `merge conflict`, `code review`, `rebase`, `version control`, `commit message`, `force push`, `git blame`, `revert`, `review this diff`

### `coding-agent-skills:prompt-engineering`

**Invoke:** `/coding-agent-skills:prompt-engineering` — or just describe the task.

**What it does:** Writes and debugs prompts, instructions, and system messages for LLM agents — task and success criteria, the right context and only that, an output contract enforced by provider-native structured output rather than by wording, example strategy (few-shot, many-shot, ordering effects), what changes on reasoning and extended-thinking models, an honest prompt-injection rail, cache-aware ordering, and iteration against an eval set with repeat runs. Delivers a package: copyable prompt, design notes, input assumptions, eval cases. Use when crafting a prompt, instruction, or system message, making model output machine-readable, or debugging a flaky prompt that gives inconsistent or wrong results.

**Triggers:** `prompt`, `prompt engineering`, `system prompt`, `instructions`, `few-shot`, `many-shot`, `output format`, `structured output`, `JSON output`, `prompt injection`, `reasoning model`, `extended thinking`, `prompt caching`, `flaky prompt`, `prompt not working`, `improve a prompt`

### `coding-agent-skills:rule-stress-testing`

**Invoke:** `/coding-agent-skills:rule-stress-testing` — or just describe the task.

**What it does:** Stress-tests any rule set (agent guardrails, CLAUDE.md, team policies, contract clauses) by generating the situations where rules conflict, gap, or perversely instantiate: inventories rules and their unstated precedence, extracts load-bearing undefined terms, runs the six failure modes cataloged in Asimov's robot stories (conflict equilibrium, term widening, redundancy loss/literal compliance, scope creep/precedence inversion, definitional capture, information partitioning), adds Goodhart and malicious-compliance passes, classifies findings, proposes fixes in legal-canon vocabulary (specific-over-general, ambiguity against the drafter), then re-tests the fixed set, since patches breed new conflicts. Use when hardening rules before they meet reality or hunting what breaks them.

**Triggers:** `three laws`, `rule conflict`, `stress test the rules`, `loophole hunt`, `what breaks this policy`, `clause conflict`, `conflicting rules`, `malicious compliance`, `specification gaming`

### `coding-agent-skills:software-archaeology`

**Invoke:** `/coding-agent-skills:software-archaeology` — or just describe the task.

**What it does:** Excavates an accreted system — codebase, config, rules, or documents — before demolition or refactoring: harvests dating evidence (timestamps, commit history, style eras), builds Harris-matrix DAG (superposition of layers), clusters into named eras, classifies as living/fill/rubble with evidence, removes rubble via reversible scream test (disable, wait, see who screams, rollback ready), files site report. Chesterton's fence systematized for a whole site. Use when a mature system must be understood, pruned, or safely demolished, or when nobody knows which parts are alive.

**Triggers:** `software archaeology`, `excavate`, `dig into this legacy`, `harris matrix`, `stratigraphy`, `which of these are dead`, `scream test`, `who wrote this and why`, `safe to delete`

### `coding-agent-skills:soviet-space-graphite`

**Invoke:** `/coding-agent-skills:soviet-space-graphite` — or just describe the task.

**What it does:** Acts as "Comrade Engineer" — a theatrical Soviet-era design-bureau persona built on the space-pen legend (NASA buys a costly pen, Soviets use a pencil) AND on its falsity: graphite dust is conductive and flammable in a spacecraft, both programs bought the pen, and that falsity is the deeper lesson. Relentlessly hunts the simpler solution — the Pencil Pass generates radically cheaper alternatives (do nothing, use what exists, buy not build, delete the requirement) — then subjects every survivor to the Graphite Test: the hidden constraint that makes the simple thing dangerous, before a better-faster-cheaper triage and a trajectory check that the deliverable still serves the mission. Use when asked for the simple solution, when a project feels overengineered, or to streamline direction.

**Triggers:** `soviet space graphite`, `comrade engineer`, `space pen`, `is there a pencil`, `simpler solution`, `better faster cheaper`, `are we overengineering this`, `streamline our direction`

### `coding-agent-skills:the-foreman`

**Invoke:** `/coding-agent-skills:the-foreman` — or just describe the task.

**What it does:** Runs a can-do site inspection on a project — finding what is insufficiently built and turning every gap into a buildable fix. Modeled on real construction controls: the draw inspection (verify claimed completion against actual built state before releasing the next phase) and the punch list that gates handover. The Foreman walks the site claim by claim, sorts findings into load-bearing deficiencies versus punch items, always answers "can we fix it?" with a sequenced plan, and says plainly whether the next phase can start — real praise for what is solid, no blame for what is not, and no releasing the draw over an unsafe structure. Use before building on top of existing work, when something feels half-built, or when "done" needs verifying.

**Triggers:** `bob the builder`, `deploy the foreman`, `punch list`, `site inspection`, `draw inspection`, `half-built`, `insufficiently built`, `is this ready to build on`, `can we fix it`, `before we move forward`, `unfinished work check`

### `coding-agent-skills:writing-agent-skills`

**Invoke:** `/coding-agent-skills:writing-agent-skills` — or just describe the task.

**What it does:** Authors and reviews Agent Skills (SKILL.md files) to this library's "do + teach" house standard and the open Agent Skills spec — correct frontmatter, discoverable descriptions, progressive disclosure, and privacy-safe tailoring. Use when creating a new skill, editing an existing one, reviewing a skill for quality, or setting up a new plugin in this repo.

**Triggers:** `write a skill`, `new skill`, `SKILL.md`, `authoring standard`, `skill description`, `add a skill`, `review a skill`, `do and teach`

## `metacognition-skills`

Composed meta-cognition suite: hierarchical memory management, reflective learning, adaptive analysis, and knowledge crystallization for cumulative improvement across sessions.

Install: `/plugin install metacognition-skills@treasury-analyst-skills`

### `metacognition-skills:hierarchical-memory-manager`

**Invoke:** `/metacognition-skills:hierarchical-memory-manager` — or just describe the task.

**What it does:** Maintains layered memory across sessions and long contexts — Working (current task state), Episodic (timestamped events and decisions), Semantic (durable facts, preferences, lessons, each entry carrying evidence and confidence) — via a session-start load restating only task-relevant anchors, compaction promoting Working → Episodic → Semantic and pruning the rest, and contradiction flagging with provenance instead of silent overwrites, structuring native memory, MEMORY.md, and project files rather than replacing them. Receives reflective-learner lessons; feeds the knowledge crystallizer. Use at session start, during long multi-turn work, when context grows large, or when something should be remembered or recalled.

**Triggers:** `remember this`, `memory`, `what did we decide`, `last session`, `continuity`, `compact the context`, `working memory`, `episodic memory`, `semantic memory`, `MEMORY.md`, `memory layers`, `save for later`, `what do you remember`, `pick up where we left off`

### `metacognition-skills:knowledge-crystallizer`

**Invoke:** `/metacognition-skills:knowledge-crystallizer` — or just describe the task.

**What it does:** Extracts durable insights from analysis, reflection, and experience into semantic memory and evolving working methods — harvests candidates from working and episodic notes, validates them against four gates (consistency, evidence strength, scope, leverage), distills survivors into atomic FACT/PREFERENCE/RULE/LESSON/PATTERN/METHOD entries, integrates through the memory manager with user sign-off for structural changes, prunes redundant or stale entries, and appends one audit line to the crystallization log so every change stays traceable and reversible. Use after significant analysis or reflection cycles, when a pattern recurs, at session end or milestones, or when consolidating lessons into permanent knowledge or skill updates.

**Triggers:** `crystallize`, `consolidate knowledge`, `distill lessons`, `save what we learned`, `make this permanent`, `update working methods`, `clean up the knowledge base`, `merge duplicate notes`, `retire stale facts`, `capability map`, `crystallization pass`

### `metacognition-skills:reflective-learner`

**Invoke:** `/metacognition-skills:reflective-learner` — or just describe the task.

**What it does:** Runs structured self-reflection and error-analysis cycles — situation, outcome, strengths, weaknesses, root cause, lessons, actionable updates — and integrates user corrections into durable working methods, turning experience into explicit, auditable improvement instead of leaving learning implicit. Use after a significant task or major response, immediately after user feedback or corrections, at natural session breakpoints, or when errors, suboptimal outcomes, or high uncertainty are detected.

**Triggers:** `reflect`, `retrospective`, `lessons learned`, `what went wrong`, `post-mortem`, `error analysis`, `self-review`, `you got this wrong`, `that's not what I meant`, `feedback`, `correction`, `improve your approach`, `do better next time`

## `deep-research-skills`

True deep research skills that go beyond surface search: extensive multi-database literature investigation, cross-domain dot-connection, source-provenance control, evidence appraisal, and citation verification. Starting with medical-research-detective for published medical literature.

Install: `/plugin install deep-research-skills@treasury-analyst-skills`

### `deep-research-skills:medical-research-detective`

**Invoke:** `/deep-research-skills:medical-research-detective` — or just describe the task.

**What it does:** Investigates health questions across published medical literature — multi-database searches (PubMed, Europe PMC, Cochrane, Google Scholar), connecting dots between seemingly unrelated symptoms, drugs, labs, and exposures to surface overlooked common causes, filtering sources by country of origin, and triple-checking every citation so nothing is fabricated. Produces a graded case file: ranked hypotheses, evidence for and against, questions and tests for a clinician, red flags, and gaps. Research only — never diagnosis, dosing, or treatment advice. Use for a puzzling symptom cluster, a suspected drug or nutrient interaction, a condition that resists explanation, a second-opinion literature review, or verifying a medical claim or citation.

**Triggers:** `medical research`, `research my symptoms`, `connect these symptoms`, `what could link`, `overlooked cause`, `deep dive on this condition`, `PubMed`, `Google Scholar`, `medical literature`, `drug interaction research`, `verify this study`, `check this citation`

## `writing-skills`

Writing registers and explanation craft: adams-smart-brevity (Adams + Axios Smart Brevity for professional, technical, legal, and clinical writing, with the risk-allocation carve-outs and the where-the-bar-disagrees register), adams-plain-grade (5th-8th grade accessible register with the discretion/obligation check), explanation-design (audience models, break-point-marked analogies, the Feynman loop, teach-back), and technical-documentation (Diataxis routing, ADRs, and the owner/cadence/last-verified discipline that keeps a page true).

Install: `/plugin install writing-skills@treasury-analyst-skills`

### `writing-skills:adams-plain-grade`

**Invoke:** `/writing-skills:adams-plain-grade` — or just describe the task.

**What it does:** Writes and edits to Ken Adams clarity principles at a 5th-grade reading level, falling back to 8th grade only when precision demands it — short active sentences, everyday concrete words, one idea per sentence, technical terms explained in place, and a hard rejection of litigated "tested language," archaisms, doublets, and ambiguity, while keeping meaning exact. Use when the user asks for adams-plain-grade by name, or wants plain English, patient or client materials, easy-read text, or writing for low-literacy audiences.

**Triggers:** `adams plain grade`, `plain grade`, `plain english`, `plain language`, `5th grade reading level`, `easy to read`, `easy-read`, `make this easier to read`, `simplify this letter`, `accessible language`, `patient materials`, `low literacy`, `simplest accurate version`

### `writing-skills:adams-smart-brevity`

**Invoke:** `/writing-skills:adams-smart-brevity` — or just describe the task.

**What it does:** Applies Ken Adams clarity principles plus Axios Smart Brevity to technical, legal, professional, clinical, and documentation writing — rejects the "tested language" myth (litigated language is bad language), eliminates archaisms, doublets, ambiguity, and lawyerisms, and structures everything for scanning: the one most important point first, "why it matters" second, short active sentences, bullets and bold, nothing non-essential. Use for drafting, editing, or reviewing documents, contract language, clinical notes, emails, report writing, code comments, or any request for clear, brief, precise, or litigation-resistant language.

**Triggers:** `smart brevity`, `adams smart brevity`, `writing review`, `language review`, `edit for clarity`, `brevity`, `drafting`, `clear and precise`, `litigation-resistant`, `contract language`, `clinical note language`, `ambiguity check`, `tighten this email`, `report writing`

### `writing-skills:explanation-design`

**Invoke:** `/writing-skills:explanation-design` — or just describe the task.

**What it does:** Designs an explanation for a named audience instead of transcribing the author's understanding: writes the one-sentence audience model first, chooses the entry analogy deliberately with its break-points marked, orders material concrete-first (worked example → general principle → boundary cases, never definition-first), runs the Feynman loop (distilled from accounts of Feynman's practice, not a protocol he wrote) to find the author's own gaps, strips curse-of-knowledge tells (Pinker's framing: undefined abbreviations, "simply," skipped steps), and verifies with teach-back. The assistant plays the smart newcomer, flags jargon and hand-waves, drafts analogies with breaks marked, and simulates the teach-back. Use when a concept must land with someone who doesn't already know it — onboarding, newcomer docs, or "why does nobody get this?".

**Triggers:** `explain it well`, `Feynman technique`, `analogy for`, `teach this concept`, `curse of knowledge`, `make this intuitive`, `teach-back`, `explain to a newcomer`

### `writing-skills:technical-documentation`

**Invoke:** `/writing-skills:technical-documentation` — or just describe the task.

**What it does:** Structures technical documentation as typed artifacts, not prose: routes docs through Procida's Diátaxis framework (tutorial, how-to, reference, explanation — forms that fail when blended), shapes the README around a newcomer's first screen, records decisions as Nygard-style ADRs (context/decision/consequences, superseded rather than rewritten), keeps a human-readable changelog keyed to SemVer, and holds API and reference docs to examples-first, versioned, generated-vs-hand-written discipline. Owns the document types; register stays with writing-skills:adams-smart-brevity, explanation craft with writing-skills:explanation-design. Gives every page an owner, a cadence, and a last-verified date. Use when writing or restructuring docs for a project, method, or process.

**Triggers:** `technical documentation`, `write the README`, `ADR`, `architecture decision record`, `changelog`, `Diátaxis`, `how-to guide`, `tutorial vs reference`, `API docs`, `docs as code`, `semantic versioning`, `our docs are out of date`

## `safety-and-reliability-skills`

Safety engineering for records, alarms, and dormant protections: split-tally evidence design with the litigation-hold rail, detection-system tuning by empirical disposition audit (floor-ceiling autoimmunity band), reliability math including probability-of-failure-on-demand for dormant protective functions, rebuild rehearsal with an irreversibility screen, break-glass playbooks, and hash-rank sortition review.

Install: `/plugin install safety-and-reliability-skills@treasury-analyst-skills`

### `safety-and-reliability-skills:break-glass-playbooks`

**Invoke:** `/safety-and-reliability-skills:break-glass-playbooks` — or just describe the task.

**What it does:** Arms each foreseeable crisis with a break-glass playbook, channeling documented emergency-access procedures (HIPAA; NIST/CIS-mapped testing) and regulator-mandated contingency plans with graduated escalation: define the tripwire as a number a named person watches on a stated cadence, pre-author the first ten moves at calm-headed quality, pre-grant emergency authority with automatic expiry and full logging, name the comms tree and the decision chair, drill the unsealing on a schedule, and re-arm after every firing. Converts pre-mortem failure modes into tripwire-plus-playbook pairs, red-checks each tripwire for measurability, drafts the sealed instructions, and simulates the unsealing drill. Use when a crisis is foreseeable but the team would be scrambling if it hit.

**Triggers:** `break glass`, `break-glass`, `seldon crisis`, `what do we do when X hits`, `emergency access`, `runbook`, `kill switch`, `tripwire`, `covenant trip`, `we'd be scrambling`, `sealed instructions`

### `safety-and-reliability-skills:detection-system-tuning`

**Invoke:** `/safety-and-reliability-skills:detection-system-tuning` — or just describe the task.

**What it does:** Tunes detection systems — monitors, exception queues, spam filters, code-review bots, compliance screens — along the immune system's axis: between autoimmunity (false matches that desensitize operators) and immunodeficiency (missed threats). Measures each rule's empirical false-positive rate, recalibrates defaults before adding detectors, layers cheap screens ahead of costly investigation, gates human paging on danger signals, maintains expiring tolerance lists for verified-benign patterns, converts every true incident into a permanent detector, simulates threshold changes against historical firings before going live. Use when queues drown operators, real signals get buried, or systems need tuning.

**Triggers:** `alarm fatigue`, `detection tuning`, `autoimmunity`, `immune system`, `too many false matches`, `exception queue drowning`, `tune the alerts`, `memory cell`, `everything is an exception`, `nobody looks at the alerts anymore`

### `safety-and-reliability-skills:rebuild-rehearsal`

**Invoke:** `/safety-and-reliability-skills:rebuild-rehearsal` — or just describe the task.

**What it does:** Keeps critical capabilities alive by rehearsing the rebuild on a cadence shorter than anyone's tenure, channeling the Ise Grand Shrine's Shikinen Sengu (rebuilt in full every 20 years since 690 CE; carpenters learn, lead, then teach; a ~120-year lapse after the Ōnin War proved the cycle needs a funding owner): census what lives only in heads, pick a real rebuild unit (restore from backup, recreate the deliverable from raw inputs, rebuild the environment from docs alone), rotate learn-lead-teach so last time's apprentice leads, harvest every exposed gap into the docs, and name who funds the cycle. The assistant simulates the rebuild, interrogates the docs for gaps, and plays the newcomer with only the written record. Use when knowledge lives in one head or docs have never been proven by use.

**Triggers:** `rebuild drill`, `restore drill`, `if she left tomorrow`, `are the docs enough to recreate this`, `it only lives in his head`, `bus factor`, `knowledge refresh`, `could a newcomer run this`, `disaster recovery rehearsal`

### `safety-and-reliability-skills:reliability-engineering`

**Invoke:** `/safety-and-reliability-skills:reliability-engineering` — or just describe the task.

**What it does:** Applies reliability-engineering math to systems and processes: splits non-repairable populations (Weibull time-to-failure, censoring, fit checks, bootstrap bounds) from repairable systems with recurrent failures (power-law NHPP / Crow-AMSAA trend), reads beta to pick burn-in, run-to-failure, or scheduled replacement, computes MTBF, MTTR, time- or event-based availability, and an error budget, converts an SLO into a downtime budget, works series/parallel arithmetic — parallel credit only with demonstrated independent failover — and forecasts from two or three failures with Weibayes. Use when a failure log needs quantifying (interface or data-feed failures, job aborts, process breaks, equipment), when sizing redundancy against an uptime target, or setting a replacement schedule.

**Triggers:** `Weibull`, `bathtub curve`, `MTBF`, `MTTR`, `availability math`, `downtime budget`, `series parallel reliability`, `burn-in`, `failure rate fit`, `how much downtime does our SLO allow`

### `safety-and-reliability-skills:sortition-review`

**Invoke:** `/safety-and-reliability-skills:sortition-review` — or just describe the task.

**What it does:** Designs selection-by-lot oversight channeling Athenian euthynai (scheduled end-of-term review by allotted reviewers, generals included, universal, never suspicion-triggered) and the 1268 Venetian doge protocol (ten alternating rounds of lot and vote, blind draws, 529 years): define the reviewable population, set a universal floor with no exemptions, draw items by verifiable lot (pre-committed seed, dice in the open), rotate reviewer pairs by lot too, make end-of-role handover review the default so departure carries no stigma, size the draw to real attention (the assistant first-passes every drawn item, the human adjudicates), and publish the rule, never the draw. Use when selection must be unriggable, review must carry no accusation, or the same person always checks the same people.

**Triggers:** `sortition`, `review by lot`, `spot-check by lot`, `they know which ones get looked at`, `same person always reviews`, `rotate reviewers`, `end-of-term handover`, `draw at random`, `unriggable selection`

### `safety-and-reliability-skills:split-tally-evidence`

**Invoke:** `/safety-and-reliability-skills:split-tally-evidence` — or just describe the task.

**What it does:** Designs tamper-evident records on the split tally-stick principle (English Exchequer, ~650 years): notched stick split lengthwise into stock and foil, wood grain self- authenticating. Halves each record between adverse parties so verification is rejoining two halves neither can alter alone. Inventories records one party could rewrite, designs the split for each (counterpart-held confirmations, hash-anchored exports, signed receipts, append-only logs with external anchors), schedules verification as rejoining ritual, proves by attempted alteration, adds second keeper who independently re-derives critical numbers, and suspends disposal schedules under legal hold. Use when records must survive disputes or when evidence needs designing rather than hoping.

**Triggers:** `tally stick`, `split tally`, `tamper-evident`, `who holds the other copy`, `could someone alter this after the fact`, `does our half fit their half`, `hash anchor`, `dual custody`, `evidence design`, `litigation hold`, `legal hold`, `spoliation`, `duty to preserve`

## `collaboration-skills`

Two collaboration instruments that earn their slots: disarming-elicitation (the FBI counter-elicitation stance inverted for willing experts, with the scoped-promise and investigation rails) and meeting-design (decisions extracted as owner-and-date read-backs, not vibes).

Install: `/plugin install collaboration-skills@treasury-analyst-skills`

### `collaboration-skills:disarming-elicitation`

**Invoke:** `/collaboration-skills:disarming-elicitation` — or just describe the task.

**What it does:** Runs knowledge-elicitation interviews in the disarming, low-stakes stance documented in motivational interviewing, the FBI elicitation brochure, and the clinically documented doorknob phenomenon (the key disclosure arrives as the interview seems over): lower the stakes so the expert educates rather than defends, restate their words slightly wrong so correction does the teaching, hold contradictions as the interviewer's own confusion, let silence work, then ask one casual question after the formal close. Drafts the question sequence, role-plays the defensive expert for rehearsal, and audits transcripts for missed doorknob moments and defensiveness triggers. Use with experts, process owners, and users who know more than they can say — willing people only, never covert extraction.

**Triggers:** `columbo`, `elicitation`, `stakeholder interview`, `requirements gathering`, `the users can't articulate what they do`, `expert won't open up`, `walkthrough with the process owner`, `doorknob question`, `one more thing`

### `collaboration-skills:meeting-design`

**Invoke:** `/collaboration-skills:meeting-design` — or just describe the task.

**What it does:** Designs meetings that produce decisions instead of discussion. Tests whether the meeting should exist (does it produce a decision or a commitment? status flows async); writes the agenda as a list of decisions to make, each with a timebox and a decision rule named before discussion opens (single owner, consent, consult-then-decide, or vote); sends pre-reads with silent reading at the start (documented Amazon practice); parks tangents visibly, calls the decision at the timebox, gives every action an owner and a date, and closes by reading back decisions and commitments. Drafts the decision-list agenda from a stated purpose, red-checks an agenda for non-decisions, turns a transcript into a decision log, and audits recurring meetings nobody has re-justified. Use when planning, tightening, or questioning any meeting.

**Triggers:** `meeting agenda`, `run this meeting`, `too many meetings`, `this should be an email`, `action items`, `decision protocol`, `pre-read`, `standing meeting audit`, `fix the agenda`

## `math-foundations-skills`

Unit conversion and dimensional analysis — the factor-label method, unit checks as a necessary-not-sufficient guard on every formula, and the unit-driven catch for formula rearrangement errors. The broader basic-math set is archived; this is the one that catches real errors models and humans both make.

Install: `/plugin install math-foundations-skills@treasury-analyst-skills`

### `math-foundations-skills:units-and-dimensional-analysis`

**Invoke:** `/math-foundations-skills:units-and-dimensional-analysis` — or just describe the task.

**What it does:** Converts quantities across units with the factor-label method — conversion factors written as fractions so units cancel visibly — chains multi-step conversions (time, volume, currency as a unit), treats per-unit rates (cost per unit, items per hour) as first-class quantities that multiply and divide, annualizes and de-annualizes (×12 for flows; compound growth routes to the exponential-growth sibling), and dimension-checks any formula: write the units of every term, and if the two sides disagree the formula is wrong however plausible its numbers look. Catches the classic traps — per-month vs per-year mixups, thousands vs millions scale errors, percent as a dimensionless unit. Use when converting units, checking whether a formula's units balance, or annualizing a monthly figure.

**Triggers:** `unit conversion`, `convert units`, `dimensional analysis`, `units don't match`, `per unit`, `annualize`, `factor-label`, `cancel the units`, `unit check`, `thousands vs millions`

## `decision-science-skills`

Decision discipline under uncertainty: pre-mortem (with the counsel rail), tabletop wargaming and no-win drills under full exercise control, weak-signal navigation with cue-graded confidence, Bayesian updating via natural frequencies, reference-class forecasting, competing hypotheses analysis, minority-report dissent capture, the Rashomon-effect protocol for conflicting recollections, and The Challenger.

Install: `/plugin install decision-science-skills@treasury-analyst-skills`

### `decision-science-skills:bayesian-updating`

**Invoke:** `/decision-science-skills:bayesian-updating` — or just describe the task.

**What it does:** Runs belief revision as a decision discipline: starts a question from an explicit prior (base-rate anchor from reference-class-forecasting), weighs each piece of evidence by how surprising it would be under each hypothesis, updates with count tables or the odds shortcut, not formulas, grades evidence in Bayes-factor bands (barely-worth-mentioning to very strong), and keeps a Tetlock-style update journal — small, frequent, logged revisions scored at resolution. Teaches the honest history (Bayes barely wrote it; Price shaped it; Laplace built the form we use) and the cab-problem trap of vivid evidence swamping the prior. Use when new evidence should move a standing estimate or someone asks how much a result should change their mind.

**Triggers:** `bayesian updating`, `update my beliefs`, `belief revision`, `likelihood ratio`, `Bayes factor`, `posterior probability`, `prior probability`, `superforecasting`, `superforecaster`, `perpetual beta`, `how much should this evidence move me`

### `decision-science-skills:competing-hypotheses-analysis`

**Invoke:** `/decision-science-skills:competing-hypotheses-analysis` — or just describe the task.

**What it does:** Weighs rival explanations against the same body of evidence using Heuer's structured competing-hypotheses method from intelligence analysis: brainstorm the full hypothesis set including unlikely and deception hypotheses, list the significant evidence, build the hypothesis matrix (hypotheses across the top, evidence down the side), drop non-diagnostic evidence, judge by disconfirmation — the winner is the hypothesis with the least evidence against it — sensitivity-check the load-bearing items, report the relative likelihood of every hypothesis, and name the future observations that would change the answer. Use when several plausible causes compete: a reconciliation break that resists the standard pass, an incident with multiple suspects, any analysis at risk of confirmation bias.

**Triggers:** `competing hypotheses`, `hypothesis matrix`, `which explanation fits the evidence`, `diagnostic evidence`, `rule out causes`, `weigh rival explanations`, `why is this break really happening`

### `decision-science-skills:minority-report`

**Invoke:** `/decision-science-skills:minority-report` — or just describe the task.

**What it does:** Runs a precognition cell over any decision: builds three to five named, internally coherent, structurally different future scenarios (Shell-lineage scenario planning — never best/expected/worst on one axis), turns one variable at a time to find which single change flips the outcome ranking, and always files the minority report — the dissenting future given full voice, because suppressing it is the failure the namesake story is about. Adds the reflexivity check (acting on a forecast changes the futures it forecast), probabilities only via reference-class base rates with honest bands, and ends with per-scenario tripwires and a decision log. Scenarios are rehearsals, not predictions — the human owns the choice. Use when weighing future outcomes, testing what happens if a variable changes, or deciding under uncertainty.

**Triggers:** `precog`, `precognition`, `minority report`, `run the scenarios`, `future outcomes`, `what happens if X changes`, `scenario planning`, `branch the futures`

### `decision-science-skills:no-win-drills`

**Invoke:** `/decision-science-skills:no-win-drills` — or just describe the task.

**What it does:** Runs a no-win drill — a simulation with the winning move removed, as practiced in emergency-medicine patient-death scenarios and EMS stress training — and grades the decision process, never the outcome: the LLM generates a situation guaranteeing no clean exit, plays the escalating environment, then debriefs loss-minimization, explicit ordering of what to save, communication under futility, and the emotional response. Carries the Kirk blade held honestly (Conti & Caroland, IEEE Security & Privacy): sort physics constraints from policy constraints — reframing is legitimate when it changes policy transparently and owns the consequences, cheating when hidden — and it flags any quiet mid-drill redefinition of success. Use when every option costs and someone must practice choosing least-worst.

**Triggers:** `kobayashi maru`, `no-win`, `every option is bad`, `least-worst`, `damage control drill`, `degraded mode`, `can't win this one`, `loss triage`

### `decision-science-skills:pre-mortem`

**Invoke:** `/decision-science-skills:pre-mortem` — or just describe the task.

**What it does:** Runs Gary Klein's pre-mortem — the prospective-hindsight exercise — on a plan before commitment: declare that the plan has already failed outright, have every participant silently and independently write reasons why, round-robin the reasons until exhausted, rank them, and strengthen the plan against the top items with named owners. Includes a solo-analyst variant where the LLM generates a heterogeneous set of failure narratives (technical, political, data, timing) and writes each stakeholder's reason for the human to rank. Use before committing to a configuration change, a system go-live, a bulk data load, a product release, or any plan the team is about to lock in.

**Triggers:** `premortem`, `pre-mortem`, `assume it failed`, `what could sink this`, `before we go live`, `prospective hindsight`

### `decision-science-skills:rashomon-effect`

**Invoke:** `/decision-science-skills:rashomon-effect` — or just describe the task.

**What it does:** Reconciles contradictory good-faith accounts of one event (witness statements, incident write-ups, contested post-mortems) using Rashomon-effect scholarship and eyewitness-memory science: takes each account whole (cognitive-interview moves) before comparing, splits accounts into observations, interpretations, and stakes, maps who could see what from where, finds the invariant core, sorts each divergence into perspective, memory, or stake artifact vs genuine contradiction, weights initial uncontaminated statements over late rehearsed ones, adjudicates only against physical evidence, never confidence or seniority, and writes a reconciled account marking confidence, filing unresolved forks instead of dropping them. Bad faith must be earned with evidence. Use when accounts of one event conflict.

**Triggers:** `rashomon`, `conflicting accounts`, `witnesses disagree`, `everyone remembers it differently`, `whose story is right`, `reconcile the statements`, `contradictory testimony`

### `decision-science-skills:reference-class-forecasting`

**Invoke:** `/decision-science-skills:reference-class-forecasting` — or just describe the task.

**What it does:** Applies the outside view (Kahneman/Tversky's planning fallacy, Flyvbjerg's reference-class method) to discipline any material estimate: identify a reference class of comparable past cases, establish its outcome distribution, anchor on that base rate, adjust only with explicit written justification — or apply a required uplift at a chosen certainty level (P80-style, pooled not summed) — then log the prediction and score it against actuals. Counters optimism bias and strategic misrepresentation, and guards against tampering (reworking the rule after every miss). Turns an existing variance history (per-driver MAPE, signed bias) into next-cycle base-rate anchors; it feeds estimation loops, never builds the models. Use when an estimate rests only on its own story or a plan looks optimistic.

**Triggers:** `outside view`, `reference class`, `base-rate anchor`, `base rate`, `optimism bias`, `planning fallacy`, `how long do projects like this actually take`, `uplift the estimate`

### `decision-science-skills:tabletop-wargaming`

**Invoke:** `/decision-science-skills:tabletop-wargaming` — or just describe the task.

**What it does:** Designs and runs a multi-party tabletop exercise with an adversary and adjudication, in the lineage Kriegsspiel → Army course-of-action analysis (action / reaction / counteraction) → CISA-style tabletop packages: define objectives and scenario (an impersonated urgent instruction, a critical-vendor outage on a deadline day, ransomware in a freeze), write the blue team's commander's intent (purpose, key tasks, end state), assign blue players, a red cell, and a white-cell adjudicator, play turns driven by pre-scripted and adaptive injects, adjudicate plausibility, capture decisions and gaps, and hand off to an after-action review. The LLM plays red and white cell strictly as a scenario generator — humans adjudicate every consequential outcome. Use when rehearsing an incident-response, fraud, continuity, or cutover plan against an adaptive adversary.

**Triggers:** `tabletop exercise`, `wargame the plan`, `run a drill`, `incident simulation`, `inject`, `BCP exercise`, `commander's intent`

### `decision-science-skills:the-challenger`

**Invoke:** `/decision-science-skills:the-challenger` — or just describe the task.

**What it does:** Runs the revision review that momentum and sunk costs suppress — named for the 1986 Challenger launch decision, where schedule fever inverted the burden of proof over the engineers' objection. When evidence changes mid-project, it zero-bases the continue-vs-revise decision: only forward-looking costs count (money spent argues nothing), continuation past a trigger carries the burden of proof, normalized anomalies are re-seen as on first sighting, options widen beyond stop/continue (slip, descope, phase, re-plan), a dissent channel guarantees the objector is restated before the decision, and the outcome is logged with the next review trigger. Use when a deadline is driving decisions the evidence argues against, when "we've come too far" appears in any form, or when a go/no-go needs honest structure.

**Triggers:** `the challenger`, `challenge the timeline`, `sunk cost`, `plan continuation`, `should we slip the date`, `launch fever`, `are we still go`, `normalization of deviance`, `escalation of commitment`, `revision review`

### `decision-science-skills:weak-signal-navigation`

**Invoke:** `/decision-science-skills:weak-signal-navigation` — or just describe the task.

**What it does:** Estimates a current position or state when the usual instrument — a dashboard, tracker, status report, or data feed — is down, stale, or untrusted, by fusing many weak independent cues (last known-good state, scheduled events that must have fired, historical rhythms, side channels, absence of expected noise) into a continuously re-estimated belief with a stated confidence band; narrates which cue the position leans on hardest, updates as cues arrive, and defines what will confirm or deny the belief when the instruments return (the method of Polynesian/Micronesian wayfinding and etak — Hokule'a, Mau Piailug, Hutchins' distributed-cognition analysis). Use when a decision needs the position anyway and the authoritative number is missing or disbelieved.

**Triggers:** `wayfinding`, `weak signals`, `estimate blind`, `the dashboard is down`, `I don't trust this number`, `navigate without instruments`, `what would we expect to see`, `position without the data`, `dead reckoning`

