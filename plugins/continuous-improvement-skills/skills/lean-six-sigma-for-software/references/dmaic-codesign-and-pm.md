# DMAIC/DMADV for software, co-design, and project management

The operating methods: how to run a software effort as a Lean Six Sigma project — improvement
(DMAIC), new design (DMADV, "begin with the end in mind"), users in the room (co-design), and
delivery discipline (hybrid PM).

Contents: §1 Choosing DMAIC vs DMADV · §2 DMAIC on a software process · §3 DMADV / backward
design for new software · §4 Software CTQs and metrics · §5 Co-design · §6 Hybrid project
management · §7 Artifacts checklist

## §1 Choosing DMAIC vs DMADV

- **DMAIC** (Define–Measure–Analyze–Improve–Control): the thing exists and underperforms — slow
  releases, defect leakage, an error-prone workflow, a feature users abandon.
- **DMADV** (Define–Measure–Analyze–Design–Verify): the thing doesn't exist yet, or needs
  redesign so deep that improving the current design is throwing good money after bad.
- Deciding test: "are we tuning a process or specifying an outcome?" Tuning → DMAIC.
  Specifying → DMADV.

## §2 DMAIC on a software process

- **Define** — problem statement with a number in it ("p75 lead time is 9 days; target 2"), the
  value stream affected, the customer, the charter (scope, sponsor, team, timebox). No
  solutions yet.
- **Measure** — instrument before changing. Establish the baseline and its *variation* (control
  chart), and check your measurement system first (MSA for software: do two people classifying
  the same 20 defects agree? Does the dashboard double-count? Is "done" defined?). A metric you
  can't trust produces confident nonsense.
- **Analyze** — find the dominant cause, prove it with data: value-stream map for delay wastes,
  Pareto of defect categories, 5 Whys / fishbone on the top category
  (→ `continuous-improvement-skills:root-cause-analysis`), hypothesis tests when comparing
  groups. Resist solution-jumping: the fix for the *proven* cause is usually smaller than the
  fix for the *assumed* one.
- **Improve** — smallest change that removes the dominant cause; pilot it (one team, one flag
  cohort); PDSA with a stated prediction; keep what the data keeps.
- **Control** — make the gain permanent or it evaporates: standardize (update the golden path,
  the template, the runbook), automate the check (poka-yoke in CI), keep the control chart
  running with an owner and a response plan ("if p-chart signals, do X"). A project without a
  control plan is a temporary donation to entropy.

## §3 DMADV / backward design for new software ("begin with the end in mind")

The phrase is Covey's habit; the engineering discipline is Deming's theory-first thinking and
DFSS practice: **specify the destination before designing the route.**

- **Define** — the end state, written as verifiable statements: who uses it, for what outcome,
  and the measurable definition of "working" (SLOs, task-success rate, accessibility
  conformance, adoption). If you can't state the acceptance test, you aren't ready to design.
- **Measure** — turn Voice of the Customer into CTQs (§4): interview real users, watch current
  work (genchi genbutsu), rank what must be true for them to succeed.
- **Analyze** — candidate architectures/designs against the CTQs; prototype the risky parts
  (spike the unknown, not the familiar); FMEA the leading design: how does each component fail,
  how bad, how detectable — fix high-RPN items *in the design*.
- **Design** — build to the CTQs with quality built in (types, contracts, tests as you go), UI
  to the design system, co-designed with users (§5).
- **Verify** — against the Define-phase criteria, not against enthusiasm: acceptance tests,
  accessibility audit, adversarial pass, pilot with real users, then the control plan for life
  in production.

Backward design is also how you scope: anything that doesn't serve the defined end state is
muda — cut it (YAGNI is the code-level twin).

## §4 Software CTQs and metrics

VOC → CTQ tree: a customer voice ("checkout feels janky and I don't trust it") decomposes into
critical-to-quality requirements, each measurable ("p95 interaction latency < 200 ms", "zero
double-charges", "error messages state the fix").

Delivery-process metrics worth control-charting (I-MR chart is the default for most):
- **Lead time / cycle time** (idea→prod, start→merge) — the flow metric.
- **Deployment frequency** and **change failure rate** — the DORA pair that exposes batch size.
- **MTTR** — recovery speed; pairs with change failure rate.
- **Defect escape rate** — found-in-prod / total found; the build-quality-in metric.
- **Review latency, CI duration, flake rate** — the invisible queues that dominate lead time.

Product/runtime metrics: SLO attainment, error rate, p95/p99 latency, task success rate,
form-abandonment rate, accessibility conformance. Rules: metrics judge the *process*, never
individuals (red beads — see `deming-and-tps.md` §4); every metric has an owner, a chart, and a
response plan; prefer a few metrics watched weekly over a dashboard nobody reads.

## §5 Co-design: users design with you, not for you

Software's version of the kaizen principle that those who do the work design the improvement
(full facilitation method: `continuous-improvement-skills:kaizen-and-codesign`):

1. **Recruit the real doers** — the front-desk operator, the analyst, the biller who lives in
   the current tool daily; plus their downstream customer (who consumes the output). Not their
   managers as proxies.
2. **Go to their gemba first** — watch current work before any mockup exists. Count clicks,
   note workarounds, capture the *words they use for things* — those words become your labels
   (this is where UI-vocabulary sync starts; see the
   `continuous-improvement-skills:curve-hero-design-language` skill).
3. **Design in their language, together** — paper/low-fi mockups the users mark up; card-sort
   the navigation; let them arrange the workflow. Facilitate for equal voice — the quietest
   user often holds the critical edge case.
4. **Rapid PDSA on prototypes** — clickable prototype today, feedback today, revision tomorrow.
   Small loops beat big reveals; a big reveal is batch size in disguise.
5. **Verify by watching, not asking** — task-based usability tests ("post this payment") with
   time and error counts. People are polite in interviews and honest in behavior.
6. **Keep them in the loop after ship** — co-design doesn't end at launch; the pilot cohort
   becomes the standing user panel for kaizen.

## §6 Hybrid project management

Software delivery is iterative; commitments, integrations, and go-lives are predictive. Use
both deliberately:

- **Charter** every significant effort: problem/opportunity with a number, scope (and
  explicitly out-of-scope), sponsor, team, timebox, success criteria, top risks. One page.
- **Risk register**, reviewed on cadence: risk, likelihood×impact, owner, mitigation, trigger.
  FMEA for the technical risks; plain register for the rest. Swiss-cheese the big ones
  (multiple independent mitigations).
- **RACI** only where handoffs are ambiguous — co-design shrinks the need.
- **Iterative core**: WIP-limited flow, small batches, demo working software on cadence,
  retrospectives that produce shipped experiments (PDSA).
- **Predictive shell** where reality is date-shaped: milestones, dependency map/critical path
  for integrations and migrations, cutover plan, training, hypercare window after go-live.
- **Status by metrics, not adjectives**: the control charts from §4 plus burn-up against scope.
  "Green" is a claim; a chart is evidence.
- **Close with lessons**: retro the project itself; standardize what worked into the golden
  path; the lessons file is the org's process memory.

## §7 Artifacts checklist (minimum viable rigor)

- [ ] One-page charter with quantified problem and success criteria
- [ ] Baseline measurement + control chart before changes
- [ ] VOC notes and CTQ tree (for DMADV: written end-state definition)
- [ ] Value-stream map or Pareto identifying the dominant cause/waste
- [ ] Risk register / FMEA for high-stakes components
- [ ] Pilot/PDSA record: prediction → result → decision
- [ ] Control plan: standard updated, check automated, chart owned, response plan written
