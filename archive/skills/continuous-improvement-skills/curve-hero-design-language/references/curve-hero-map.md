# The Curve Hero map — platform, shell, modules, vocabulary, term map

The pre-built design-language map of Curve Hero, applied through the sync-audit method in
SKILL.md.

> **Provenance & verification.** Compiled 2026-08 from Curve Dental's public marketing pages,
> support-center and Curve Community guide titles/snippets, and dental-industry press.
> curvedental.com and its support sites block automated reads, so many terms rest on search
> snippets rather than full pages. Everything in §7 is explicitly unverified. Before shipping
> a synced UI, verify labels in a live Curve Hero tenant (SKILL.md step 5) and record
> corrections in `your-environment.md`.
>
> **Scope of "sync."** Mirror *vocabulary, field semantics, and interaction patterns* so users'
> habits transfer. Do **not** copy branding, logos, trade dress, trademarked names (Curve®,
> Curve SuperHero™, GRO™, SmartSync™…), or proprietary visuals into your product.

Contents: §2 Platform map · §3 Shell & navigation · §4 Modules · §5 Field & workflow
vocabulary · §6 Term map (say this, not that) · §7 Unverified — check in product

## §2 Platform map (what's what in the Curve family)

- **Curve Hero** — the core web PMS application (support docs say "Curve Hero"); base tier.
  Tenant model: each practice runs at `https://<practiceid>.curvehero.com`; the subdomain is
  the **Curve Hero Practice ID**.
- **Curve SuperHero™** — marketing name for the all-in-one bundle; adds **Curve Imaging**
  (native cloud imaging). **Curve Capture** = locally installed Windows capture/bridge agent;
  **Bridge** = the Sidekick button/module that displays bridged third-party imaging (DEXIS,
  Romexis…). Three distinct things — don't conflate.
- **Companion modules**, branded "Curve <Word>" or "<Word>+": **Curve GRO™** (patient
  engagement: reminder campaigns, two-way texting, **Smart Action List**), **Curve Pay**
  (embedded payments, text-to-pay/email-to-pay, ERA/EFT auto-posting), **Smart Forms / Curve
  Forms** (online patient forms), **Eligibility+** (AI insurance verification), **Benefits
  Advisor** (per-procedure insurance/deductible estimates), **ePrescribe** (+ iPrescribe
  mobile), **Curve Mobile** (staff app), **Curve Go / Curve Portal** (patient-facing),
  patient **Self Scheduling** platform.

## §3 Shell & navigation

- **The Sidekick** — the signature pattern: a persistent patient-context panel alongside the
  Scheduler showing billing, insurance, outstanding balances, medical alerts, and forms to be
  completed; it doubles as the module launcher (click Charting, Insurance, Billing, Bridge
  inside it) and has a **search tab** for filtered patient hunts (recare due, unscheduled
  treatment). Recare text color-codes by status.
- **More menu** — "three horizontal lines above the Sidekick"; opens Administration, Playbook
  Dashboards, and other non-patient areas.
- **Administration** — settings area (via More menu), organized in domain-grouped drop-downs:
  **User management** ("Roles and permissions"), **Patient management** ("Patient Profile
  Settings"), **Scheduling** ("Tags and recare types", "Appointment confirmations"),
  **Charting management** ("Charting settings"), plus **Get My Data** (self-service export).
- **Search** — type-ahead patient search box + **Advanced Search** (filter by birth date,
  status…); opens the patient's **Profile**.
- **Dashboards** — **SnapShot** (support-doc capitalization; the morning-huddle day view:
  Appointment Time, color-coded Appointment Status with an **Appt Status** drop-down +
  **Legend** dialog, Recare icon with count, **Tx icon** for unscheduled treatment plans, plus
  Benefits Advisor, Forms, Provider, and Clinic columns) and **Playbook Dashboards** (**KPI
  Dental Dashboard** — AR, Collections, Production, New Patients, Recare, Treatment Plan
  Value; **Practice Review Dashboard**; **Who's On Deck Dashboard**), gated by the
  **Reporting** role. One blog names "Curve Business Intelligence" as the Playbook umbrella
  (single-sourced — see §7).

## §4 Modules (Curve's own names)

**Scheduler** (per-clinic, per-operatory views; drag-and-drop; Read-Only Scheduler permission
mode; **Smart Fill** for last-minute cancellations) · **Charting** (odontogram with
**Planning / History / Imaging tabs**) · **Perio Charting** (table + graphical views, 6
pathways, keyboard shortcuts) · **Treatment Planning** (**treatment plan cards** with visits,
phases, eSignature) · **Billing** (invoice-based ledger) · **Claims** (status-filterable claim
list) · **Appointments** (per-patient) · **Smart Forms** · **Files and Letters** (Files
folders per patient + letter composer; bulk letters via mail merge in Reports) · **Reports**
(pre-built library, saveable customizations) · **Business Analytics** · **User Directory**.

## §5 Field & workflow vocabulary (verified verbatim)

**Scheduling**
- Create Appointment fields: **Provider, Patient, Clinic, Operatory, Date, Time**.
- **Appointment status** (e.g. *checked in*, *missed*) is distinct from **confirmation
  status**; confirmation types are **tenant-defined objects** (name + color) managed in the
  Appointment Confirmation Management module — treat them as configurable, never hard-coded.
- **Appointment tag** and **Recare type** configured together (Administration → Scheduling →
  Tags and recare types); recare tag has a **Default Frequency** (Months/Days).
- **Recare** — Curve's word (never "recall"): statuses **Due / Overdue / Unscheduled / Not Set
  Up for Recare**; **Add Patient Recare** button on the Profile.

**Patient record**
- **Profile** (nickname/preferred name, email, emergency contacts, address), **Medical
  Alert** (ADA-approved non-editable list + custom alerts; flags surface in Sidekick and
  Appointments), **Profile Tags**, **Responsible party** (abbrev. **RP**, as in "RP Aging") —
  the billed account holder; family members can share one RP.

**Billing & insurance**
- **Invoice-based ledger**: checking out a visit finalizes an **Invoice**; payments,
  **itemized adjustments** (incl. automatic **PPO Write-off Adjustment**), predeterminations,
  and claim rows attach to invoices. Ledger can be locked/unlocked. Automated system
  transactions show "Curve Hero" in the Created/Modified by column. A **More billing
  options** menu holds secondary actions.
- Adding a Patient Payment: **Payment amount** auto-populates with the patient balance and
  applies **top-down** to line items with an amount owing; the **Payment from** drop-down
  lists the responsible party and any **Custom Payers**; credits live as **Account Credit**
  ("Payments from Account Credit"), shareable across family members under one RP.
- **Fee guide** — the in-product term (marketing sometimes says "fee schedule"): assigned to
  a patient or an insurance plan; treatment plans can "select a different fee guide."
- Aging is phrased as **days owing** ("Insurance 0-30 days owing" … "over 90 days owing") and
  split **Responsible Party vs Insurance**: **Responsible Party Aging Summary**, **Insurance
  Aging Summary**, **Overall Aging Summary (Patient+Insurance)**; outstanding-balance hunts
  filter the **Ins Total Owing / Patient Total Owing** report columns.
- Financial reports: **Production Summary** (per-code production only) and **Period Summary**
  (production + collections = Payments + Payments from Account Credit) — Curve's stand-ins
  for a legacy "day sheet."
- **Statement** (customizable; electronic with secure pay link), **Predetermination** (from
  Charting or the Scheduler appointment; **Advanced Claim window** for attachments; **Prior
  Authorization Number** field takes the carrier's DCN), **EOB**, **Carrier** (the insurance
  company), **eClaim**, **ERA**; claim lifecycle shows a **claim status** on the claim row
  with a **Status Details** field (verbatim-confirmed statuses: **Accepted**, **Rejected**).
- Insurance setup: **Coverage tab** → Edit Insurance Plan dialog (Fee Guide drop-down);
  **plan maximum** ($ or unlimited), **remaining benefits**.

**Clinical**
- Odontogram color semantics (defaults, customizable): **red = planned**, **blue = completed
  by the practice**, **green = completed by another practice**.
- **Templated Notes** (clinical note templates; "Add Templated Note" via right-click on a
  visit in the treatment plan) and one-tap **quick buttons** for clinical entry; appointment
  tags sync with clinical quick buttons.
- Perio: **Pocket Depth (PD)**, **Gingival Margin** (= Recession in Curve), **CAL** (auto =
  PD + GM, never manually entered), Bleeding, Calculus, Suppuration, Plaque, Mobility,
  Furcation; default PD alert −4mm/+1mm.

**Forms**
- Curve Forms custom field types (current guide): **Text Input, Checkbox, Dropdown**, with an
  **Add another option** button and a **Required** checkbox (red asterisk); custom fields can
  raise a **custom flag** in the Sidekick; **Incomplete Form** state; **kiosk login code**
  for in-office completion; patients access forms via secure link + **date of birth** (not a
  password).

**Documents & engagement**
- Files and Letters: a **New** button (upper left) creates a folder, uploads a file, or
  creates letters; rows follow strict naming ("Treatment Plan - Accepted - [YYYY-MM-DD]";
  completed forms save as "[Form Name] - [YYYY-MM-DD] [HH:MM].pdf"); double-click opens the
  PDF in a new tab.
- Curve GRO campaign types: **Reminder Campaigns** (auto text/email on appointment
  add/update), **Review Campaigns** (online-review links), **Recare Campaigns** (upcoming/
  overdue recare); **text-to-pay** (patient replies "Pay" to a balance text).
- Verified appointment statuses so far: *checked in, missed, cancelled* (full list
  unverified — see §7).

**Permissions read as verb phrases** (a reliable proxy for on-screen verbs): *Check Out
Appointment, Edit Line Items on Checkout, Send Predeterminations, Manage Kiosk, Generate Get
My Data, Manage Default Folders, Create / Edit / Reschedule Appointment, Manage Insurance
Plans*.

## §6 Term map — say this, not that

| Concept | Curve Hero says | Don't say (other PMS vocabulary) |
|---|---|---|
| Hygiene re-appointment cycle | **Recare** | Recall (Dentrix/Eaglesoft) |
| Billed account holder | **Responsible party (RP)** | Guarantor |
| Checkout artifact | **Invoice** (visit is **checked out**) | Walkout / walkout statement |
| Insurance company | **Carrier** | Payer (in UI labels) |
| Chair/room | **Operatory** | Chair, room |
| Location | **Clinic** | Office, site |
| Patient context panel | **Sidekick** | Patient banner |
| Morning-huddle dashboard | **SnapShot** | Day sheet, huddle report |
| Follow-up task queue | **Smart Action List** (GRO) | Task list, worklist |
| Pre-treatment insurance estimate | **Predetermination** | Pre-auth (except the **Prior Authorization Number** claim field) |
| Data export | **Get My Data** | Backup, dump |
| Daily production/collections report | **Production Summary / Period Summary** | Day sheet (Dentrix/Eaglesoft) |
| Outstanding-balance hunt | **Ins Total Owing / Patient Total Owing** filters | Money Finder (Eaglesoft) |
| Family account view | **Profile** + Responsible party / family members | Family file (Dentrix) |
| Price list | **Fee guide** (in-app) | Fee schedule (only in marketing copy) |
| Overdue AR phrasing | **days owing** buckets | Past due |

## §7 Unverified — check in a live tenant before relying on it

- Exact **default confirmation type names** (mechanism confirmed; shipped values not).
- Full **claim status label set** (only Accepted/Rejected verbatim; ~7 lifecycle states
  described in prose).
- **Treatment plan status labels** (only "unscheduled"/"outstanding" phrasing confirmed;
  "Accepted" appears for signed plans in marketing copy).
- Patient-ID/chart-number field label; the check-in control's verbatim label; the complete
  appointment-status list; tooth-numbering setting options (Universal vs FDI vs Palmer).
- "Short answer / Long answer" form field types — legacy-forms page only; current guide shows
  Text Input/Checkbox/Dropdown.
- Copay/coinsurance field labels in coverage setup (deductible + plan maximum confirmed).
- Relationship between "Curve Hero Mobile" and "Curve Mobile" doc names; Curve Go's exact
  audience (registration uses a Curve Hero login + six-digit access code, suggesting staff).
- SnapShot ("SnapShot" in docs, "Snapshot" in marketing) — prefer the doc form.
- "Curve Business Intelligence" as the Playbook umbrella name — single blog source;
  elsewhere it's "Business Analytics."
- **Insights Reports** — a distinct zendesk article title; contents unverified.
- No "Deposit Slip" report found for Curve (Dentrix Ascend has one) — assume payment/deposit
  reporting lives in Financial Reports / Curve Pay reconciliation until verified.
- Whether a named bulk statement run exists (only per-statement electronic sending verified).
