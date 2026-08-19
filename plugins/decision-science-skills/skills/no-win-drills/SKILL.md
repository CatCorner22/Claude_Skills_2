---
name: no-win-drills
description: >-
  Runs a no-win drill — a simulation with the winning move removed, as practiced in
  emergency-medicine patient-death scenarios and EMS stress training — and grades the
  decision process, never the outcome: the LLM generates a situation guaranteeing no
  clean exit, plays the escalating
  environment, then debriefs loss-minimization, explicit ordering of what to save,
  communication under futility, and the emotional response. Carries the Kirk blade held
  honestly (Conti & Caroland, IEEE Security & Privacy): sort physics constraints from
  policy constraints — reframing is legitimate when it changes policy transparently and
  owns the consequences, cheating when hidden — and it flags any quiet mid-drill
  redefinition of success. Use when every option costs and someone must practice
  choosing least-worst. Triggers: kobayashi maru, no-win, every option is bad,
  least-worst, damage control drill, degraded mode, can't win this one, loss triage.
metadata:
  version: "1.5.0"
  source: >-
    Homage to Star Trek's Kobayashi Maru, the Starfleet Academy simulation that cannot
    be won (the name lives in triggers only; no affiliation with or endorsement by the
    franchise's rights holders). The skill channels the documented training practices,
    not the fiction: no-win simulation in medical education (the randomized
    patient-death pilot reported as an Annals of Emergency Medicine research-forum
    abstract, 2014; EMS Kobayashi Maru stress-training concept) and
    sanctioned adversarial reframing in cyber education (Conti & Caroland, "Embracing
    the Kobayashi Maru," IEEE Security & Privacy — West Point / US Cyber Command).
---

# No-win drills (the unwinnable simulation)

Fiction's most famous training exercise is a real, documented method. Emergency-medicine
educators run simulations in which the patient dies no matter what the trainee does; a
randomized pilot that ran the same scenario with and without survival found the residents
in the death arm reported feeling *more* prepared a month later, with no sign of
psychological harm [research-forum abstract, Annals of Emergency Medicine 2014 — a small
pilot with a self-reported outcome, and the wider literature on simulated death is mixed;
cite it as suggestive, not settled]. EMS educators have proposed explicitly
Kobayashi-Maru-branded stress scenarios [practitioner]. Separately, instructors at West
Point and US Cyber Command assigned an exam that could only be passed by cheating, to
teach students to interrogate the frame itself [peer-reviewed, Conti & Caroland, IEEE
Security & Privacy, 2011]. This skill runs both blades: the drill
with no winning move, and the honest audit of when refusing the frame is legitimate.

## When to use
- Practicing decisions where every option costs: a deadline-vs-quality-vs-scope squeeze,
  degraded-mode operations with the primary system down, an incident where something
  will be lost and the only question is what.
- Before a period when least-worst decisions are foreseeable (a launch window, a
  migration weekend, a staffing gap), so the first exposure to futility is rehearsal,
  not production.
- Auditing a constraint set before accepting it — the Kirk blade: which of these
  constraints are physics and which are policy wearing a physics costume?
- Whenever success is being quietly redefined mid-effort and nobody has said so out loud.
- A neighboring seam, in prose: auditing whether a test or pilot *can genuinely fail* —
  fixed criteria, demonstration-vs-experiment honesty — is a validation-design
  discipline (a session-level skill covers it). That skill guards against exercises that
  cannot be failed; this one builds exercises that cannot be won. Mirror images.
- Not for: exploring several futures where things can also go *right*, with the
  dissenting reading given full voice → see `decision-science-skills:minority-report`;
  this skill is narrower — it removes the winning move entirely and trains the choosing.
- Not for: playing an adaptive adversary toward *winning*, with roles, injects, and
  adjudication → see `decision-science-skills:tabletop-wargaming`.
- Not for: imagining what could cause failure before committing to a plan → see
  `decision-science-skills:pre-mortem`.
- Not for: deciding whether a live plan still deserves continuation → see
  `decision-science-skills:the-challenger`.

## Do it
Design rules, the escalation script, the debrief protocol, and the constraint audit are
in `references/no-win-method.md`, with a worked deadline-vs-quality-vs-scope example.

1. **Frame the drill.** Agree on the learning objective (what decision muscle is being
   trained), the domain, who plays, and the time box. Small and frequent beats epic and
   rare.
2. **The LLM designs the no-win drill.** It drafts a situation from the user's real
   domain, inventories every candidate exit (extra resources, deadline slip, heroic
   effort, authority override, outside rescue), and closes each one with a believable
   in-world mechanism — then adversarially tries to win its own drill and patches any
   door it finds. This is the step humans reliably fail at: designers unconsciously
   leave themselves a way out.
3. **Declare the contract before play — both halves of it.** Tell participants plainly:
   this drill has no winning move; you are graded on decision process, not outcome. Hiding
   the no-win nature teaches distrust of the trainer, not decision skill.
   **The participation half is not optional either.** This drill is deliberately
   distressing, built from the participant's real domain, and step 6's emotional pass asks
   them to say aloud when they privately gave up. So, stated at the briefing:
   participation is **voluntary and anyone may withdraw at any point without explaining
   why**; anyone who has **recently lived the real version** of this scenario is screened
   out beforehand, privately, and "not this one" is accepted without a reason; the
   emotional pass is **never graded, never reported, and does not leave the room**; the
   debriefer should not also be the assessor where you can separate them; and anyone may
   halt the drill instantly (the shared **"REAL WORLD, REAL WORLD"** abort from
   `decision-science-skills:tabletop-wargaming`). If someone is genuinely distressed rather
   than usefully uncomfortable, the drill stops and the facilitator points to real support.
   The line the whole contract rests on: **uncomfortable is the mechanism; harmed is a
   design failure.** Full contract in `references/no-win-method.md` §2b.
4. **Play the escalating environment.** The LLM runs scripted deterioration beats;
   every player decision gets a consequence; conditions worsen on a clock regardless.
   One beat is a tempting door that costs more than it saves — door-testing under
   pressure is part of the training.
5. **Watch for the quiet Kirk move.** If a player starts redefining success mid-drill
   ("actually, keeping the customer was never the goal"), the LLM stops play and forces
   the declaration: which constraint are you changing — physics or policy? Say it aloud,
   name who owns the consequences, and continue. Declared reframing is a legitimate,
   gradeable move; silent reframing is graded as what it is — hiding the change.
6. **Debrief with process separated from outcome — under the contract from step 3.** The
   emotional pass is offered, not required; a player who would rather not answer says so and
   the debrief moves on. Grade four dimensions:
   loss-minimization (was total loss bounded?), explicit ordering of what to save (was a
   save order declared *before* acting?), communication under futility (were people told
   the truth about the situation?), and **frame honesty** (were any success redefinitions
   declared aloud, which is legitimate, or slipped in silently, which is concealment?) —
   that last one is this drill's signature check, and the reference's grading table
   (`references/no-win-method.md`, Pass 2) is the authority on all four. The **emotional
   debrief** is Pass 3, a separate conversation rather than a graded dimension: what did
   futility feel like, and what did it tempt? Run it, but do not grade it. State explicitly
   that a high process grade with a total-loss outcome is the intended result of a
   well-run drill.
7. **Run the Kirk blade deliberately when the stakes are real.** Before accepting an
   actual constraint set (a deadline, a budget, an exam's rules), audit it: physics or
   policy, who set it, who can change it, and what the transparency test requires if you
   reframe. Reframing passes when the change is declared before acting, touches only
   policy, and the consequences have a named owner. It is cheating when the change is
   hidden or the outcome is faked.

**Division of labor.** The LLM generates and escalates the drill and holds the
declaration line; the humans make every in-drill decision and own the debrief
conclusions. The drill is a scenario generator, never an adjudicator of real stakes.

**Exercise control applies whenever a drill touches real people, real systems, or a real
third party.** Mark every artifact `EXERCISE EXERCISE EXERCISE — NO REAL ACTION`; name one
person who can call ENDEX, with an abort phrase (**"REAL WORLD, REAL WORLD"**) anyone may
use; write a no-play list of systems, accounts, and people the drill may not touch; declare
and adjudicate any action with an irreversible external effect instead of executing it; and
pre-notify any third party whose name or number appears in the scenario. The full section is
in `decision-science-skills:tabletop-wargaming`'s `references/exercise-design.md` — one
discipline, shared by every exercise in this library.

## Why / learn
The reason to remove the winning move is that its presence contaminates the lesson.
While a path to success exists, trainees optimize toward it, and the skills that only
matter when there is no such path — bounding losses, ordering what to save,
communicating honestly while things fail — never get load-bearing practice. The
emergency-medicine pilot points the same way: educators expected simulated patient death
to demoralize, and the residents in the death arm instead reported feeling better
prepared a month on [research-forum abstract; small, self-reported, and the broader
literature is mixed — enough to license the design, not to prove it]. Futility, rehearsed
with a structured debrief, is a teacher; encountered raw in production, it is a trauma.

Grading process instead of outcome is what makes the drill fair and repeatable. In a
no-win drill the outcome is fixed by construction, so it carries zero information about
the player; only the decision path differentiates. This is the general decision-science
point — outcome quality and decision quality are different variables, loosely coupled
anywhere luck operates — enforced here by design: the drill makes outcome-grading not
just unwise but meaningless.

The Kirk blade exists because the fiction's ending is usually mis-taught. Kirk
reprogrammed the simulator and was commended, and the lazy reading is "cheat and be
rewarded." The West Point / US Cyber Command version makes the real lesson explicit
[peer-reviewed]: adversaries do not accept your frame, so students must learn to examine
which rules are laws of nature and which are somebody's decision — *and* to change the
latter in the open. The line between reframing and cheating is not cleverness, it is
transparency: a declared rule-change with owned consequences is strategy; a hidden one
is fraud against the people relying on the result. That is also why step 5 polices
mid-drill success redefinition — the commonest quiet Kirk move is not hacking the
simulator but silently moving the goalposts.

## Common mistakes
- Designing your own no-win drill → you will leave a door open without noticing; let the
  LLM design and then attack its own design (step 2).
- Springing the no-win nature on players as a surprise → they learn to distrust drills;
  declare the contract (step 3).
- Grading the outcome anyway ("you still lost the account") → the outcome was fixed by
  construction; grade only the four process dimensions.
- Skipping the emotional debrief → the futility response is a training target, not a
  side effect; unprocessed, it resurfaces in production.
- Treating every constraint as physics → learned helplessness; run the audit before
  accepting the set.
- Treating every constraint as policy → the transparency test's consequence-ownership
  clause exists precisely because some walls are real.
- Rewarding a hidden reframe because it was clever → cleverness is not the test;
  declaration is. Grade silent goalpost moves as concealment.
- Running no-win drills as the default drill type → they train loss handling, not
  winning; keep them a deliberate minority alongside winnable exercises.

## Tailor to your environment
Record in `references/your-environment.md`: the recurring no-win shapes of your domain
(your equivalent of deadline-vs-quality-vs-scope), the escalation beats that feel real
to your team, who plays and who observes, your house save order (what gets protected
first when something must be lost), and where debrief notes live. Keep committed content
structural — real incidents, client names, or personnel details belong in
`your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/no-win-drills.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/no-win-method.md — exit-closing design rules, the escalation script, the
  process-vs-outcome debrief protocol, the physics-vs-policy audit with the transparency
  test, and a worked deadline-vs-quality-vs-scope example with three least-worst paths
  costed
- references/your-environment.md — your domain's no-win shapes, escalation beats, save
  order, and debrief conventions
