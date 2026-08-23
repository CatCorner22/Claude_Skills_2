---
name: rule-stress-testing
description: >-
  Stress-tests any rule set (agent guardrails, CLAUDE.md, team policies, contract clauses) by
  generating the situations where rules conflict, gap, or perversely instantiate: inventories
  rules and their unstated precedence, extracts load-bearing undefined terms, runs the six
  failure modes cataloged in Asimov's robot stories (conflict equilibrium, term widening,
  redundancy loss/literal compliance, scope creep/precedence inversion, definitional capture,
  information partitioning), adds Goodhart and malicious-compliance passes, classifies findings,
  proposes fixes in legal-canon vocabulary (specific-over-general, ambiguity against the
  drafter), then re-tests the fixed set, since patches breed new conflicts. Use when hardening
  rules before they meet reality or hunting what breaks them. Triggers: three laws, rule
  conflict, stress test the rules, loophole hunt, what breaks this policy, clause conflict,
  conflicting rules, malicious compliance, specification gaming.
metadata:
  version: "1.2.1"
  source: >-
    Commissioned by the user, inspired by Isaac Asimov's robot stories — homage in
    triggers and teaching only; no affiliation. The stories are cited as fiction that
    catalogs rule-failure modes, never as an engineering standard. The mechanism is
    documented practice: property-based testing (QuickCheck lineage), red-teaming,
    Goodhart's Law and AI specification-gaming research, work-to-rule, and the legal
    canons of construction. Provenance marks: [snippet-only] = verified from search
    snippets, not the full source; the ×N suffix is how many independent snippets agreed
    (×2 is thin — present it carefully; ×4 is well corroborated).
---

# Rule stress-testing (the Asimov pass)

Asimov's Three Laws were never a safety standard — they were a story engine, and their
author said so: "There was just enough ambiguity in the Three Laws to provide the
conflicts and uncertainties required for new stories" (*The Rest of the Robots*, 1964)
[snippet-only, ×3]. Nearly every robot story is a carefully drafted rule set meeting the
one situation its drafters didn't imagine — which makes the corpus something genuinely
useful: a failure-mode catalog for rule sets, worked out across four decades of thought
experiments. This skill runs that catalog, plus its real-world descendants
(property-based testing, red-teaming, specification-gaming research, the legal canons),
against whatever rules you hand it, and returns the concrete story where your rules
collide, fall silent, or win on the letter while losing on the point.

## When to use
- A rule set is about to meet reality: agent guardrails, a CLAUDE.md, a team policy, a
  code-freeze or on-call policy, contract clauses, house git rules — and you want the
  collisions found on paper first.
- Someone already found a loophole, or two rules just gave contradictory instructions,
  and you want the rest of the family found before they fire in production.
- A natural pair: stress-testing the guardrails that
  `coding-agent-skills:agentic-workflow-design` produces, before an agent lives inside
  them.
- Not for: commissioning or adversarially auditing a prompt or system prompt →
  `coding-agent-skills:master-prompt-architect` (it owns the adversarial interrogation
  of a prompt under construction; this skill owns rule-conflict and loophole discovery
  inside an existing rule set).
- Not for: failure-mode analysis of a process or design →
  `continuous-improvement-skills:fmea` (it ranks how a process fails; this skill finds
  where rules fight each other).
- Not for: designing agent guardrails from scratch →
  `coding-agent-skills:agentic-workflow-design`.
- Not for: deciding whether to remove a rule →
  `coding-agent-skills:soviet-space-graphite` (Chesterton's fence: understand a rule
  before deleting it; this skill helps by showing what a rule is FOR — what breaks
  without it).

## Do it
The six-mode taxonomy with its story exhibits, the term-extraction drill, the fix
vocabulary, and a worked code-freeze example are in `references/rule-stress-method.md`.

1. **Inventory the rules and their intended precedence.** Write every rule verbatim,
   numbered, with its source and owner. Then ask: when two of these collide, which wins?
   Asimov's Laws carry explicit precedence in their own text ("except where such orders
   would conflict with the First Law"); most human policies carry none — an unstated
   precedence order is finding #1 before any collision is even generated.
2. **Extract every load-bearing undefined term.** The nouns and verbs the rules' force
   hangs on: "harm," "done," "emergency," "deployment," "reasonable," "urgent." Each one
   is a widening risk (the term quietly grows until the rule fires everywhere) or a
   capture risk (whoever defines the term controls the rule). List them with the rule
   they anchor.
3. **Run the six-mode pass.** For each mode, ask its generator question against your
   rule pairs — "what situation makes THIS pair collide HERE?": conflict equilibrium
   (two rules balancing forever instead of resolving); ambiguous-term widening; modified-
   rule redundancy loss plus literal compliance (which clause looks safe to drop; which
   order would be catastrophic followed exactly as worded); scope creep with precedence
   inversion (a rule's beneficiary or scope generalizes until it authorizes what it was
   written to prevent); definitional capture; information partitioning (the gated action
   split into steps so no single step trips the rule). One concrete story per hit.
4. **Add the Goodhart pass.** For every rule that references a measure, metric, or
   threshold: how does the measure get satisfied while the goal gets defeated? This is
   the specification-gaming/reward-hacking lineage, and real systems supply a compiled
   catalog of examples [snippet-only, ×3].
5. **Add the malicious-compliance pass.** What does following the letter while defeating
   the spirit look like here? Work-to-rule is the documented human form — organized
   labor slowing an operation to a crawl by obeying every rule exactly
   [snippet-only, ×4]. If perfect compliance can be used as a weapon, the drafting is
   carrying intent it never wrote down.
6. **Classify and fix.** Each finding is a CONFLICT (rules collide), a GAP (no rule
   reaches the situation), or a PERVERSE INSTANTIATION (rule followed, purpose
   defeated). Fixes, in the legal canons' vocabulary: explicit precedence
   (specific-over-general / lex specialis; later-over-earlier, solid for statutes and
   weaker for contracts — anchor on the statute form); a term definition (only for
   load-bearing terms); or rule repair — rewrite, split, or delete (deletion goes
   through the Chesterton's-fence check first). Adopt contra proferentem internally:
   read your own ambiguity against yourself, because that is the reading a motivated
   party will find.
7. **Re-test the fixed set.** Fixes breed new conflicts. The canonical warning: the
   Zeroth Law was the patch for the individual-vs-humanity conflict, and adopting it
   destroyed Giskard, the robot that formulated it (*Robots and Empire*, 1985)
   [snippet-only, ×4]. Run at least the modes your fixes touched, plus the Goodhart pass
   on any new threshold a fix introduced.

## Why / learn
The core move is borrowed from property-based testing (QuickCheck — Claessen & Hughes,
ICFP 2000; the Hypothesis lineage carries it on) [snippet-only, ×4]: don't check the
examples you already thought of — state the invariant and generate inputs hunting for the
counterexample. A rule set is a specification in prose, so it deserves the same
treatment; the six modes are the generators, and red-teaming supplies the adversarial
stance [snippet-only, ×4]. Fiction earns its seat because each story is a minimal
reproduction case: one failure mode, isolated, run to its conclusion — "Runaround" is
what miscalibrated rule weights do (equilibrium instead of decision); "Liar!" is what an
undefined term does when it silently widens; "Little Lost Robot" is what removing a
"redundant" clause does, and simultaneously what literal compliance does to a hyperbolic
order [snippet-only, ×4 each; exhibits and provenance per mode in the reference].

The honesty rail matters because the Laws are so quotable that they get cited as real
engineering, which inverts the stories' point. They are narrative devices: the EPSRC/AHRC
Principles of Robotics explicitly set them aside as unworkable for actual robotics, and
the machine-ethics literature concurs [snippet-only, ×4]. Related discipline: the most
common misquote of the First Law drops "or, through inaction, allow a human being to come
to harm" — and removing exactly that clause is the plot of "Little Lost Robot"
[snippet-only, ×4], a live demonstration that a rule's most-forgotten clause is often its
most load-bearing.

Goodhart's Law explains why the measure pass is separate: when a measure becomes a
target, it stops being a good measure, and both machine learners (specification gaming,
reward hacking — Krakovna's compiled examples; DeepMind's popularization
[snippet-only, ×3]) and humans (malicious compliance, work-to-rule [snippet-only, ×4])
optimize the letter the moment the letter pays better than the spirit. The legal canons
earn their place as the fix vocabulary because courts have resolved rule collisions for
centuries and their solutions compress well: the specific rule beats the general one;
ambiguity costs its drafter; for statute-like sequences, later beats earlier
[snippet-only, ×3-4]. The re-test discipline closes the loop: a fix is a new rule, and
new rules enter the same collision space they were written to calm.

## Common mistakes
- Citing the Three Laws as a real safety framework → they are fiction that catalogs
  failures; EPSRC set them aside, and using them as a standard inverts the stories'
  point.
- Quoting the First Law without the inaction clause → the dropped clause is the one
  whose removal drives "Little Lost Robot"; quote it whole or not at all.
- Attributing "fail in interesting ways" to Asimov → circulating commentary; use his
  real ambiguity quote from *The Rest of the Robots*.
- Testing rules one at a time → conflicts live in pairs and precedence; generate
  collisions, not per-rule read-throughs.
- Defining every term exhaustively → each definition adds boundaries to game; define
  only the load-bearing terms the extraction drill surfaced.
- Treating malicious-compliance findings as accusations → they measure drafting quality,
  not colleagues' character; the fix is better rules, not suspicion.
- Declaring victory after the fix → patches breed new conflicts (the Zeroth-Law lesson);
  the fixed set gets its own pass.
- Leaning on later-over-earlier to fix a contract-style rule set → that canon is solid
  for statutes and jurisdiction-dependent for contracts; prefer explicit precedence
  clauses.

## Tailor to your environment
Record in `references/your-environment.md`: the standing rule sets worth testing (your
CLAUDE.md, git rules, code-freeze and on-call policies, agent guardrails), where
precedence decisions are recorded once made, the measures your rules reference (ripe for
the Goodhart pass), and your re-test cadence after amendments. Where a fix must bind your
own future self — a definition you know you'll be tempted to re-widen under deadline
pressure — write it as a pre-commitment with the unbinding condition stated in advance
(`decision-science-skills:ulysses-pact`). Anything naming real contracts, clients, or
personnel goes in `your-environment.private.md` (git-ignored), never in a committed file.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/rule-stress-testing.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/rule-stress-method.md — the Three Laws quoted whole with provenance and
  quote cautions, the six-mode taxonomy with one story exhibit per mode, the
  undefined-term extraction drill, the Goodhart and malicious-compliance passes, the
  legal-canon fix vocabulary with the statute-vs-contract caveat, a worked example
  stress-testing a five-rule code-freeze policy, and the re-test discipline
- references/your-environment.md — your rule sets, precedence records, referenced
  measures, and re-test cadence (fill in)
