# Python and Code Standards

Read this when the deliverable is code: a script, module, tool, automation asset, or AI system component.

## Contents

- Governing principle
- Structure
- Interfaces and naming
- Error handling
- Data handling
- Testing
- AI system components
- Security, reliability, and performance
- What to deliver alongside the code

## Governing principle

Prefer clarity over cleverness. Code gets read far more often than it gets written, and the reader is usually the author months later with no memory of the context. A clever one-liner that saves three lines but costs a minute of comprehension is a bad trade.

Prefer robust patterns over fragile shortcuts. Prefer boring solutions that fail loudly over elegant ones that fail silently.

## Structure

Separate concerns into distinct units: reading input, transforming data, writing output, and orchestrating the run. Mixed concerns make a module impossible to test and painful to change.

Keep functions small enough to hold in your head at once and named well enough that the body confirms what the name promised.

Avoid abstraction that has no second caller. An interface introduced for one use case guesses at a future you cannot see, and the guess is usually wrong. Add the abstraction when the second case arrives and shows you its actual shape.

Put the entry point behind `if __name__ == "__main__":` so the module can be imported and tested without executing.

## Interfaces and naming

Make interfaces explicit. Use type hints on function signatures — they document intent, catch a class of errors before runtime, and let editors help the reader.

Name to reveal intent. `unreconciled_lines` beats `data2`. Match the user's domain vocabulary rather than inventing a parallel one, since they must maintain this.

Use one term per concept throughout. Alternating between `record`, `row`, and `entry` for the same thing forces the reader to keep proving the three are identical.

Avoid magic behavior — hidden global state, implicit conversions, side effects a caller cannot predict from the signature — unless the user asks for it.

## Error handling

Handle errors deliberately. Decide, for each failure, whether the right response is to stop, skip, retry, or record and continue, then implement that decision explicitly.

Catch narrow exceptions. A bare `except:` swallows real bugs along with the expected failure and turns a crash into silent wrong output, which is strictly worse.

Fail loudly and early on bad input. A script that processes a malformed file into plausible-looking garbage causes more damage than one that refuses to start.

Write error messages that tell the reader what failed, what value caused it, and what to do next.

## Data handling

Never mutate the source data. Read the raw input, write results to a new location, and keep the original recoverable so any step can be rerun.

Validate on the way in: expected columns present, types coercible, ranges sane, row count plausible. Data that arrives from a bank, an ERP, or another team will eventually arrive malformed.

Make runs deterministic and idempotent where possible. Running twice should produce the same result and should not double-count, because reruns happen — after a crash, after a fix, after someone wonders whether it worked.

Log what ran: inputs read, rows in and out, decisions taken, anomalies skipped. When output looks wrong three weeks later, the log is the only evidence of what actually happened.

## Testing

Test the parts where being wrong would matter and being wrong is plausible: parsing, matching, calculation, edge-case branches.

Cover the empty case, the single-item case, the malformed case, and the boundary condition. Bugs cluster at boundaries far more than in the middle of a range.

When fixing a bug, first write the test that reproduces it. Otherwise you cannot prove the fix worked, and nothing stops the bug from returning.

Keep test data small, readable, and committed alongside the code.

## AI system components

State the model, the prompt, and the expected output shape explicitly rather than burying them in string concatenation.

Treat model output as untrusted input. Validate structure before use, and handle the case where the model returns prose instead of the JSON you asked for.

Make prompts inspectable and version them with the code. A prompt is program logic; an undocumented prompt change is an undocumented behavior change.

Handle rate limits, timeouts, and partial failures explicitly, since network calls fail routinely at scale.

## Security, reliability, and performance

Never hardcode credentials, tokens, or connection strings. Read them from the environment or a secrets store, and say so in the setup notes.

Never commit real data containing personal, financial, or confidential information to a repository. Use synthetic fixtures.

Address performance when the data volume warrants it, and say which volume you assumed. Optimizing a script that handles 500 rows wastes effort; ignoring volume on 5 million rows produces something unusable.

## What to deliver alongside the code

- **Setup** — dependencies, versions, and how to install them
- **Execution** — the exact command, with an example
- **Inputs and outputs** — what it expects, what it produces, where it writes
- **Assumptions and limits** — what you assumed, what it does not handle
- **Known risks** — what to watch, what would break it

## House additions (this library)

- Preserve identifier fidelity: reference numbers, account tokens, and merchant IDs are
  **strings** — never let pandas/Excel float-coerce `0006789599` into `6789599.0`. The
  reconciliation engines ban pandas outright for this reason.
- Money is integer cents or `Decimal` — this is engine-enforced in the recon projects.
- Prefer `logging` (timestamps + levels) over `print` for anything scheduled: the 2 a.m.
  failure is diagnosed from the log.
- Escalation: for production services, libraries, or anything with users beyond the author
  (full typing, packaging, CI, property-based tests), compose with
  `full-stack-dev-skills:elite-python-engineer` — script-wizard keeps the workflow, that
  skill supplies the production toolchain.
