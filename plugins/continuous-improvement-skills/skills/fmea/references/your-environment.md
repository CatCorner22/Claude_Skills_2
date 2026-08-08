# Your FMEA environment (sanitized template)

Fill this in with your real setup. If any value is sensitive (real account numbers, bank names,
counterparties, incident details), keep it in `your-environment.private.md` instead — that suffix
is git-ignored. Commit only sanitized, structural examples.

- **Processes under FMEA:** <e.g. daily bank reconciliation; auto-recon rule set for account X;
  the payment run>
- **Structure tree:** <process → stages → tasks, as you decompose it>
- **Failure-mode taxonomy:** <your named break/defect types, e.g. duplicate line, truncated
  addenda, tolerance mismatch, missing sweep, unparsed reference>
- **Calibrated Severity anchors:** <what a 9–10 means here — materiality threshold, regulatory
  exposure, audit-finding level>
- **Calibrated Occurrence anchors:** <your volumes: what "1 in 100 items" means per day/month>
- **Detection inventory:** <the controls that exist today: unreconciled report worked daily,
  month-end tie-out, loader warnings, sign-offs — and which are reliably worked>
- **Register location:** <where the FMEA lives — sheet, tracker — and its owner>
- **Adjudication:** <who reviews and finalizes every S/O/D rating; who prunes drafted modes>
- **Re-run cadence:** <after incidents + changes, plus the standing rhythm>
- **Current High rows / open actions:** <sanitized summary>
