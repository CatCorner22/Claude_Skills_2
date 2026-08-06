# Cultural guidance — intake data, notification logic, idioms, cluster patterns

Preserved near-verbatim from the source spec ("Chicken Little, College Kid" v1.0.0). This
is the serious, professional core of the skill — clinical communication quality, not
parody. Every cluster below is a **starting point for awareness, never a stereotype**;
the individual patient's stated preferences always win.

Contents: §1 Patient data inputs · §2 Notification logic · §3 Southern US idioms ·
§4 Cross-cultural cluster guidance · §5 Dental-specific application notes · §6 Cursor
implementation notes (source truncated)

## §1 Patient data inputs (web app requirements)

Intake forms and patient profiles must support:

1. **Country / nationality / country of birth** — full ISO 3166-1 dropdown (common
   English names + official codes); separate fields as useful (birth, primary
   residence/nationality, origin); "United States" a clear option; searchable/type-ahead
   preferred.
2. **Language fields** — **Preferred language** (required or strongly encouraged),
   **Native language**, **Other languages spoken** (multi-select or free-text); ISO 639
   list or a practical medical subset (English, Spanish, Mandarin, Cantonese, Arabic,
   Vietnamese, Korean, Tagalog, Hindi, French, Portuguese, Russian…) plus "Other"
   free-text; checkbox: **"Interpreter needed / preferred."**
3. **Related trigger fields** — preferred communication method; optional free-text
   cultural or religious considerations the patient volunteers; family decision-maker
   notes where relevant.

## §2 Non-US-born / non-English-preferred notification logic

**Trigger conditions** (any one suffices): country of birth/nationality/residence ≠ US;
preferred language ≠ English (or the practice's primary language); interpreter flagged;
staff manually request cultural guidance.

**When triggered**, surface a clear, non-alarmist staff note:

> **Cultural & Language Awareness Note**
> Patient country of origin/birth: [Country]. Preferred language: [Language].
> Interpreter recommended if not already arranged.
> Quick cultural considerations (general guidance only — individuals vary): [2–4
> relevant tips from §4].
> Always ask the patient about their own preferences for communication, touch, family
> involvement, and privacy.

Plus a one-click or hover quick-reference card with the most relevant notes. Never assume
the patient holds every trait of their country of origin — frame everything as "common
patterns that may apply — confirm with the individual."

**Staff quick-reference card example:**
> Country of origin: Vietnam. Preferred language: Vietnamese.
> Key notes: softer eye contact with the dentist often signals respect; patients from
> this background may under-report pain; family involvement in decisions is common.
> Prefer a professional interpreter when available. Always confirm the individual
> patient's preferences for communication and privacy.

## §3 Southern US regional idioms (Tennessee / Appalachia / South)

Non-native English speakers (and Americans from other regions) often misinterpret:

- **"I'm covered up" / "covered up with work"** = extremely busy, overloaded — not
  literally covered by objects.
- **"Fixin' to"** = about to / preparing to.
- **"Bless your heart"** = genuine sympathy OR gentle criticism, depending on tone.
- **"Over yonder"** = over there (sometimes vague distance).
- **"Might could"** = maybe can / possibly able to.

Advise staff to politely clarify ambiguous regional slang with patients or colleagues
from other backgrounds.

## §4 Cross-cultural nonverbal & communication guidance

Dental relevance prioritized: greeting, explaining procedures, proximity in the chair,
touch around the face/head, pain discussion, family presence, hierarchy, modesty.

**General principles for all patients**
- Observe the individual's comfort level and mirror it when appropriate.
- Use professional interpreters, not family members, for clinical accuracy and privacy.
- Pain expression varies: some cultures under-report (stoicism), others are more
  expressive. Use validated scales carefully; watch nonverbal cues.
- Collectivist cultures often involve family in decisions; ask who the patient wants
  present or consulted.
- In many cultures the dentist is high-status; patients may not question
  recommendations. Invite questions explicitly and check understanding.
- Dental exams inherently invade personal space — acknowledge gently, explain steps.

**East Asia (China, Japan, Korea, Vietnam…)** — softer, intermittent eye contact with
authority often preferred; larger personal space; limited touch (avoid casual head
touching — the head is sacred in some traditions); point with an open hand, not the index
finger; silence is comfortable and respectful; a polite "yes" may mean "I hear you," not
agreement; pain may be under-reported. Confirm understanding without putting the patient
on the spot.

**South Asia (India, Pakistan, Bangladesh…)** — eye contact/hierarchy similar with
elders; the left hand is often considered unclean (avoid handing items or gesturing near
the face/mouth with it); the head is sacred in many traditions; a head wobble can mean
understanding or agreement; family involvement common; modesty and same-gender provider
preferences may arise.

**Middle East, North Africa, Muslim-majority contexts** — eye contact often more limited
between opposite genders; same-gender handshakes usually fine, opposite-gender touch
frequently avoided; left hand unclean; thumbs-up and the "OK" circle are offensive in
parts of the region; showing the sole of the foot is rude; modesty is important —
same-gender providers preferred when feasible; Ramadan fasting, prayer times, and gender
norms may affect scheduling. Extra sensitivity around face/mouth exposure and
opposite-gender contact.

**Latin America** — warmer, more direct eye contact; closer personal space; light touch
on the arm can be friendly and expected; high family involvement; rapport before
business; the OK sign is offensive in Brazil and elsewhere; pain expression may be more
open. Build brief rapport; expect possible family presence.

**Sub-Saharan Africa (highly diverse)** — eye contact frequently reduced with authority
as respect; often high-context, indirect communication; family/community
decision-making can be strong; touch and space norms vary widely. Respect for elders;
ask about decision-makers.

**Europe (broad differences)** — Northern/Germanic/Scandinavian: larger space, direct
communication, firm handshakes, direct eye contact valued. Southern (Italy, Spain,
Greece…): closer space, expressive gestures, warmer style. Eastern Europe/Balkans: head
movements can be inverted (a nod means "no" in parts of Bulgaria and neighbors);
directness often appreciated. Match the patient's preferred directness; give clear,
detailed explanations when expected.

**Indigenous / Native American contexts (highly varied)** — eye contact often less
direct as respect; communication may favor storytelling and listening; high respect for
elders. Avoid assumptions; ask about individual and community preferences.

**Other high-value tips** — point with an open palm; avoid aiming the soles of your feet
at a person (Middle East, parts of Asia); silence is respectful in many East Asian and
Indigenous contexts — don't read it as disagreement; volume and expressiveness norms
vary (louder/animated in some Latin, African, Caribbean, Arab contexts; softer in many
East Asian and some Indigenous settings); standing when an elder enters is respectful in
many places; crossed legs or visible soles can be problematic.

## §5 Dental-specific application notes

- The dental chair places the provider in physical dominance close to the face:
  explicitly explain each step, offer breaks, and watch for discomfort cues that may be
  culturally muted.
- Consent conversations: in collectivist cultures, patients may want family present or
  consulted — offer the option.
- Pain scales: under- and over-reporting both have cultural components; combine
  self-report with clinical observation.
- Written materials: key instructions in the patient's preferred language when possible;
  plain language even in English (see `writing-skills:adams-plain-grade`).
- Sensitive topics (hygiene habits, tobacco, diet, costs, non-compliance): direct
  confrontation can be face-threatening — prefer collaborative framing ("What has worked
  well for you so far?" / "How can we make this easier?").
- Patients from systems with episodic dental care may need gentle education on US
  preventive schedules — explain the "why."
- Staff training cue: generate short quick-reference cards or talking points tailored to
  a patient's recorded country/language profile.

## §6 Cursor implementation notes (source truncated)

From the spec, verbatim where available:
- Prefer this persona for any generation or review of patient-facing or staff-facing
  text, forms, alerts, or communication tools.
- When designing intake forms or profile schemas, ensure the country and language fields
  in §1 are present and correctly typed (ISO standards preferred).
- When staff query about a specific patient, automatically surface relevant cultural and
  language notes if the §2 trigger conditions are met.

> **Source truncation.** The uploaded spec cuts off mid-list at a fourth bullet
> beginning "When". Supply the remainder of the implementation notes to complete this
> section; everything above it is preserved.
