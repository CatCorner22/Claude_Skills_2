# Bank connectivity channels (reference)

Channel availability, ISO 20022 flavors, and API coverage vary by bank and country — **confirm for
each bank/region.**

## Contents
- Channel options
- Trade-off matrix
- SWIFT access models
- File security
- API vs file transfer
- Decision guide

## Channel options
- **Single-bank portal (web):** the bank's browser front end. Manual upload/download of files and
  manual payment entry. Zero build, immediate — but no straight-through processing, no automation,
  and one portal per bank. Fine as a backup or for very low volume; not a production strategy at scale.
- **Host-to-host (H2H) over SFTP:** your ERP/TMS exchanges files directly with the bank over SFTP.
  Automatable, cheap per link, supports any file format the bank accepts (ISO 20022 `pain`/`camt`,
  BAI2, MT940). The cost is **one integration per bank** with **bank-specific** specs and mappings.
- **SWIFT:** a single, standardized, resilient network reaching thousands of banks. Corporates use
  **FIN** messages (e.g. MT101 payment request, MT940/942 statements) and **FileAct** (files,
  including ISO 20022). Higher setup cost and governance, but standardization and reach scale with
  bank count. Access models below.
- **API / open banking:** real-time request/response and webhook push for balances, transactions,
  payment initiation, and status. Driven by open-banking regulation (e.g. PSD2 in Europe/UK) and by
  banks' proprietary APIs. Best for immediacy and event-driven flows; standardization still maturing.

## Trade-off matrix
| Channel | Cost | Per-bank effort | Resilience | Standardization | Best for |
|---------|------|-----------------|------------|-----------------|----------|
| Single-bank portal | Low | Low (manual) | Low (manual, per bank) | Low | 1–2 banks, backup |
| Host-to-host SFTP | Low–mid | High (one build per bank) | Medium (point-to-point) | Low–mid (bank-specific) | Few banks, high volume |
| SWIFT (direct/bureau/SCORE) | High | Low once on-network | High (managed network) | High (ISO/MT) | Many banks, multi-country |
| API / open banking | Mid | Mid (per API) | Medium–high | Emerging | Real-time balances, status, instant payments |

## SWIFT access models
- **Direct (Alliance):** you run SWIFT infrastructure. **Alliance Access** for higher volumes;
  **Alliance Lite2** is a lighter, cloud-based connection for lower volumes and simpler setup.
- **Service bureau:** a third party hosts and operates the SWIFT connectivity for you; you connect to
  the bureau. Lowers in-house infrastructure and ops burden; adds a vendor dependency.
- **SCORE (Standardised Corporate Environment):** a model under which a **corporate** joins SWIFT to
  exchange messages with any participating bank in a many-to-many relationship (rather than each bank
  running its own closed user group). Reaches many banks under one standardized agreement.

## File security
- **PGP encryption:** encrypt the file **payload** with the counterparty's public key so only they
  can decrypt; sign with your private key for integrity/authenticity. Protects data at rest and in
  transit regardless of the transport.
- **SSH keys for SFTP:** authenticate the SFTP session with key pairs, **not passwords**. Register
  your public key with the bank; protect the private key; **rotate** on a schedule and on staff change.
- **Transport + access controls:** IP allowlisting, dedicated/VPN links where offered, and least-
  privilege service accounts.
- **Non-repudiation / digital signatures:** where supported, personal signing tokens or PKI
  (e.g. per-user signing) so a payment file is provably authorized — pairs with **dual control** on
  release.
- **APIs:** OAuth2 client credentials or mTLS, scoped/short-lived tokens, request signing, and
  webhook signature verification.

## API vs file transfer
Use **files** (H2H or SWIFT FileAct) for **high-volume batch**: payroll, AP payment runs, end-of-day
statement retrieval. Files are efficient at scale and fit the banks' batch/cutoff processing.

Use **APIs** when **latency or events** matter:
- Real-time or on-demand **balance and transaction** retrieval (vs waiting for a batch statement).
- **Payment status** tracking and confirmations (vs polling files).
- Initiating **instant rails** (RTP/FedNow) and reacting to Request-for-Payment.
- Event-driven / customer-facing flows needing an immediate response.

Most treasuries run a **hybrid**: files for bulk payments and statements, APIs for real-time balances
and status. The payload standard (ISO 20022) can be shared across both.

## Decision guide
1. **One or two banks, low volume?** Portal to start; H2H SFTP if you need automation.
2. **A handful of banks, high batch volume?** Host-to-host SFTP with ISO 20022 files.
3. **Many banks / multi-country?** SWIFT (choose direct, bureau, or SCORE by in-house capacity).
4. **Need real-time balances, status, or instant payments?** Add bank **APIs** on top of files.
5. **Whatever the channel:** standardize on **ISO 20022**, isolate bank-specific mapping, secure with
   PGP + SSH keys (files) or OAuth/mTLS (APIs), and parallel-run before cutover.
