# The symmetry method

How to repair a risk asymmetry: map the transfer, draft the graduated table, write
the attestations, make it contractual, check the incentive — and tell the Hammurabi
story with its provenance intact.

## Contents
1. [The risk-transfer map](#1-the-risk-transfer-map)
2. [The symmetry-table template](#2-the-symmetry-table-template)
3. [Worked example A — software vendor contract](#3-worked-example-a--software-vendor-contract)
4. [Worked example B — internal go-live sign-off](#4-worked-example-b--internal-go-live-sign-off)
5. [Attestation language patterns](#5-attestation-language-patterns)
6. [Graduated-consequence design](#6-graduated-consequence-design)
7. [The perverse-incentive check](#7-the-perverse-incentive-check)
8. [The provenance parable, told properly](#8-the-provenance-parable-told-properly)

## 1. The risk-transfer map

Four questions, answered with names (roles, not "the team"):

1. **Who decides?** Who chooses the design, the shortcut, the vendor, the date — the
   decisions that create or hide risk?
2. **Who eats the tail?** If the bad outcome lands — outage, defect, lost matter,
   failed launch, safety event — whose money, time, reputation, or standing absorbs it?
3. **What is currently binding the decider to the tail?** Contract terms, personal
   sign-off, bonus linkage, professional liability — or nothing?
4. **What does the decider know that the loss-bearer cannot see?** This names the
   hidden risk symmetry must price in: the decider's private knowledge is exactly
   what monitoring can't reach and consequence can.

If answer 1 and answer 2 are different names and answer 3 is "nothing," you have the
asymmetry. The rest of this file is the repair.

## 2. The symmetry-table template

One row per harm class. The table is the contract-in-miniature; every attestation and
clause should trace back to a row.

| Harm class | Example outcome | Who bears what | Bound how, and when |
|---|---|---|---|
| Minor | Cosmetic defect, small rework | Creator fixes at own cost | Standing remedy clause / team norm, agreed before work |
| Moderate | Missed deliverable, degraded service | Creator remedies + absorbs the delay cost (holdback not released) | Contract holdback / attestation on the acceptance gate |
| Severe | Outage, breach of obligation, material loss | Creator's payment/bonus/renewal at stake; named attester answers for the failed verification | Defect-liability clause + named attestation, signed pre-go-live |
| Catastrophic | Safety event, existential loss to the loss-bearer | Contract termination, clawback, professional consequence for the deciding role | Warranty + liability terms negotiated before award |

Rules for filling it in:
- **Graduate** (see section 6) — each row's consequence scales with its harm.
- **Bind before the work** — the "when" column must predate the risk-creating
  decision, or the table is blame, not incentive.
- **Power test every row** — the person named must have had the authority to decide
  otherwise. If they didn't, move the consequence up to whoever did.

## 3. Worked example A — software vendor contract

Situation (generic contracting pattern — adapt to any industry): an organization is
buying a system implementation from a vendor. Past experience: the delivered system
failed within weeks and the vendor quoted extra fees to repair its own defects. The
buyer wants the next contract symmetric. Illustrative terms, not legal advice — run
final language past counsel.

Risk-transfer map: the vendor decides architecture, staffing, and testing depth
(creates risk); the buyer eats outages, rework, and business disruption (bears loss);
current binding: none beyond "best efforts."

| Harm class | Example outcome | Who bears what | Bound how |
|---|---|---|---|
| Minor | Cosmetic/UI defects at handover | Vendor fixes free within the defect-liability period | Defect-liability clause (a defined period after acceptance during which defects are the vendor's cost) |
| Moderate | Function fails acceptance tests | Payment milestone withheld until pass; retention (a % of fee) held until the warranty period ends | Milestone + retention/holdback clauses |
| Severe | System failure in production within the warranty period | Vendor remedies at own cost within a defined response time; service credits; renewal at risk | Warranty + remedy clause with named response times |
| Catastrophic | Data loss / prolonged outage from vendor defect | Liability up to a negotiated cap that actually bites; termination for cause; clawback of paid fees for the failed component | Liability and termination clauses |

The named-attestation layer: the vendor's engagement lead signs the acceptance
package personally — "I, ⟨name⟩, ⟨role⟩, attest the delivered system passed the
agreed acceptance tests ⟨list⟩ on ⟨date⟩" — so acceptance is a person, not a letterhead.

The tell to negotiate around: a vendor who resists *every* row is pricing their own
hidden knowledge of the work's quality. Either the symmetry goes in, or the price
should fall to cover the risk being transferred to you.

## 4. Worked example B — internal go-live sign-off

Situation (works for a system cutover, a product launch, a filing, an event — any
internal gate): a go-live gate currently reads "sign-offs: QA ✔ Security ✔ Ops ✔."
Nobody can say afterward who verified what; when a launch fails, the retrospective
finds each group assumed another had covered the gap.

Risk-transfer map: the go-live decision-maker and workstream leads create the risk
(choose readiness); frontline staff and users eat the loss (work the outage, absorb
the harm); current binding: team checkmarks — diffuse to the point of zero.

The repair — replace each checkmark with a named attestation into a graduated table:

| Harm class | Example outcome | Who bears what | Bound how |
|---|---|---|---|
| Minor | Cosmetic issues at launch | Owning workstream fixes in the first cycle, no escalation | Punch-list norm, agreed at gate design |
| Moderate | A launch-day workaround needed | The attester who verified that area leads the remediation and the follow-up verification | Named attestation per area |
| Severe | Rollback / material disruption | The go-live decision-maker answers for the decision in the post-incident forum; their attestation record is part of it | Decision attestation (below) |
| Catastrophic | Harm to users/clients | Decision authority reviewed; gate redesign owned by the decision-maker's chain | Gate charter, written before first use |

Attestations that replace the checkmarks:
- "I, ⟨name⟩, verified the restore procedure by executing it against ⟨environment⟩ on
  ⟨date⟩; recovery completed in ⟨duration⟩."
- "I, ⟨name⟩, verified the load result: ⟨test⟩ sustained ⟨level⟩ for ⟨time⟩ with
  ⟨outcome⟩."
- Decision attestation, the keystone: "I, ⟨name⟩, reviewed the attestations above and
  accept the residual risks ⟨list⟩. Go-live approved." — the decision-maker signs into
  the severe row personally.

The honesty rail, applied: the operator who executes the cutover runbook signs
nothing here — they decided nothing. If the runbook was wrong, that is a system fix
for whoever wrote and approved it.

## 5. Attestation language patterns

The anatomy of an attestation that carries weight — five parts, all present:

> I, **⟨name⟩**, ⟨role⟩, verified **⟨the specific thing⟩** by **⟨the specific
> means⟩** on **⟨date⟩**. ⟨What I did NOT verify / residual risk I am flagging.⟩

- **Name** — a person, never a team. Diffusion is the failure being repaired.
- **The specific thing** — "the restore procedure," not "backups." An attestation
  over a vague noun verifies nothing.
- **The specific means** — "by executing it," not "by reviewing the document."
  The means clause is where hollow attestations are caught: if the honest means is
  "I read the config," the attestation says so, and the gate can judge whether
  reading was enough.
- **Date** — attestations age; a verification from before the last change is history,
  not assurance.
- **The exclusion** — what was NOT verified. This is the anti-concealment valve: an
  attester who can flag residual risk without penalty has no reason to hide it, and
  the decision-maker signs the residual-risk list knowingly.

Anti-patterns: "reviewed by team" (no name); "QA passed" (no thing, no means);
"verified as per process" (means launders into proceduralism); attestations demanded
of people who had no authority over the thing attested (power-rail violation — move
it up).

## 6. Graduated-consequence design

Why graduation is load-bearing, not decorative:

- **Flat-severe** ("any failure and you're out") over-prices minor errors → people
  stop signing, everything escalates upward, and the organization re-invents the
  diffuse committee to hide inside. The gate seizes.
- **Flat-mild** (every failure gets a retro and a promise) under-prices catastrophe →
  tail risk stays free to manufacture, which is the original disease.
- **Graduated** keeps ordinary work survivable while making the catastrophic
  shortcut personally expensive to the person who could choose it. That matches how
  the source text actually reads: §229 (death of the owner) and §232 (rebuild at own
  cost for property damage) are different rows of one table, not one rule
  [snippet-only].

Design moves:
- Define harm classes in the loss-bearer's terms (what lands on them), not the
  creator's (how embarrassing it is).
- Make the minor rows cheap and automatic (fix-at-own-cost norms) so the table is
  exercised routinely and doesn't only appear at disasters.
- Reserve person-level consequence (renewal, clawback, authority review) for rows
  where a person genuinely chose the risk.
- Write the "bound how/when" column first if the table stalls — a row with no
  binding mechanism is a wish.

## 7. The perverse-incentive check

Run these four questions against the finished table before it goes live:

1. **Over-caution:** does any row make refusing to sign safer than doing the work?
   Symptom to predict: approvals migrate upward, gates back up, the diffuse committee
   returns under a new name. Fix: cheapen the minor rows; make the attestation's
   exclusion clause a first-class, penalty-free channel.
2. **Concealment:** does surfacing a problem cost the surfacer under any row?
   Symptom: silent workarounds, "no issues found" streaks too clean to be true. Fix:
   consequence attaches to the decision and the verification claim, never to the act
   of reporting; pair with blameless treatment of system-caused failure.
3. **Gaming the class boundaries:** can a creator reclassify harm downward (call the
   outage "degradation") to slide rows? Fix: harm classes defined by the
   loss-bearer's measurable experience, with the classification decision itself owned
   by the loss-bearer's side.
4. **Symmetry theater:** is any consequence nominally severe but practically
   unenforceable (a liability cap that rounds to zero, an attestation nobody stores)?
   Fix: the "bound how" column must name a mechanism that has actually fired
   somewhere before, or a named owner who can fire it.

Then send the whole rule set to `coding-agent-skills:rule-stress-testing` — it owns
the systematic loophole hunt (conflict, term-widening, malicious compliance) and will
find the collisions this checklist-of-four cannot.

## 8. The provenance parable, told properly

Told at full strength, with sources marked the way the library's research dossier
marks them (docs/research/epic-wave-held-research.md, Lane 1 entry 5):

**The real thing.** The Code of Hammurabi, carved on a diorite stele around 1754 BCE,
contains a graduated building-liability section that survives verbatim: §229 — a
builder whose house collapses and kills the owner is put to death; §230 — if it kills
the owner's son, the builder's son is put to death; §231 — if it kills a slave, the
builder replaces the slave; §232–233 — property destroyed or defects appearing, the
builder rebuilds and repairs at his own cost [snippet-only: ehammurabi.org, cross-checked].
(§230 also shows the text's moral distance — punishing the builder's son is symmetry
by bloodline, which nobody should import; the design lesson survives the era's
brutality: consequence graduated by harm class, bound to the risk creator, in force
before the work.)

**The legend.** "Roman engineers had to stand beneath the arch as the scaffolding was
removed" — repeated in engineering ethics talks, safety trainings, and management
books. No ancient source contains it. The Kiwi Hellenist blog traced its earliest
findable instance to a USENET signature line from around 2004, and the practice is
implausible on its face [snippet-only: kiwihellenist, via search]. It is folklore
with excellent production values: modern, anonymous, and optimized for retelling.

**Why teach the fake one at all.** Because the pairing is the sharpest available
lesson in *both* directions this skill cares about. On incentives: the legend spread
because it dramatizes precisely the correct mechanism — creator under the creation,
consequence at the moment of truth — which tells you the mechanism's appeal is real
even where the anecdote isn't. On honesty: an accountability designer who launders a
fake story into evidence has surrendered the exact asset the work runs on. The rule
of use: tell the arch story if it helps, *always labeled as folklore* — and then put
the real stele on the table, because a verbatim source from ~1754 BCE outranks any
invented Roman every time. If a claim's provenance can't be shown, it goes in the
legend column, no matter how well it teaches.
