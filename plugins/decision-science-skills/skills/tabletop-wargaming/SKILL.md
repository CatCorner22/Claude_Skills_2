---
name: tabletop-wargaming
description: >-
  Designs and runs a multi-party tabletop exercise with an adversary and adjudication, in
  the lineage Kriegsspiel → Army course-of-action analysis (action / reaction /
  counteraction) → CISA-style tabletop packages: define objectives and scenario (an
  impersonated urgent instruction, a critical-vendor outage on a deadline day,
  ransomware in a freeze), write the blue team's commander's intent (purpose, key tasks,
  end state), assign blue players, a red cell, and a white-cell adjudicator, play turns
  driven by pre-scripted and adaptive injects, adjudicate plausibility, capture decisions
  and gaps, and hand off to an after-action review. The LLM plays red and white cell
  strictly as a scenario generator — humans adjudicate every consequential outcome. Use
  when rehearsing an incident-response, fraud, continuity, or cutover plan against an
  adaptive adversary. Triggers: tabletop exercise, wargame the plan, run a drill,
  incident simulation, inject, BCP exercise, commander's intent.
metadata:
  version: "1.2.0"
---

# Tabletop wargaming (with commander's intent)

## When to use
- Rehearsing a plan against an *adaptive* opposition or environment: an out-of-band
  urgent instruction from a named authority, timed against the approver's absence — a
  payment release, an access grant, a data export (pair with
  `safety-and-reliability-skills:bowtie-barrier-analysis` — it maps the barriers the
  drill exercises); a critical-vendor connectivity outage on a hard-deadline day
  (`safety-and-reliability-skills:break-glass-playbooks` arms the contingency path the
  drill tests); ransomware landing during a period-close or release freeze; a cutover
  that meets a hostile Monday.
- Testing whether people two levels down can act when the plan breaks — which is what
  commander's intent exists for (see `references/commanders-intent.md`).
- As the multi-party procedure that
  `continuous-improvement-skills:project-command-center` lacks: that doctrine carries the
  Millennium Challenge validity lesson and adversarial plan review; this skill supplies
  the roles, turns, injects, and adjudication to actually run an exercise.
- A neighboring seam, in prose: auditing whether an exercise *can genuinely fail* — fixed
  criteria, intervention logging, demonstration-vs-experiment honesty — is a
  validation-design discipline (a user-level skill covers it); this skill *runs* the
  exercise, and borrows that discipline rather than owning it.
- Not for: solo prospective failure imagination before commitment → see
  `decision-science-skills:pre-mortem`. Epistemic validity audit of a test or benchmark →
  see `continuous-improvement-skills:project-command-center`
  (preserve-the-possibility-of-failure doctrine). The post-exercise debrief itself → see
  `decision-science-skills:after-action-review` (the hand-off in step 7).

## Do it
1. **Define objectives and scenario.** What must the exercise reveal (decision gaps, call
   trees, authority limits, detection lag)? Pick a scenario that matters: three
   high-yield starters, portable to any organization, are the impersonated urgent
   instruction, the critical-vendor outage on a hard-deadline day, and ransomware during
   a close or freeze — each with a worked payments-operations instantiation in
   `references/exercise-design.md`. Ground the scenario in your own process documents,
   not generic templates.
2. **Write the blue team's commander's intent** — purpose, key tasks, end state — so
   players can act without further orders when the plan breaks. Apply the test: could
   someone achieve the intent while violating the plan's specifics? If not, it is a task
   list, not intent. Format in `references/commanders-intent.md`.
3. **Assign roles.** Players (blue) operate the real process with their real authorities;
   a red cell plays the adversary or hostile environment; a white cell facilitates,
   adjudicates plausibility, tracks state, and keeps time. One person can hold white cell
   solo; red and white should not be the same human if avoidable.
4. **Play turns: action → reaction → counteraction.** Blue acts on the critical event;
   red reacts as an intelligent adversary would; blue counters. Adjudicate each exchange
   before the next. Turns stop the exercise collapsing into a discussion of the plan.
5. **Escalate with injects.** Deliver pre-scripted injects (spoofed emails, bank alerts,
   news items, a caller claiming to be the CFO) at planned times, plus adaptive injects
   responding to what players actually chose. Templates in
   `references/exercise-design.md`.
6. **Hold the safety discipline (non-negotiable, from documented LLM failure modes).**
   The LLM plays red cell and white cell as a SCENARIO GENERATOR, never a decision-maker:
   research on LLMs in wargame simulations reports sudden, hard-to-predict escalation
   dynamics [snippet-only], and default sycophancy erodes an adversary role into
   agreement. So: use explicit anti-agreement prompting for red ("do not soften, do not
   let blue win a turn cheaply"); ground every inject in the real process documents;
   cap red's escalation at the scenario's scripted bounds; and route every consequential
   adjudication — what "worked," what the outage broke, whether the fraud succeeded — to
   the human white cell. The LLM proposes; humans rule.
7. **Capture and debrief.** White cell logs each turn: decision made, authority invoked,
   information available, gaps exposed. Then hand the log to
   `decision-science-skills:after-action-review` — the four questions turn the exercise
   into sustained and improved practice.

## Why / learn
The lineage explains the design. Kriegsspiel's insight was the umpire: a free adversary
plus an adjudicator produces surprises a scripted walkthrough cannot. The Army's
course-of-action analysis added the action/reaction/counteraction turn — plans meet an
enemy who gets a move, so testing a plan without an adversary's move tests only its
penmanship. CISA-style packages [snippet-only: Army doctrine and CISA exercise packages
are the provenance here — practitioner doctrine, not controlled trials] made the format
portable: scenario, injects, facilitator, debrief. Commander's intent is load-bearing
for any operating team because real incidents break the plan first —
purpose, key tasks, and end state are what let the person at the desk act correctly at
2 a.m. without calling anyone. The safety discipline earns its prominence from documented
LLM behavior: models given adversary or adjudicator seats have shown abrupt escalation in
wargame studies [snippet-only], and a model's agreeableness quietly hands blue easy wins,
which manufactures false confidence — the most expensive possible output of an exercise.
Kept to scenario generation with human adjudication, the LLM is a superb red cell writer:
tireless, various, and grounded in your actual documents.

## Common mistakes
- No adversary move — a read-through labeled a wargame → use turns; red always gets its
  reaction.
- Letting the LLM adjudicate outcomes or "win" decisions → humans rule on every
  consequential outcome; the model generates scenario and injects only.
- A sycophantic red cell that folds each turn → explicit anti-agreement prompting, and
  check red's moves against the scenario bounds.
- Generic injects from templates → ground them in your real approval flow, vendor
  portals, and deadline calendar, or players learn nothing about *their* process.
- Commander's intent that is a task list → apply the violate-the-plan test; rewrite as
  purpose / key tasks / end state.
- Skipping the debrief → the exercise's value lands in the AAR; schedule it with the
  exercise, not after.
- Declaring the plan "validated" because the exercise ran → an exercise is a rehearsal;
  validity claims need the fixed-criteria discipline in project-command-center.

## Tailor to your environment
Wire in your current role here — roles, turns, injects, and adjudication are
domain-neutral, and the same machinery rehearses a payments team, a clinic, a newsroom,
or a release train. Record in `references/your-environment.md`: your scenario
priorities, the real process documents injects must be grounded in, role rosters and
authority limits, escalation bounds for the red cell, and where exercise logs are filed.
Anything naming real accounts, counterparties, people, or live controls goes in
`your-environment.private.md` (git-ignored) — an exercise file that leaks real controls
is itself an incident.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/tabletop-wargaming.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/exercise-design.md — scenario library (incl. three high-yield starters),
  inject templates, adjudication rules, escalation-safety discipline
- references/commanders-intent.md — purpose / key tasks / end state format, the
  violate-the-plan test, and the briefing-an-agent application
- references/your-environment.md — your scenarios, rosters, bounds, and filing (fill in)
