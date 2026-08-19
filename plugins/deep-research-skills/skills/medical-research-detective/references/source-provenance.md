# Source provenance and the country-of-origin policy

Read at stage 4. How this skill decides which sources may support a conclusion, how country of origin
is determined, and how excluded-country findings are handled without losing the lead.

## Contents
- [The policy](#the-policy)
- [What this is and is not](#what-this-is-and-is-not)
- [Determining country of origin](#determining-country-of-origin)
- [Hard cases](#hard-cases)
- [The quarantine tier](#the-quarantine-tier)
- [Applying it in practice](#applying-it-in-practice)
- [Reporting provenance](#reporting-provenance)

## The policy

**Allowed** — sources whose research originates in a modern, high-income country with an established
independent-research and regulatory tradition. Explicitly including the user's named set: the
**United States, Canada, England** (and the rest of the United Kingdom), **Germany, South Africa,
Japan** — plus peer countries: Australia, New Zealand, Ireland, France, Italy, Spain, Portugal,
Netherlands, Belgium, Austria, Switzerland, the Nordic countries (Denmark, Sweden, Norway, Finland,
Iceland), Poland, Czechia, and other EU/EEA member states, Israel, South Korea, Singapore, and
Taiwan.

**Excluded** — research originating in **Russia** and **China**, per the user's standing instruction.
Excluded sources may never support a conclusion and never appear in the main reference list.

**Always allowed regardless of country:** multinational bodies and regulators that publish their own
independently-reviewed output — WHO, Cochrane, EMA, FDA, MHRA, Health Canada, PMDA — and multinational
trials coordinated from an allowed country.

**Unlisted countries** are judged on the same underlying criteria (independent peer review, research-
integrity enforcement, regulatory transparency, data-availability norms) rather than assumed
excluded. When a source from an unlisted country is central to a finding, say which way you resolved
it and why, so the user can overrule.

## What this is and is not

This is a **source-integrity control**, applied at the level of research systems and institutions —
the same kind of judgment as preferring peer-reviewed journals over preprints, or excluding predatory
venues. The relevant considerations are structural: independence of peer review, enforcement against
data fabrication, transparency of trial registration, and the ability of outside parties to verify or
replicate the work.

It is **not** a statement about the ability, honesty, or worth of any nation's scientists or people,
and it must never be described that way in output. Excellent researchers work everywhere, including
in excluded countries, and this policy will sometimes set aside good work. That cost is accepted in
exchange for a uniformly verifiable evidence base.

Because it is a filter the user chose rather than a scientific universal, it is: **stated openly**
(never applied silently), **auditable** (the excluded appendix shows exactly what was set aside), and
**overridable** (the user can change the country list at any time — record it in
`your-environment.md`).

## Determining country of origin

Provenance follows the **research**, not the publisher or the journal's home country. In priority
order:

1. **Corresponding author's primary affiliation** — the strongest single signal.
2. **Lead/first author's affiliation** and the affiliation of the majority of authors.
3. **The site(s) where data were collected** — for a clinical trial, where patients were enrolled.
4. **The data-coordinating center / sponsor** running the analysis.
5. **Funding source**, as a secondary signal when the above are ambiguous.

A journal published in an allowed country does **not** make a study from an excluded country
allowed — journals publish work from everywhere. Conversely, an allowed-country study published in an
excluded-country journal is judged on the research, though the venue itself still gets the usual
quality check from `evidence-appraisal.md`.

`scripts/verify_citation.py` reports the affiliation countries it can infer from the metadata and
flags excluded ones. **Treat its output as a first pass, not a verdict** — confirm against the paper
itself when a source is load-bearing. Read its provenance line as one of four distinct states:

| State | Means | What you must do |
|---|---|---|
| A country, no caveat | Every affiliation string resolved to a country the table knows, none of them excluded | Proceed (if two allowed countries are listed, it is a collaboration — note it) |
| `PROVENANCE PARTIAL` | Some affiliations resolved, others named nothing the script knows | Read the paper's corresponding-author affiliation — the unresolved one may be the lead |
| `PROVENANCE UNRECOGNIZED` | Affiliation data exists but names nothing the script's table carries | Not a verdict in either direction. It may be an unlisted country, or a listed one named only by a city the table lacks ("Xijing Hospital, Xi'an, Shaanxi") or written in its own script. Resolve it from the paper, then apply the criteria above |
| `PROVENANCE UNKNOWN` | No affiliation metadata at all (common for Crossref-only records) | Resolve from the paper itself |

Two limits are structural. The script's country table covers common research countries and their
larger cities only, so anything outside it reads as *unrecognized* — which is a prompt to resolve it
yourself, never a finding of "excluded" and never a clean pass. And a city is only ever a fallback
signal: a country name in the same institution beats it, and a city sitting in a *complete* US
postal address ("Moscow, ID 83844, USA") is read as American, because that one is the University of
Idaho and not Russia. Note the exact behaviour, which is deliberately conservative: the state code
must sit immediately after the city AND be followed immediately by a ZIP or the country name. On a
bare "Moscow, ID 83844" with no country, the script reports **UNRECOGNIZED** rather than either
country — it will not guess, and the ambiguity comes to you.
A city that resolves without either of those checks firing is still the weakest signal the script
has — confirm it before letting it decide anything.

## Hard cases

**Multinational collaborations.** A trial with sites in many countries, coordinated from an allowed
country, with a corresponding author in an allowed country, is **allowed** — this is the normal shape
of large modern trials. Note the multinational enrollment when it matters to interpretation.

**One co-author from an excluded country.** Not disqualifying. International co-authorship is routine;
the policy looks at where the research was led and conducted, not at individual passports.

**Systematic reviews and meta-analyses.** Judge the review by *its* authors' provenance. If an
allowed-country review pools some excluded-country primary studies, the review may be cited — but say
so, since the pooled effect partly rests on data the policy would otherwise set aside. If excluded-
country studies dominate the pooled estimate, downgrade confidence and note it explicitly.

**Diaspora affiliations.** Researchers at institutions in allowed countries are allowed-country
sources regardless of nationality or where they trained. This policy is about institutional research
systems, never about individuals' origins.

**Excluded-country data licensed or re-analyzed elsewhere.** Treat as excluded-derived and disclose:
re-analysis does not fix the underlying data-integrity question.

**Historic literature.** Apply the policy to the country as it existed when the research was
conducted, and note when a source predates the modern regulatory regime.

## The quarantine tier

Excluded-country sources are **not** simply deleted, because a unique lead is still information the
user should know exists. They go to a clearly-marked appendix under these rules:

- They **never** support a conclusion, never appear in the main reference list, and never contribute
  to a confidence grade.
- They are listed **only** when they contain a lead found nowhere in the allowed literature — not to
  pad the output. If allowed sources already cover the point, the excluded one is simply dropped.
- Each entry states what the lead claims, why it was set aside, and — the actionable part — **what
  allowed-source evidence would be needed to confirm it**, so the thread can be picked up legitimately.
- They are labeled `[X] Excluded-source — not verified, not supporting any conclusion`.

Rationale: a hard delete would silently lose a real detective thread, and silent loss is exactly what
this skill exists to prevent. Quarantining keeps the investigation complete while keeping the
conclusions clean.

## Applying it in practice

Apply the filter **during** stage 4, as sources are collected, not at the end:

1. For each candidate source, determine provenance by the priority list above.
2. **Allowed** → goes to the working set; proceed to appraisal and citation verification.
3. **Excluded** → does it contain a lead absent from the allowed literature?
   - No → drop it silently.
   - Yes → quarantine appendix, with the confirm-path note.
4. **Unclear** → try to resolve from the paper itself. A country you *can* identify but the policy
   does not list is not unclear — judge it on the criteria in [The policy](#the-policy). Only a
   provenance you genuinely cannot determine falls back to excluded, and say so when it does.

Then run one check at the end: **is any conclusion resting on a thin allowed-source base because the
main literature on this topic is excluded-country?** If so, say it plainly — "the majority of
published work on this specific question originates outside the allowed source set, so confidence is
limited." An honest thin base beats a padded one.

## Reporting provenance

The case file's reference list gives each source's country, and the verification summary reports the
filter's effect, e.g.:

> Sources screened: 84. Allowed and cited: 27. Excluded by country policy: 9 (7 duplicative of
> allowed sources and dropped; 2 unique leads listed in Appendix A). Country filter: allowed set per
> your-environment.md; Russia and China excluded.

Two lines, and the reader knows exactly how the filter shaped the evidence base — including how much
was set aside.
