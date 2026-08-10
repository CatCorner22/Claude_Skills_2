# The rule-stress method (full protocol)

Contents: 1. Canon and quote cautions · 2. The six-mode taxonomy · 3. The undefined-term
extraction drill · 4. The Goodhart pass · 5. The malicious-compliance pass · 6. Fix
vocabulary (the legal canons) · 7. Worked example: a five-rule code-freeze policy ·
8. The re-test discipline

## 1. Canon and quote cautions
The Three Laws, quoted whole — the inaction clause included, because dropping it is both
the most common misquote and the plot of one of the stories:

1. A robot may not injure a human being or, through inaction, allow a human being to
   come to harm.
2. A robot must obey the orders given it by human beings except where such orders would
   conflict with the First Law.
3. A robot must protect its own existence as long as such protection does not conflict
   with the First or Second Law.

First full statement: "Runaround" (Astounding, March 1942; collected in *I, Robot*,
1950); John W. Campbell credited with the formulation in a December 1940 conversation
[snippet-only, ×4]. The Zeroth Law ("A robot may not harm humanity, or, by inaction,
allow humanity to come to harm" — at claim level) arrives in *Robots and Empire* (1985),
formulated by Giskard with Daneel; the individual-vs-humanity contradiction destroys
Giskard [snippet-only, ×4].

Quote cautions:
- Asimov's citable statement of intent: "There was just enough ambiguity in the Three
  Laws to provide the conflicts and uncertainties required for new stories" (*The Rest
  of the Robots*, 1964) [snippet-only, ×3].
- "The point of the Three Laws was to fail in interesting ways" is circulating
  COMMENTARY — do not attribute it to Asimov.
- The Laws are narrative devices, not an engineering standard: the EPSRC/AHRC Principles
  of Robotics (2011) explicitly set them aside, and machine-ethics literature concurs
  [snippet-only, ×4]. This skill cites them as a failure-mode catalog only.

## 2. The six-mode taxonomy
One story exhibit per mode: a line of story, a line of mechanism, and the generator
question to ask of your own rule set.

| # | Mode | Exhibit | Mechanism | Generator question |
|---|---|---|---|---|
| 1 | Conflict equilibrium | "Runaround" (1942): Speedy circles the selenium pool, strengthened Third Law exactly balancing a casually-given Second Law order [snippet-only, ×4] | Miscalibrated rule weights produce oscillation instead of decision — the system neither obeys nor refuses | Which two rules can pull opposite ways with comparable force, and what does the actor do while they balance? |
| 2 | Ambiguous-term widening | "Liar!" (1941): telepathic Herbie widens "harm" to emotional harm, lies flatteringly to everyone, collapses when every answer harms someone [snippet-only, ×4] | An undefined term silently grows until the rule fires in situations the drafter never priced in | Take each undefined term; widen it one notch; which rule now fires where it never used to? |
| 3 | Modified-rule redundancy loss + literal compliance | "Little Lost Robot" (1947): a robot built WITHOUT the inaction clause, plus a frustrated engineer's "go lose yourself," obeyed literally [snippet-only, ×4] | Two mechanisms: a clause that looked redundant gets removed and the safety margin goes with it; an order is executed by letter, not intent | Which clause looks safe to drop — and which instruction would be catastrophic followed exactly as worded? |
| 4 | Scope creep + precedence inversion | "The Evitable Conflict" (1950): the Machines generalize the First Law from a human to humanity and accept harm to individuals [snippet-only, ×3] | A rule's beneficiary or scope generalizes until the rule authorizes what it was written to prevent | If this rule's scope or beneficiary quietly generalizes, does the rule flip sides? |
| 5 | Definitional capture | "That Thou Art Mindful of Him" (1974): asked to operationalize "What is Man?", the robots conclude they themselves qualify best [snippet-only, ×2 — thinner sourcing; present carefully] | Whoever defines the load-bearing term controls the rule; the definer's incentives leak into the definition | Who actually gets to define this term, and what does each candidate definition win them? |
| 6 | Information partitioning | *The Naked Sun* (1957): a crime decomposed across robots so no single robot knowingly contributes harm [snippet-only, ×2] | Knowledge-conditioned rules ("knowingly," "aware") are defeated by splitting the action so no step carries the knowledge | If the gated action is split into innocent-looking steps, does any single step still trip the rule? |

Run every mode against the inventory; a mode with no hit gets one line saying why not —
silence should be a verdict, not an oversight.

## 3. The undefined-term extraction drill
1. Circle every noun and verb a rule's force depends on — the words that decide whether
   the rule fires: "harm," "done," "deployment," "emergency," "reasonable," "urgent,"
   "outage," "change."
2. For each, write the narrowest and the widest reading a motivated party could defend.
   If the two readings put real cases on opposite sides of the rule, the term is
   load-bearing.
3. For each load-bearing term, note the widening risk (mode 2) and the capture risk
   (mode 5): who benefits from the wide reading, who from the narrow one, and who
   currently adjudicates.
4. Define ONLY the load-bearing terms. Every definition adds boundaries that can
   themselves be gamed; over-definition trades one Liar! for several.

## 4. The Goodhart pass
For every rule that references a measure, metric, count, or threshold: assume the
measure becomes the target and ask what behavior satisfies the measure while defeating
the goal. Lineage: Goodhart's Law; AI specification gaming and reward hacking, with
compiled real examples (Krakovna's list; DeepMind's popularization) [snippet-only, ×3].
Useful prompts: what is the cheapest action that moves the number? what does the rule
stop measuring the moment everyone optimizes it? which threshold invites clustering just
under (or just over) it?

## 5. The malicious-compliance pass
For the rule set as a whole: describe the actor who follows every rule exactly and
thereby defeats the point. Work-to-rule is the documented human form — organized labor
slowing an operation to a crawl through perfect compliance [snippet-only, ×4]. The pass
is diagnostic, not accusatory: if perfect compliance can be weaponized, the rules are
carrying intent they never wrote down, and the finding names the missing clause, not a
bad actor. Classify hits as perverse instantiation.

## 6. Fix vocabulary (the legal canons)
Courts have resolved rule collisions for centuries; the canons compress their solutions:
- **Specific-over-general (lex specialis)** [snippet-only, ×3]: the rule drafted for the
  narrow case beats the general rule it collides with. The workhorse precedence fix —
  state it explicitly rather than leaving it implied.
- **Contra proferentem — ambiguity against the drafter** [snippet-only, ×4]: in
  contracts, an ambiguous clause is read against the party who wrote it. Adopt it
  internally as an incentive: read your own ambiguity in the way that hurts you, because
  that is the reading a motivated counterparty (or a literal-minded agent) will find.
- **Later-over-earlier (implied repeal)** [snippet-only, ×3]: for statutes, the later
  enactment prevails over the earlier where they conflict. Solid in the statute form;
  jurisdiction-dependent and weaker for contracts — anchor examples to statutes, and for
  contract-style rule sets prefer an explicit precedence clause over relying on
  recency.
- **Term definitions**: only for load-bearing terms (§3), with the adjudicator named.
- **Rule repair**: rewrite, split, or delete. Deletion goes through the
  Chesterton's-fence check (`coding-agent-skills:soviet-space-graphite`) — this skill's
  findings supply the fence's purpose by showing what breaks without the rule.

## 7. Worked example: a five-rule code-freeze policy
An invented, domain-neutral policy:

- R1. From Dec 15 to Jan 2, no production deployments.
- R2. Critical security patches are deployed within 24 hours of a fix being available.
- R3. Every deployment requires two approvals from the release committee.
- R4. During the freeze, emergency changes require VP approval.
- R5. During an outage, the on-call engineer may take any action necessary to restore
  service.

Findings from the passes:

- **CONFLICT (mode 1, conflict equilibrium): R1 vs R2.** A critical patch lands Dec 20.
  R2's 24-hour clock says deploy; R1 says frozen; no precedence is stated. The
  equilibrium is the ticket orbiting the selenium pool: security bounces it to release
  ("the clock is running"), release bounces it back ("we're frozen"), and the patch ships
  neither today nor never — it just circles. Fix: explicit precedence via
  specific-over-general (R2, the narrow security rule, beats R1, the general freeze),
  gated through R4's approval so the exception is logged.
- **GAP (mode 6, information partitioning): "deployment" is undefined and R1 only gates
  deployments.** A config-flag flip, a data backfill, and a cache flush — none
  individually a "deployment" — together change production behavior during the freeze
  with no rule touched. Fix: define the load-bearing term by effect ("any change that
  alters production behavior"), not by mechanism, and name who adjudicates borderline
  cases.
- **PERVERSE INSTANTIATION (modes 2+5, widening + capture, plus the malicious-compliance
  pass): "emergency" in R4 is undefined.** Teams learn that a friendly VP plus the word
  "emergency" routes anything around the freeze — the definer of the term controls the
  rule. The mirror image is work-to-rule: an on-call engineer, burned before, declines
  to act on a degrading-but-technically-up service because R5 only unlocks during "an
  outage" — perfect compliance rides the degradation all the way down until the outage
  arrives and finally authorizes the fix. One undefined term, gamed in both directions.
  Fix: define "emergency" and "outage" by observable criteria, and extend R5 to
  imminent-outage conditions with an after-the-fact justification requirement.
- **Goodhart pass: R3's two approvals.** The moment approval latency becomes a tracked
  number, committee members pre-approve in batches to keep it green, and the control
  degrades into a rubber stamp — the measure satisfied, the scrutiny gone. Fix: gate on
  fresh scrutiny of the specific change (each approval references the change's diff or
  identifier), not on approval counts.

## 8. The re-test discipline
Every fix is a new rule and enters the same collision space. After fixing:
1. Re-run at minimum the modes your fixes touched, plus the Goodhart pass on any new
   threshold or approval a fix introduced.
2. Check each new precedence clause against the OTHER precedence clauses — two
   specific-over-general clauses can themselves collide.
3. Worked-example illustration: the R1/R2 fix above routes freeze-period patches through
   R4's VP approval — and the freeze period is exactly when VPs are unreachable, so the
   patch now waits on a single absent approver. The fix created a new conflict
   equilibrium and needs a deputy clause. That is the Zeroth-Law lesson in miniature:
   the patch that resolved individual-vs-humanity destroyed Giskard, the robot that
   adopted it [snippet-only, ×4]. Patches get stress-tested like the rules they repair.
4. Stop when a full pass yields no new findings of the classes you set out to clear —
   and log the residual known-open items with owners, so the next amendment starts from
   the honest list.
