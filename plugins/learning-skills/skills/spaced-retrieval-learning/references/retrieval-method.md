# The retrieval method: authoring, scheduling, interleaving

Research base: the testing effect (Roediger & Karpicke, 2006), the spacing meta-analytic
work of Cepeda and colleagues, and Bjork's desirable-difficulties framework. Successive
relearning — retrieving until correct across multiple separate sessions — comes from the
retrieval-practice literature and combines the first two effects.

## Contents
- [Question-authoring patterns by material type](#question-authoring-patterns-by-material-type)
- [Question difficulty grades](#question-difficulty-grades)
- [Grading buckets and the expanding-interval table](#grading-buckets-and-the-expanding-interval-table)
- [Building the schedule around a deadline](#building-the-schedule-around-a-deadline)
- [The interleaving plan](#the-interleaving-plan)
- [Handling persistent failures](#handling-persistent-failures)
- [The session tracker](#the-session-tracker)
- [Worked example: passage → graded question set](#worked-example-passage--graded-question-set)

## Question-authoring patterns by material type

Author from the source with the answer and its location recorded per item. Aim for items that
are *atomic* (one retrievable fact or move each), *unambiguous* (a knowledgeable person gives
one answer), and *cue-realistic* (the question resembles how the knowledge is actually
summoned in use).

| Material | Good question forms |
|---|---|
| Expository document / textbook chapter | "What is X?"; "Why does X hold?"; "What follows if X changes?"; compare/contrast pairs of nearby concepts |
| Procedure or runbook | "What is the first step when X?"; "What comes after step N, and why that order?"; "What check tells you step N worked?"; generation: "produce the whole procedure from memory" |
| Codebase / conventions | "Where does X live?"; "What is the naming rule for Y?"; "What would break if you did Z the obvious way?"; "Which module owns this responsibility?" |
| Exam syllabus | Mirror the exam's own item formats; weight topics by blueprint weight; add discrimination items between commonly confused options |
| Terminology / vocabulary | Both directions (term→meaning, meaning→term); usage in a sentence; nearest-confusable contrast ("how does X differ from Y?") |
| Rules / regulations / policy | "What does the rule require when X?"; "What is the exception?"; scenario application: "does this fact pattern fall under the rule?"; edge cases that distinguish adjacent rules |

Avoid: questions answerable from the question's own wording; multi-fact omnibus questions
(split them); trivia the user never needs unaided (that is what lookup is for).

## Question difficulty grades

Author each topic across four grades; sessions should climb the grades as the low ones pass.

1. **Recall** — reproduce a fact or definition.
2. **Application** — given a concrete scenario, use the fact.
3. **Discrimination** — decide *which* of two or more similar things applies, and say why
   the others don't. Author these deliberately for anything commonly confused.
4. **Generation / transfer** — produce a procedure, explanation, or solution from memory in
   a context the source never showed.

A topic answered only at grade 1 is not yet usable knowledge; the queue should not consider
a topic solid until grades 2–3 pass.

## Grading buckets and the expanding-interval table

Grade every attempt into one of four buckets and act on it:

| Bucket | What it looks like | Action |
|---|---|---|
| Fluent correct | Right, fast, no hedging | Expand the interval (roughly 2–3× the last gap) |
| Effortful correct | Right after visible work | Repeat the current interval; do not expand yet |
| Partial | Right pieces, wrong or missing pieces | Corrective feedback now; re-ask before the session ends; next gap shrinks one step |
| Wrong / blank | Incorrect, or "I don't know" | Corrective feedback now; re-ask before the session ends; restart at the shortest interval |

The actions are *relative to the last gap*, so they only bite from session 2 on. On session
1 there is no prior gap: schedule everything at the session-2 gap below (1–2 days), and apply
the bucket actions from then. "The shortest interval" for a wrong/blank item means that same
1–2 days — never longer than the next scheduled session.

**Successive relearning rule:** an item is *retired* only after fluent-correct in three or
more separate sessions (not three times in one session). Retired items get one long-gap spot
check before the deadline; a miss un-retires them.

## Building the schedule around a deadline

Expanding gaps, anchored so the final full pass lands shortly before the material is needed:

| Session | Gap from previous | Purpose |
|---|---|---|
| 1 | — | Author the set; first pass, all items |
| 2 | 1–2 days | Relearn misses; expand passes |
| 3 | ~1 week | Interleaved mix; grades 2–3 dominate |
| 4 | ~2–3 weeks | Spot-check retired items; drill the failure list |
| 5+ | ~monthly | Maintenance for "keep forever" material |
| Final | a few days before deadline | Full pass; misses get daily re-asks until the date |

Honest calibration note: Cepeda's work shows the best gap *scales with the retention
interval* — longer retention wants longer gaps — so treat this table as a sane default, not
a law. Cepeda et al. (2008) put a usable ratio on it: the optimal gap runs roughly 10–20% of
the retention interval at week-scale delays and falls to roughly 5–10% at a one-year delay.
So an exam ten weeks out (70 days) wants gaps of roughly 7–14 days; "keep it for a year"
(365 days) wants roughly 18–36 days — about a month, and growing. A held session at a rough
interval still beats a skipped session at a perfect one. Short runway (an exam in ten days)
compresses the whole table; "know it forever" stretches it.

## The interleaving plan

- Put 2–4 *related* topics in each session — related enough to be confusable, distinct
  enough to have different right answers. Confusability is the point: discrimination is
  learned only where confusion is possible.
- Shuffle item order every session; never let the order itself become the cue.
- Convert observed confusions into explicit contrast items ("you gave the X answer to a Y
  question — here is a question that forces the difference").
- Blocked practice (one topic at a time) is acceptable only for the very first exposure to a
  brand-new topic; from session 2 on, it joins the mix.

## Handling persistent failures

An item missed in three separate sessions is treated as a defect in the material, not just
the memory:

1. **Rewrite** — ambiguous wording, or the answer is genuinely multiple facts → split it.
2. **Contrast** — it keeps colliding with a specific neighbor → author a side-by-side
   discrimination item and drill the *pair*.
3. **Anchor** — abstract and slippery → attach a worked example, a concrete case from the
   user's own work, or a mnemonic, and quiz through the anchor first.
4. **Demote honestly** — if the user will always be able to look it up in use, take it off
   the unaided-recall queue and say so. Queue space is for what must be known cold.

## The session tracker

A markdown table per material set is enough; keep it wherever the user keeps notes.

```
| Item | Topic | Grade | S1 | S2 | S3 | Status | Next ask |
|----------------------|----------|---------|----|----|----|--------|----------|
| ach-vs-wire-finality | payments | discrim | W  | P  | F  | active | +2w |
| ach-return-window    | payments | recall  | F  | F  | P  | active | +2d |
```

Codes: F fluent, E effortful, P partial, W wrong. "Status" is active / retired / demoted.
Add S4, S5… columns as sessions accrue.

Read the two rows against the bucket table — both were last asked at the ~1-week S2→S3 gap.
Row 1's latest attempt was fluent, so the gap **expands** 2–3× → ~2 weeks. Row 2's was
partial, so it **shrinks one step** down the schedule table → 1–2 days. Neither retires yet:
retirement needs fluent-correct in three *separate* sessions, and row 2 lost its third.
The assistant reads this to resume ("quiz me on the overdue items") and updates it each
session.

## Worked example: passage → graded question set

Source passage (short, work-flavored):

> A wire transfer settles with immediate finality: once released, the sender cannot recall
> it, only request its return. An ACH credit settles in batches and can be reversed by the
> originator within five banking days, but only for specific error conditions — duplicate
> entry, wrong amount, or wrong account. A check provides no finality at deposit; it can be
> returned unpaid for many reasons, so funds availability is not funds finality.

Graded set the assistant would author (answers kept hidden during the quiz):

- **Recall:** "What does 'finality' mean for a wire transfer once it is released?"
- **Recall:** "Within what window, and for which error conditions, can an ACH credit be
  reversed by its originator?"
- **Application:** "A vendor payment went out this morning to the wrong account. It was sent
  by wire. What are your options?" (Then re-ask later with "…sent by ACH.")
- **Discrimination:** "Your bank shows a deposited check as 'available.' A colleague says
  the payment is final. What's wrong with that claim, and which instrument *would* make it
  final?"
- **Generation:** "From memory: rank wire, ACH credit, and check from most to least payment
  finality, and give the one-line reason for each rank."

Notes on the authoring: the two recall items are atomic (one per instrument-fact); the
application pair interleaves by re-running the same scenario across instruments; the
discrimination item targets the passage's designed confusion (availability vs. finality);
the generation item forces reconstruction of the whole structure. That progression — not
five paraphrases of "what is a wire?" — is what a graded set means.
