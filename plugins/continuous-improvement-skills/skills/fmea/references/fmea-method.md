# FMEA method (reference)

The seven steps expanded, anchored 1–10 rating scales adapted to office/transactional processes,
the Action-Priority-vs-RPN story, and a worked bank-reconciliation FMEA.

## Contents
- The seven steps, expanded
- Anchored rating scales (Severity, Occurrence, Detection)
- Action Priority vs RPN
- Worked example: bank-reconciliation FMEA
- Living-register cadence

## The seven steps, expanded

1. **Scope and structure analysis.** Fix what is in and out, then build the structure tree:
   system → subsystem → step. For a process FMEA: the process (daily bank reconciliation) →
   stages (load statement, auto-match, manual match, investigate breaks, post adjustments) →
   tasks within each stage. Each FMEA covers one coherent slice of the tree.
2. **Function analysis.** For every element in the tree, write its function as a measurable
   requirement: *what must it do, to what standard?* "Parse rule extracts the full remittance
   reference from every 88-record continuation." A function stated fuzzily produces failure
   modes you cannot rate.
3. **Failure analysis.** For each function, enumerate:
   - **Failure mode** — the way the function is not performed (no match, wrong match, partial
     parse, duplicate load). A mode is observable at the element itself.
   - **Effect** — the consequence experienced upstream/at the system level (misstated cash
     position, silent wrong posting, wasted investigation time). Effects carry the Severity.
   - **Cause** — the downstream mechanism that produces the mode (file re-transmission, parse
     rule truncation, tolerance set too wide). Causes carry the Occurrence.
   Chain them explicitly: cause → mode → effect. One mode can have several causes and several
   effects; give each cause its own row so actions stay targeted.
4. **Rate S, O, D** using the anchored scales below. Rate the *effect* for Severity, the *cause*
   for Occurrence, and the *current controls* for Detection. Rate current state, not hoped-for
   state. Drafted ratings (including LLM-drafted ones) are adjudicated by the process owner
   before entering the register.
5. **Prioritize by Action Priority** (High/Medium/Low) using the logic below — not by S×O×D.
6. **Take action and re-rate.** Prevention actions reduce Occurrence; detection controls reduce
   the Detection score (better = lower). Severity only moves if the process is redesigned so the
   effect itself is smaller. Record action, owner, date; re-rate the row once the action is real.
7. **Keep it living.** Re-run on every incident (was the mode listed? were O and D honest?), on
   every process/rule change, and on a standing cadence.

## Anchored rating scales (Severity, Occurrence, Detection)

Adapted to office/transactional processes. Calibrate the anchors once to your own volumes and
materiality, then hold them fixed so ratings compare across rows and across time.

### Severity (of the effect) — how bad if it happens
| S | Anchor (transactional/finance processes) |
|---|---|
| 9–10 | Regulatory breach, misstated financial statements, unrecoverable loss of funds, undetected fraud path |
| 7–8 | Material error reaching a customer, bank, or the GL; costly recovery; audit finding |
| 5–6 | Error caught downstream but causing rework across teams, missed close/SLA dates |
| 3–4 | Localized rework; delay absorbed within the team; no external impact |
| 1–2 | Cosmetic; negligible effect on outcome |

### Occurrence (of the cause) — how often it arises
| O | Anchor |
|---|---|
| 9–10 | Expected almost every cycle (daily process: most days; ≥1 in 10 items) |
| 7–8 | Frequent — several times a month; ~1 in 100 items |
| 5–6 | Occasional — monthly-ish; ~1 in 1,000 items |
| 3–4 | Rare — a few times a year; ~1 in 10,000 items |
| 1–2 | Never seen here; barely conceivable given current controls |

### Detection (by current controls) — will you catch it before it hurts? (10 = worst)
| D | Anchor |
|---|---|
| 1–2 | Failure is blocked or flagged automatically before any impact (validation rejects it) |
| 3–4 | Surfaces automatically in a report someone reliably works (e.g. the unreconciled report) |
| 5–6 | Caught by a routine human review that usually happens (sign-off, tie-out) |
| 7–8 | Only found if someone happens to look; sampling; downstream complaint |
| 9–10 | No current control would surface it — it silently succeeds *looking* correct |

The Detection question for auto-matching rule sets is exactly this scale: a failed match that
lands in the unreconciled report is a D 3–4; a *wrong* match that auto-posts cleanly is a D 9–10 —
which is why wrong-match modes usually dominate the Action Priority even at lower Occurrence.

## Action Priority vs RPN

The classical ranking multiplied the three ratings into a **Risk Priority Number** (RPN = S×O×D,
range 1–1000) and worked the biggest numbers first. The arithmetic has a flaw: multiplication
treats the three dimensions as interchangeable, so S=9, O=2, D=3 gives RPN 54 while S=3, O=6, D=6
gives 108 — the trivial-but-common annoyance outranks the near-catastrophe. Teams gaming a single
number also learned to argue Detection down a point to duck a threshold. The harmonized AIAG-VDA
handbook replaced RPN with an **Action Priority table** — a lookup over the (S, O, D) combination
in which Severity dominates, then Occurrence, then Detection `[snippet-only]`.

Working logic (use this if you don't carry the full published table):
- **High** — S 9–10 with anything beyond minimal O or D; or S 7–8 with mid-or-worse O and D.
  Action is required, or the current risk must be explicitly accepted by the owner in writing.
- **Medium** — mid-range combinations (e.g. S 5–8 with moderate O/D). Action should be taken;
  justify if not.
- **Low** — low S, or higher S with both O and D excellent. Action discretionary.

The generalizable lesson: any scheme that compresses multi-dimensional risk into one arithmetic
score can let the dimension you least afford to ignore be averaged away. Order the dimensions by
dominance instead.

## Worked example: bank-reconciliation FMEA

Process: daily bank reconciliation (statement load → auto-match → manual match → investigate →
adjust). Break types are failure modes. Ratings shown as adjudicated examples — yours will differ.

| Step | Failure mode | Effect (S) | Cause (O) | Current control (D) | S | O | D | AP | Action |
|---|---|---|---|---|---|---|---|---|---|
| Load | Duplicate statement line loaded | Cash overstated; double match possible | Bank re-transmits file; loader lacks dedupe key | Loader warning, sometimes ignored | 7 | 4 | 6 | High | Prevention: reject duplicate (date+ref+amount) keys at load |
| Load/parse | Truncated addenda (continuation record dropped) | Reference lost → auto-match fails or mismatches | Parse rule reads first record only | None — line just looks reference-poor | 6 | 6 | 8 | High | Fix parse rule; add parse-completeness check |
| Auto-match | Wrong pair matched inside tolerance | Real missing item hidden; books quietly wrong | Tolerance too wide on one-to-one rule | None — match posts cleanly | 8 | 3 | 9 | High | Tighten tolerance; require reference key, not amount-only |
| Auto-match | Valid match not made | Line sits unreconciled; rework | Date window too narrow for weekend lag | Unreconciled report, worked daily | 3 | 6 | 3 | Low | Widen window after evidence review |
| Adjust | In-tolerance difference dropped, not posted | Book balance drifts | Writer nets difference silently | Month-end tie-out | 6 | 3 | 5 | Medium | Auto-post difference as external transaction |

Read the table the way the method intends: the D=9 wrong-match row outranks the noisy-but-visible
failed-match row despite lower Occurrence — silent success is the enemy, visible failure is cheap.

## Living-register cadence

- **After every incident:** find the row (or the missing row). Adjust O/D honestly; add the mode
  if absent. The incident post-mortem itself belongs to
  `continuous-improvement-skills:root-cause-analysis`; feeding its output back here is what makes
  the FMEA a living document rather than a go-live artifact.
- **On every rule/process change:** re-rate affected rows; new rules get new failure rows before
  go-live, not after.
- **Standing cadence:** review the High rows and open actions on a fixed rhythm the owner sets.
