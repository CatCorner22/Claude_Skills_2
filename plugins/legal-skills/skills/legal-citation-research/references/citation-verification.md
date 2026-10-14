# Citation verification — the rail, the mechanism, the sanctions record, the statuses

Contents: §1 The rail · §2 How fabrication happens · §3 The sanctions record · §4 The verifier's
statuses and what each requires of you · §5 Manual verification routes · §6 Citation anatomy ·
§7 The ledger

## §1 The rail

**No citation goes into a document until it has passed three separate checks:**

1. **Existence** — the decision, statute or rule exists at that citation. The bundled verifier
   checks this against CourtListener for cases and says where to check everything else.
2. **Support** — the pinpointed page says what the sentence says it says. Only reading does this.
3. **Currency** — it is still the law on the date the document is used. A citator, or the manual
   routes in `research-method.md` §5.

A citation that fails any check is removed or marked, never left in on the chance that it is
right. A document that leaves with an UNVERIFIED citation in it has left with a fabricated one, as
far as anyone reading it can tell.

## §2 How fabrication happens

A generative tool produces text by pattern. A legal citation has a strong pattern — a volume, a
reporter, a page, a court, a year — and the tool will produce one that fits it whether or not a
decision sits there. The output is fluent, well-formed and sometimes fictional, and the tool
cannot tell the difference from the inside, which is why asking it to *confirm* a citation
produces a confident confirmation of the invention. The lawyers sanctioned in *Mata* did exactly
that [snippet-only]. The protection is procedural: a corpus check, then reading, then a citator.
Nobody detects a fabricated citation by looking at it.

## §3 The sanctions record

**The anchor case.** *Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443 (S.D.N.Y. 2023) [snippet-only,
cross-checked ×2 — the reporter citation was confirmed by two independent sources]: counsel filed an
opposition citing six decisions that did not exist, with fabricated quotations and internal
citations, produced by a generative tool; the court imposed sanctions under Rule 11, found
subjective bad faith in the continued assertion of the cases after they were questioned, and
ordered a $5,000 penalty along with other measures [snippet-only]. The decision stresses that the
duty to verify authorities rests with the lawyer who signs the filing, however the authorities
were produced.

**What has followed** [snippet-only — every item below must be verified before it is cited; the
titles and figures came from secondary trackers, not from the opinions]: trial and appellate
courts in multiple jurisdictions have sanctioned, fined, referred and in some cases suspended
lawyers for filings containing fabricated or unsupported citations; sanctions increasingly count
per citation; appellate courts have said expressly that the sanction is for the failure to verify,
not for using a tool; and some courts have amended their rules or issued standing orders requiring
independent verification of, or certification about, tool-generated citations. Check the standing
orders of every court you file in and record them in `your-environment.md`.

**The practical reading.** The rules of professional conduct and Rule 11 (and their state
analogues) already required a reasonable inquiry; the tools changed the failure rate, not the duty.
Disclose where a rule requires it, verify everywhere.

## §4 The verifier's statuses and what each requires of you

| Status | Meaning | What you do |
|---|---|---|
| **VERIFIED** | CourtListener returned a decision at that citation: case name, date, URL | Open it. Read the pinpointed page against your sentence (support). Run the currency check. VERIFIED is existence only |
| **NOT FOUND** | the citation is well-formed and nothing sits at that reporter, volume and page in the corpus | Treat as fabricated until a second source finds it. Check the reporter's coverage on CourtListener, then Westlaw/Lexis/the official reporter. If it is found, record where; if not, it goes |
| **AMBIGUOUS** | several decisions match (parallel citations, a reporter with overlapping series) | Add the case name and year, re-run, and open the one you mean |
| **UNRECOGNIZED** | CourtListener did not recognise the reporter string | Check the abbreviation against the Bluebook table or the reporter's own name; a typo in the reporter is the usual cause |
| **UNVERIFIED** | the check could not be completed: no token, no network, rate-limited, a malformed reply, or a 200 with no decision attached | Verify by hand (§5) before the citation is used. It does not go into the document on the strength of the parse |
| **STATUTE / REGULATION / RULE** | parsed and classified; CourtListener's lookup does not cover them | Verify text and currency at the official source named in the output |
| **DATABASE** | a Westlaw or Lexis cite (`WL`, `LEXIS`) | Verify in that database; there is no free lookup |
| **SLIP** | a reporter placeholder (`___ U.S. ___`) | Verify by docket number and date on the court's site |

The verifier never produces VERIFIED from anything but a decision returned by the corpus, and
every failure path produces UNVERIFIED. If it is wrong, it is wrong in the direction of more work.

## §5 Manual verification routes

A citation counts as verified by hand when a source that holds the decision returns **the case
name and the reporter citation together**. Generated prose, a bare URL, a search snippet with one
but not the other, or a secondary article quoting the citation does not count.

- **CourtListener** (free): search the citation or the case name; the opinion page shows both.
- **Google Scholar, case law tab** (free): the citation search returns the opinion with its cites.
- **The court's website**: slip opinions by docket number and date.
- **Official and West reporters** in print or in Westlaw/Lexis/Fastcase.
- **Statutes**: *uscode.house.gov*, *govinfo.gov*, the state code; **regulations**: *ecfr.gov*
  and the Federal Register; **rules**: *uscourts.gov* for the federal rules and the court's site
  for local rules.

## §6 Citation anatomy

A standard case citation: *Case Name*, volume reporter first-page, pinpoint (court year).
*Mata v. Avianca, Inc.*, 678 F. Supp. 3d 443, 448 (S.D.N.Y. 2023) reads: volume 678 of the
Federal Supplement, Third Series, beginning at page 443, the proposition at page 448, decided by
the Southern District of New York in 2023. Parallel citations give the same decision in a second
reporter. Short forms (*Id.*, *supra*, *Mata*, 678 F. Supp. 3d at 450) cannot be verified alone;
the verifier ignores them and checks the full citation they point to. Statutes: title, code,
section (*42 U.S.C. § 1983*); regulations: title, C.F.R., section (*29 C.F.R. § 541.600*).
Citation form follows the Bluebook, the ALWD Guide, or a state style manual, and local rules can
override all of them — record which applies in `your-environment.md`.

## §7 The ledger

One line per authority, kept with the memo and reproduced as its footer:

```
| Authority | Existence (how, date) | Support (pinpoint read?) | Currency (how, date) | Status |
| Mata v. Avianca, 678 F. Supp. 3d 443 | CourtListener API, 2026-10-14 | p. 448 read against ¶2 | cited-by scan 2026-10-14, no negative history found | OK |
| 29 C.F.R. § 541.600 | ecfr.gov, 2026-10-14 | text read | FR docket checked: 2024 rule vacated, rescinded May 2026 | OK — note threshold reverted |
```

A line whose existence or currency cell is empty is a citation that is not ready.
