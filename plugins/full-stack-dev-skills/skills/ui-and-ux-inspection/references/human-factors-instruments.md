# Human-factors instruments

Two classical instruments — Fitts's law for pointing/tap-target findings and NASA-TLX for
the cognitive-load pass — with the rules for carrying them into this skill's finding
schema honestly. Provenance: compiled from the standard human-factors canon at
search-snippet level (the ISO standard text is paywalled); verify wording against the
source before quoting a standard verbatim.

## Contents
1. [Fitts's law](#1-fittss-law)
2. [NASA-TLX](#2-nasa-tlx)
3. [Carrying the instruments into findings](#3-carrying-the-instruments-into-findings)
4. [Honest limits](#4-honest-limits)

## 1. Fitts's law
Movement time to acquire a target grows with distance and shrinks with target size:

```
MT = a + b · log2(D/W + 1)
```

where `D` is the distance to the target's center, `W` its width along the axis of
approach, and `a`, `b` are empirically fitted device/population constants. The logarithm
is the **index of difficulty (ID)**, in bits — it is computable from DOM geometry alone,
which is what makes the law usable inside a static inspection.

Design implications for findings:
- **Bigger and closer beats smaller and farther.** Frequent or destructive-recovery
  actions deserve large, near targets; a tiny icon far from the pointer's resting area is
  a quantifiable cost, not a taste judgment.
- **Screen edges and corners are effectively infinite-width targets** — the pointer stops
  there, so `W` is unbounded along that axis. Toolbars, docks, and dismiss actions gain
  from edge placement; a control floating 4 px inside the edge forfeits this for nothing.
- **Tap-target findings can cite the index of difficulty**: report the measured `D` and
  `W` and the resulting ID for the current versus proposed placement/size. That turns
  "this button feels small" into "ID drops from 4.9 to 3.1 bits at the same distance".
- Pair with, not instead of, the accessibility pass: WCAG target-size minima are a floor;
  Fitts explains why generous targets keep paying above the floor.

ISO 9241-9 frames pointing-device efficiency as **throughput** (bits/second, ID divided
by movement time averaged over a standardized multi-directional tapping task) so that
devices and designs can be compared on one number [snippet-only — paywalled standard;
verify against the standard's text before citing clauses]. Use the framing, not fabricated
numbers: throughput is measured with instrumented users, never derived from a screenshot.

## 2. NASA-TLX
A post-task subjective workload instrument: six subscales, each rated on a 0–100 scale
immediately after the task —
- **Mental demand** — how much thinking, deciding, remembering, searching.
- **Physical demand** — how much physical activity the task required.
- **Temporal demand** — how much time pressure was felt.
- **Performance** — how successful the person judges they were (scored so that better
  performance means lower workload contribution).
- **Effort** — how hard they had to work to reach that level of performance.
- **Frustration** — how insecure, discouraged, irritated, or annoyed they felt.

The original protocol adds pairwise weighting of subscales; the unweighted average
("raw TLX") is a common simplification in practice [snippet-only].

Administration discipline (what makes scores comparable):
- Administer **immediately after the task**, before discussion or another task dilutes
  the impression.
- Use **identical wording and scale anchors every time** — reworded subscales are a
  different instrument, and cross-session comparisons silently break.
- Keep the task constant: TLX scores attach to a task on a design, not to a design.

Use in this skill: the six subscales are a **structured rubric for the cognitive-load
pass**. When walking a critical process (choices, progressive disclosure, forms,
feedback), ask of each step: what drives mental demand here (recall vs recognition,
cross-referencing, mental arithmetic)? temporal demand (timeouts, auto-advancing steps)?
frustration (validation losses, dead ends)? Each subscale that flags becomes a candidate
finding with a named driver — sharper than an undifferentiated "high cognitive load".

## 3. Carrying the instruments into findings
Conform to references/finding-schema.md — read it first; these instruments add no new
fields, they discipline existing ones.
- **severity**: rate the user impact as usual (task success, time-on-task, error rate) —
  an ID regression on a rarely used control can still be `low`.
- **confidence**: DOM-measured geometry (`D`, `W`, computed ID) is observed evidence and
  can carry `high` confidence *about the geometry*; any predicted movement time or
  workload score is inference — cap the finding's confidence at `medium` and say which
  part is which in `observed_evidence`.
- **evidence_type**: geometry and walkthrough results are `["code", "runtime"]` as
  applicable; instrument-derived predictions are inference — never list them as if they
  were user measurements.
- **heuristics**: tag e.g. `fitts-index-of-difficulty` or `tlx-mental-demand` /
  `tlx-frustration` so the backlog can be filtered by driver.
- **standards**: cite `ISO 9241-9 (throughput framing)` only for framing; WCAG target-size
  criteria remain the enforceable standard.
- **verification**: state the re-check — recompute ID after the layout change; re-run the
  structured TLX-rubric walkthrough on the same task with identical wording.

## 4. Honest limits
Real Fitts measurement fits `a` and `b` from instrumented pointing trials with live
users; real TLX scores come from users rating their own completed task. A static
inspection has neither — here both instruments are **design-heuristic proxies**: the ID
is real geometry, but the movement-time claim is a model prediction, and a TLX-structured
walkthrough is the inspector's judgment organized by six subscales, not workload data.
This extends the skill's standing evidence-vs-inference discipline (the same rule that
forbids calling a static hierarchy check "eye tracking"): label such findings as
model-based or rubric-based inference, keep predicted numbers out of the
`observed_evidence` field, and when a finding would only stand on measured throughput or
measured workload, pose it as a human-validation prompt instead of asserting it.
