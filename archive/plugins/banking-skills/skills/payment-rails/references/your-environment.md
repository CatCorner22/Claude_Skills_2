# Your payment-rails environment (sanitized template)

Fill in your real setup. Keep anything sensitive (account numbers, provider IDs) in
`your-environment.private.md`, which is git-ignored.

- **Rails you use:** <ACH / same-day ACH / Fedwire / CHIPS / RTP / FedNow / SWIFT / checks>
- **Typical use per rail:** <e.g. payroll = ACH, supplier wires = Fedwire, urgent = RTP>
- **Cutoff times (by rail, your bank):** <e.g. Fedwire 4:45pm ET; same-day ACH windows>
- **Per-item / daily limits:** <your bank's limits and your internal approval thresholds>
- **Cost per rail:** <negotiated per-item pricing>
- **Providers / bank(s):** <which bank or TMS originates each rail>
- **Return / recall handling:** <ACH return window process; wire recall process>
