# Your ACH environment (sanitized template)

Fill in your real setup. Keep anything sensitive — company IDs, account numbers, bank names
tied to accounts, counterparty details — in `your-environment.private.md`, which is git-ignored.

- **ODFI(s):** <bank(s) through which you originate>
- **Origination platform:** <bank portal / ERP payment batch / payroll provider>
- **SEC codes you originate:** <e.g. PPD payroll + student refunds; CCD/CTX vendor payments>
- **Where returns surface:** <returns report name, statement addenda field, portal screen>
- **Where NOCs surface and who applies them:** <report + master-data owner (payroll / AP)>
- **Exception routing:** <who owns R01-family vs unauthorized vs account-data returns>
- **Prenote policy:** <always on new payroll accounts? on vendor bank changes?>
- **Re-initiation policy:** <whether/when you retry R01/R09, and the count limit you enforce>
- **Same Day ACH:** <whether enabled, your ODFI's cutoffs, when you use it>
- **Debit blocks / ACH filters on your accounts:** <which accounts, who maintains the rules>
- **Where you confirm current NACHA rules:** <ODFI bulletins, NACHA rules subscription, counsel>
