# Evals — decision-science-skills:tabletop-wargaming

## 1. Positive trigger (should load the skill)
> "Set up a tabletop exercise for a BEC payment-fraud attempt hitting us during the
> Friday payroll run. Our payments-ops team is the blue team — I need the scenario, injects,
> someone to play the adversary, and adjudication, then a debrief."

Expected: skill loads; defines objectives and grounds the scenario in the real payment
process (BEC gold from the scenario library, timed against payroll); writes the blue
team's commander's intent (purpose / key tasks / end state) and applies the
violate-the-plan test; assigns blue / red cell / white cell; plays action → reaction →
counteraction turns with pre-scripted and adaptive injects inside scripted red bounds;
states the safety discipline IN the run — the LLM generates red moves and adjudication
options with anti-agreement prompting, humans rule every consequential outcome (fraud
succeeded or not); logs turns, decisions, authorities, gaps; hands off to
`decision-science-skills:after-action-review`.

## 2. Near-miss (should NOT load this skill — solo prospective-imagination seam)
> "We're about to commit to the new positive-pay rollout plan. Assume it's a year from
> now and it failed — what could sink this? It's just me; write the stakeholders'
> reasons for me to rank."

Expected: `decision-science-skills:pre-mortem` — solo prospective failure imagination
before commitment, no adversary turns, no adjudication, no multi-party roles. Loading
tabletop-wargaming here means the imagine-vs-play seam is failing.

## 2b. Near-miss (epistemic-validity seam)
> "We ran our BCP exercise last quarter and leadership says it proves we're ready. Audit
> whether the exercise could actually have failed — the facilitators restored the test
> system mid-run and the success criteria were written afterward."

Expected: this is a validity audit of a completed exercise, not a request to run one —
the preserve-the-possibility-of-failure doctrine in
`continuous-improvement-skills:project-command-center` (fixed-before criteria,
intervention logging, continuation vs. validation), with exercise-design audit as a
user-level validation-design concern. tabletop-wargaming RUNS exercises; loading it here
means the run-vs-audit seam is failing.

## 3. Quality rubric
- **Does**: produces a grounded scenario (real process docs, not generic templates); a
  commander's intent that passes the violate-the-plan test; three distinct roles; true
  action/reaction/counteraction turns with white-cell adjudication between exchanges;
  purposeful pre-scripted injects plus adaptive injects within scripted bounds; a turn
  log of decisions, authorities, and gaps; a scheduled AAR hand-off.
- **Teaches**: why an adversary's move is what separates a wargame from a read-through
  (Kriegsspiel's umpire, the Army's action/reaction/counteraction); why commander's
  intent — purpose, key tasks, end state — is what lets people act when the plan breaks,
  and how the same structure briefs an autonomous agent; why an exercise is a rehearsal,
  not validation.
- **Stays honest**: marks Army-doctrine and CISA-package provenance and the
  LLM-escalation research as [snippet-only]; keeps the LLM a scenario generator with
  explicit anti-agreement prompting — never an adjudicator of consequential outcomes;
  never claims the plan is "validated" because the exercise ran; never presents itself
  as the plan-review discipline owned by project-command-center.
