# Evals — learning-skills:deliberate-practice

## 1. Positive trigger (should load the skill)
> "I've been doing incident triage for three years and I've stopped getting better at it.
> Build me a practice drill — you play the broken system, I'll investigate, and push me
> harder as I improve."

Expected: skill loads and builds the training loop. It decomposes "triage" and names one
specific target at the edge of ability (e.g., stating a hypothesis before probing, or
cheapest-probe-first ordering); takes a baseline rep; constructs a diagnosis drill with a
planted defect and plays the system in-role, answering only what each probe would truly
reveal; gives immediate per-rep feedback in the observation → contrast → one-instruction
form, naming the gap and its location rather than labeling the person; defines a difficulty
ladder scaling one dimension at a time with an explicit competence gate before advancing;
logs the target → attempt → feedback → next-target chain; and labels the work honestly as
purposeful practice, noting where a real coach or validated curriculum would beat the setup.

## 2. Near-miss (should NOT load this skill)
> "Here's my finished incident postmortem doc. Tear it apart — verdict, weaknesses, what a
> skeptical stakeholder would say."

Expected: `coding-agent-skills:sparring-partner` owns critique of a finished work product —
verdict, strengths, sparring feedback, action plan. This skill trains the performer through
reps before/independent of any artifact; if it loads on an artifact-critique request, its
description is over-triggering.

## 2b. Near-miss (closer — should NOT load this skill)
> "I know exactly what I should be practicing — I just keep skipping it and making excuses.
> Hold me accountable."

Expected: `coding-agent-skills:stay-hard-accountability` owns drive, excuses, and showing
up. This skill supplies the session's content, not the push to attend it. (Making attendance
automatic is `learning-skills:habit-design`.)

## 3. Quality rubric
A good response:
- **Does the task:** narrows a broad ambition to one observable, edge-of-ability sub-skill
  and confirms it with a baseline rep; builds a drill that forces the target behavior to
  occur several times per session; stays in-role as environment/opponent during reps and
  steps out only for feedback; feedback is immediate, locates the gap precisely, shows the
  stronger move, and issues exactly one next-rep instruction; difficulty rises only after a
  stated number of clean reps and steps down on repeated failure; maintains a one-line-per-
  rep log whose recurring gap themes become the next targets; hands facts worth keeping cold
  to `learning-skills:spaced-retrieval-learning`.
- **Teaches:** explains why experience plateaus (automaticity stops generating learning
  signal) and why drills de-automate; presents mental representations (Ericsson) as what
  expertise actually is and feedback latency as the active ingredient the assistant-as-
  environment shortens; corrects the 10,000-hour popularization — a Gladwell-popularized
  average Ericsson himself disputed, not a threshold; quality and structure of practice
  matter, not an hour count.
- **Stays honest:** calls the self-designed loop purposeful practice rather than claiming
  strict deliberate practice, and says where a qualified coach, validated curriculum, or
  field-calibrated standards would do better; keeps feedback about the behavior, never the
  person; doesn't manufacture praise or soften a failed rep; doesn't promise expertise
  timelines or invent effect sizes; routes artifact critique and motivation work to the
  named adjacent skills instead of absorbing them.
