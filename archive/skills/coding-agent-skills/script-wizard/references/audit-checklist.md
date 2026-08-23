# Audit Checklist

Read this in Phase 5, before presenting any substantial deliverable.

Audit with fresh eyes. The mindset that builds an artifact cannot see the artifact's gaps, because it is still holding the intentions that the artifact was supposed to express. Put a gap between building and reviewing — reread the original request first, then read what you produced as though someone else wrote it.

## The four questions that matter most

Answer these on every deliverable, regardless of type:

1. **Does this actually address the objective?** Not the task as literally phrased — the outcome the user needs. Reread the original request and check the artifact against it, line by line.
2. **What breaks it?** Name the specific input, condition, or dependency that produces a wrong result or a failure.
3. **What could be misread?** Find the sentence, variable name, or structure that a reasonable reader takes a different way than intended.
4. **What does a skeptical expert attack first?** Identify the weakest claim, the thinnest section, the assumption doing the most unexamined work.

If any answer is uncomfortable, fix it before presenting rather than disclosing it as a caveat. Caveats are for residual risk, not for known defects you chose not to fix.

## General checklist

- The objective is addressed, not merely the literal request
- Assumptions are stated explicitly rather than buried in the implementation
- No hidden contradictions between sections, or between the artifact and its description
- Nothing ambiguous that should be precise
- No unnecessary complexity — every part earns its place
- The result is usable as delivered, not a sketch presented as finished
- Risks and limits are surfaced honestly
- Terminology is consistent throughout
- The recommendation appears first, not buried

## Code-specific checks

- Runs on the happy path, and you verified it rather than assuming
- Handles empty input, a single record, malformed rows, and the boundary case
- Errors fail loudly and early; no bare `except` swallowing real bugs
- Source data is never mutated; reruns are safe and do not double-count
- No hardcoded credentials, tokens, or absolute paths from your own environment
- Dependencies are declared with versions
- Names reveal intent; a reader can follow the data flow without you
- Setup and execution instructions are present and accurate
- Assumed data volume is stated, and the approach fits it

## Prose-specific checks

- The conclusion leads
- One term per concept, used consistently
- Active voice, except where passive is deliberate
- Headings reveal content
- Parallel elements are grammatically parallel
- Scanned for the four ambiguities: antecedent, syntactic, lexical, and scope
- No archaisms, redundant doublets, or throat-clearing
- Every sentence has a purpose you can state
- Cross-references point to something that exists

## Plan-specific checks

- Dependencies and sequence are honest, including what waits on other people
- The critical path is identified
- Each phase produces something verifiable
- Risks carry mitigations, not just labels
- Dates are achievable, and dependent dates are flagged as dependent
- Scope states what is out as well as what is in

## Red-team pass

Before presenting, argue against your own work:

- **What would make this hard to implement in reality?** Not in principle — on the actual system, with the actual data, by the actual person.
- **Which dependency is fragile?** What happens the day it changes or disappears.
- **What did I assume without checking?** Especially about data shape, access, permissions, or someone else's availability.
- **Where did I claim more confidence than I have?** Find the sentence stating as verified something you inferred, and rewrite it honestly.
- **What did I not test?** Say so plainly rather than letting silence imply verification.

## The honesty rule

Never present untested work as verified, invent a source or citation, or report a result you did not produce.

If you did not run the code, say you did not run it. If a number came from an assumption, label the assumption. If a claim rests on your general knowledge rather than on the user's data, distinguish the two.

This matters more than any other item on this list. Every other defect is visible to the user on inspection; a false claim of verification is not, and it is the one failure that makes them stop trusting the work that was good.

## House additions (this library)

Financial-data checks, on any artifact that touches money or reconciliation:

- Totals tie to an independent source; row counts in vs out are accounted for
- Signs, units, currency, and rounding behave at the boundaries; money is cents/`Decimal`, never binary floats
- Leading-zero identifiers survived every tool in the chain (no float-coerced reference keys)
- Behavior at 10× the expected volume is known, not assumed

Exit rule: the audit is done when it has found something (fix it), or when you can say
specifically why each section above came up clean. "No findings" without the pass is not an audit.
