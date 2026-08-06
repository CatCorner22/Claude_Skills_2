# Command doctrine — adaptive command, OODA, Toyota flow, co-design, writing

Preserved near-verbatim from the source spec (project-command-center v1.0.0).

Contents: §1 Adaptive command · §2 OODA, three nested loops · §3 Toyota-inspired flow ·
§4 Co-design · §5 Writing discipline and the ambiguity audit · §6 Smart Brevity frame

## §1 Adaptive command

- Expect an intelligent environment: users, attackers, dependencies, regulators, and
  production systems do not follow the plan merely because the plan requires it. Test
  plans under adaptation, denial, delay, and partial information.
- Decentralize with clear intent: shared purpose, bounded autonomy, observable outcomes,
  rapid feedback. Decentralization without clear intent is fragmentation; central control
  without local authority is brittleness.
- Do not confuse instrumentation with understanding. Dashboards and summaries reinforce a
  wrong orientation unless the underlying assumptions are challenged.

## §2 OODA, three nested loops

- FAST (minutes to a day): failing tests, logs, user corrections, blocked dependencies →
  pick the next smallest useful action and instrument it.
- DELIVERY (pull request to release): cycle time, rework, escaped defects, WIP, blocked
  time → adapt scope, sequence, testing, rollout.
- STRATEGIC (milestone+): changed user needs, architecture limits, regulation, economics
  → reassess assumptions, options, commitments.

Orientation is the decisive element: it determines what you notice. Tempo comes from
better orientation, shorter feedback paths, smaller reversible actions, and faster
recovery — not hurried decisions. For each consequential loop, record: observation,
interpretation, confidence, decision, expected outcome, actual outcome, next trigger. No
retrospective storytelling in place of a learning log.

## §3 Toyota-inspired flow, translated to software

- Jidoka: stop the line on abnormality — failing CI, security gates, visible blocked
  states, rollback controls. Defects do not flow downstream.
- Andon: abnormalities are highly visible signals with owners, never quiet.
- Pull and JIT: small vertical slices, WIP limits, start work only when capacity and
  inputs exist.
- Inventory is waste: speculative features, unmerged branches, oversized backlogs, stale
  docs, unvalidated code.
- Genchi genbutsu: reproduce the failure, read the real code path, inspect real data. Do
  not reason exclusively from reports.
- Kaizen and standard work: document the best-known procedure, use it, update it on
  evidence. Root-cause analysis never stops at "human error."
- Respect for people: sustainable pace, stop-the-line authority, psychologically safe
  problem reporting.
- Software is not vehicle assembly: variation and discovery are often the work. Optimize
  time from identified need to validated outcome, not utilization.

## §4 Co-design

Map stakeholders: primary users, operators, maintainers, support, people exposed to
failure, people excluded by the current design, decision-makers. Make decision rights
explicit. The binding control is FEEDBACK CLOSURE: every material contribution gets a
visible disposition — what was said, what changed, what did not and why, who owns
follow-through, when it will be validated. Consultation after the consequential decisions
are fixed is ceremony; call it that.

## §5 Writing discipline (contract-drafting rules for technical text)

- Standard English, active voice when the actor matters, actor near the action, one
  principal requirement per sentence, terms defined once, no needless synonyms.
  Distinguish obligations, prohibitions, permissions, recommendations, and statements of
  fact consistently.
- Never adopt wording solely because it is called "tested," "standard," "market," or
  "court-approved." Litigation is a dispute signal and a source of cautionary examples,
  not proof of drafting quality. State the intended meaning directly.
- Run ambiguity audits across thirteen types: lexical, syntactic, pronoun, modifier,
  coordination, quantifier, temporal, conditional, exception, cross-reference, unit,
  boundary, actor. Ambiguity permits multiple readings; vagueness leaves fuzzy
  boundaries. Bound or remove "reasonable," "promptly," "material," "regularly," "as
  needed" — with thresholds, factors, examples, an owner, or a decision process.

For the full writing system see `writing-skills:adams-smart-brevity` (professional
register) and `writing-skills:adams-plain-grade` (accessible register).

## §6 Smart Brevity frame (default update structure)

**What changed → Why it matters → Evidence → Decision or blocker → Next action, owner,
trigger → Chicken Little watch.**

Brevity moves optional detail below the decision-critical message. It is never permission
to conceal uncertainty, drop conditions, suppress dissent, or leave ownership unstated.
