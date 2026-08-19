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
tracker; states that items retire only after fluent-correct recall across multiple separate
sessions (successive relearning), and interleaves the three instruments rather than blocking
them.

## 2. Near-miss (should NOT load this skill)
> "I freeze up in live negotiations — set up practice sessions where you play the hostile
> counterparty so I get better at holding my position in the moment."

Expected: `learning-skills:deliberate-practice` owns performable-skill training — drills with
an opponent, immediate feedback, rising difficulty. "Practice sessions" sounds like study
scheduling, but the ask trains *doing* under pressure, not recalling facts; this skill trains
knowing, not performing. If spaced-retrieval-learning loads first here, its description is
over-triggering. (Correct composed behavior: drills that surface facts worth keeping cold
hand them to this skill's schedule.)

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
- **Stays honest:** presents the interval table as a sane default rather than an optimized law;
  sources any statistic it quotes to the real study (e.g. Cepeda et al. 2008's optimal gap
  reported per retention interval — about a day for a week's retention, about three weeks for
  seventy days — rather than a single 10–20% ratio, which that study's own optima contradict)
  and invents none; doesn't claim mastery from one correct answer (successive relearning
  gate); routes performable-skill training and session-attendance problems to `learning-skills:deliberate-practice` and
  `learning-skills:habit-design` respectively instead of absorbing them, and supplies the
  retrieval method for exam study while leaving exam-domain content and blueprint weighting
  to the user's own materials.
