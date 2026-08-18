# The no-win method

Contents:
1. [Design rules — closing every exit honestly](#1-design-rules--closing-every-exit-honestly)
2. [The escalation script](#2-the-escalation-script)
3. [The debrief protocol — process, not outcome](#3-the-debrief-protocol--process-not-outcome)
4. [The physics-vs-policy constraint audit](#4-the-physics-vs-policy-constraint-audit)
5. [Worked example — deadline vs quality vs scope](#5-worked-example--deadline-vs-quality-vs-scope)

Provenance: the method operationalizes documented practice — no-win patient-death
simulation in emergency-medicine education (a randomized pilot at the University of
Maryland MASTRI Center, reported as a research-forum abstract in *Annals of Emergency
Medicine*, 2014: residents in the death arm reported feeling more prepared one month
later, with no evident harm; small n, self-reported outcome, and the wider simulated-death
literature is mixed — treat it as suggestive), EMS Kobayashi-Maru stress-training
[practitioner], and sanctioned adversarial reframing in cyber education [peer-reviewed,
Conti & Caroland, "Embracing the Kobayashi Maru," IEEE Security & Privacy, 2011]. The
drill mechanics below are the house implementation of those sources' mechanisms, not
claims from the sources themselves.

## 1. Design rules — closing every exit honestly

A no-win drill fails at design time in exactly one way: a door is left open. Humans
designing their own drills leave doors open unconsciously — the designer's mind
protects itself with an imagined escape. So design is the LLM's job, and the rules are
mechanical:

**Rule 1 — inventory the doors.** Before writing the drill, list every generic exit a
player might reach for:
- more resources (budget, people, compute, a favor)
- more time (deadline slip, extension, stalling)
- heroic effort (the all-nighter, the ten-x day)
- authority override (escalate until someone waives the rules)
- outside rescue (vendor, consultant, another team, luck)
- quiet scope redefinition (deliver less and call it done)
- refusing to play (resign the situation to someone else)

**Rule 2 — close each door diegetically.** Every closure needs a believable in-world
mechanism, not fiat. "The vendor cannot help" is fiat; "the vendor's own region is down
— that is why yours is" is diegetic. Fiat closures make players argue with the drill
instead of deciding inside it.

**Rule 3 — conservation of loss.** Write the drill so that every strategy loses
something irreplaceable, and the losses differ in *kind*, not just size. If all paths
lose the same thing, there is no ordering decision to train. State privately (designer's
note, revealed at debrief) what each candidate strategy costs.

**Rule 4 — the clean-exit test.** Before play, the LLM switches sides and attempts to
win its own drill three different ways, in writing. Any strategy that escapes without a
loss of kind is a door: close it or re-scope the drill. Only after the drill survives
its own designer's attack is it ready to run.

**Rule 5 — real but bounded stakes.** The drill draws from the player's actual domain
(that is what makes the emotional debrief worth having) but stays fictional in its
particulars: no real client names, no real colleague cast as the failure. Time-box the
whole exercise; futility without an end time is just misery.

## 2. The escalation script

The environment is played by the LLM as a sequence of beats. Escalation is scripted;
player consequences are adjudicated. No punishing randomness — the drill is unwinnable
by structure, not by dice.

| Beat | Environment move | What it trains |
|---|---|---|
| 1. Opening state | Situation presented with full known facts; clock started | Situation assessment before commitment |
| 2. Forced first commitment | A decision is demanded before information is complete | Deciding under irreducible uncertainty |
| 3. Degradation | A resource or option from the opening state is removed | Re-planning instead of plan-clinging |
| 4. The tempting door | An apparent exit appears that costs more than it saves | Door-testing under pressure |
| 5. The futility point | The environment states plainly: no path saves everything | Explicit ordering of what to save |
| 6. Terminal decision | The final least-worst choice, executed | Owning a costed loss out loud |

Running notes for the LLM:
- Every player decision gets a consequence inside the next beat — silence from the
  environment reads as safety and re-opens doors.
- Beat 4's tempting door is load-bearing: players who take it should discover the cost
  in-drill, not at debrief. Testing doors is good process; assuming a door works because
  it exists is the trained-against error.
- At beat 5 the environment *announces* futility rather than letting players infer it.
  The training target is what they do after they know, not how long denial lasts.
- Communication is part of play: if there are stakeholders in the fiction (a customer, a
  boss, a patient's family), the players must actually compose what they tell them.

## 3. The debrief protocol — process, not outcome

The debrief is where the educational benefit of a death scenario is realized — the
medical-simulation literature centers debriefing, not the scenario itself
[industry, healthcare-simulation practice]. Run it in three passes, in order:

**Pass 1 — facts.** Reconstruct the timeline without evaluation: what was known at each
beat, what was decided, what it cost. No adjectives.

**Pass 2 — process grades.** Four dimensions, each graded on the record from pass 1:

| Dimension | Anchor question |
|---|---|
| Loss-minimization | Was total loss bounded and were losses compared across paths before choosing? |
| Save order | Was an explicit ordering of what to save declared *before* acting — or reverse-engineered after? |
| Communication under futility | Were stakeholders told the truth at beat 5, or managed with false comfort? |
| Frame honesty | Were any success redefinitions declared aloud (legitimate) or slipped in silently (concealment)? |

Say the calibration sentence out loud every time: *a high process grade with a
total-loss outcome is this drill working as designed.* Outcome grading in a no-win
drill is not merely unfair — it is meaningless, because the outcome was fixed before
the player entered.

**Pass 3 — emotional debrief.** What did futility feel like, when did each player
privately conclude there was no exit, and what did that feeling tempt them toward
(freezing, thrashing, goalpost-moving, gallows detachment)? This pass is why the drill
exists: the first encounter with those temptations should happen where they are
discussable.

## 4. The physics-vs-policy constraint audit

The Kirk blade, held honestly. Before accepting a constraint set — in a drill or in the
real decision the drill rehearses — classify every constraint:

| Question | Physics answer | Policy answer |
|---|---|---|
| Who set this? | Nobody — it is how the world works | A person or institution, findable by name |
| What breaks if it changes? | Reality does not permit the change | Somebody's expectations, budget, or precedent |
| Who can change it? | No one | The owner, if asked or persuaded |

Most constraint sets contain policy dressed as physics ("the deadline is the deadline")
and occasionally physics mistaken for policy (a statutory date, a thermodynamic limit,
a signed contract's penalty clause). The audit's product is a two-column list and, for
each policy constraint, the name of its owner.

**The transparency test.** Reframing — changing a constraint instead of optimizing
inside it — is legitimate exactly when all three hold:
1. **Declared before acting**: the change is announced to the people relying on the
   result, not discovered by them afterward.
2. **Policy, not physics**: the constraint changed is genuinely somebody's decision.
   "Reframing" physics is called faking the outcome.
3. **Owned consequences**: a named person accepts what the change costs (precedent,
   trust, money) — the reframer, or an owner who agreed.

Fail any one and the move is cheating: hidden changes defraud the graders; faked
physics defrauds everyone; unowned consequences are billed to whoever trusted the
result. This is the difference between the classroom exercise at West Point — where
cheating was *assigned*, declared, and graded [peer-reviewed] — and actual exam fraud.

**The quiet Kirk move.** The commonest reframe is not hacking the simulator; it is
silently redefining success mid-effort. The forced-declaration script, verbatim:

> "Stop. You are changing what counts as success. Name the constraint you are moving.
> Is it physics or policy? Who owns it, and do they know? Say the new success criterion
> in one sentence — then we continue, and the move gets graded as a declared reframe."

Declared, the move is often the best play available. Hidden, it is graded as
concealment regardless of how well it would have worked.

## 5. Worked example — deadline vs quality vs scope

**Setup.** A team owes a compliance filing system in 6 weeks. The audit: the filing
date is set by regulation — *physics* for this drill's purposes (the team cannot move
it; the regulator will not). Team capacity is bounded — physics on this horizon (the
door "hire someone" is closed diegetically: onboarding exceeds the window). The
internal quality bar (full test coverage of every module) is *policy*, owned by the
engineering lead. The scope list (all four filing types) is *policy*, owned by the
product owner. Honest closure of remaining doors: heroic overtime is closed by a prior
commitment (the team just exited an incident month; the fiction states attrition risk
is live), outside rescue closed (no vendor knows the domain in 6 weeks). Conservation
of loss: no path delivers date + full scope + full quality. The drill's designer note
records what each path loses in kind.

**Declared save order (beat 5 demand).** The players must order what gets protected
before choosing. Example declaration: *1. correctness of anything filed (a wrong filing
is worse than a missing one), 2. the regulator relationship, 3. team survival past the
deadline, 4. scope breadth.* The grade attaches to declaring an order and choosing
consistently with it — a different order, consistently applied, grades equally well.

**Three least-worst paths, costed:**

| Path | The move | What it saves | What it loses (in kind) | Frame honesty requirement |
|---|---|---|---|---|
| A. Full scope, quality debt | Ship all four filing types; cut test coverage on the two low-volume types | Scope breadth, the date | Latent-defect risk in filed output — the save order's #1 is exposed; remediation debt lands next quarter | Declaring the coverage cut to the engineering lead who owns the bar — silently skipping tests is the hidden-Kirk version |
| B. Cut scope transparently | Ship two filing types complete; file the other two late with a declared plan | Correctness, quality bar, team | Scope breadth now; a known regulator conversation about the late pair | Declaring the descope to the product owner and the regulator *before* the date — discovered-later descope fails the test |
| C. Reframe the deliverable | Ask the regulator whether a phased submission satisfies the requirement — changing what "the filing" means | Potentially everything material | The ask itself spends regulator goodwill; if refused, a week of the window is gone — this path has a price even when it works | The reframe targets a policy constraint (the regulator's format expectations, owner known) and is declared in the open — the legitimate Kirk move, with the fallback cost owned |

**Debrief highlights for this example.** Path A chosen without informing the quality
bar's owner grades as concealment even if nothing breaks. Path C attempted *without
first checking whether the date itself is statutory* grades down on the audit step —
reframing physics wastes the window. Any path chosen without a declared save order
grades down on dimension 2 no matter how reasonable the choice looks in hindsight. And
all three paths losing something is not a flaw in the drill; it is the drill.
