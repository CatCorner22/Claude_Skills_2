# Writing and Drafting Standards

Read this when the deliverable is prose: documentation, markdown, a specification, a report, a policy, or contract language.

## Contents

- Governing principle
- Sentence-level discipline
- Terminology
- Structure
- Markdown conventions
- Contract-drafting discipline (Ken Adams / MSCD)
- Ambiguity: the four kinds worth hunting
- What to cut

## Governing principle

Write to be understood on one reading by a competent reader who is short on time and lacks your context.

Formality is not clarity, and length is not rigor. Inflated prose usually signals that the writer has not finished thinking. Where the thinking is genuinely complete, plain sentences carry it.

## Sentence-level discipline

Use active voice. "The script writes the file" states who acts; "the file is written" hides it. Passive voice is defensible when the actor is genuinely unknown or irrelevant — use it deliberately, not by default.

Give instructions in short declarative sentences. Compound instructions hide steps, and a reader following along will drop one.

Put one concept in one sentence when precision matters. Two obligations joined by "and" produce an argument later about whether both were required.

Prefer concrete words to abstract ones, and verbs to nominalizations: "decide" beats "make a determination."

Keep parallel elements parallel in grammar and structure. Broken parallelism makes a reader wonder whether the difference is meaningful.

## Terminology

Use one term per concept for the entire document. Consistency matters more than elegant variation, and the instinct to vary word choice — sound in literary prose — creates ambiguity in technical and legal prose.

Avoid false synonyms. If "user," "operator," and "administrator" name the same person, pick one. If they name different people, define each.

Define a term at first use when the meaning is not obvious to the audience, then use it unchanged. Do not define a term you use once.

Expand acronyms at first use.

## Structure

Lead with the conclusion. Readers who stop after two paragraphs should still get the point.

Make headings reveal content, not category. "How reconciliation fails" beats "Discussion."

Keep sections scannable. Use lists where the content is genuinely a list, and prose where the content is an argument — a list of reasoning fragments loses the logic connecting them.

Use enumerated structure when complexity rises: numbered conditions, lettered subparts, tabulated alternatives. Structure that mirrors the logic lets the reader follow branching without holding it all in memory.

Cross-reference explicitly rather than gesturing at "the above."

## Markdown conventions

Use one `#` H1, then a clean descending hierarchy with no skipped levels.

Use tables only when the content has real rows and columns. A table with one column is a list wearing a costume.

Format code, filenames, paths, and commands in backticks so the reader can tell text from literal.

Add a table of contents to any reference document over roughly 300 lines.

Avoid ornamental markdown: decorative rules, emphasis on entire paragraphs, emoji as section markers. Formatting should carry meaning.

## Contract-drafting discipline (Ken Adams / MSCD)

Apply the discipline in Kenneth A. Adams's *A Manual of Style for Contract Drafting* (5th ed., 2023) to any prose where precision governs — not just contracts. It aims at prose free of archaisms, redundancy, and ambiguity. Apply the discipline without importing legal stiffness.

**Distinguish the categories of contract language, and use the verb structure that matches:**

- **Obligation** — a duty imposed on a party
- **Discretion** — permission to act, with no duty to act
- **Prohibition** — a duty not to act
- **Condition** — a state of affairs that must exist before something follows
- **Policy** — a rule that operates without a party acting on it
- **Declaration** — a statement of fact by the parties

Blurring these is the most common structural defect in drafting. Most disputes over "shall" arise from using it for all six.

**Avoid these habits:**

- Archaisms: *hereinafter*, *witnesseth*, *aforesaid*, *the party of the first part*
- Redundant doublets and triplets: *any and all*, *cease and desist*, *give, devise, and bequeath*
- Throat-clearing recitals that state nothing operative
- Provisions that merely restate background law
- Capitalizing ordinary words to make them look defined

**Prefer these:**

- Defined terms only where the definition does real work
- Sentence structure that mirrors the logic, including tabulation for multi-part conditions
- One idea per provision
- The same word every time for the same thing

## Ambiguity: the four kinds worth hunting

Read your draft looking specifically for each:

1. **Antecedent ambiguity** — a pronoun or reference that could attach to more than one thing. *"The vendor will notify the client after it completes the audit."* Who completes it?
2. **Syntactic ambiguity** — modifier placement that admits two readings. *"Reports and invoices submitted late"* — does "late" reach both?
3. **Lexical ambiguity** — a word with more than one plausible sense in context. *"Monthly"* meaning once per month, or every month.
4. **Scope ambiguity** — *and*, *or*, and negation across a list. *"Not A or B"* rarely means what the writer intended.

The test is not whether you can tell what you meant. The test is whether a reader looking for a second reading can find one.

## What to cut

- Throat-clearing openers: "It is important to note that"
- Filler transitions that connect nothing: "That being said"
- Vague assurances: "robust," "seamless," "best-in-class," "world-class"
- Generic consultant language and buzzwords
- Overlong disclaimers that dilute the real caveat
- Any sentence you cannot state a purpose for
