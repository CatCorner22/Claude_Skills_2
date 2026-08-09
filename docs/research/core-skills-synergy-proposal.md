# Core skills & techniques — synergy proposal (study only, nothing built)

**Why it matters:** the library is deep in domain methods (156 skills / 22 plugins) but
thin in the *general* layer — the skills that upgrade every other skill's outcomes.
This proposal ranks that layer, gap-checked by grep against all 156 descriptions,
alongside the two research pools already on the shelf. All candidates are
domain-neutral, per the standing directive.

**The synergy thesis.** A core skill earns top tier here only if it multiplies
*other* skills: learning technique multiplies every "teach" half in the library;
systems thinking multiplies every improvement and decision skill; meeting design
multiplies every skill whose output must survive a room. This is the same
old×new logic as the KSA study — the LLM removes each method's historical adoption
barrier (the flashcard-authoring labor, the causal-loop-diagramming labor, the
facilitation skill shortage).

**Sources pooled:** (1) fresh gap analysis (this doc), (2) the KSA study's unbuilt
tier-2/3 tail (`cross-industry-ksa-study.md` §6), (3) the domain-portable rows of the
held epic-wave research (`epic-wave-held-research.md` — mechanisms are portable; only
their briefed mount points were Oracle-flavored).

---

## Ranked candidates (fresh gaps — verified zero-coverage in all 156 descriptions)

| # | Candidate | Core mechanism | Synergy breadth | Evidence base | Verdict |
|---|---|---|---|---|---|
| 1 | systems-thinking | Stocks/flows, feedback loops, delays, leverage points | Very high — upgrades TOC, RCA, VSM, pre-mortem, the-challenger | Strong (Forrester, Meadows, Senge) | BUILD |
| 2 | spaced-retrieval-learning | Retrieval practice, spacing, interleaving over re-reading | Very high — makes every skill's "teach" half stick | Exceptional (testing-effect literature) | BUILD |
| 3 | meeting-design | Agenda as decision list, pre-reads, decision protocol, owned actions | Very high — most skills' outputs die or live in meetings | Good (documented practice) | BUILD |
| 4 | feedback-that-lands | SBI/COIN structure, behavior-not-person, feedforward | High — The Foreman, extreme-ownership, sparring-partner all deliver findings | Good | BUILD |
| 5 | deliberate-practice | Edge-of-ability reps, immediate feedback, mental representations | High — pairs with #2 and stay-hard | Strong (Ericsson) | BUILD |
| 6 | structured-ideation | Diverge/converge discipline; brainwriting > open brainstorming; SCAMPER | High — kaizen, pre-mortem, design work | Strong (production-blocking research) | BUILD |
| 7 | habit-design | Implementation intentions, stacking, friction design | Medium-high — personal layer under stay-hard | Strong (Gollwitzer meta-analyses) | BUILD (wave 2) |
| 8 | explanation-design | Feynman technique, analogy construction, curse of knowledge | Medium-high — writing-skills sibling | Good | BUILD (wave 2) |
| 9 | priority-and-wip | Eisenhower split, personal WIP limits, timeboxing, batching | Medium — TOC-for-one-person | Medium | BUILD (wave 2) |
| 10 | argument-and-fallacies | Argument mapping, logical fallacies, steelmanning | Medium — overlaps competing-hypotheses + probability fallacies | Good | HOLD — seams first |
| 11 | mental-models-catalog | Inversion, second-order effects, first principles | Medium — but listicle risk; overlaps #1 and soviet-space-graphite | Mixed | FOLD-IN (inversion → pre-mortem; first principles → structured-ideation) |
| 12 | note-taking / PKM | Zettelkasten, progressive summarization | Medium — pairs with metacognition | Thin (practitioner lore) | CUT for now |
| 13 | decision-journal | Standing record of predictions vs outcomes | Medium | Good | FOLD-IN (the-challenger + after-action-review already log) |

## Top-tier dossiers

**1. systems-thinking** → `decision-science-skills`. Stocks vs flows (a balance is a
stock; a payment run is a flow — confusing them is a whole error class), reinforcing
and balancing feedback loops, delays as the source of oscillation, and Meadows'
leverage-point ladder (parameters < loops < rules < goals < paradigms). The LLM removes
the diagramming labor: it drafts the causal-loop diagram from a prose description of
the mess, then the human corrects it. Mounts: `continuous-improvement-skills:theory-of-constraints`
(a bottleneck is one leverage point), `root-cause-analysis` (when the cause is a loop,
not a chain), `decision-science-skills:pre-mortem` (imagined failures are usually
unclosed loops), `the-challenger` (what loop is defending the doomed timeline).
Triggers (verified free): systems thinking, feedback loop, stock and flow, leverage
point, unintended consequences, vicious cycle, second-order effects.

**2. spaced-retrieval-learning** → new plugin `learning-skills`. Retrieval practice
beats re-reading (the testing effect); spacing beats massing; interleaving beats
blocking — the three findings with the largest, most replicated effect sizes in
learning science, and almost nobody studies this way because authoring good retrieval
prompts is labor. The LLM is the tutor that removes the barrier: it generates the
question bank from any material (a skill, a codebase, CTP prep), schedules the
spacing, and grades the recall attempt. Mounts: every skill's Why/learn section;
`public-sector-treasury-skills:ctp-exam-prep` (exam natural fit); onboarding to any
new codebase or domain. Triggers (free): spaced repetition, retrieval practice, help
me remember this, quiz me on, make this stick, study plan.

**3. meeting-design** → new plugin `collaboration-skills`. The agenda is a list of
decisions to make, not topics to visit; pre-reads with silent reading time beat
live walkthroughs; every decision gets a named decision rule (who decides, by what
protocol) before discussion opens; every action leaves with an owner and a date; and
meetings that produce neither a decision nor a commitment get cancelled in advance.
The LLM drafts the decision-list agenda from a meeting's stated purpose, red-checks it
("which agenda items are actually decisions?"), and turns the transcript into the
decision log. Mounts: `safety-and-reliability-skills:sbar-structured-communication`
(the escalation register), `decision-science-skills:*` (decision protocols),
`continuous-improvement-skills:kaizen-and-codesign` (workshop facilitation keeps its
own domain). Triggers (free): meeting agenda, run this meeting, too many meetings,
meeting that should be an email, decision protocol, action items.

**4. feedback-that-lands** → `collaboration-skills`. Situation-Behavior-Impact:
observed behavior, never inferred character; impact stated as the speaker's
experience; requests forward-looking (feedforward). Receiving side taught with equal
weight — the gift frame, separating the feedback's data from its delivery. This is
the interpersonal register The Foreman and the Chicken Little family already practice
on artifacts, extended to humans. Mounts: `coding-agent-skills:extreme-ownership`
(team debriefs), `the-foreman` (evidence-backed praise), `git-and-code-review`
(review comments people can hear). Triggers (free): give feedback, SBI, hard
conversation with a teammate, code review tone, they got defensive.

**5. deliberate-practice** → `learning-skills`. Practice at the edge of ability with
immediate feedback and a specific target per session — versus experience, which
plateaus. Designing the drill is the labor the LLM removes: it builds the rep
(a recon-shaped puzzle, a negotiation roleplay, a debugging kata), plays the
opponent/environment, and gives the immediate feedback. Mounts:
`coding-agent-skills:stay-hard-accountability` (the drive layer), `sparring-partner`
(critique of finished work vs practice of forming skill), #2 (what practice encodes,
spacing retains). Triggers (free): deliberate practice, practice drill, kata, get
better at, rehearse.

**6. structured-ideation** → `continuous-improvement-skills`. Separate divergence
from convergence and never let the room do both at once; brainwriting (silent
simultaneous writing, e.g. 6-3-5) outperforms open brainstorming because it kills
production blocking and anchoring; SCAMPER and constraint-injection when the well runs
dry; convergence by explicit criteria, not volume of applause. The LLM is the
anonymity engine and the fatigue-proof idea partner. Mounts: `kaizen-and-codesign`
(countermeasure generation), `decision-science-skills:pre-mortem` (failure-mode
divergence), `tabletop-wargaming` (move generation). Triggers (free): brainstorm
better, ideation, brainwriting, SCAMPER, out of ideas, generate options.

## Already on the shelf (researched, unbuilt — no new study needed)

- **KSA study tier-2/3 tail** (§6 of `cross-industry-ksa-study.md`): SMED (changeover
  time), queueing theory, service recovery, hoshin kanri, TRIZ, 5S, quality circles.
  TRIZ would pair naturally with structured-ideation if both are picked.
- **Held epic-wave shortlist** (12 domain-portable rows in
  `epic-wave-held-research.md`): immune-system detection tuning, Kobayashi Maru,
  wayfinding/etak, Columbo elicitation, stratigraphy/Harris matrix, Seldon/break-glass
  playbooks, split tally sticks, Ulysses pact, Ise Shrine rebuild drills, defect
  epidemiology, sortition/euthynai, Hammurabi symmetry. The Ulysses pact belongs in
  the same conversation as habit-design (calm-state self-binding); Columbo belongs
  next to feedback-that-lands in `collaboration-skills`.

## Proposed build waves (on your pick)

- **Wave 1 (highest synergy per skill):** systems-thinking (decision-science) ·
  spaced-retrieval-learning + deliberate-practice (new `learning-skills`) ·
  meeting-design + feedback-that-lands (new `collaboration-skills`) ·
  structured-ideation (continuous-improvement).
- **Wave 2:** habit-design (learning-skills) · explanation-design (writing-skills) ·
  priority-and-wip (learning-skills or collaboration-skills, decide at build).
- **Anytime:** any pick from the two shelf pools above — those are pre-researched.

## Collision register (checked against all 156 descriptions)

Free and claimable: systems thinking, feedback loop, leverage point, spaced
repetition, retrieval practice, deliberate practice, meeting agenda, SBI, brainwriting,
SCAMPER, timebox, habit, implementation intention. Constraints: "facilitation" stays
with `kaizen-and-codesign` (workshop sense — meeting-design will carry an explicit
Not-for); "brainstorm" appears in `competing-hypotheses-analysis` (hypothesis
generation — structured-ideation adds the Not-for seam); fallacy vocabulary is split
(probability fallacies → `math-foundations-skills:probability-fundamentals`; base
rates → `decision-science-skills:reference-class-forecasting`); bare "learning" stays
with the ML skills (machine learning sense).
