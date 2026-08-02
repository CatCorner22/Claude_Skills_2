# Evidence discipline

Read at stage 2. A slide is a durable artifact — it gets forwarded, screenshotted, pasted into a
board packet, and quoted back months later by someone who never heard the talk. Whatever appears on
it must survive that trip. This file defines how a claim earns a place on a slide.

## Contents
- [The governing asymmetry](#the-governing-asymmetry)
- [Claim tiers](#claim-tiers)
- [The source ledger](#the-source-ledger)
- [Source tags on the slide](#source-tags-on-the-slide)
- [Stating a gap](#stating-a-gap)
- [Numbers that need extra care](#numbers-that-need-extra-care)
- [The pre-delivery check](#the-pre-delivery-check)

## The governing asymmetry

A wrong number on a slide costs more than a missing number on a slide.

A missing number invites a question, and the answer — "we have not been able to extract that yet;
here is what it would take" — demonstrates command of the problem. A wrong number, once discovered,
retroactively taints every other figure in the deck, including the correct ones. The audience cannot
tell which claims were checked, so it discounts all of them.

Reconciliation practice already encodes this asymmetry: a false match is worse than an unreconciled
item, because the false match hides while the unreconciled item announces itself. Presentation
follows the same rule. Prefer the honest gap.

## Claim tiers

Sort every factual claim into one of three tiers before it reaches a slide.

### Verified
Read out of a named artifact during this session — a file on disk, a query result, a configuration
export, a report retrieved from its source. A verified claim goes on a slide. Record the artifact
name and its date.

### Reported
Supplied by the user, carried forward from a previous conversation, or taken from a summary document
that itself cites something you have not opened. A reported claim goes on a slide only after the user
confirms it, and it carries an "as reported" qualifier in the source tag. Summaries drift: a figure
that was right in March may describe a configuration that changed in May. Take particular care with
figures that arrive through a chain of summaries — each retelling can round, re-scope, or lose a
qualifier, and none of that is visible in the final sentence.

### Inferred
Derived by calculation, estimated, recalled, or reconstructed from context. An inferred claim never
appears on a slide as a bare figure. Three ways out:
1. **Verify it** — open the artifact and promote it to verified.
2. **Label it** — present it as an estimate with its basis and its bound: "on the order of 800,
   pending the full export."
3. **Convert it to a gap** — state what is unknown and what would resolve it.

The third option is usually the strongest for a leadership audience, because it converts a soft
number into a concrete request.

## The source ledger

Maintain one table for the whole deck. Build it as you gather, not afterward.

| Slide | Claim | Value | Source artifact | Source date | Tier |
|---|---|---|---|---|---|
| 3 | Bank accounts in scope | 31 | `bank_accounts_export.csv` | 2026-07-14 | Verified |
| 5 | Rules on two merchant codes | 76.3% | `04_CONFIG_FORENSICS_VERIFIED.md` | 2026-07-21 | Verified |
| 6 | Tolerance window | ±15 days | Tolerance rule set export | 2026-07-21 | Verified |
| 8 | Review volume driver | departmental backlog | user interview | 2026-07-18 | Reported |
| 9 | Auto-reconciliation rate | — | not extracted | — | Gap |

The ledger does three jobs:
1. It lets anyone trace a slide figure to its origin without reopening the analysis.
2. It makes the tier distribution visible. A deck that is nine-tenths *reported* needs more
   verification work before it goes to leadership.
3. It becomes the answer to "where did that come from?" months later.

Deliver the ledger with the deck. A markdown table in the same folder is enough.

## Source tags on the slide

Every body slide carrying a figure gets a source tag along its bottom edge, at 12–14 point, not bold,
in a gray that clears 4.5:1 contrast.

Format:
```
Source: <artifact>, <date>[; <scope or qualifier>]
```

Worked examples:
```
Source: Cash Management configuration export, 2026-07-21
Source: Engine run 2026-07-19; 12,481 statement lines, FHB Master only
Source: Comptroller report, FY25; figures as reported
Source: Departmental receipt log, 2026-06-30; excludes Extension
```

Three rules for tags:
- **Name the scope when the figure is partial.** "FHB Master only" prevents a reader from
  generalizing a single-account result to all 31 accounts.
- **Date the run, not the deck.** A result from a 19 July run stays a 19 July result no matter when
  the deck ships.
- **Tag the "as reported" claims explicitly.** The qualifier is the difference between citing a
  source and vouching for it.

## Stating a gap

Write gaps as claims, in the same sentence-headline voice as everything else. A gap slide is not an
apology; it is a statement about the state of the evidence and a request.

**Pattern:** name what is unknown, name why it is unknown, name what closes it.

> **Headline:** Three figures remain unavailable until the reconciliation results export includes
> rule attribution.
>
> **Evidence:** a three-row table — the figure needed, the blocker, the action that unblocks it.
>
> **Source tag:** Source: open items list, 2026-07-21.

Avoid hedge words that soften without informing — "roughly," "approximately," "various,"
"significant" — unless you attach a bound. "Approximately 800" says less than "between 780 and 870,
pending the export." When you truly cannot bound it, say the figure is not yet established and stop.

## Numbers that need extra care

Some figures mislead even when they are individually correct.

- **Rates without denominators.** "93 percent" means nothing without the population. Put the
  denominator in the tag or the label.
- **Counts without windows.** Volumes depend entirely on the period. Always state the window.
- **Percentages of small bases.** Two of three is 67 percent and also just two. Show the count
  alongside the rate when the base is under about 30.
- **Currency without a date.** A balance is a snapshot. Name the as-of date.
- **Comparisons across changed definitions.** When scope, rules, or a system changed between two
  periods, a period-over-period comparison measures the change in definition as much as the change in
  performance. Say so, or drop the comparison.
- **Results from a partial dataset.** State what is missing and in which direction it likely biases
  the result.

## The pre-delivery check

Run this before handing over any deck.
1. Read every slide and list every number on it.
2. Match each number to a ledger row. An unmatched number is a defect — remove it or source it.
3. Confirm every *reported* claim carries its qualifier.
4. Confirm no *inferred* figure appears as a bare number.
5. Confirm every rate has a denominator and every count has a window.
6. Confirm the gap list in the deck matches the gap rows in the ledger.

The check takes a few minutes and catches the one class of error the linter cannot see — a
well-formatted, well-designed, confidently wrong figure.
