# Curve Hero Benchmark — Dental Notes Standardizer

This document records every vocabulary substitution the standardizer makes and the
Curve Hero canonical term it maps to. Use it to verify coverage, track gaps, and
evaluate standardizer accuracy against live Curve Hero notes.

---

## 1. Canonical Term Map

| Non-standard / legacy term | Curve Hero canonical term | Source |
|---------------------------|--------------------------|--------|
| recall | **Recare** | Curve Hero UI — Recare module |
| hygiene recall | **Recare** | Curve Hero UI — Recare module |
| maintenance recall | **Recare** | Curve Hero UI — Recare module |
| guarantor | **Responsible Party (RP)** | Curve Hero patient record header |
| account holder | **Responsible Party (RP)** | Curve Hero patient record header |
| head of household | **Responsible Party (RP)** | Curve Hero patient record header |
| walkout | **Invoice** | Curve Hero checkout flow |
| walkout statement | **Invoice** | Curve Hero checkout flow |
| checkout receipt | **Invoice** | Curve Hero checkout flow |
| insurance company | **Carrier** | Curve Hero insurance panel |
| insurer | **Carrier** | Curve Hero insurance panel |
| payer | **Carrier** | Curve Hero insurance panel |
| plan carrier | **Carrier** | Curve Hero insurance panel |
| treatment room | **Operatory** | Curve Hero schedule grid |
| op (abbreviation) | **Operatory** | Curve Hero schedule grid |
| fee schedule | **Fee Guide** | Curve Hero admin / Carrier setup |
| UCR fee | **Fee Guide** | Curve Hero admin / Carrier setup |
| CDT fee table | **Fee Guide** | Curve Hero admin / Carrier setup |
| days outstanding | **Days Owing** | Curve Hero AR / aging view |
| aging bucket | **Days Owing** | Curve Hero AR / aging view |
| past-due days | **Days Owing** | Curve Hero AR / aging view |

---

## 2. Benchmark Methodology

### 2.1 Provenance
The canonical terms above were derived from the Curve Dental product documentation and
direct UI inspection as of **2026-Q3**.  
Key provenance note from `MEMORY.md` (2026-08-02):

> Curve-specific vocabulary differs from other dental PMSs: Recare (not recall),
> Responsible Party/RP (not guarantor), checkout finalizes an Invoice (no "walkout"),
> Carrier, Operatory, Sidekick, SnapShot, fee guide, "days owing" aging.

### 2.2 Test Corpus Construction
A benchmark run consists of:

1. **Positive cases** — notes containing each non-standard term; assert the canonical
   replacement appears in output and the original does not.
2. **Near-miss cases** — notes that look similar but should *not* be altered
   (e.g. `"operator"` should not match the `op` rule).
3. **No-op cases** — already-compliant notes; assert output equals input and
   `replacements` is empty.

Unit tests covering all three categories live in
`src/lib/standardize.test.js` and can be run with:

```bash
npm test
```

### 2.3 Scoring

| Category | Pass criterion |
|----------|----------------|
| Recall   | 100 % of known non-standard terms mapped to canonical |
| Precision | 0 false positives on the near-miss corpus |
| No-op    | Input unchanged when no non-standard terms present |

---

## 3. Known Gaps & Future Work

| Gap | Priority | Notes |
|-----|----------|-------|
| **Sidekick** normalization | Medium | No legacy synonym identified yet; add when found |
| **SnapShot** normalization | Medium | "quick exam" or "snapshot exam" → SnapShot |
| Case-sensitive proper names | Low | "Op" mid-sentence vs "op" abbreviation — current regex may over-match |
| Multi-language notes | Low | Non-English clinical notes out of scope for v0.1 |
| Abbreviation chains | Low | "pt w/ ins co" — tokenize before replacing |

---

## 4. Running the Benchmark

```bash
# 1. Install dependencies
cd tools/dental-notes-standardizer
npm install

# 2. Run unit tests (vitest)
npm test

# 3. Start the interactive UI for manual review
npm run dev
# → open http://localhost:5173
```

---

## 5. Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-08-02 | Initial 19-rule map; all terms from Curve Hero vocabulary reference |
