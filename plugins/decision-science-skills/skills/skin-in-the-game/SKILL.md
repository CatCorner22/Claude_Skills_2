---
name: skin-in-the-game
description: >-
  Designs consequence symmetry for decisions that transfer risk: maps who creates a
  risk versus who eats the loss when the tail lands (Hammurabi §229–233, the oldest
  written rule against transferring hidden tail risk — Taleb's Skin in the Game
  framing), drafts a graduated symmetry table (harm class → who bears what), converts
  diffuse "reviewed by team" approvals into named-owner attestations, puts real
  defect-liability and warranty terms into vendor and contractor agreements, then
  checks the new consequence for perverse incentives such as over-caution and
  concealment. Consequence design binds decision-makers with power, never
  punishment-washing onto the powerless. Use when a sign-off carries no consequence,
  a vendor will not stand behind its work, or accountability needs structure instead
  of exhortation. Triggers: skin in the game, who signs their name to this, who eats
  the loss, accountability without consequence, attestation, vendor won't stand
  behind it, hammurabi, consequence mapping.
metadata:
  version: "1.0.0"
  source: >-
    Built from the library's operational-wisdom research lane
    (docs/research/epic-wave-held-research.md, Lane 1 entry 5). The stele text of
    Hammurabi §229–233 is real and graduated; the "Roman engineer under the arch"
    companion story is modern folklore, earliest traced to a USENET signature line
    around 2004 (Kiwi Hellenist) — this skill teaches both, labeled. The modern
    framing is Nassim Nicholas Taleb's Skin in the Game (2018), cited as his. All
    external claims [snippet-only] provenance, cross-checked.
---

# Skin in the game (Hammurabi §229)

The Code of Hammurabi, carved around 1754 BCE, is verbatim real, and its
building-trade sections are graduated: if a builder's house collapses and kills the
owner, the builder is put to death (§229); if it kills the owner's son, the builder's
son (§230); if it kills a slave, the builder replaces the slave (§231); if it destroys
property or shows defects, the builder rebuilds or repairs at his own cost (§232–233)
[snippet-only]. Taleb (*Skin in the Game*, 2018) reads §229 as the oldest written rule
against transferring hidden tail risk: the party who creates the risk must be the one
standing under it when it lands [snippet-only]. The famous companion anecdote — the
Roman engineer made to stand beneath the arch as the scaffolding came down — is modern
folklore: no ancient source, earliest trace a USENET signature line from around 2004
[snippet-only]. This skill teaches both, labeled, because the contrast is the lesson
twice over: the real mechanism is consequence bound to the decision-maker before the
work, and the fake-but-viral story shows how much we want that mechanism to be true —
wanting it doesn't excuse citing it.

## When to use
- A sign-off, approval, or acceptance exists, but the person granting it loses nothing
  if it proves wrong — the signature is decoration, not consequence.
- A vendor or contractor will not stand behind the work: no warranty, no defect
  liability, maintenance sold separately from the failure it repairs.
- Designing an acceptance gate — a go-live, a release, a deliverable handover in any
  field — where the person creating the risk and the person eating the loss are
  different people.
- Auditing an incentive structure where losses land on people who had no say
  (the asymmetry Taleb's framing exists to expose).
- Not for: deciding whether a committed plan should continue or change course →
  see `decision-science-skills:the-challenger` (it governs the revision decision; this
  skill designs who bears what before the work starts).
- Not for: building a leader's or team's accountability culture → see
  `coding-agent-skills:extreme-ownership` (it owns the ownership ethos; this skill
  designs the contractual and structural symmetry underneath any culture).
- Not for: hunting loopholes in the consequence rule you just drafted → see
  `coding-agent-skills:rule-stress-testing` (the downstream partner — every rule this
  skill produces should visit it before going live).

## Do it
The risk-transfer map, symmetry-table template, worked examples, attestation language,
and the perverse-incentive check are in `references/symmetry-method.md`.

1. **Map the risk transfer.** For the decision or work product at hand, write two
   names: who creates the risk (chooses the design, the shortcut, the vendor, the
   date) and who eats the loss if the tail outcome lands (the outage, the defect, the
   lost matter, the failed launch). If the two names differ, you have found the
   asymmetry this skill exists to fix. If they are already the same person, you are
   done — the incentive is already honest.
2. **Draft the symmetry table, graduated.** One row per harm class, from annoyance to
   catastrophe, each row naming who bears what consequence — scaled to the harm, the
   way §229–233 scales. A flat consequence for every harm class over-punishes small
   errors and under-prices catastrophes; graduation is what makes the table usable.
3. **Convert diffuse approvals into named attestations.** Replace "reviewed by team"
   and "QA passed" with "I, ⟨name⟩, verified ⟨specific thing⟩ by ⟨specific means⟩ on
   ⟨date⟩." A name concentrates what a team label diffuses. Attach the attestation to
   the symmetry table: the attester is signing into a row, and should be able to read
   exactly what their signature costs them if the verified thing fails.
4. **For vendors and contractors, make the symmetry contractual.** Real
   defect-liability periods, warranty terms that cover failure of the delivered thing
   (not just "best efforts"), holdbacks or retention released on proven performance,
   and remedy obligations at the vendor's own cost — the §232–233 move, in any
   industry's contracting vocabulary. "Won't stand behind it" is a price signal:
   a counterpart who refuses all symmetry is telling you what they think of their
   own work.
5. **Check the incentive after the fix.** Every new consequence creates new behavior.
   Ask: does this rule now reward over-caution (nobody will sign anything, everything
   escalates) or concealment (problems get buried because surfacing one costs the
   surfacer)? Draft the answer, then send the finished rule to
   `coding-agent-skills:rule-stress-testing` for the full loophole-and-collision pass
   before it goes live.
6. **Hold the honesty rail.** Consequence design is for decision-makers with power —
   the people who choose the risk. Aiming it at the powerless (the operator following
   the runbook, the junior who couldn't refuse) is punishment-washing, and it breaks
   the mechanism: system problems get system fixes (the Deming reconciliation this
   library already holds in `coding-agent-skills:extreme-ownership` — fix the process,
   not the person). The test for every row of the symmetry table: could the person
   named in it have decided otherwise?

## Why / learn
The mechanism is asymmetry repair. When the risk creator and the loss bearer are
different people, the creator is playing with someone else's downside — and hidden
tail risk is the cheapest thing in the world to manufacture: skip the inspection,
thin the material, ship the untested path, and the savings are visible today while
the collapse is somebody else's, later. Taleb's point, and Hammurabi's, is that no
amount of monitoring fully substitutes for symmetry, because the creator always knows
more about the hidden risk than any inspector — so instead of trying to see
everything, bind the creator's payoff to the outcome and let their private knowledge
work for safety instead of against it. The binding must happen *before* the work:
consequence agreed after a failure is negotiation, not incentive.

Graduation and naming are what make symmetry practical rather than draconian. The
stele does not prescribe death for a cracked wall — §232 prices property damage as
rebuilding at the builder's cost, and reserves the extreme consequence for the extreme
harm [snippet-only]. A graduated table keeps small errors survivable (so people keep
building) while making catastrophic shortcuts personally expensive. Naming works on
diffusion of responsibility: "reviewed by team" lets each member assume another
actually checked, so accountability rounds to zero even when everyone is diligent.
"I, ⟨name⟩, verified X" makes one person imagine the failure with their signature on
it — which is the moment the verification actually happens.

Two rails keep this honest. First, power: §229 binds the *builder* — the party with
full knowledge and full choice — not the laborer carrying bricks. Consequence aimed
at people who couldn't have decided otherwise doesn't create safety; it creates
concealment, and it is how bad organizations counterfeit accountability. Blameless
treatment of system-caused failure and hard symmetry for decision-makers are not in
tension; they are the same principle applied at different altitudes. Second,
provenance: the arch story is the library's perfect parable because the impulse
behind repeating it is good — it dramatizes exactly the right mechanism — and it is
still false. Hold the real stele in one hand and the labeled legend in the other, and
you get to keep both the teaching and your credibility; cite the legend as history
and you lose the second, which in accountability work is the asset.

## Common mistakes
- Punishment-washing onto the powerless → the table binds whoever chose the risk;
  operators following the runbook get system fixes, not consequences.
- One flat consequence for every harm class → graduate it; §229 and §232 are
  different rows for a reason.
- "Reviewed by team" or "QA passed" as an approval record → replace with a named,
  specific, dated attestation tied to a symmetry-table row.
- Adding the consequence after the work (or after the failure) → symmetry binds
  before the work starts; afterward it is just blame with paperwork.
- Accepting "we don't do warranties" as a vendor norm → it is a price signal about
  their own confidence; negotiate the symmetry or price the hidden risk in.
- Skipping the perverse-incentive check → new consequences breed over-caution and
  concealment; check, then stress-test via `coding-agent-skills:rule-stress-testing`.
- Citing the Roman arch story as history → it is folklore traced to a ~2004 USENET
  signature line; the real stele text is stronger anyway — cite that [snippet-only].
- Confusing this with culture-building → ethos and debriefs belong to
  `coding-agent-skills:extreme-ownership`; this skill writes the structure that
  survives a culture change.

## Tailor to your environment
This skill ships domain-neutral on purpose — wire in your current role in
`references/your-environment.md`: the approval gates you own or sit inside, the
contracts and renewal dates you can influence, your organization's harm-class
vocabulary, who holds signing power at each gate, and where attestations are stored.
Keep the committed file structural — gate names and role titles, no live details.
Real counterpart names, contract terms, or dispute history go in
`your-environment.private.md`, which is git-ignored and never committed.

## References
- references/symmetry-method.md — the risk-transfer map, the graduated symmetry-table
  template with two worked examples (a software vendor contract and an internal
  go-live sign-off), attestation language patterns, graduated-consequence design, the
  perverse-incentive check, and the provenance parable told properly
- references/your-environment.md — your gates, contracts, harm-class vocabulary, and
  attestation registry (fill in)
