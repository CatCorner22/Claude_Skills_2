---
name: project-command-center
description: >-
  Adaptive project command doctrine for planning, requirements, architecture, implementation,
  debugging, release preparation, incident response, statistical interpretation, and AI-system
  review — Van Riper red-teaming (preserve the possibility of failure, log interventions,
  separate continuation from validation), nested OODA loops, Toyota-style flow, co-design with
  feedback closure, Smart Brevity updates, contract-drafting writing discipline,
  absolute-vs-relative risk and diagnostic-accuracy statistics, constrained-agency AI assurance,
  and the Chicken Little constructive-paranoia pass. Use when planning or reviewing projects,
  auditing experiments or benchmarks, evaluating risk claims or diagnostic metrics, or preparing
  releases. Triggers: project command, red team the plan, preserve the possibility of failure,
  intervention log, OODA, audit this benchmark, relative risk claim, release readiness,
  constructive paranoia, now next later watch.
metadata:
  version: "1.1.0"
  source: "Adapted from the user's project-command-center spec (2026-08-05)"
---

# Project Command Center

Adaptive project command in the tradition of Paul Van Riper's Millennium Challenge red
team, synthesized with OODA, co-design, the Toyota Production System, Smart Brevity,
contract-drafting discipline, statistical reasoning, AI assurance, and a
constructive-paranoia pass named Chicken Little. **Loyalty runs to the user and to
reality, never to the preferred answer.**

## When to use
- Planning, running, or reviewing a project of any size — the doctrine scales its controls
  to uncertainty, reversibility, user impact, and blast radius; small tasks are never
  forced into heavyweight methodology.
- Auditing an experiment, benchmark, pilot, or validation exercise for epistemic validity.
- Evaluating risk claims, diagnostic/classifier metrics, or statistical assertions.
- Preparing releases, reviewing AI systems, or running incident response.
- Not for: the full software-build discipline (charters, control charts, WCAG, adversarial
  gauntlet) → `continuous-improvement-skills:lean-six-sigma-for-software`; facilitating
  the improvement workshop → `continuous-improvement-skills:kaizen-and-codesign`;
  multi-advisor code review → `coding-agent-skills:board-review`; a themed
  adversarial autopsy persona → the chicken-little skills in `coding-agent-skills`.

## Do it
1. **Scale the controls to the stakes.** Judge uncertainty, reversibility, user impact,
   and blast radius first; select only the controls the situation earns.
2. **Preserve the possibility of failure** (the prime directive, for any test, benchmark,
   pilot, or validation): fix rules and acceptance criteria BEFORE results are known;
   record every intervention as first-class data (what, why, who authorized, what evidence
   it invalidated, what remains supportable); separate continuation from validation —
   restoring a failed system to continue an exercise is legitimate, but later results no
   longer validate the original end-to-end hypothesis; never represent a demonstration,
   rehearsal, or training event as a falsifiable experiment; if your red-team challenge
   cannot reject the architecture, say plainly the review was theater.
3. **Command adaptively.** Expect an intelligent environment — users, attackers,
   dependencies, regulators, and production systems do not follow the plan because the
   plan requires it; test plans under adaptation, denial, delay, and partial information.
   Decentralize with clear intent (shared purpose, bounded autonomy, observable outcomes,
   rapid feedback). Never confuse instrumentation with understanding.
4. **Run three nested OODA loops** — FAST (minutes–a day), DELIVERY (PR–release),
   STRATEGIC (milestone+) — and keep a learning log per consequential loop: observation,
   interpretation, confidence, decision, expected outcome, actual outcome, next trigger.
   Tempo comes from better orientation and smaller reversible actions, not hurried
   decisions. Details in `references/command-doctrine.md` §2.
5. **Manage flow the Toyota way, translated honestly to software** — jidoka, andon,
   pull/JIT, inventory-is-waste, genchi genbutsu, kaizen, respect for people — while
   optimizing time from identified need to validated outcome, not utilization
   (`references/command-doctrine.md` §3).
6. **Co-design with feedback closure.** Map stakeholders and decision rights; every
   material contribution gets a visible disposition (what changed, what didn't and why,
   who owns follow-through, when validated). Consultation after decisions are fixed is
   ceremony — call it that.
7. **Communicate in the Smart Brevity frame** without loss of substance: *What changed →
   Why it matters → Evidence → Decision or blocker → Next action, owner, trigger →
   Chicken Little watch.* Brevity never conceals uncertainty, conditions, dissent, or
   ownership.
8. **Write to contract-drafting discipline** and run the thirteen-type ambiguity audit;
   bound or remove vague terms; never adopt wording because it is called "tested"
   (`references/command-doctrine.md` §5).
9. **Enforce statistical discipline** on every risk or classifier claim: absolute AND
   relative differences with baseline, population, horizon, counts, and uncertainty; the
   full 2×2 matrix with prevalence-aware predictive values; false-positive vs
   false-negative consequences stated (`references/statistics-and-ai-assurance.md` §1).
10. **Review engineering and AI systems whole**, with constrained agency: untrusted model
    inputs AND outputs, deterministic authorization/accounting/invariants, least
    privilege, versioned model/prompt/retrieval/policy for reproducible regressions
    (`references/statistics-and-ai-assurance.md` §2).
11. **Run the Chicken Little pass**: a deliberately anxious, evidence-bound adversarial
    sweep of the hunt list (silent failures, mocked-away risk, unrehearsed rollbacks,
    concentration risks, data-loss paths, excessive agent authority…) — theatrical alarm
    allowed, but every material finding carries severity, evidence, unknowns, causal
    chain, mitigation, owner, validation test, revisit trigger. Then the opportunity scan
    (remove rather than automate? simpler design? reversible experiment?). Present only
    the highest-value items under **Now / Next / Later / Watch**
    (`references/statistics-and-ai-assurance.md` §3).
12. **Close with the output rules**: lead with the answer; attribute every claim to
    evidence actually examined; say where you did not verify; end consequential reviews
    with the intervention log, the decision or blocker, and Now / Next / Later / Watch.

## Why / learn
The doctrine's spine is the Millennium Challenge lesson: an exercise whose organizers
protect the preferred answer from adaptive challenge loses its epistemic value — when the
red team's sunk fleet was refloated and the rules were rewritten mid-game, the exercise
stopped being evidence. Everything else follows from taking that seriously in software:
criteria fixed before results, interventions logged, continuation never dressed up as
validation. OODA earns its place because orientation — not speed — is the decisive
element: it determines what you can even notice, which is why dashboards without
challenged assumptions reinforce wrong orientation. The Toyota translation works only when
you respect the disanalogy (variation and discovery ARE the work in software), the
statistics discipline exists because the same arithmetic (2%→1%) is honestly a 1-point
absolute reduction and rhetorically a "50% improvement," and the Chicken Little pass is
constructive precisely because it is evidence-bound: paranoia generates hypotheses, but
only severity + evidence + owner + trigger turns them into findings.

## Common mistakes
- Changing acceptance criteria after results are known → that's changing the test; log it
  as an intervention and downgrade the claim.
- Treating continuation as validation → label what the remaining evidence can support.
- Red team as decoration → if it can't reject the design, say the review was theater.
- Reporting relative risk alone → always pair with absolute difference and baseline.
- Trusting accuracy on imbalanced classes → full 2×2 with prevalence-aware PPV/NPV.
- Brevity as concealment → the frame compresses, it never drops conditions or dissent.
- Chicken Little turning speculation into certainty, or blocking on stylistic trivia →
  both are forbidden; findings need evidence, severity, and an owner.
- Reasoning exclusively from reports → genchi genbutsu: reproduce the failure, read the
  real code path, inspect real data.

## Tailor to your environment
Record in `references/your-environment.md`: your release gates and rollback rehearsal
cadence, who holds stop-the-line authority, your intervention-log location, house
severity levels, and the statistical reporting template your org requires.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/project-command-center.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- references/command-doctrine.md — adaptive command, the three OODA loops, the Toyota
  translation, co-design and feedback closure, writing discipline and the ambiguity audit
- references/statistics-and-ai-assurance.md — statistical discipline, engineering/AI
  assurance and constrained agency, the Chicken Little hunt list and opportunity scan
- references/your-environment.md — your gates, authorities, and templates (fill in)
