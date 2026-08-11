# Your bank-connectivity environment (sanitized template)

Fill in your real setup. Keep host names, keys, and credentials OUT of git entirely —
never commit them, even redacted, beyond structural notes in `your-environment.private.md`.

- **Channels in use:** <host-to-host SFTP / SWIFT (Alliance / service bureau / SCORE) / bank API / portal>
- **What flows over each:** <payments out, statements in, by bank>
- **File formats exchanged:** <ISO 20022 pain/camt, BAI2, proprietary>
- **Security:** <PGP encryption, key rotation cadence, IP allowlisting — describe, don't paste secrets>
- **Middleware / TMS / ERP:** <what originates and receives files>
- **Resilience:** <fallback channel if the primary is down>
