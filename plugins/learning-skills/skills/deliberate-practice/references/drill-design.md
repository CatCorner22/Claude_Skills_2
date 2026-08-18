# Drill design: patterns, ladders, feedback

Research base: Ericsson's expert-performance research — deliberate practice, mental
representations, and the purposeful/deliberate distinction. The "10,000-hour rule" is a
popularization Ericsson disputed; hour counts appear nowhere in this file on purpose.

## Contents
- [The session template](#the-session-template)
- [Drill patterns by skill type](#drill-patterns-by-skill-type)
- [Difficulty-ladder design](#difficulty-ladder-design)
- [Feedback that names the gap, not the person](#feedback-that-names-the-gap-not-the-person)
- [The rep log](#the-rep-log)
- [Purposeful vs. deliberate: the honest label](#purposeful-vs-deliberate-the-honest-label)

## The session template

Every session, regardless of skill type:

1. **Target (1 min).** Restate the single target and the current ladder rung. If the log
   shows the last session ended mid-rung, resume there.
2. **Warm rep (1 rep).** One rep at the *previous* rung to reload the representation. At
   rung 1 there is no previous rung: run one rep of the target with the scaffolds still on
   (notes allowed, no time limit) instead.
3. **Working reps (bulk of session).** Reps at the current rung. After each rep: feedback
   (formula below), one next-rep instruction, immediately rep again. Stop the session while
   attention is still full — a session that ends sloppy trains sloppy.
4. **Ladder decision (1 min).** Clean-rep count vs. the rung's gate: advance, stay, or step
   down. Named out loud, with the reason.
5. **Log (1 min).** One line per rep; one line for the session's next target.
6. **Hand-off check.** Any rule/pattern surfaced that should be *known cold* → send it to
   `learning-skills:spaced-retrieval-learning`.

Session sizing: reps should be short enough that several fit in a sitting with full attention
on each. If a single rep takes 30+ minutes (e.g., a long brief), drill an extracted slice
(the opening two paragraphs; the single cross-examination exchange), not the whole artifact.

## Drill patterns by skill type

**Analysis / diagnosis (debugging, incident triage, financial-statement anomalies).**
The assistant plants a defect in a realistic artifact and plays the system: the user
interrogates ("what does the log show at 14:02?", "run the query"), the assistant answers
only what the probe would truly reveal. Target examples: hypothesis discipline (state it
before probing), cheapest-probe-first ordering, knowing when to stop confirming. Ladder:
subtler defects, noisier evidence, multiple interacting causes, time pressure.

**Writing.** Constraint exercises: rewrite the paragraph at half its length with no meaning
lost; write the same finding for an analyst and then for a board member; every sentence
carries exactly one claim; forbidden-crutch drills (no passive voice, no "there is/are").
The assistant supplies source material, enforces the constraint mercilessly, and shows a
contrast version after the attempt — never before. Ladder: tighter limits, worse source
material, faster turnaround, combined constraints.

**Argument / negotiation / examination.** Roleplay with the assistant as the counterparty,
opposing counsel, or hostile questioner, playing one calibrated persona per rung. Target
examples: keeping concessions conditional; returning to interests when positions lock;
answering only the question asked under cross. The assistant stays *in role* during the rep
and steps out only for feedback — mixing the two blunts both. Ladder: counterparty
competence and hostility, information asymmetry, time pressure, audience present.

**Code (beyond debugging).** Reading kata: given an unfamiliar function, predict its output
for an input before running it — the assistant scores the prediction. Refactoring kata: make
this change with all tests green at every intermediate step. API-recall kata: implement
without docs, then diff against docs. Ladder: bigger units, worse code, less familiar
idioms, stricter step discipline.

Common structure across all four: the drill makes the target behavior *unavoidable and
frequent* — several forced occurrences per session — where real work might surface it once a
month. Frequency of the target, not realism of the wrapper, is what to optimize.

## Difficulty-ladder design

- **Scale one dimension at a time.** Candidate dimensions: time pressure, ambiguity/noise,
  volume, opposition quality, scaffolds removed (notes allowed → no notes; hints → none).
  Raising two at once makes failure undiagnosable.
- **Define the gate before the session:** what counts as a clean rep (observable, binary if
  possible) and how many buy the next rung — two or three consecutive is a sane default.
- **Step down without ceremony.** Repeated failure at a new rung means the previous rung
  wasn't actually stable, or the increment was too big; both are design facts, not verdicts
  on the user.
- **Keep the success rate in the productive band.** Reps that nearly always succeed are
  comfort; reps that nearly always fail are flailing — neither trains. When most reps
  succeed only with visible effort, the rung is right.
- **Re-baseline occasionally** with an unassisted, full-context rep (no drill wrapper) to
  confirm the drilled component transfers into whole performance — the point was never the
  drill itself.

## Feedback that names the gap, not the person

Three-part formula, delivered immediately after the rep:

1. **Observation** — what happened, located precisely: "In turn 3 you conceded the deadline
   without asking for anything."
2. **Contrast** — what the stronger move was, concretely: "A conditional form: 'we can do
   that date if the scope drops X.'"
3. **One instruction** — a single thing to do differently in the very next rep: "Next rep,
   no concession leaves your mouth without an *if*."

Rules that keep it working:
- One instruction per rep. Three corrections at once produce zero changes.
- The gap, never the person: "the concession was unconditional," not "you're too agreeable."
  Person-level labels give the learner nothing to *do* and something to defend.
- Include what was strong when true — not as a courtesy, but because knowing what to keep is
  information; omit ritual praise.
- Immediate beats complete. A short correction now outperforms a thorough review at
  session's end, because each subsequent rep either reinforces or corrects the pattern.

## The rep log

One line per rep, one file per skill:

```
| # | Rung | Rep summary | Gap named | Next-rep instruction | Clean? |
|---|------|-------------|-----------|----------------------|--------|
| 14 | R3: +time pressure | vendor call, deadline push | turn-3 unconditional concession | every concession carries an *if* | no |
| 15 | R3 | same scenario, reshuffled | — | hold | yes |
```

Plus one session-footer line: `Next target: <target> @ <rung>`. Recurring entries in the
"gap named" column are the next targets — the log is where the curriculum comes from.

## Purposeful vs. deliberate: the honest label

Ericsson's own hierarchy, kept honest:

- **Naive practice** — repetition of the whole activity, no target, no feedback. This is
  "experience," and it plateaus.
- **Purposeful practice** — self-designed: specific target, edge-of-ability, full attention,
  immediate feedback, adjustment. Effective, and it is what this skill builds.
- **Deliberate practice** (strict sense) — purposeful practice under a training regimen
  designed by a qualified coach, in a field with established training methods and objective
  performance standards.

The assistant approximates the coach's two cheapest functions — drill construction and fast
feedback — and approximates them well for language-heavy, judgment-heavy skills. It does not
bring a validated curriculum, field-calibrated standards, or the trained eye for errors the
learner cannot yet perceive. Where those exist (a bar-advocacy course, a code-review mentor,
a negotiation instructor), say so and recommend them; the drill practice here then becomes
the between-sessions work, which is exactly where it belongs.
