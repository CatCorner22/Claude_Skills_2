---
name: legal-citation-research
description: >-
  Plans and runs legal research with a verification ledger — frames the question, maps binding
  versus persuasive authority, searches statute, regulation, caselaw and secondary sources in
  order, reads holdings not headnotes, checks subsequent history and currency, and verifies every
  citation before it is cited, because a fabricated citation is sanctionable (Mata v. Avianca).
  Ships a verifier that parses citations offline and checks CourtListener, reporting UNVERIFIED
  rather than guessing. Delivers Smart Brevity memos: answer first, confidence, authorities, gaps.
  Use for a legal question, a research memo, checking the citations in a brief, or finding the
  current rule. Not for medical or scientific literature →
  deep-research-skills:medical-research-detective. Triggers: legal research, research memo, find
  case law, is this citation real, verify these citations, check the cites in this brief, good
  law, statute lookup, what does the law say, legal authority, CourtListener.
metadata:
  version: "1.0.1"
  source: >-
    Method built from standard legal-research practice and the post-2023 sanctions record for
    fabricated citations; the one case cited in the body is Mata v. Avianca, Inc., 678 F. Supp. 3d
    443 (S.D.N.Y. 2023), confirmed by search [snippet-only, cross-checked]. Later sanctions
    decisions named in references/citation-verification.md are [snippet-only] and must be verified
    before being cited. CourtListener's citation-lookup endpoint shape is from its documentation.
---

# Legal research with a verification ledger

Legal research is a verification discipline wearing a search discipline's clothes. The search is
the easy half; the half that protects a client and a licence is proving that each authority exists,
says what you say it says, and is still the law. This skill runs both halves in order, keeps a
ledger of what was checked and how, and delivers the answer the way a partner reads it: bottom
line first, confidence stated, authorities pinpointed, gaps named.

## When to use
- A legal question that needs an answer with authority behind it, for a memo, a brief, advice, or
  a drafting decision.
- Checking the citations in a brief, a memo, or anything a generative tool helped write.
- Finding the current rule when a statute, regulation or agency position may have moved.
- Not for: medical or scientific literature → `deep-research-skills:medical-research-detective`
  (it owns "check this citation" for studies). Drafting the clause the research supports →
  `legal-skills:mscd-contract-drafting`. Employment and HR issue-spotting →
  `legal-skills:employment-law-issues` (it names the sources; this skill verifies them). Auditing
  a video's claims against its sources → `deep-research-skills:video-source-audit`.

## Do it

1. **Frame the question before searching.** Write one sentence: *Under [jurisdiction] law, does
   [rule] apply when [facts]?* Record the posture (transactional, litigation, advice), the date the
   answer must be current as of, the facts that matter, and what finding would change the answer.
   A question without a jurisdiction is not yet a legal question. `references/research-method.md` §1.

2. **Map the authority before reading any of it.** Binding first: constitution, statute,
   regulation, then the highest court of the jurisdiction and its intermediate courts. Then
   persuasive: other jurisdictions, trial courts, agency guidance. Secondary sources — treatises,
   Restatements, law reviews, practice guides — are finding aids and orientation, cited only when
   nothing primary exists. Note where federal and state law interact and whether an agency
   interpretation still gets deference. `references/research-method.md` §2.

3. **Search in order and log every search.** Secondary for orientation if the area is unfamiliar;
   then the statute and regulation from the official source; then caselaw, starting from one good
   case and following what cites it; then the most recent applications. Each search goes in the
   ledger with the database, the query, the date and what was reviewed. `references/research-method.md` §3.

4. **Read the authority, not the summary.** For each case: the holding (what the court decided on
   these facts) versus dicta; the procedural posture and standard of review; whose words a quotation
   is; the pinpoint page. A headnote or a search snippet is a claim about the case, not the case.
   For each statute: the operative text, its definitions, its effective date, and any amendment.
   `references/research-method.md` §4.

5. **Check currency and subsequent history.** A licensed citator if available; otherwise
   CourtListener's cited-by listing plus a search of the case name with *overruled*, *abrogated*,
   *superseded* and *reversed*; for statutes, the amendment history and pending bills; for
   regulations, whether the rule was vacated or withdrawn — two recent federal rules were, and both
   still look current in cached copies. `references/research-method.md` §5.

6. **Verify every citation before it leaves, with the script and then with your eyes.**
   ```
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/legal-citation-research/scripts/verify_legal_citation.py" brief.docx
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/legal-citation-research/scripts/verify_legal_citation.py" --cite "678 F. Supp. 3d 443"
   ```
   With `COURTLISTENER_API_TOKEN` set it checks each citation against CourtListener and reports
   VERIFIED, NOT FOUND, AMBIGUOUS, UNRECOGNIZED or UNVERIFIED; without a token or a network it
   still parses everything and reports UNVERIFIED with the manual route. VERIFIED means the
   citation resolves to a real decision — you still read it (step 4). NOT FOUND is treated as
   fabricated until found in another source. UNVERIFIED does not go in the document. **Never ask a
   generative tool to confirm its own citation**; that is the step that produced the sanctions in
   *Mata*. `references/citation-verification.md` §1–§5.

7. **Write the memo in Smart Brevity.** Bottom line and confidence in the first two sentences; why
   it matters; the rule with pinpointed authorities; the application; what was not checked and the
   open questions; next steps; and the verification ledger as a footer. A brief or a client letter
   uses the same order with the register adjusted. `references/memo-template.md`.

8. **Say what is unsettled.** Name circuit splits, contested readings and jurisdiction-dependent
   points as such, and say when the answer turns on a fact you do not have. A confident answer to
   an unsettled question is the second most expensive error in this skill, after a fabricated
   citation.

## Why / learn

**Existence, support and currency are three different checks, and the failures are different.**
A citation can exist and not support the proposition (the most common error in careful work); it
can support it and no longer be good law; and it can fail to exist at all. The last is new at
scale: a generative tool produces citations by pattern, so its output is fluent, well-formed and
sometimes fictional, and it will confirm its own invention when asked. The protection is
procedural, not perceptual — nobody can tell a fabricated citation from a real one by looking,
which is why the verifier checks a corpus and reports what it could not check rather than
guessing.

**Why NOT FOUND is treated as fabricated but is not proof of fabrication.** CourtListener's
coverage is broad but not complete, and some reporters and years are thin. The rule is asymmetric
on purpose: an unfound citation stays out of the document until a second source finds it, because
the cost of a fabricated citation in a filing (sanctions, referral, a client's case damaged, a
record that follows the lawyer) is not symmetrical with the cost of an extra search.

**Why secondary sources are finding aids.** A treatise summarises what the author read, as of
when they read it, for the jurisdictions they chose. It is the fastest way to learn the shape of
an area and the slowest way to be wrong about a specific rule in a specific state this year.

**Why the ledger.** A memo that says *verified* without saying how is a claim; the ledger makes it
an audit trail — which database, which query, which status, which date — so the next reader (or
the same lawyer a year later) can see what was checked and repeat it.

**Why Smart Brevity.** The reader of a research memo decides in the first two lines whether to
read the rest, and the reader of a brief is a judge with forty others. Bottom line first,
confidence stated, then the support.

## Common mistakes
- Citing a headnote, a snippet, or a tool's summary as if it were the opinion → read the pinpointed
  page; the claim is yours once you cite it.
- Treating a VERIFIED status as "checked" → VERIFIED proves existence only; support and currency are
  steps 4 and 5.
- Asking the tool that produced a citation to confirm it → it will; that is how *Mata* happened.
- Researching without a jurisdiction, or mixing persuasive and binding authority without saying
  which is which → the memo cannot be relied on.
- Taking a cached or secondary statement of a regulation as current → check for vacatur,
  withdrawal and amendment in the Federal Register or the official code.
- Quoting a dissent, a concurrence or a party's argument as the court's holding → say whose words
  they are.
- Stopping at the first case that agrees → look for the contrary authority; if there is none, say
  you looked.
- Burying the answer under the research → bottom line first; the path goes in the ledger.

## Tailor to your environment
Record in `references/your-environment.md`: the jurisdictions you practise in and their citation
and style rules (Bluebook, ALWD, a state manual, local rules on unpublished opinions); the
databases you are licensed for and which citator; how your firm wants memos structured and
headed; standing orders in the courts you file in about generative-tool disclosure. The
CourtListener token lives in the environment variable or a token file outside any repository,
never in this file or any committed one.

**Keep your filled-in copy outside the plugin.** This file ships as a *template* and lives inside
the installed plugin, where a `/plugin marketplace update` can overwrite it or refuse to run against
a dirty tree. Copy it into your own project — `.claude/skills-env/legal-citation-research.private.md` works well — fill it in
there, and point this skill at that copy. Your specifics then survive updates and stay somewhere you
own rather than in a cache you may not realise is disposable.

## References
- `references/research-method.md` — framing, the authority hierarchy, the search protocol, reading the authority, currency and subsequent history, and when to stop
- `references/citation-verification.md` — the no-fabricated-citation rail, how fabrication happens, the sanctions record, the verifier's statuses and what each requires, manual verification routes, citation anatomy, the ledger format
- `references/memo-template.md` — the Smart Brevity research memo, brief and client-update variants, with a worked example and the ledger footer
- `references/your-environment.md` — jurisdictions, databases, citator, memo conventions, court standing orders (fill in; the `.private.md` twin is git-ignored)

## Scripts
> Paths use `${CLAUDE_PLUGIN_ROOT}` so they resolve from **any** working directory once the plugin
> is installed. A bare `scripts/…` path only works inside a clone of the marketplace repo.
- `python3 "${CLAUDE_PLUGIN_ROOT}/skills/legal-citation-research/scripts/verify_legal_citation.py" <brief.docx|memo.md|text.txt> [--json] [--offline] [--token-file PATH]`,
  or `--cite "<citation>"` (repeatable) — parses case citations offline with a compact reporter
  table derived from the Free Law Project's reporters-db (BSD-2-Clause, license text shipped beside the table; spacing and period variants
  and the known variant spellings all resolve), classifies statutes, regulations, rules and
  Westlaw/Lexis database cites with the place to verify each, and with `COURTLISTENER_API_TOKEN`
  set POSTs the text to CourtListener's citation-lookup endpoint. Statuses: VERIFIED (a decision
  came back, with case name, date and URL), NOT FOUND (well-formed, absent from the corpus — the
  fabrication signal), AMBIGUOUS (several decisions; listed), UNRECOGNIZED (reporter not known to
  CourtListener), UNVERIFIED (no token, no network, rate-limited, malformed reply, or a 200 with no
  decision attached — never a false VERIFIED). Every non-verified case citation prints the manual
  route. Exit 0 all verified (or nothing found by either parser after CourtListener answered), 1
  any NOT FOUND / AMBIGUOUS / UNRECOGNIZED, 3 any UNVERIFIED — including a text in which nothing
  parsed locally and CourtListener was not consulted — 2 unreadable input. The token is read from the environment or a file, is sent only as
  the `Authorization` header, and is never printed. `--self-test` runs the parser fixtures and a
  local mock of the endpoint, including a fabricated citation that must come back NOT FOUND, a
  rejected token, a dead network and a malformed reply, each of which must come back UNVERIFIED.
  It cannot read the opinion: VERIFIED is existence, not support or currency.
