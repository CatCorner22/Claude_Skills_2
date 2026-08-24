# Process, Projects, and Stakeholders

Read this when the work involves improving a process, scoping a project, or serving several stakeholders with differing needs.

## Contents

- Process improvement (Lean Six Sigma / DMAIC)
- Waste, variation, and root cause
- Project scoping and management
- Co-design with stakeholders
- Decision rationale

## Process improvement (Lean Six Sigma / DMAIC)

Use DMAIC as an operating discipline rather than a label. Name the stages only when naming them helps the user follow the reasoning.

**Define.** State the problem in terms of the defect and its consequence, not the desired solution. "Twelve percent of statement lines fail auto-reconciliation, costing roughly forty staff hours a month" is a problem statement. "We need better matching rules" is a proposed solution wearing a problem's clothes — and it forecloses the analysis before it starts.

**Measure.** Establish the baseline before changing anything. Without a measured starting point, no one can tell afterward whether the change helped, and the improvement becomes a matter of opinion.

**Analyze.** Find the root cause. Push past the first plausible explanation, since the first is usually a symptom. Check whether the cause you identified actually accounts for the size of the effect.

**Improve.** Design the change against the root cause. Prefer changes that remove a defect opportunity over changes that add an inspection step, because inspection catches defects while prevention eliminates them.

**Control.** Build in the mechanism that keeps the improvement from decaying — a checklist, a validation step, an exception report, a scheduled review. Improvements without controls revert, usually within two staffing changes.

## Waste, variation, and root cause

Look for the standard forms of waste: rework, waiting, unnecessary handoffs, over-processing, duplicate data entry, and defects passed downstream.

Reduce variation, not just the average. A process that takes two days on average but sometimes takes three weeks is harder to live with than one that reliably takes four days, because the tail drives the staffing and the promises.

Distinguish common-cause variation, which is inherent to the process, from special-cause variation, which comes from something identifiable. Reacting to common-cause noise as if it were signal makes processes worse — it adds churn without addressing anything.

Use measurable criteria wherever measurement is available. Where it is not, say the assessment is qualitative rather than dressing an opinion in numbers.

## Project scoping and management

Treat any meaningful task as a scoped project. Manage:

- **Scope** — what is in, and explicitly what is out
- **Sequence and dependencies** — what must precede what, and what blocks on someone else
- **Roles** — who does the work, who decides, who must be informed
- **Risks** — what could derail it, with a mitigation for each
- **Decision points** — where the work forks and someone must choose
- **Quality gates** — the checkpoints where work gets verified before proceeding
- **Change control** — how a mid-course change gets evaluated rather than absorbed silently

Identify the critical path: the chain of dependent work that sets the earliest finish. Effort spent accelerating off-path work does not move the date.

Prevent scope drift. When a request grows past what one pass can hold, restructure it into phases and say why. Phases with defined outputs beat one long effort with a vague finish, because each phase produces something verifiable.

Sequence honestly. A plan that assumes nothing goes wrong is not a plan; it is a best case. Where a date depends on someone else, mark it as dependent rather than committing on their behalf.

## Co-design with stakeholders

Co-design treats the people affected by a solution as participants in building it, not as recipients. Iterative collaboration, transparent communication about constraints, and staged review produce solutions that survive contact with actual users.

**Identify stakeholders early**, and separate three roles that often get conflated: the sponsor who authorizes the work, the users who operate the result, and the consumers who depend on its output. Their needs diverge, and a solution optimized for the sponsor alone tends to fail at the desk.

**Surface user needs, not just sponsor preferences.** The sponsor describes the problem as it appears from above. The person doing the work knows the workarounds, the exceptions, and the reason the obvious fix already failed once.

**Test structure before investing in detail.** Show an outline, a schema, a wireframe, or a worked example while changing it is still cheap. Feedback on a finished artifact arrives too late to change its shape, so people comment on wording instead of structure.

**Ask for feedback at the right altitude.** Ask about structure when structure is the open question; asking "what do you think?" on a full draft invites line edits on decisions that should have been settled earlier.

**Make constraints transparent.** When a request cannot be met, say what constrains it. Stakeholders accept limits they understand and resent limits that appear arbitrary.

**Iterate rather than authoring once.** Two rounds of cheap drafts beat one expensive draft, because the first round reveals what the requirements actually were.

## Decision rationale

Record why a tradeoff went the way it did — the options, the choice, and the reason. Six months later the reasoning is invisible, and someone will reopen a settled decision or, worse, reverse it without knowing what it was protecting against.

Keep it short. A decision log entry needs the decision, the alternatives considered, the reason, and the date.

## House additions (this library)

Deep-method companions when a phase needs more than this summary:

- Root-cause discipline (5 Whys, fishbone, Pareto) → `continuous-improvement-skills:root-cause-analysis`
- Current/future-state mapping → `continuous-improvement-skills:value-stream-mapping`
- Full DMAIC project structure → `continuous-improvement-skills:dmaic-problem-solving`
- Locking improvements into standards → `continuous-improvement-skills:standard-work`
- Facilitated co-design sessions → `continuous-improvement-skills:kaizen-and-codesign`
