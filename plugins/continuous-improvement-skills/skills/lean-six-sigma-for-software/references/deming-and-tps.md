# Deming and the Toyota Production System, translated to software

The intellectual foundation of this skill: what Deming and TPS actually say, and the exact
software equivalent of each idea. Use this when you need the *why* behind a practice or when
choosing which control to install.

Contents: §1 Deming's System of Profound Knowledge · §2 PDSA · §3 Deming's points that matter
most in software · §4 Variation: the two mistakes · §5 TPS pillars and tools → software ·
§6 Respect for people

## §1 Deming's System of Profound Knowledge → software

Four lenses, all four required:

| Lens | Deming's claim | In software |
|---|---|---|
| **Appreciation for a system** | An organization is a system; optimize the whole, not the parts | Optimizing one team's velocity while integration, review, or deploy queues starve is sub-optimization. The unit of improvement is the **value stream** (idea → running in production), not the sprint. |
| **Knowledge of variation** | Every process varies; management's job is to know common cause from special cause | Cycle time, defect escape rate, build duration, and incident counts all vary week to week. React to *signals* (special cause), not *noise* (common cause). Control charts, not gut feel. |
| **Theory of knowledge** | Learning requires prediction and test — theory, not anecdote | Every change is a hypothesis: "this will cut checkout errors 30%." State the prediction, measure the result (PDSA). "We shipped it" is not evidence it worked. |
| **Psychology** | People are intrinsically motivated; fear destroys data | Blameless postmortems exist because blamed engineers stop reporting near-misses — and then you lose your best data. Metrics used to rank people get gamed (Goodhart); metrics used to improve the *process* stay honest. |

## §2 PDSA — Plan, Do, Study, Act

Deming's cycle (he insisted on **Study**, not "Check" — the point is learning, not inspection):

1. **Plan** — state the theory and the *predicted* result, and decide what you'll measure.
2. **Do** — run the change small (one team, one canary slice, one feature flag cohort).
3. **Study** — compare results *to the prediction*. Surprises are the most valuable output.
4. **Act** — adopt and **standardize** (the new way becomes the documented default), adapt, or
   abandon. Then cycle again.

Software-native PDSA loops already exist — treat them as such: A/B tests, canary deploys,
retrospectives with experiments, error-budget policy reviews. What's usually missing is the
*prediction before* and the *standardization after*. Without standardizing the win, the next
improvement starts from scratch — this is Deming's "standardize and measure to improve": the
standard is the baseline that makes the next measurement meaningful.

## §3 The Deming points that matter most in software

Selected from the 14 Points, translated:

- **Constancy of purpose** — a product direction stable enough that quality investment pays
  back. Thrash kills quality cheaply.
- **Cease dependence on inspection; build quality in** — a QA phase at the end is inspection.
  Types, tests, contracts, and reviews *during* construction are building quality in. Shift
  left; make the pipeline the inspector.
- **End lowest-bid purchasing** — for software: don't pick dependencies, vendors, or contractors
  on price alone; total cost of ownership includes maintenance, security, and exit cost.
- **Improve constantly and forever** — kaizen; the codebase, pipeline, and process are never
  "done."
- **Institute training and leadership** — pairing, onboarding docs, golden paths; leaders who
  understand the work at the gemba (see §5).
- **Drive out fear** — blameless culture; a team afraid to surface bad news ships you surprises
  in production.
- **Break down barriers between departments** — the wall between dev and ops (or dev and
  design, or dev and the business) is where defects breed; DevOps and co-design are
  barrier-demolition.
- **Eliminate slogans and quotas; remove barriers to pride of workmanship** — "zero bugs by
  Friday" posters don't fix the system that produces bugs. Numerical quotas on
  lines/tickets/points get gamed. Give people a system they can be proud of instead.

## §4 Variation: the two mistakes (the funnel and the beads)

- **Mistake 1 — treating noise as signal (tampering).** Deming's funnel experiment: adjusting a
  stable process after every result *increases* variation. Software version: rearchitecting
  after one bad week, adding process after one incident, re-estimating after one slow sprint.
  If the metric is inside control limits, the fix is to improve the *system*, not to react to
  the *point*.
- **Mistake 2 — treating signal as noise.** The complement: a genuine special cause (a real
  regression, a new failure mode) explained away as "just a blip." Detection needs rules, not
  vibes — use a control chart (I-MR for most delivery metrics) with Western Electric/Nelson
  rules.
- **The red bead experiment**: workers drawing beads from a mixed lot can't change their defect
  count — the system determines it, and rewarding/punishing individuals for it is management
  malpractice. Software version: defect counts, velocity, and incident tallies are mostly
  properties of the *system* (codebase age, test coverage, deploy tooling, schedule pressure) —
  fix the system, don't rank the people.

## §5 TPS pillars and tools → software

TPS stands on two pillars — **Just-in-Time** (make only what's needed, when needed) and
**jidoka** (build in the ability to detect and stop on abnormality). Everything else serves
them.

| TPS concept | Meaning | Software equivalent |
|---|---|---|
| **Jidoka** | Machines stop themselves on abnormality; humans fix the cause | CI gates that *block* merge on failure; crashing loudly over corrupting silently; alerts tied to runbooks. Quality is enforced by the system, not vigilance. |
| **Andon cord** | Any worker stops the line on a defect | Anyone can revert/rollback/halt a deploy without permission theater; a red main build is everyone's top priority — *stop the line, fix, then resume*. |
| **Just-in-Time / pull** | Downstream pulls; no overproduction | Small batches: small PRs, short-lived branches, continuous delivery. Build features when actually needed (YAGNI is JIT for code — see `full-stack-dev-skills:lean-code-principles`). |
| **Kanban / WIP limits** | Visualize flow; cap work-in-process | WIP-limited boards; finishing beats starting. High WIP = high cycle time (Little's Law). |
| **Heijunka** (leveling) | Smooth the schedule; avoid mura (unevenness) | Steady release cadence over big-bang releases; avoid crunch (muri = overburden) — exhausted engineers are a defect generator. |
| **Poka-yoke** (mistake-proofing) | Make the error impossible, not forbidden | Types that make illegal states unrepresentable; NOT NULL and foreign keys; required PR checks; linters; idempotency keys; confirmation for destructive ops. Prefer *can't* over *shouldn't*. |
| **Standard work** | The current best-known method, documented, followed, and improved | Coding standards, golden-path templates, runbooks, ADRs. The standard is the *baseline for kaizen*, not bureaucracy — you can't improve a method that isn't defined (→ `continuous-improvement-skills:standard-work`). |
| **Genchi genbutsu** (go and see) | Decide from observed reality, not reports | Watch real users use the feature; read production telemetry and session replays; reproduce the bug before theorizing. The gemba of software is production + the user's desk. |
| **Muda** (waste) | Seven wastes | Partially done work, extra features, relearning, handoffs, delays (wait for review/CI/approval), task switching, defects (the Poppendiecks' mapping). Value-stream-map the pipeline to find them (→ `continuous-improvement-skills:value-stream-mapping`). |
| **Kaizen** | Continuous small improvement by the people who do the work | Retro actions that actually ship; boy-scout rule; scheduled paydown of the top friction item every iteration (→ `continuous-improvement-skills:kaizen-and-codesign`). |

## §6 Respect for people

The pillar both systems share and the one most often dropped in "lean" adoptions: the people
doing the work hold the deepest knowledge of it, so improvement is done **by** them, not **to**
them. In software: engineers design their own standards and automation; users co-design the
product (see the co-design section of `dmaic-codesign-and-pm.md`); problems are framed as
process problems, never person problems; and credit flows to the people whose ideas shipped.
A team treated as the system's sensors and designers will keep surfacing improvements; a team
treated as resources will go quiet — and quiet teams ship surprises.
