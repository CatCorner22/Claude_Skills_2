---
name: spaced-retrieval-learning
description: >-
  Turns any material — a document, a skill, a codebase, an exam syllabus — into retrieval
  practice: the assistant authors recall questions at graded difficulty, quizzes the user
  without showing answers first, grades each attempt against the source, and schedules
  re-asks at expanding intervals, interleaving related topics and retrieving until correct
  across multiple sessions (successive relearning). Tracks what keeps failing and turns it
  into focused remedial material. Built on the testing effect (Roediger & Karpicke), spacing
  over massing (Cepeda), and desirable difficulties (Bjork). Use when the user wants material
  to stick — for an exam, a new domain, a standard they keep re-looking-up — or asks to be
  quizzed rather than lectured. Triggers: spaced repetition, retrieval practice, quiz me,
  make this stick, study plan, flashcards, help me remember this, test me on.
---

# Spaced retrieval (make it stick)

Re-reading feels like studying; retrieval *is* studying. Roediger & Karpicke (2006) showed
that testing yourself on material beats re-reading it on delayed tests — even though
re-reading wins on immediate tests and feels more productive. This skill applies that
finding, plus spacing (Cepeda's meta-analytic work) and interleaving, to any material the
user needs to keep: the assistant does the historically expensive part — authoring good
questions, withholding answers, grading, and bookkeeping the schedule.

## When to use
- Making any material durably recallable: a regulation, a domain the user is onboarding
  into, a codebase's conventions, another skill in this library, an exam syllabus, a
  language's terminology.
- The user asks to be quizzed, wants flashcard-style drilling, or wants a study plan with
  actual sessions rather than a reading list.
- Something keeps being re-looked-up and the user wants it in their head instead.
- Not for: exam *domain content* — e.g. CTP treasury material and blueprint weighting
  (archived: `public-sector-treasury-skills:ctp-exam-prep`, restorable from `archive/`);
  this skill owns the method, not the material. A domain or exam-prep source pairs
  naturally: run its question bank on this skill's schedule.
- Not for: machine learning in the model-training sense → see the `machine-learning-skills`
  plugin (start at `machine-learning-skills:ml-project-framing`).
- Not for: building a *performable* skill (debugging, negotiating, writing under pressure) →
  see `learning-skills:deliberate-practice`. Rough boundary: that skill trains doing, this
  one trains knowing; drills that surface facts worth keeping hand them here.
- To make the study session itself automatic — showing up, not the content → see
  `learning-skills:habit-design`.

## Do it
Question-authoring patterns by material type, the interval table, the interleaving plan, and
a worked example are in `references/retrieval-method.md`.

1. **Scope the material and the deadline.** Ask what has to be recalled *unaided* versus
   merely recognized or looked up — only the former earns queue space. Note the retention
   goal (exam date, "forever"), because it stretches or compresses the interval schedule.
2. **Author a graded question set.** The assistant writes it from the source: factual recall
   ("what is X?"), application ("given this scenario, what applies?"), discrimination
   ("which of A/B fits here, and why not the other?"), and generation ("produce the
   procedure from memory"). Every item carries its answer and source location — kept by the
   assistant, hidden from the user.
3. **Quiz without showing answers first.** One question at a time; wait for a real attempt.
   "I don't know" is an acceptable answer and useful data — better than a hint that turns
   retrieval into recognition. After the attempt (and only after), give the correct answer
   with brief corrective feedback and the source location.
4. **Grade into buckets and schedule re-asks.** Fluent-correct expands the interval;
   effortful-correct repeats it; partial or wrong shrinks it and re-asks before the session
   ends. An item leaves the queue only after correct recalls in *multiple separate sessions*
   — that is successive relearning, and it is the difference between "got it once" and
   "have it."
5. **Interleave rather than block.** Mix 2–4 related topics within a session and shuffle
   order between sessions, so each question also forces the meta-question "which knowledge
   applies here?" — the question real use always asks.
6. **Track what keeps failing and turn it into focused material.** An item missed three
   times is a signal about the item, not just the learner: rewrite it, split it, build a
   contrast question against whatever it's being confused with, or attach a worked example
   or mnemonic. Persistent-failure handling is in the reference.
7. **End every session with the plan for the next one.** State which items return when, at
   expanding gaps anchored to the deadline (table in the reference), and log results in a
   simple tracker (a markdown table is enough). Offer to run the next session on request —
   "quiz me on the overdue items" resumes from the tracker.

**Division of labor.** The assistant carries everything that made this method historically
expensive — authoring good questions, withholding answers, grading against the source, and
bookkeeping the intervals. The user's whole job is the one thing that cannot be delegated:
the honest, unaided retrieval attempt. Guessing before peeking, admitting blanks, and not
self-upgrading a shaky answer to "correct" are what keep the schedule's data real — a
tracker fed by flattered grades schedules the wrong items.

## Why / learn
**The testing effect.** Retrieving a memory strengthens and re-encodes it in a way that
re-exposure does not; Roediger & Karpicke (2006) found retrieval practice outperforming
repeated study on delayed tests even while students *predicted* the opposite. That
mis-prediction is the trap this skill exists to close: the strategy that feels best performs
worst at a delay.

**Spacing beats massing.** Cepeda and colleagues' meta-analytic work shows spaced study
reliably beats massed study for delayed retention, with the useful gap scaling with how long
the material must be retained. Cramming genuinely works for tomorrow — and evaporates. The
schedule here is expanding-and-roughly-right rather than precisely optimized, because a
session actually held beats a perfect interval skipped.

**Desirable difficulties (Bjork).** Conditions that make studying feel harder and slower —
spacing, interleaving, testing, generating before being told — improve retention and
transfer. The inversion to internalize: *fluency is a lie*. Ease of processing during study
feels like knowledge but only measures familiarity. Highlighting and re-reading feel
productive precisely because they maximize fluency while adding little retrievability —
recognition masquerading as recall. Struggle during retrieval is not a symptom of failing
study; it is the signal that the study is doing something.

**Why the answer stays hidden.** Shown the answer alongside the question, the mind verifies
instead of retrieves — a recognition event with little strengthening. Even a failed retrieval
attempt followed by corrective feedback beats being handed the answer up front.

**Why interleave.** Blocked topics let the learner answer from context ("this is the ACH
chapter, so the answer is ACH-shaped"). Interleaving removes the crutch and trains
discrimination between similar ideas — which is what an exam, and reality, actually test.

## Common mistakes
- Showing the answer with the question, or hinting on hesitation → recognition, not
  retrieval; let the attempt finish, then correct.
- Cramming the night before and concluding it worked → it did, for a day; check retention at
  a delay before trusting the method.
- Retiring an item after one correct answer → successive relearning: correct across multiple
  sessions before it leaves the queue.
- Blocking a session by topic → interleave related topics; blocked wins the session and
  loses the exam.
- Authoring only definition-recall questions → grade difficulty up to application and
  discrimination; those are the forms use demands.
- Trusting "this feels easy now" from re-reading → fluency illusion; the only honest measure
  is an unaided retrieval attempt.
- Making the quiz feel like judgment → errors followed by immediate correction are the
  productive path; grade the item, not the person.
- Guilt-tracking missed sessions with streaks → a missed session is a scheduling fact; for
  making sessions automatic, see `learning-skills:habit-design`.

## Tailor to your environment
Record your standing setup in `references/your-environment.md`: the materials you drill
recurrently, exam or certification dates, preferred session length and cadence, and where the
question bank and tracker live. Keep committed content structural — actual exam registrations,
employer-specific material, or anything sensitive goes in `your-environment.private.md`
(git-ignored), never in a committed file.

## References
- references/retrieval-method.md — question-authoring patterns by material type, the
  grading buckets and expanding-interval table, the interleaving plan, and a worked example
  turning a short passage into a graded question set
- references/your-environment.md — your recurring materials, deadlines, cadence, and tracker
  location
