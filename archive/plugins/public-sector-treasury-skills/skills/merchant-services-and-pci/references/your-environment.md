# Your merchant-services environment (sanitized template)

Fill in your real setup. Keep anything sensitive — actual MID numbers, negotiated pricing,
account numbers, breach/compromise history — in `your-environment.private.md`, which is
git-ignored.

- **Acquirer(s)/processor(s):** <who holds your merchant agreements>
- **Gateway(s):** <hosted page / campus commerce platform / terminals by vendor>
- **MID inventory location:** <where the authoritative list lives; owner>
- **Funding pattern:** <gross or net funded, by acquirer; separate Amex funding? funding lag>
- **Batch cutoffs:** <per channel/terminal type>
- **Depository mapping:** <which MIDs fund which DDA; GL accounts for fees and chargebacks>
- **Pricing model per acquirer:** <interchange-plus terms / tiered / flat>
- **Chargeback workflow:** <portal, who responds, evidence sources, internal deadline buffer>
- **PCI program:** <SAQ type(s) per channel, merchant level, validation cycle, QSA/ASV if any,
  who signs the attestation>
- **Department onboarding rule:** <required treasury/PCI sign-off path for new acceptance>
- **Who you confirm current rules with:** <acquirer rep, QSA, card-brand bulletins>
