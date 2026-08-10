# Evals — learning-skills:spaced-retrieval-learning

## 1. Positive trigger (should load the skill)
> "I keep re-looking-up the difference between wire, ACH, and check finality every time it
> comes up. Here's the page from our payments guide — make this stick. Quiz me, don't just
> summarize it."

Expected: skill loads and runs the method rather than summarizing. It scopes what must be
recalled unaided; authors a graded question set from the passage (recall → application →
discrimination → generation), keeping answers hidden; quizzes one question at a time and
waits for a real attempt before revealing anything; grades attempts into buckets
(fluent/effortful/partial/wrong) with corrective feedback and source location after each
attempt; ends the session by scheduling re-asks at expanding intervals and starting a
tracker; states that items retire only after correct recall across multiple separate
sessions (successive relearning), and interleaves the three instruments rather than blocking
them.

## 2. Near-miss (should NOT load this skill)
> "I'm sitting for the CTP in November. Build me a study plan across the exam domains with
> practice questions weighted by the blueprint."

Expected: `public-sector-treasury-skills:ctp-exam-prep` owns CTP domain material, blueprint
weighting, and CTP-style questions. This skill supplies only the generic retrieval method;
if it loads first on an explicitly CTP request, its description is over-triggering. (The
correct composed behavior: ctp-exam-prep supplies the material and may run its question bank
on this skill's schedule.)

## 2b. Near-miss (closer — should NOT load this skill)
> "I want the model to learn the seasonality in our daily receipts series and improve as new
> data arrives."

Expected: "learn" here is machine learning — model training, not human memory. Routes to the
`machine-learning-skills` plugin (e.g., `machine-learning-skills:time-series-forecasting` or
`machine-learning-skills:ml-project-framing`), not to a study-session skill.

## 3. Quality rubric
A good response:
- **Does the task:** authors atomic, unambiguous questions at graded difficulty from the
  actual source (not generic trivia); quizzes without showing answers first and treats
  "I don't know" as data rather than prompting with hints; grades into the four buckets and
  applies the interval rule per bucket (expand / repeat / shrink+re-ask); re-asks misses
  before the session ends; interleaves related topics and shuffles order between sessions;
  produces a concrete next-session schedule anchored to the user's deadline and a tracker
  the next session can resume from; converts thrice-missed items into rewritten, split,
  contrasted, or anchored material — or honestly demotes them to lookup.
- **Teaches:** explains the testing effect (Roediger & Karpicke — retrieval beats re-reading
  at a delay, opposite of how it feels), spacing over massing (Cepeda — useful gap scales
  with retention interval), and desirable difficulties (Bjork — fluency is a misleading cue;
  struggle during retrieval is the signal), including why highlighting and re-reading feel
  productive and aren't.
- **Stays honest:** presents the interval table as a sane default rather than an optimized
  law; cites the research at author level without invented statistics or precise "optimal
  interval" numbers; doesn't claim mastery from one correct answer (successive relearning
  gate); routes exam-domain content, performable-skill training, and session-attendance
  problems to `public-sector-treasury-skills:ctp-exam-prep`,
  `learning-skills:deliberate-practice`, and `learning-skills:habit-design` respectively
  instead of absorbing them.
