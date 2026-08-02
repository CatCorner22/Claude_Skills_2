# Your reconciliation environment (sanitized template)

Fill this in with your real conventions. If any value is sensitive (account numbers, real bank
data), keep it in `your-environment.private.md` instead — that suffix is git-ignored.

- **Balance tied to:** <booked/ledger balance | available balance>
- **Cutoff convention:** <e.g. 5:00pm ET; items after cutoff belong to next day>
- **Statement source/format:** <BAI2 | MT940 | CAMT.053 | CSV | Oracle Fusion import>
- **Systems:** <GL/ERP, e.g. Oracle Fusion Cash Management; treasury system if any>
- **Tolerance policy:** <e.g. $2 or 0.1% on one-to-one matches>
- **Stale-check policy:** <e.g. outstanding checks > 90 days are escalated>
- **GL accounts for adjustments:**
  - Bank fees → <account>
  - Interest income → <account>
  - Returned items / NSF → <account>
  - Cash / Cash clearing → <accounts>
- **Reconciliation owner / reviewer / SLA:** <who prepares, who reviews, by when>
- **Recurring known items:** <e.g. monthly lockbox sweep, standing wire, analysis fee>
