# Human-error taxonomy (Reason on Rasmussen)

"Human error" is where a lazy RCA stops and where a good one starts — the library's
command doctrine already forbids stopping there (see
`continuous-improvement-skills:project-command-center`, references/command-doctrine.md).
This taxonomy is *how* you go past it: classify the error type first, because each type
has a different mechanism and therefore demands a **different countermeasure**. Source:
James Reason's error taxonomy (*Human Error*, 1990), built atop Jens Rasmussen's
skill–rule–knowledge (SRK) framework of performance levels.

## The performance levels (Rasmussen)
- **Skill-based** — automatic, practiced routines run with little conscious attention
  (typing an amount, clicking through a familiar screen). Errors here are execution
  failures.
- **Rule-based** — recognized situations handled by stored if-then rules ("if the
  difference is under tolerance, auto-match"). Errors here are applying the wrong rule
  or misapplying a good one.
- **Knowledge-based** — novel situations reasoned through from first principles. Errors
  here come from incomplete or wrong mental models.

## The error types (Reason)
| Type | What failed | Performance level | Signature |
|---|---|---|---|
| **Slip** | Right plan, wrong execution | Skill-based | The person knew what to do and did something else — transposed digits, clicked the adjacent row |
| **Lapse** | Memory failure | Skill-based | A step was omitted or forgotten — usually invisible in the moment, found later |
| **Mistake (rule-based)** | Wrong plan: bad rule or wrong rule for the situation | Rule-based | The action went exactly as intended — the intention was wrong |
| **Mistake (knowledge-based)** | Wrong plan: reasoning from a wrong or incomplete model | Knowledge-based | Novel situation, plausible-but-wrong diagnosis |
| **Violation** | Intentional deviation from a known rule | any | The person chose not to follow the procedure |

Violations subdivide, and the subtype matters:
- **Routine** — cutting a corner that has become normal ("nobody does the callback for
  small vendors"), usually because the compliant path is slow and the deviation is
  tolerated.
- **Situational** — the rule could not be followed as written in that context (missing
  tool, time pressure, conflicting instruction), so the person improvised.
- **Exceptional** — a one-off departure in an unusual situation, often well-intentioned.

## Countermeasure mapping — the point of the taxonomy
| Error type | What works | What does not |
|---|---|---|
| Slip | **Forcing functions / poka-yoke**: make the wrong action impossible or immediately visible — input masks, confirmation of high-risk values, constraints that reject the transposition | "Be more careful" reminders, retraining (the person already knew) |
| Lapse | **Checklists and system-carried memory**: read-do or challenge-confirm checklists, required fields, workflow steps that cannot be skipped — see `safety-and-reliability-skills:checklist-design` | Relying on vigilance; punishing the forgetter |
| Mistake (rule-based) | **Fix or retire the bad rule; decision support** at the point of choice — better criteria, examples of the boundary cases | Adding another rule on top of the misfiring one |
| Mistake (knowledge-based) | **Training and better mental models**: teach the mechanism, give reference material and escalation paths for novel cases | Punishment (they were reasoning in good faith with a bad map) |
| Violation | **Culture and incentives**: make the compliant path as fast as the shortcut, remove the tolerated normalization, fix the conflicting pressures — never just restate the rule | More rules and sternly worded memos (the rule was already known and declined) |

The mapping is the payoff: a checklist does nothing for a slip (the step wasn't
forgotten — it was executed wrong), a forcing function does nothing for a violation (it
will be worked around), and retraining does nothing for either. Classify first, then
countermeasure.

## Worked example: three recon failures, one lazy label
All three would be closed as "human error / re-trained the clerk" — classification sends
each somewhere different:

1. **A keying error in a reconciliation** — the clerk intended $4,562.19 and entered
   $4,652.19. Right plan, wrong execution → **slip** (skill-based). Countermeasure:
   poka-yoke — the system compares the entry against the bank-reported amount and
   rejects or flags the mismatch at entry; no amount of training reduces transpositions.
2. **A tolerance-rule misjudgment** — the analyst applied the "auto-match within $5"
   rule to a foreign-currency line where the tolerance was never meant to apply. The
   action went exactly as intended; the intention was wrong → **rule-based mistake**.
   Countermeasure: fix the rule's stated scope and add decision support at the match
   screen (show which tolerance applies and why); the worked boundary cases go into
   training.
3. **A skipped callback** — the payment-detail change was processed without the required
   callback verification because "we never call back the small vendors, there's no
   time on payment-run day." A known rule, knowingly skipped, normalized by the team →
   **routine violation**. Countermeasure: culture and incentives — make the callback
   take two minutes (verified-number directory), stop measuring the team solely on
   run-day throughput, and have leadership close the tolerated exception. Restating the
   rule in a memo changes nothing; the rule was already known.

## Using it inside the RCA
Classify the error *within* the 5 Whys chain, not instead of it: "clerk keyed the wrong
amount" (slip) still gets a *why* — why could a transposed amount post without a check?
The taxonomy names the human failure mode; the chain keeps going to the process condition
that let it through. If the classification is ambiguous (slip vs violation often is), ask
whether the person intended the action: unintended → slip/lapse; intended action, wrong
plan → mistake; intended deviation from a known rule → violation. Intent decides the
branch, and the branch decides the fix.
