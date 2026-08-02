# Your cash controls environment (sanitized template)

Fill this in with your real setup. Sensitive specifics (named signers, exact limits, bank
entitlements) belong in `your-environment.private.md` instead — that suffix is git-ignored. Never
commit real signer lists or entitlement details.

- **Approval limits:** <thresholds by amount and payment type; who approves each tier>
- **Dual-control triggers:** <amount/type above which two approvers are required; first-time-payee rule>
- **SoD assignments:** <who initiates / approves / records / reconciles; any accepted conflicts + compensating control>
- **Bank fraud tools enabled:** <Positive Pay type (amount vs. payee); ACH debit filters/blocks; reverse positive pay>
- **Exception default:** <pay/no-pay default on unmatched items — should be "no pay">
- **Bank mandate management:** <who maintains signer/entitlement lists; leaver-removal SLA; review cadence>
- **BEC verification procedure:** <how bank-detail changes and urgent payments are verified out-of-band; known-good contact source>
- **Vendor master controls:** <access restrictions; dual approval on bank-detail changes; verification step>
- **Audit trail / logging:** <systems that log payments and master-data changes; retention; who reviews>
- **Control owner / reviewer / cadence:** <who owns the control set; frequency of SoD and exception review>
