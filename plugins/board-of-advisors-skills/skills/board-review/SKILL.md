---
name: board-review
description: >-
  Runs the full Board of Advisors multi-agent swarm — five read-only specialist subagents
  (performance, accuracy/correctness, structure/architecture, clarity/maintainability,
  robustness/edge-cases) launched in parallel over the code under review, then the board-chair
  subagent synthesizing their findings into one deduplicated, ranked revision report that
  optimizes for speed and accuracy while strictly preserving the original deliverable goals.
  Nothing is implemented without explicit user approval. Use when the user asks for a board
  review, board of advisors, full optimization review, performance+accuracy audit, or a deep
  multi-angle code audit. Triggers: board review, board of advisors, run the board, full
  optimization review, performance and accuracy audit, deep code audit, multi-agent review,
  suboptimal code audit, optimize this code thoroughly.
---

# Board of Advisors review

## When to use
- The user asks for a thorough, multi-angle audit of code — "run the board," "full
  optimization review," "find everything suboptimal" — where the goal is speed and accuracy
  improvements that strictly preserve intended behavior.
- A significant module is about to be optimized, hardened, or refactored and the owner wants
  the complete picture before touching it.
- Not for: routine PR review → see `coding-agent-skills:git-and-code-review`. Designing
  multi-agent systems in general → see `coding-agent-skills:agentic-workflow-design`.

## Do it
1. **Extract goals and scope first — the board reviews against goals, not taste.** Identify
   the exact code under review (selection, files, directory, or diff) and restate the
   original goals, intended behavior, and accuracy requirements in a few sentences. If goals
   are ambiguous, ask the user before launching anything; if you must proceed, state your
   assumptions explicitly. Do not expand scope beyond what was given without asking.
2. **Launch the five specialists in parallel** — each is a read-only subagent shipped with
   this plugin (namespaced `board-of-advisors-skills:<name>`):
   - `performance-advisor` — speed, complexity, allocations, hot paths
   - `accuracy-correctness-advisor` — logic, precision, invariants, wrong results
   - `structure-architecture-advisor` — modularity, boundaries, ordering
   - `clarity-maintainability-advisor` — naming, density, dead code, cognitive load
   - `robustness-edgecase-advisor` — validation, failure modes, leaks, races
   Give every specialist the same package: the exact code/files, the restated goals, and the
   instruction to stay read-only and use the canonical Finding schema
   (`references/finding-schema.md`). Launch them in one parallel batch — they are
   independent by design.
3. **Wait for all five, then hand everything to the chair.** Invoke
   `board-of-advisors-skills:board-chair` with the restated goals plus the complete,
   unedited findings from all five specialists. The chair deduplicates, prioritizes
   (accuracy-critical first, then goal-preserving speed wins, then structure, robustness,
   clarity), enforces a written Goal Preservation Check on every proposal, and produces the
   ranked Optimization Review report. Do not synthesize yourself — the chair's strict
   priority order and preservation checks are the control.
4. **Present the chair's report in full**, then offer the concrete next action: "Implement
   any of the prioritized revisions? Which ones?" The board is read-only by construction —
   no advisor edits code, and neither do you at this stage.
5. **Apply only what the user approves.** Implement approved revisions carefully (one at a
   time or as an approved batch), run the chair's Recommended Verification for each (tests,
   checks), and re-verify against the restated goals. For substantial applied changes, offer
   a focused re-run of the relevant specialist as the confirmation pass.
6. **Keep the noise contract.** Specialists cap at their top 8–12 findings; the chair
   delivers roughly ≤15–20 revisions. If the board finds nothing material, the correct
   output is "nothing material" — a clean report is a valid, preferred result, not a
   failure to try hard enough.

## Why / learn
The board works because of three deliberate design choices. **Parallel isolated
specialists** beat one big review for the same reason five focused proofreaders beat one
tired one: each subagent runs in its own context window with a single mission, so the
performance reviewer never gets distracted by naming and the correctness reviewer reads
every boundary condition instead of skimming — and isolation means one advisor's framing
can't anchor another's. **Synthesis as a separate role** exists because merging is a
different cognitive job from finding: the chair holds the strict priority order (accuracy
outranks speed, always — a fast wrong answer is worthless), deduplicates overlapping
findings into root causes, and — critically — is forbidden from inventing findings, which
keeps the pipeline auditable: every final revision traces to a specialist's evidence.
**Goal preservation as the invariant** is what separates optimization from vandalism: every
proposal must state *why the original deliverable survives it*, which forces the burden of
proof onto the change, where it belongs. The read-only-until-approved rule is the same
principle at the workflow level — analysis and mutation are separated so a review can be
trusted not to have quietly "fixed" things, and the human stays the approval gate. The caps,
finally, are respect for attention: an audit that returns 200 findings returns none.

## Common mistakes
- Launching advisors without restated goals → findings drift into taste; goals first, always.
- Running specialists sequentially → slower and lets earlier output anchor later analysis; one parallel batch.
- Synthesizing the findings yourself instead of invoking the chair → the priority order and preservation checks are the chair's controls; use them.
- Letting the chair (or yourself) add findings during synthesis → breaks traceability; merge, reframe, or drop only.
- Implementing "obvious" fixes during the review phase → the board is read-only; approval gates every edit.
- Expanding scope to neighboring files uninvited → review what was given; ask to widen.
- Treating "no significant issues found" as a failed review → a clean board is a valid outcome; say so and stop.
- Skipping verification after applying approved revisions → each revision ships with its Recommended Verification; run it.

## Tailor to your environment
Record your board conventions in `references/your-environment.md`: standing goal statements
per project/module, severity calibration for your domain, the verification commands (test
suites, benchmarks) the chair should recommend, and any additional specialist you've added
to the swarm.

## References
- references/finding-schema.md — the canonical Finding schema, severity/category definitions, and the chair's report structure
- references/your-environment.md — your goal statements, calibration, verification commands (fill in)
