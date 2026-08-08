# House of Quality — construction, math, roof, and cascade

Working mechanics for `qfd-house-of-quality`, with a worked dental-app house.

## Contents
1. The rooms of the house
2. WHATs — gathering, hierarchy, and weighting math
3. HOWs — writing measurable characteristics
4. The relationship matrix and importance scores
5. The roof — tradeoff analysis
6. Benchmarks and targets
7. Worked example — dental-app house
8. Cascade mechanics — house to house

## 1. The rooms of the house

```
                      [ roof: HOW × HOW correlations ]
                 [ HOWs: technical characteristics, ↑/↓ ]
[ WHATs + weights ] [ relationship matrix: 9 / 3 / 1 ]  [ customer benchmarks ]
                 [ importance scores (computed)      ]
                 [ technical benchmarks              ]
                 [ targets (the CTQs handed on)      ]
```

Left wall: what customers need, weighted. Ceiling: what engineering can measure and set. Body:
how strongly each HOW serves each WHAT. Roof: how HOWs help or fight each other. Basement: the
arithmetic verdict, the comparisons, and the targets.

## 2. WHATs — gathering, hierarchy, and weighting math

- Sources: co-design/kaizen output (`continuous-improvement-skills:kaizen-and-codesign`),
  interviews, support tickets, complaint logs. Keep the customer's own words — "I know what I'll
  owe before I sit in the chair", not "billing transparency module".
- Group into a 2-level hierarchy (theme → leaf need); matrix only the leaves; aim for 10–25.
- Weight leaves 1–5 (or 1–10). Distribute-100-points forces harder choices than rating scales,
  which cluster at 4–5. Different segments (patients vs. dentists) get separate weight columns —
  don't average them into mush; carry both and let conflicts show.
- **Ratification is the gate:** the LLM may *draft* weights inferred from notes, marked as
  proposals; actual customers/users confirm or correct them before the house's scores are used.

## 3. HOWs — writing measurable characteristics

Each HOW needs: a **name**, a **unit**, a **direction** (↑ more is better, ↓ less is better, ◎
hit a target), and an **owner**. Tests: could two people measure it independently and agree?
Could it go in a spec? Anti-patterns → fixes: "intuitive UI" → steps-to-complete-task,
time-to-first-success; "reliable" → uptime %, error rate; "fast" → p95 latency. A WHAT with no
strong HOW anywhere is a gap in engineering vocabulary — invent the characteristic, don't drop
the need.

## 4. The relationship matrix and importance scores

- Cell values: **strong = 9, medium = 3, weak = 1, blank = 0.** The 9/3/1 spread is deliberate —
  it lets strong relationships dominate so priorities don't blur toward the middle.
- Fill column by column asking "if we move this HOW, which WHATs move?" — then row by row as a
  cross-check ("what serves this need?").
- **Importance of HOW_j = Σ over i ( weight_i × relationship_ij )**, down each column. Normalize
  to % of total for readability.
- Audit before trusting: an **empty row** = a need nothing serves (add a HOW); an **empty
  column** = a characteristic serving no one (cut it or find the need it silently serves);
  a matrix where everything is 9 = nobody made choices.

## 5. The roof — tradeoff analysis

For each HOW pair, mark + (moving one helps the other), − (they fight), or blank. Only the
strong signals matter. Each **negative** cell demands one of: a design idea that breaks the
tradeoff, an explicit compromise with both targets adjusted, or a decision recorded for the
cascade. Tradeoffs left blank in the roof reappear later as integration surprises and schedule
slips — the roof is where they're cheap.

## 6. Benchmarks and targets

- **Customer benchmarks** (right wall): how customers rate you vs. alternatives *per WHAT*, from
  their perception, not your telemetry. A heavily weighted WHAT where you trail is the
  competitive battleground.
- **Technical benchmarks** (basement): measured competitor values per HOW where obtainable.
- **Targets:** one value per HOW, set considering importance score, benchmark gap, and roof
  constraints. The target row — measurable characteristics with numbers — is the CTQ set handed
  to `continuous-improvement-skills:lean-six-sigma-for-software`.

## 7. Worked example — dental-app house

Patient/front-desk WHATs (weights ratified in the co-design session), development HOWs.

WHATs and weights: book/change an appointment without calling (5); know what I'll owe before the
visit (4); insurance "just works" (4); reminders that don't spam me (3); check-in is fast (3).

HOWs (unit, direction): steps-to-book (count ↓); estimate accuracy (% of pre-visit estimates
within $25 of final invoice ↑); eligibility auto-check rate (% of visits verified without staff
touch ↑); reminder configurability (channels × opt-out granularity ↑); check-in time (minutes ↓).

Relationship matrix (9/3/1, blank = 0):

| WHAT (weight)              | steps-to-book | est. accuracy | elig. auto-check | reminder config | check-in time |
|----------------------------|:---:|:---:|:---:|:---:|:---:|
| Book without calling (5)   | 9   |     |     | 3   | 1   |
| Know what I'll owe (4)     |     | 9   | 3   |     |     |
| Insurance just works (4)   |     | 3   | 9   |     | 3   |
| Non-spammy reminders (3)   |     |     |     | 9   |     |
| Fast check-in (3)          | 1   |     | 3   |     | 9   |

Importance = Σ(weight × cell), per column:
- steps-to-book: 5×9 + 3×1 = **48**
- estimate accuracy: 4×9 + 4×3 = **48**
- eligibility auto-check: 4×3 + 4×9 + 3×3 = **57**
- reminder configurability: 5×3 + 3×9 = **42**
- check-in time: 5×1 + 4×3 + 3×9 = **44**

Verdict: **eligibility auto-check leads** — it serves three weighted needs at once, which is
exactly the kind of unglamorous, high-leverage characteristic gut-feel prioritization skips in
favor of visible features. Roof: eligibility auto-check **+** estimate accuracy (verified
coverage feeds better estimates) and **+** check-in time; reminder volume **−** non-spammy
reminders (more reminders serve booking but burn the no-spam need — resolve with preference-
driven cadence rather than more sends). Targets (the CTQs): steps-to-book ≤ 3; ≥ 90% of
estimates within $25; ≥ 80% of visits eligibility-verified untouched; every channel individually
opt-out-able; check-in ≤ 2 minutes. The numbers here are illustrative — the *procedure* (ratified
weights → 9/3/1 → column sums → roof → targets) is the deliverable.

## 8. Cascade mechanics — house to house

House 1's prioritized HOWs + targets become House 2's WHATs, carrying their importance scores as
the new weights:

- **House 1** customer needs → product characteristics (the example above).
- **House 2** product characteristics → module/part characteristics ("eligibility auto-check
  ≥ 80%" → payer-API coverage %, retry policy, fallback-to-manual queue latency).
- **House 3** part characteristics → process/build settings (test coverage on the payer
  integration, monitoring alert thresholds).

Each translation uses the same matrix arithmetic, so a weight a patient assigned in the
co-design session still shapes a retry-policy decision three houses later — that unbroken chain
of custody for customer priority is the entire point of QFD. Cascade only the top-scoring HOWs;
carrying every column through every house is the ceremony that killed Western adoptions.
