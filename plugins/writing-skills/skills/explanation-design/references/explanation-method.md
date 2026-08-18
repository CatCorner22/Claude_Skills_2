# The explanation method: audience model, analogy design, Feynman loop, teach-back

Attributions, held honestly: the "Feynman technique" is a posthumously popularized study method
distilled from accounts of Richard Feynman's practice — his insistence on plain-language
reconstruction and his habit of testing understanding by explaining from scratch — not a
protocol he wrote. The curse-of-knowledge framing is Steven Pinker's in *The Sense of Style*.

## Contents
- [The audience-model template](#the-audience-model-template)
- [Analogy design with break-point marking](#analogy-design-with-break-point-marking)
- [Worked example: explaining a database index](#worked-example-explaining-a-database-index)
- [The Feynman-loop protocol](#the-feynman-loop-protocol)
- [The curse-of-knowledge tell list, with rewrites](#the-curse-of-knowledge-tell-list-with-rewrites)
- [The teach-back script](#the-teach-back-script)

## The audience-model template

One sentence, written before anything else:

> **A <role> who already knows <X> and needs this in order to <do Y>.**

- **<role>** — specific enough to picture one person. "A new paralegal," not "non-technical
  users."
- **<X>** — what they *reliably* own, not what they might have heard of. This is the pool the
  analogy's source domain must come from.
- **<do Y>** — the action or decision the understanding enables. This sets the stopping point:
  explain until Y is possible, then stop.

Derived checks, applied to every draft paragraph:
- Does this term appear in <X>? If not, it gets defined at first use or cut.
- Does this detail serve <do Y>? If not, it's for the author, not the reader — cut or move to a
  "going deeper" section.
- Could <role> act on this paragraph? If three paragraphs in a row are pure abstraction, the
  concrete-first ordering has been lost.

If two audiences genuinely differ in <X>, write two explanations. A merged one serves neither:
it bores the knowledgeable reader in the passages that carry the newcomer and loses the newcomer
in the passages that respect the knowledgeable one.

## Analogy design with break-point marking

An analogy transfers an inference engine from a source domain the reader owns to a target they
don't. The design work is a two-column mapping plus an explicit break list — one deliverable,
not two.

Worksheet:

1. **Candidates.** Generate 2–3 source domains the reader demonstrably owns — start from the
   audience model's <X>, and widen to common experience when <X> is narrow (the worked example
   below draws one candidate from <X> and two from ordinary life). Reject any source the reader
   knows only as well as the target.
2. **Correspondence map.** For the leading candidate, list `source element → target element`
   pairs. Each pair licenses inferences; that's the point of the analogy.
3. **Break list.** For each correspondence, ask: what would the reader conclude by extending
   this that is *wrong* about the target? Every such conclusion is a break. Rank breaks by how
   likely the reader is to hit one while doing <Y>.
4. **Mark the top break inside the explanation itself** — "like S, *except* B" — not in a
   footnote. The reader meets the boundary at the same moment they receive the engine.
5. **Choose one analogy.** Multiple analogies interfere: each carries its own breaks and the
   reader can't tell which engine to run. A second analogy is allowed only for a distinct
   sub-concept.

## Worked example: explaining a database index

Audience model: *a new paralegal who already knows how legal reference books work and needs to
understand why some case-search queries are instant and others take minutes.*

Candidates: a book's back-of-book index; a library card catalog; a phone's contact list. Chosen:
the back-of-book index (deepest familiarity for this audience).

Correspondence map:
- pages of the book → rows in the table
- index entry (term → page numbers) → index entry (value → row locations)
- reading the whole book to find a term → a full-table scan
- flipping to the index first → an index lookup
- a book with no index → an unindexed column (every search reads everything)

Break list, ranked:
1. **A book's index is printed once; a database index must be updated on every write.** A reader
   extending the analogy concludes indexes are free — index everything. Wrong in exactly the way
   that matters operationally. → Marked in the explanation itself: "like a book's index, except
   the book is being rewritten all day, and every rewrite has to fix the index too — so each
   index you add makes every save a little slower."
2. A book's index covers chosen terms; a database index covers every value in the column (a
   reader might think rare values are "not in the index").
3. Book indexes point to pages you then skim; some database lookups end inside the index itself
   (covering indexes) — harmless at this audience's <Y>; left unmarked, noted for the author.

Concrete-first ordering for the same explanation: walk one real search ("find all cases citing
*Smith v. Jones*") twice — once as a full scan with rough timing, once via the index — *then*
state the principle (an index trades write-time work and storage for read-time speed), *then*
the boundary cases (writes get slower; searches the index doesn't cover still scan).

## The Feynman-loop protocol

Distilled from accounts of Feynman's practice; labeled as such whenever it's named.

1. **Write the plain-words version.** Explain the concept as if to a smart newcomer — full
   sentences, no term the audience model doesn't license, start to finish without notes.
2. **Mark the stumbles.** Every place you (a) reached for jargon, (b) hand-waved ("...and then
   it just works out"), or (c) went vague right where precision was needed — mark it. Do not fix
   it yet.
3. **Reattribute the stumbles.** Each mark is *your* gap, not the reader's limitation. Jargon at
   a stumble is a pointer to the exact piece the author knows by name but not by mechanism.
4. **Re-learn the marked pieces.** Go back to the source material for those pieces only, until
   you can state the mechanism in plain words.
5. **Simplify again.** Rewrite the plain-words version end to end. Loop until a pass produces no
   new marks.

The assistant's role: it plays the smart newcomer against your draft — asking the naive-but-sharp
questions, flagging every jargon reach and hand-wave with the sentence it occurred in — and it
can draft plain-words candidates. The re-learning step is the human's; a gap outsourced is a gap
kept.

## The curse-of-knowledge tell list, with rewrites

Each tell marks a spot where the author's knowledge silently substituted for the reader's
(Pinker's framing: knowing makes un-knowing effortful, so the failure is systematic).

| Tell | Why it happens | Rewrite |
|---|---|---|
| Undefined abbreviation ("check the WAL first") | Expansion feels redundant to the author | Expand at first use, with one plain-words clause: "the write-ahead log (WAL) — the running record of changes not yet saved to the main files" |
| "simply / just / obviously / of course" | The step is one chunk *to the author* | Delete the adverb; expand the step it was hiding, or consciously accept the skip |
| Skipped step ("then reconcile the two and move on") | Automatized expertise — the author no longer sees the sub-steps | Walk it once concretely; the worked example is where skipped steps surface |
| Abstraction with no instance ("the system ensures consistency") | Experts think in categories; novices need members | Attach an instance: "consistency — e.g., no search returns a case that was deleted an hour ago" |
| Forward reference ("as we'll see, this follows from locality") | The author's knowledge is a graph; prose is a line | Reorder so nothing is used before it's built, or cut the reference |
| Precision the task doesn't need (three caveats per sentence) | The author protects against expert readers who aren't the audience | Check against <do Y>; move caveats to boundary cases at the end |

Sweep mechanically: search the draft for abbreviations, for "simply/just/obviously/clearly/of
course," and for paragraphs containing no concrete noun. The assistant runs this sweep well
precisely because it isn't the author.

## The teach-back script

Purpose: test by generation, not recognition. "Does that make sense?" collects politeness;
teach-back collects evidence.

1. **Ask for the concept back in the learner's own words** — not a recital: "Explain it to me
   like I'm the next new person on the team."
2. **Ask for a transfer case.** Give one new instance the explanation didn't cover and ask them
   to walk it. Transfer is where borrowed words fail and real structure shows.
3. **Probe the analogy's edge.** Ask a question whose analogy-extended answer is wrong (from the
   break list). If they hit the break, the marking worked; if they run through it, the break
   wasn't marked well enough.
4. **Log distortions without correcting mid-stream.** Let the teach-back finish; interruptions
   convert it back into recognition.
5. **Map each distortion to the explanation, not the learner.** Distorted piece → the passage
   that taught it → rewrite that passage. Then re-verify the rewritten part only.

The assistant can simulate a full teach-back before any human learner's time is spent: it adopts
the audience model, explains the concept back, attempts the transfer case, and — usefully —
extends the analogy past its breaks on purpose to show which misconceptions the current draft
licenses. A simulated pass is a cheap first filter; a real learner is still the final test,
because the assistant's not-knowing is an act and a real newcomer's isn't.
