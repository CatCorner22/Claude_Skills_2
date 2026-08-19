# Grade targets, Adams rules, and the self-check

§1–§4 are preserved from the source spec (adams-plain-grade v1.0.0, 2026-08-04), organized
for use; §5–§8 are house additions.

Contents: §1 Grade targets · §2 The Adams rules · §3 Measuring the grade · §4 Self-check ·
§5 Where the targets come from · §6 Worked example (before/after) · §7 The plain-word
ladder · §8 Routing within the register family

## §1 Grade targets

**Preferred — 5th grade**
- Average sentence length: 10–14 words.
- Everyday concrete words; prefer 1–2 syllables.
- Active voice.
- One main idea per sentence.
- Concrete examples.
- Target: Flesch Reading Ease 90 or higher, **or** Flesch-Kincaid grade at or below 5.0 —
  two separate scales, not two readings of the same number (§3). Either one is a pass, and
  both are floors, not windows: Reading Ease runs past 100, and scoring 105 is not "too
  easy," it is easy. Only the read-aloud test can fail a text for being too simple.

**Fallback — 8th grade (only when precision requires it)**
- Sentences may reach 15–18 words.
- Words stay common and concrete.
- Any technical term is explained right away in plain words.

**Hard limits**
- Never go above 8th grade.
- Never sacrifice Adams clarity to hit a lower grade.
- Never make the meaning fuzzy just to hit a grade — meaning always wins; that is what the
  8th-grade fallback is for.

## §2 The Adams rules (never drop these)

1. Litigated language is bad language. Do not use it.
2. No archaisms, no doublets or triplets, no ambiguity.
3. Use the simplest accurate modern English word.
4. If you must use a technical term, say it once and explain it right away in plain words.
5. Structure the text so the reader never has to guess what you mean.
6. Keep the subject, verb, and object close.

Common offenders to replace on sight: *herein, hereto, aforesaid, whereas, pursuant to,
prior to, in the event that, notwithstanding, indemnify and hold harmless, null and void,
cease and desist, terms and conditions* (when one word does the job), *utilize, commence,
endeavor, remuneration*.

## §3 Measuring the grade

- Flesch Reading Ease ≈ 206.835 − 1.015 × (words/sentence) − 84.6 × (syllables/word).
  Higher is easier; 90–100 reads at roughly 5th grade.
- Flesch-Kincaid Grade ≈ 0.39 × (words/sentence) + 11.8 × (syllables/word) − 15.59.
- **The two do not agree, and §1 does not ask them to.** Solve both formulas at this
  register's 10–14 words per sentence: FRE 90–100 lands at FKGL ≈ 1.8–4.2, while FKGL 5.0
  lands at FRE ≈ 77–84. Text that passes on one scale will read a grade or two off on the
  other. Pick the scale you are reporting, say which, and never lengthen sentences to raise
  a Flesch-Kincaid number.
- Estimate honestly when you can't compute: count words per sentence (the dominant lever)
  and watch for 3+ syllable words — swapping those two things moves the grade more than
  anything else.
- **The sentence count is the fragile input, and this register attacks it.** The skill asks
  for bullets, and most scorers find sentence boundaries by splitting on `.` `!` `?` only —
  so a bulleted list whose items end without punctuation is read as one enormous sentence.
  The same six lines scored Reading Ease 106.6 with terminal periods and 77.0 as
  unpunctuated bullets (Flesch-Kincaid −0.2 against 11.2), on identical words. Punctuate the
  bullet items, or score the prose alone, before you believe any number.
- Scores are a check, not the goal. Choppy fragments can game a formula; they fail the
  read-aloud test. The read-aloud test is the judge: a clear adult talking to a smart
  11-year-old, in plain American English with no regionalisms. If your readers share a
  dialect, record it in your-environment.md and read aloud in that voice.

## §4 Self-check before you finish

- [ ] Main point is first and simple.
- [ ] Sentences are short.
- [ ] Words are everyday words.
- [ ] No litigated or traditional formulas.
- [ ] No ambiguity.
- [ ] Grade is 5th if possible, never higher than 8th.
- [ ] A 5th-grader in your audience's own community could understand it without help.
- [ ] The meaning is exactly what the source meant — nothing softened, nothing dropped.
- [ ] Nothing added that the source doesn't support; every concrete detail the rewrite
      supplies (a number, a step, a name) was confirmed against something real.

## §5 Where the targets come from

The register this skill enforces is not a private taste — it sits on a documented public
lineage. Provenance: claims marked [snippet-only] were verified against web-search snippets,
not full primary texts.

- **The Plain Writing Act of 2010** is a US federal law requiring federal agencies to write
  the documents the public relies on in clear, straightforward language [snippet-only].
  Plain language for high-stakes reader-facing text is codified policy, not a stylistic
  indulgence.
- **The Federal Plain Language Guidelines** operationalize the Act, leading with the same
  moves this skill drills: define your audience and write for their needs, put the main
  point first, keep sentences short, prefer active voice and everyday words [snippet-only].
  Where to find them moved: GSA redirected plainlanguage.gov in September 2025 to a shorter
  guide series on Digital.gov, and the Guidelines came down with the old site. The originals
  live in the plainlanguage.gov GitHub archive, and the Center for Plain Language reposted
  them (checked 2026-08-19). A citation that still reads "maintained at plainlanguage.gov"
  is a small live demonstration of why the sibling `writing-skills:technical-documentation`
  stamps "last verified" separately from "last edited."
- **Flesch Reading Ease** was published by Rudolf Flesch in 1948 and scores text 0–100 from
  two surface features — average sentence length and average syllables per word — with
  higher scores meaning easier reading [snippet-only].
- **Flesch-Kincaid Grade Level** was derived in 1975 by J. Peter Kincaid and colleagues under
  contract to the US Navy, recalibrating readability formulas against reading tests of
  enlisted personnel so the output reads as a US school grade [snippet-only]. The formulas
  were built to make *technical manuals usable by their real readers* — the same job this
  skill does for patient letters and public notices.
- **The honest boundary of the formulas:** both measure only sentence length and word
  length. They cannot detect ambiguity, a dropped qualifier, or a softened meaning. That is
  why the Adams rules (§2) and the read-aloud test outrank the score, and why "meaning
  always wins" is a hard limit rather than a preference.
- **The Adams core** is adapted from Ken Adams's contract-drafting clarity doctrine as
  carried by the source spec: litigated language is language with a documented failure
  history, and the modern plain formulation is the safer one because it leaves nothing to
  interpret.

## §6 Worked example (before/after)

Domain-neutral by design — the same notice could go out from an analyst's team, a law
office, an operations department, or a software product. The organization is adding a
sign-in code.

**Before** (typical first draft — 2 sentences, 67 words, ~34 words per sentence, ~1.8–2.0
syllables per word — **FRE ≈ 7–19, FKGL ≈ 19–21** — passive voice, archaic connectors,
unexplained jargon):

> Pursuant to our updated security protocols, effective May 1, multi-factor authentication
> will be required for all account access; users must therefore furnish, in addition to
> their password, a one-time verification code, which shall be transmitted via SMS to the
> mobile number associated with the account. In the event that a user is unable to receive
> SMS transmissions, alternative verification arrangements may be made by contacting
> customer support.

**After** (plain grade — 9 sentences, 71 words, ~8 words per sentence, ~1.15–1.23 syllables
per word; by the §3 formulas that is **FRE ≈ 95–101**, clearing the 90 floor. Note the
divergence §3 warns about: the same text scores **FKGL ≈ 1–2**, far under 5.0, and it is the
right text anyway. The ranges are not sloppiness — two syllable counters run over this exact
paragraph disagreed by six Reading Ease points, which is why §3 calls the score a check and
the read-aloud test the judge):

> We are changing how you sign in.
>
> Starting May 1, you will need a one-time code as well as your password. A one-time code
> is a short set of numbers that works only once. We will text it to your phone. Type it on
> the sign-in page after your password.
>
> This keeps your account safer.
>
> Can't get text messages? Call us at 555-0100 and we can set up another way.

What the rewrite did, move by move:
- **Main point first:** "We are changing how you sign in" replaces a buried lead behind
  "pursuant to our updated security protocols."
- **Litigated/archaic formulas removed:** *pursuant to* → gone; *in the event that* → "Can't
  get…?"; *shall be transmitted* → "We will text it."
- **Technical term said once, explained immediately:** "one-time code" gets one plain
  sentence of explanation right where it first appears. "Multi-factor authentication" does
  not survive at all — the reader needs the behavior, not the term.
- **Actor named, active voice:** "We will text it to your phone" instead of "which shall be
  transmitted via SMS."
- **Meaning preserved, including the *category* of each statement:** the date, the requirement,
  the delivery channel, the safety rationale, and the fallback path all survive, and each stays
  the same *kind* of statement it was.
- **The category check is the one this example nearly failed — run it explicitly.** The source
  says alternative arrangements "**may be made**": that is discretion, and the company is not
  bound. An earlier version of this rewrite read "Call us at 555-0100. **We will set up another
  way for you**" — which is an *obligation*, and it hands the reader a commitment the source
  never made. It reads better, it scores better, and it is a different document. The current
  wording ("we **can** set up another way") keeps the discretion. Plain-language rewriting pulls
  toward the confident, concrete, active form, and the confident form of a discretion is an
  obligation — so on anything with legal or contractual weight, test every sentence for the
  category it belongs to before you certify that nothing changed. The categories, and which verb
  forms signal which, are in `writing-skills:adams-smart-brevity`'s
  `references/adams-and-brevity-checks.md` §3.
- **Two details were added, and they are the part to check:** the phone number and "type it
  on the sign-in page after your password" are not in the source. Concrete beats abstract, so
  a plain rewrite pulls toward specifics — which is exactly the moment a rewrite invents one.
  Every specific the rewrite supplies has to be confirmed before it ships; 555-0100 stands in
  here for the number you would actually look up (it is a reserved fictional exchange).
- **Not gamed:** the sentences are short because each carries one idea — not chopped
  fragments planted to fool the formula. Read it aloud: it sounds like a person.

## §7 The plain-word ladder

Swap on sight; the left column adds syllables and legal fog, never meaning. Two entries
carry a condition in the right column — read it, because those words have more than one
sense and only one sense swaps cleanly.

| Instead of | Say |
|---|---|
| utilize | use |
| commence | start |
| endeavor | try |
| remuneration | pay |
| prior to | before |
| subsequent to | after |
| in the event that | if |
| pursuant to | under |
| in order to | to |
| notwithstanding | despite (before a noun); even though (before a clause) |
| obtain | get |
| provide | give — but "the contract provides that…" becomes "says" |
| request | ask for |
| regarding | about |
| approximately | about |
| sufficient | enough |
| additional | more |
| assistance | help |
| immediately | right away |
| terminate | end |

If a swap would change the meaning even slightly, the swap loses — keep the precise word and
explain it in plain words right after (that is the 8th-grade fallback working as designed).

## §8 Routing within the register family

Four registers, one library — the audience picks the skill:

- **This skill** — the most accessible accurate version: patients, clients, the public,
  low-literacy readers. Grade-measured, meaning-exact.
- **`writing-skills:adams-smart-brevity`** — the same Adams core for jargon-fluent
  professional readers: point first, scannable, precise; no grade ceiling.
- **`writing-skills:explanation-design`** — when the job is building *understanding* of a
  concept, not delivering a notice: audience model, entry analogy, teach-back. Design the
  explanation there; bring its words down to grade here.
- **`writing-skills:gonzo`** — the deliberately wild register, engaged by name only, for
  commentary that polite registers can't reach. Never for anything a patient or client must
  rely on.
