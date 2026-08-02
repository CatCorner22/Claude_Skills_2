# The assertion-evidence method

Read at stages 3–4. Full checklist, evidence-type guide, failure modes, and worked before/after
examples.

Source of record: Melissa Marshall, *Present Your Science* exercises and resources handout (2024),
and Michael Alley, *The Craft of Scientific Presentations*, 2nd ed. (Springer, 2013).

## Contents
- [Why the method works](#why-the-method-works)
- [The checklist](#the-checklist)
- [Writing the headline](#writing-the-headline)
- [Choosing the evidence](#choosing-the-evidence)
- [Snorkel and scuba](#snorkel-and-scuba)
- [Filtering and structuring details](#filtering-and-structuring-details)
- [Slide patterns that work](#slide-patterns-that-work)
- [Failure modes and their fixes](#failure-modes-and-their-fixes)
- [Before and after](#before-and-after)

## Why the method works

A bullet-list slide asks the audience to hold fragments in working memory and assemble the argument
themselves while the speaker talks over them. Reading and listening compete for the same channel, so
the audience does neither well.

An assertion-evidence slide removes that work. The headline hands over the conclusion in one
sentence. The visual supplies the proof. The audience reads one sentence, looks at one picture, and
listens to the speaker for the rest.

The method also disciplines the speaker. A headline that cannot be written as a falsifiable sentence
signals that the slide has no point. That is worth discovering while drafting rather than mid-talk.

## The checklist

### Style
1. Begin each body slide with a sentence-assertion headline, left-justified, no more than two lines.
2. Support the headline with visual evidence — photographs, drawings, graphs, films, or words and
   equations arranged visually. Avoid bullet lists.
3. In the body of the slide, use words only when necessary. Design so the audience reads no more than
   20 words per minute.

### Typography
1. Use a bold sans-serif typeface such as Calibri.
2. Use 28-point type for the headline, 18–24 point for body text, and 12–14 point (not bold) for
   reference listings.
3. Avoid all capital letters, italics, and underline.

### Layout
1. Keep blocks of text, especially headlines, to no more than two lines.
2. Keep lists to two, three, or four items.
3. Use small side margins so you can insert sufficient white space between elements — for instance,
   at least a half-inch of white space below the headline.

Note the tension between Style rule 2 and Layout rule 2: the method avoids bullet lists yet permits
short lists. Read them together. A list of two to four parallel labeled items, arranged spatially
with an icon, number, or image, counts as words arranged visually. A stack of sentence fragments
with bullet glyphs does not.

## Writing the headline

The headline carries the slide's entire argument, so write it first and revise it hardest.

**Test it three ways.**
1. *Sentence test* — does it have a subject and a verb?
2. *Falsifiability test* — could evidence contradict it? "Reconciliation challenges" cannot be
   contradicted; "Two merchant codes absorb three-quarters of all transaction creation rules" can.
3. *Standalone test* — read only the headlines in order. Do they form the argument? If a reader gets
   the talk from the headlines alone, the spine is sound.

**Keep it to two lines.** At 28 point across an 11.52-inch box, two lines run roughly 105
characters. Long headlines usually contain two claims; split the slide instead of shrinking the type.

**Write in the present tense and the active voice.** "The engine rejects same-amount candidates that
fall outside seven days" beats "Same-amount candidates falling outside seven days were rejected by
the engine."

**Put the number in the headline when the number is the point.** "Two merchant codes absorb 76
percent of transaction creation rules" outperforms "Transaction creation rules concentrate heavily,"
because the audience gets the magnitude without decoding a chart first.

## Choosing the evidence

Match the evidence type to what the claim asserts.

| The claim asserts | Use | Notes |
|---|---|---|
| A distribution or comparison | Bar or column chart | Sort by value, label directly, drop the legend for a single series |
| A trend over time | Line chart | Label the endpoints; annotate the inflection the headline names |
| A composition | Stacked bar or a small table | Avoid pie charts beyond three slices |
| A sequence or process | Flow diagram, left to right | One box per stage, arrows between, no more than seven stages |
| A structure or relationship | Labeled diagram | Label the parts the headline names; leave the rest unlabeled |
| A magnitude | Two to four large numbers | Number large, label small beneath, unit stated once |
| A comparison across cases | Table | Three to six rows; bold the column the headline is about |
| A physical or visual reality | Photograph or screenshot | Crop hard; annotate the region the headline names |

**Annotate the evidence to point at the claim.** A chart proves nothing on its own. Circle the
outlier, arrow the inflection, bold the row. The audience should find the headline's proof without
hunting.

**Show the data, not a picture of the data.** Build charts natively in PowerPoint so numbers stay
editable and legible when projected. Reserve images for chart types PowerPoint cannot draw.

## Snorkel and scuba

For any technical explanation, write the *scuba* version — full mechanism, full precision — then
write the *snorkel* version that answers "so what?" for someone who does not share your specialty.

The slide shows snorkel. The speaker notes hold scuba. The speaker knows scuba and can descend on
demand when a question arrives.

**Example.**

*Scuba:* "The tolerance rule set applies a symmetric ±15-day window against the statement line's
value date with amount tolerance disabled, so a candidate matching to the cent but posting 22 days
later is excluded, while one posting 14 days later passes and is flagged Date Match = N."

*Snorkel:* "A single 30-day window lets a match pass the amount test and fail the date test at the
same time."

The snorkel version becomes the headline. The scuba version becomes the note.

## Filtering and structuring details

Structure a talk as one main message supported by three key details. Use this to decide what
survives the cut.
1. Write the main message of the talk in one sentence.
2. Name three key details that support it — no more.
3. For each key detail, ask: does the audience act differently knowing it? If not, it goes in the
   notes, an appendix, or the leave-behind.

Three supporting details is the working limit for a short talk. A defect-review deck may run one
headline per defect and still hold together, because each defect is an instance of a single main
message about the system.

## Slide patterns that work

**The map.** One diagram of the whole system, shown once, early. Every later slide can then point at
a region of it. Number the stages so headlines can reference them.

**The magnitude trio.** Three numbers, large, with small labels beneath. Use for scale-setting:
accounts, volume, exposure.

**The defect pair.** Left half shows what the configuration does now; right half shows what it should
do. The headline names the consequence, not the mechanism.

**The measured result.** A chart of outcomes with the measurement window and the run date stated in
the source tag. Never present a result without its window.

**The open-items table.** Three to six rows, one column for the item, one for who decides, one for
the date. Bold nothing except the column the headline names.

**The summary.** Restate the main claim as the headline. Below it, the two or three supporting claims
in the same words used earlier. Repetition of exact wording is a feature — it is how the audience
retains the argument.

## Failure modes and their fixes

| Failure | Why it happens | Fix |
|---|---|---|
| Topic-label headline ("Next steps") | Writing headlines last, from an outline | Write headlines first, as sentences |
| Headline runs three lines | Two claims in one headline | Split into two slides |
| Bullet list under a good headline | Reflex from prior decks | Convert to a diagram, table, or labeled trio |
| Chart with no annotation | Exporting the analysis chart as-is | Annotate the feature the headline names |
| Body text over 40 words | The claim is too large | Split the slide; move detail to notes |
| Unsourced number | Pulled from memory or an old summary | Verify it or convert it to a stated gap |
| Fifty-slide deck for a 20-minute slot | No duration budget in stage 1 | One minute per body slide; cut to fit |
| Jargon in the headline | Writing for peers, presenting to leadership | Keep the term, add the consequence: "…, which strands real subledger activity" |
| Screenshot of a spreadsheet | Skipping the design step | Extract the three numbers that matter |

## Before and after

**Before.** Headline: "Tolerance Rules." Body: four bullets reading "±15 day window," "Amount
tolerance disabled," "Applies globally," "Impacts date match flag."

**After.** Headline: "A single 30-day tolerance window undermines date integrity on auto-reconciled
rows." Evidence: two horizontal bars, one showing the configured window and one showing the typical
settlement lag, with the gap between them shaded and labeled. Body words: "Configured window,"
"Typical lag," and the shaded region labeled with the resulting flag. Source tag names the
configuration export and its date. Speaker note carries the scuba version.

The after version makes one claim, proves it with a picture, uses about a dozen body words, and can
be traced to its source.
