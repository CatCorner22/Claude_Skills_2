---
name: stakeholder-mapping
description: >-
  Maps who can sink or save the work before it matters: builds the
  power-interest grid — with the open correction that the grid everyone draws is
  Johnson & Scholes (1999) / Eden & Ackermann (1998), not Mendelow's 1981 paper, whose
  matrix is power/dynamism — assigns engagement moves per quadrant (manage closely,
  keep satisfied, keep informed, monitor), writes the RACI so "consulted" stops meaning
  "surprised", plans influence without authority (Cohen & Bradford's exchange
  currencies), and sets re-map triggers at milestones,
  because the map is a snapshot, not a truth. For a process change with opponents, a
  multi-party matter, a migration, or a deprecation you lack authority to force. Once
  the map says who matters, disarming-elicitation is how to talk to them. Triggers:
  stakeholder map, stakeholder mapping, stakeholder analysis, power-interest grid,
  RACI, responsibility matrix, influence without authority, buy-in, who needs to sign
  off, stakeholder management, who can sink this.
metadata:
  version: "1.1.0"
  source: >-
    Built from the general-use expansion dossier
    (docs/research/general-use-expansion-research.md §7 stakeholder-mapping) —
    research-verified anchors with the misattribution warnings carried as teaching
    content. [snippet-only] marks claims verified via cross-checked search snippets,
    not primary documents; the Mendelow power/dynamism finding is convergent-secondary
    — fetching the 1981 ICIS paper (AIS eLibrary) would upgrade it to primary.
---

# Stakeholder mapping (who can sink or save the work)

The honesty point first, because it is the method's own best lesson: the
"Mendelow matrix" everyone draws — power on one axis, interest on the other — is not in
Mendelow. His 1981 ICIS paper on environmental scanning carries a power/**dynamism**
matrix; the power/**interest** grid comes from Johnson & Scholes' *Exploring Corporate
Strategy* (1999 edition, adapting Mendelow by swapping dynamism for interest) and
independently from Eden & Ackermann's *Making Strategy* (1998) [snippet-only,
convergent secondary — the dossier flags that the ICIS paper text itself was not
fetched]. Cite the grid to Johnson & Scholes or Eden & Ackermann; cite Mendelow for the
idea that stakeholder power should drive scanning priority. A mapping skill that
mis-cites its own map has already failed its first audit.

## When to use
- Before work that needs other people's cooperation to survive: an ops manager driving
  a process or system migration past known opponents, an attorney structuring a
  multi-party deal or dispute, an analyst whose recommendation needs sign-offs, a
  developer sunsetting an internal API with no authority over its consumers.
- Writing the RACI for a project's workstreams — who is responsible, accountable,
  consulted, informed.
- Planning influence over someone you cannot compel — the currencies-of-exchange plan.
- At every milestone of live work: stakes shift, so the map gets re-drawn.
- Not for: interviewing a stakeholder to learn what they know → see
  `collaboration-skills:disarming-elicitation`, which owns the stakeholder interview;
  this skill maps *who matters*, that one elicits *what they know*.
- Not for: bargaining once a mapped stakeholder becomes a counterpart across the table
  → see `decision-science-skills:principled-negotiation` (interests, BATNA, criteria).
- Not for: binding a sign-off to real consequences → see
  `decision-science-skills:skin-in-the-game`; this skill maps who must sign, that one
  designs what their signature costs them.
- The engagement moves' instruments live elsewhere: the decision forum is
  `collaboration-skills:meeting-design`; the hard conversation about behavior is
  `collaboration-skills:feedback-that-lands`.

## Do it
The grid with its attribution notes, the quadrant move catalog, RACI rules, the
currencies catalog, the re-map protocol, and worked examples are in
`references/stakeholder-method.md`.

1. **List everyone who can sink or save the work.** Not the org chart — the people and
   groups whose action or inaction changes the outcome: approvers, budget holders, the
   teams who must change behavior, the veto-holders nobody put on the invite, the quiet
   beneficiaries of the status quo. Record roles in committed files; real names go in
   `your-environment.private.md` — never commit a real power map.
2. **Place each on the power-interest grid.** Power: can they materially help or block?
   Interest: how much does the outcome touch them? Mark each placement as *evidence*
   (they said or did something) or *inference* (your read) — inferences are hypotheses
   to test, not facts to act on.
3. **Assign the quadrant's default move** — manage closely (high power, high interest),
   keep satisfied (high power, low interest), keep informed (low power, high interest),
   monitor (low power, low interest) — knowing the labels are folk-simplifications
   layered onto the grid, not part of the cited sources: treat them as default effort
   allocations, never as personality types.
4. **Write the RACI on the workstreams.** One accountable per row; consulted means
   *before* the decision, informed means *promptly after*. RACI has no named inventor
   and no canonical origin paper — it descends from 1950s linear responsibility
   charting; say so rather than inventing a source [snippet-only].
5. **Plan currencies for whoever you cannot compel.** Cohen & Bradford's *Influence
   Without Authority* (1989; 2nd ed. 2005): influence is exchange, and the currencies —
   inspiration, task, position, relationship, personal — are what the other party
   actually values [snippet-only]. For each such stakeholder: what do they value that
   you can genuinely offer, and what are you asking for?
6. **Wire the moves to their instruments.** "Manage closely" mostly means designed
   decision forums (`collaboration-skills:meeting-design`) and real conversations —
   elicitation when you need what they know
   (`collaboration-skills:disarming-elicitation`), negotiation when they become a
   counterpart (`decision-science-skills:principled-negotiation`), feedback when the
   problem is behavior (`collaboration-skills:feedback-that-lands`).
7. **Stress-test the map.** Run `decision-science-skills:pre-mortem` with
   stakeholder-shaped failure narratives — "the plan failed because the keep-satisfied
   executive discovered X and became an opponent" — and let each credible narrative
   revise a placement or a move.
8. **Set re-map triggers.** The map is a snapshot: re-draw at named milestones, at any
   reorganization, and whenever a stakeholder's behavior contradicts their placement.
   Note what moved and why — the deltas are the intelligence.

Division of labor: the assistant drafts the candidate list, the grid, the RACI, and the
currencies plan, and generates the stakeholder-shaped failure narratives; the human
supplies the actual politics, corrects placements, and owns every engagement move —
the map informs relationships, it never replaces them.

## Why / learn
Map before it matters because opposition compounds silently. The stakeholder who could
have been consulted in week one becomes the stakeholder who was surprised in week six —
and surprise converts neutral parties into opponents on procedural grounds even when
they like the substance. Mapping early is cheap; every option (consult, involve, trade,
re-scope) is still open. Mapping late is forensics.

The grid earns its place by allocating a scarce resource: your engagement effort.
Treating all stakeholders equally over-invests in the indifferent and under-invests in
the powerful; the two axes are the minimum model that prevents both. But hold it
lightly — the quadrant labels are folk-simplifications: useful defaults that harden
into nonsense when read as fixed types. A "monitor" stakeholder whose pet system your
migration touches becomes "manage closely" overnight; the grid did not change them,
your project's stakes did. That is why the re-map trigger is part of the method rather
than an afterthought, and why placements carry their evidence-or-inference tag.

The lineage runs through Freeman's *Strategic Management: A Stakeholder Approach*
(1984), the foundational text of stakeholder theory — with its own honesty note:
Freeman did not coin "stakeholder"; the term traces to a Stanford Research Institute
working group around 1963, and Freeman credits it [snippet-only]. The misattribution
trio — the grid to Mendelow, the word to Freeman, RACI to whichever vendor page you
read last — makes this skill the library's cleanest exhibit of *often cited, rarely
read*. Teaching the corrections is not pedantry: a discipline whose core artifact is
routinely mis-cited is a discipline whose users repeat diagrams instead of checking
sources, and checking sources is exactly the habit stakeholder work needs.

Influence without authority works as exchange because cooperation you cannot command
must be worth someone's while. Cohen & Bradford's currencies enumerate what "worth
their while" can mean beyond money — recognition, meaningful tasks, visibility,
belonging, gratitude — and the reciprocity that follows genuine help is the engine.
The rail: currencies are offered openly, as trade between colleagues, never as
manipulation; a traded favor both sides can name is influence, a hidden ledger is
politics.

## Common mistakes
- Citing the power-interest grid to Mendelow 1981 → that paper's matrix is
  power/dynamism; cite Johnson & Scholes (1999) or Eden & Ackermann (1998), and cite
  Mendelow for power-driven scanning priority.
- Crediting Freeman with coining "stakeholder" → SRI working group, ~1963; Freeman
  himself credits it.
- Narrating a RACI origin story → it has no inventor and no canonical paper; it
  descends from 1950s linear responsibility charting.
- Treating quadrants as personality types → they are effort defaults on a snapshot;
  re-place people when stakes shift.
- Mapping once at kickoff → the map decays at every milestone; set re-map triggers.
- "Consulted" discovering the decision after it is made → consult before, inform after;
  that ordering is the entire point of the two letters.
- Two accountables on one workstream → nobody is; one A per row.
- Committing a grid with real names → a power map of colleagues is org politics on the
  record; roles in git, names in the git-ignored private file only.
- Confusing the map with the conversation → the map says who matters;
  `collaboration-skills:disarming-elicitation` owns how to interview them.
- "Keep satisfied" read as "spam with updates" → high-power low-interest stakeholders
  want their specific concerns pre-empted, not a newsletter.

## Tailor to your environment
Record your standing landscape in `references/your-environment.md`: recurring
stakeholder *roles* and their default placements, your RACI conventions, house
milestone/re-map cadence, and where maps live. **Privacy rule: never commit a real
power map.** Real names of colleagues, actual placements, currencies plans, and
anything about live org dynamics go in `your-environment.private.md` — git-ignored,
never committed. A leaked power map damages every relationship on it.

## References
- references/stakeholder-method.md — the grid with attribution notes, quadrant move
  catalog, RACI rules, the Cohen & Bradford currencies catalog, the re-map protocol,
  and worked examples across roles
- references/your-environment.md — your roles, conventions, and cadences (sanitized
  stub; real names and live maps go in the `.private.md` twin)
