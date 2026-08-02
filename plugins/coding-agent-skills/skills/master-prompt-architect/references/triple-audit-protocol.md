# The Triple-Audit Protocol (in full)

Run all three audits, in this order, silently, before any final output. Apply every
correction found. The lenses catch different defect classes — do not blend them into one
read-through.

## Contents
- Audit 1: Hostile red team
- Audit 2: Expert panel review
- Audit 3: Adams/MSCD compliance
- The deliverable-format template

## Audit 1: Hostile red team (the "terrible draft" assumption)

Assume the first pass contains structural flaws and inefficiencies — then find them:

- **Logical loops** — instructions that can cycle ("if unclear, ask; if asked, restate")
  or self-referential conditions with no exit.
- **Ambiguity** — any line a motivated misreader can take two ways (the four ambiguity
  types: antecedent, syntactic, lexical, scope).
- **Breaking points** — inputs, formats, or conversation states that derail the artifact:
  empty input, oversized input, adversarial input, out-of-order turns.
- **Token waste** — instructions that restate each other, defensive padding, examples that
  don't change behavior, boilerplate the end state never required.
- **Conflict** — two instructions that a single situation can trigger simultaneously with
  contradictory demands; resolve by precedence or deletion.

Tear down and rebuild every weak section. A patched weak section is still weak.

## Audit 2: Expert panel review

Scrutinize the draft as a rigorous panel spanning advanced AI, data structures, computer
science, and technical writing would:

- **Modern LLM capability use** — does the artifact leverage tool/function calling,
  structured output, multi-turn memory, and self-verification loops where they beat prose
  instructions? An instruction to "always return JSON" is weaker than a schema-enforced
  tool call.
- **Programmatic logic** — conditions are exhaustive and mutually exclusive where they
  must be; sequences are ordered by dependency; state the artifact relies on is state it
  actually has.
- **Data handling** — stable treatment of identifiers, formats, encodings; no instruction
  that corrupts data it touches (confirm identifier fidelity and money-handling against
  the house rules in `script-wizard`'s python-and-code reference).
- **Optimization strategy** — the structure that reaches the end state in the fewest
  tokens with the most reliable behavior; note what was considered and rejected.

## Audit 3: Adams/MSCD compliance

Evaluate the text against the drafting discipline of *A Manual of Style for Contract
Drafting* (the full treatment lives in `script-wizard`'s writing-and-drafting reference):

- **Eliminate passive voice** — every instruction names its actor.
- **One term per concept** — enforce strict terminology consistency; kill false synonyms.
- **Remove redundant couplets** and technical bloat — "each and every", "any and all",
  restatements of the obvious.
- **Absolute clarity, concise phrasing** — every sentence has a purpose you can state;
  structure mirrors logic (tabulate multi-part conditions).
- **Category discipline** — obligations, permissions, prohibitions, and conditions each
  get the verb structure that matches; blurring them is the classic drafting defect.

## The deliverable-format template

Deliver only after the user authorizes execution, in exactly this structure:

```markdown
## 1. Risk Assessment
- <Deployment risk: where this artifact can fail in its target environment>
- <Ingestion risk: file naming, size, format, encoding hazards>
- <Execution risk: what the user must verify before/while running it>

## 2. Blueprint Summary
<Concise breakdown: the exact end state, and how the engineered sequence, context
constraints, variable assignments, and token budget reach it. State what was measured
or assumed.>

## 3. The Deliverable
```<language or text>
<the fully optimized, commercial-grade artifact — complete, no placeholders,
no truncation, single copyable block>
```
```

Order is deliberate: risks precede the artifact so they get read; the blueprint proves the
logic; the deliverable arrives last, whole, and copyable in one motion.
