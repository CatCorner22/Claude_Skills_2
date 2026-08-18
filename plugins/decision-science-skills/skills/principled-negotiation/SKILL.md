---
name: principled-negotiation
description: >-
  Prepares and runs a negotiation with a two-layer method — Fisher/Ury strategy (map the
  interests behind each side's positions, build your BATNA and estimate theirs, assemble
  objective criteria, invent options for mutual gain) plus Voss conversation tactics
  (accusation audit, mirrors, labels, calibrated how/what questions) — drafting BATNA
  trees, interest maps, criteria tables, and question banks, and roleplaying the
  counterpart for rehearsal, while the human sets the walk-away line and makes every
  concession decision. Use when preparing for, rehearsing, or debriefing a negotiation
  over a fee or price increase (a benchmarking analysis builds the case; this skill runs
  the ask), a processor or carrier fee schedule, or a vendor contract renewal or
  dispute. Triggers: BATNA, prepare for a
  negotiation, push back on this fee increase, renegotiate the contract, calibrated
  questions, tactical empathy, accusation audit, talk them down.
---

# Principled negotiation

## When to use
- Preparing for, rehearsing, or debriefing a negotiation: a bank fee increase, merchant
  processor markup (the processor's markup is the only layer open to negotiation —
  interchange and network fees are set upstream), an insurance-carrier fee schedule, a
  vendor or carrier contract renewal or dispute.
- Building the prep pack almost nobody writes: interest map, BATNA tree,
  objective-criteria table, accusation audit, calibrated-question bank — then roleplaying
  the counterpart before the real conversation.
- Not for: computing what the fees *should* be → that is a fee-benchmarking analysis
  (archived: `banking-skills:bank-fee-analysis`, restorable from `archive/`) — decoding
  the account-analysis statement into benchmark tables and levers builds the case; this
  skill runs the ask.
- Not for: patient-complaint or service-recovery conversations → that is service
  recovery, a different discipline; this library does not yet carry a skill for it.

## Do it
Preparation worksheets, the tactic-response table, and the worked case are in
`references/negotiation-prep-and-tactics.md`.

1. **Map interests behind positions.** A position is what each side says it wants ("the
   12% increase stands"); an interest is *why* they want it (revenue target, cost to
   serve, retention, risk). Write both sides' interests in a two-column map — yours from
   your own stakeholders, theirs inferred and marked as inference until tested in
   conversation. Deals are built from interests; positions only collide.
2. **Build your BATNA; estimate theirs.** Your BATNA — best alternative to a negotiated
   agreement — is what you actually do if talks fail (run an RFP, consolidate accounts,
   switch carriers, insource). Cost it realistically, including switching pain, then take
   the strongest branch as your walk-away floor. Improving the BATNA before you talk
   (get a live competing quote) raises your power more than any line you say. Estimate
   theirs too: what losing you costs them is your leverage map.
3. **Assemble objective criteria.** Benchmarks, market rates, precedent, published price
   schedules, your own historical pricing. Whatever analysis benchmarks the disputed
   prices produces exactly these tables (for bank fees: AFP-coded unit-price benchmarks,
   volume × price drivers, the ECR trade-off) — run it first and carry its output in.
4. **Draft the accusation audit.** List every negative thing they might think or say
   about your side ("you probably think we're a small account", "you think we're just
   shopping you") and plan to name the worst ones yourself, first. Named objections
   deflate; ambushed ones harden.
5. **Rehearse.** Have the LLM roleplay the counterpart from the interest map — one pass
   cooperative, one positional hardliner, one evasive — while you practice the tactics
   out loud. Debrief each pass against the prep pack.
6. **In conversation, run tactical empathy.** Mirror (repeat their last one to three
   words, as a question, then be silent). Label emotions and positions ("It seems like
   this increase is coming from above you"). Ask calibrated how/what questions that hand
   them your problem ("How am I supposed to justify this fee to my board?") — never
   "why", which reads as accusation. Summarize their view until you hear "that's right".
7. **Invent options for mutual gain before dividing value.** Longer commitment for lower
   unit price, volume consolidation, dropping services you don't use, different payment
   or compensation structure. Expand the pie before slicing it — then anchor every ask to
   an objective criterion ("the benchmark for this AFP code is X"), never to pressure.
   Criteria let both sides concede to a standard instead of to each other.
8. **Close against your BATNA.** Accept only what beats it; walk away above it. Never
   split the difference below it — half of unacceptable is still unacceptable. Trade
   concessions ("if you move the unit price, we move volume"), never give them away, and
   log what was agreed while it's fresh.

**Human gate (in force on every run):** the human sets the walk-away line before any
conversation and makes every concession decision. The LLM preps, drafts, and rehearses;
it never negotiates live unattended, and it never sends the ask on its own.

## Why / learn
The method is two layers because negotiations fail at two different altitudes. Fisher and
Ury's strategy layer (*Getting to Yes*, from the Harvard Negotiation Project) answers
"what is a good deal and how do I know?": interests, not positions, are where agreements
hide; the BATNA — not politeness, size, or nerve — is the real source of negotiating
power, because it converts "should I accept?" into a comparison; objective criteria turn
haggling into joint problem-solving, since neither side loses face conceding to a
benchmark. Voss's tactics layer (*Never Split the Difference*, from FBI hostage-negotiation
practice) answers "what do I actually say?": mirrors and labels lower the counterpart's
guard by proving they are heard; calibrated how/what questions create the illusion of
control while making your constraint their problem; the accusation audit takes the sting
out of objections by naming them first. Strategy without tactics collapses under pressure
in the room; tactics without a BATNA are charm with no floor. Be honest about the evidence:
this is practitioner canon — Harvard Program on Negotiation teaching practice and FBI
field practice — not controlled-trial science, so treat it as well-tested craft, and note
that most counterparties here are repeat relationships, which is exactly why honest
tactics beat clever ones. The reason an LLM amplifies this method is mundane: the prep is
a structured document set almost nobody actually writes, and rehearsal needs a
counterpart. Drafting interest maps, BATNA trees, criteria tables, accusation audits, and
question banks — and playing the other side of the table — is precisely the work the LLM
can do in minutes, leaving the human the two things only they can supply: the walk-away
line and the concessions.

## Common mistakes
- Defending a position instead of an interest → collision. Ask what the position is *for*, on both sides.
- Walking in without a BATNA → any deal looks acceptable. Build and cost the alternative first; it is the floor.
- Splitting the difference below the walk-away line → half of unacceptable is still unacceptable. Test against BATNA, not against the midpoint.
- Skipping the accusation audit → their objections land mid-conversation at full force. Name the worst ones first.
- Using mirrors and labels as gimmicks or gotchas → it reads as mockery and backfires. Tactical empathy is genuine perspective-taking.
- Anchoring with pressure ("take it or we walk") instead of criteria → positional standoff. Let the benchmark do the arguing.
- Giving concessions instead of trading them → the counterpart pockets each one and asks again. Every move gets a reciprocal.
- Letting the LLM run the negotiation live or send the ask unattended → prep and rehearsal only; the human makes every commitment.

## Tailor to your environment
Record your standing counterparties (banks, processors, carriers, key vendors), your
authority chain (who may approve which concession), and your usual objective-criteria
sources in `references/your-environment.md`. Keep walk-away lines, target prices, live
positions, and anything about a negotiation still in progress in
`references/your-environment.private.md` — git-ignored, never committed: a committed
walk-away line is a leaked one.

## References
- references/negotiation-prep-and-tactics.md — the full prep template, tactic catalog
  with example lines, the bank-fee-increase worked example built from account-analysis
  benchmark outputs, and the ethics line (honest tactics only)
- references/your-environment.md — your counterparties, authority chain, and criteria
  sources (fill in; sensitive detail goes in the git-ignored .private variant)
