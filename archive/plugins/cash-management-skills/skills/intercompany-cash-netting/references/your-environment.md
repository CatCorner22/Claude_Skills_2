# Your netting environment (sanitized template)

Fill this in with your real structure. Sensitive figures, entity names, and bank details belong in
`your-environment.private.md` instead — that suffix is git-ignored.

- **Participating entities:** <legal entities in the netting cycle, by region>
- **Currencies:** <currencies netted; functional currency per entity>
- **Netting type:** <bilateral | multilateral through a netting center>
- **Netting center / system:** <treasury entity or IHB running it; netting module/TMS>
- **Calendar:** <invoice cutoff day; match/dispute window; calc date; advice date; settlement date>
- **Dispute handling:** <how disputed intercompany items are flagged and deferred>
- **FX policy:** <settlement currency per participant; rate source/timestamp; who bears FX; hedging>
- **In-house bank / POBO-COBO:** <is an IHB in place; which flows go POBO/COBO; internal account structure>
- **Pooling:** <notional | physical/ZBA; header account; tax/legal sign-off status>
- **Clearing account:** <the intercompany netting clearing account reconciled to zero each cycle>
- **Owners:** <who runs the cycle; who confirms; who posts and reconciles>
- **Tax/legal notes:** <transfer pricing on interco interest, thin-cap, set-off enforceability by jurisdiction>
