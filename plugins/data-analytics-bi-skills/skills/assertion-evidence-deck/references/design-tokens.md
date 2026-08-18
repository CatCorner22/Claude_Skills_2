# Design tokens

Read at stage 5. Every value below carries its provenance. Two sources supply them: the official
Microsoft assertion-evidence template (geometry and typography), and — for the optional
`warm-accent` brand pack only — a published institutional brand standard, kept because it is a
useful worked case rather than because you should use it. The builder ships a **neutral palette as
its default**. `scripts/build_deck.py` encodes the geometry, typography, and colors for the slide
kinds it builds; copy the geometry table when building outside the script.

## Contents
- [Slide geometry](#slide-geometry)
- [Typography](#typography)
- [The font-substitution problem](#the-font-substitution-problem)
- [Color](#color)
- [Applying the tokens](#applying-the-tokens)

## Slide geometry

Extracted directly from `Assertion_evidence_presentation.pptx` — the official template Microsoft
published in cooperation with Melissa Marshall. Values in inches, converted from the template's EMU.

| Element | x | y | width | height | Size |
|---|---|---|---|---|---|
| Slide canvas | — | — | 13.333 | 7.5 | 16:9 |
| Headline | 0.92 | 0.62 | 11.52 | 0.94 | 28 pt bold, left |
| Body, full width | 0.92 | 1.95 | 11.52 | 5.00 | 18 pt |
| Body, two columns | 2.15 / 7.65 | 1.95 | 3.53 each | 4.30 | 16 pt |
| Body, three rows | 3.17 / 6.68 | 2.21 / 3.80 / 5.38 | 3.50 each | 1.34 | 16 pt |
| Slide number | 9.42 | 6.95 | 3.00 | 0.40 | 12 pt, right |
| Title-slide headline | 0.00 | 1.67 | 13.33 | 2.22 | 40 pt |

Derived values:
- **Side margin: 0.92 inch.** Small margins, as the checklist requires.
- **Gap below the headline: 0.39 inch** measured box-to-box. The handout asks for at least half an
  inch of white space; the template achieves the visual half-inch because the headline box holds
  28-point text at 90 percent line spacing and sits taller than its single line of text. Keep body
  content at y = 1.95.
- **Headline line spacing: 90 percent.** Set in the slide master's title style.
- **Body line spacing: 90 percent**, with 10-point space before each paragraph.
- **Two-line headline budget: about 105 characters** at 28 point across 11.52 inches. Verify by
  rendering, not by counting.

The template's slide master sets titles bold, left-aligned, with bullets suppressed. Its body style
also suppresses bullets at the first level — the template ships with bullets off, which is the method
expressed as a default.

## Typography

Three typefaces compete for this slot. Choose deliberately.

| Source | Requirement |
|---|---|
| *Present Your Science* handout | A bold sans-serif such as **Calibri** |
| Microsoft assertion-evidence template | Theme major and minor fonts both set to **Arial** |
| The same institutional brand standard | Primary **Goudy Old Style** (serif); supporting **Gotham** (sans-serif); sanctioned free alternative for presentations by non-designers: **Montserrat** |

That brand page states that its office licenses Gotham and Goudy Old Style, and that open-source
alternatives are encouraged for non-designers producing presentations and letters, naming
Montserrat as the preferred substitute for Gotham. The pattern generalizes: a licensed brand face
you do not have a seat for is a font-substitution problem waiting to happen, and most brand
standards name their own fallback — find it before you pick one yourself.

Point sizes come from the handout and hold regardless of typeface: 28 point headline, 18–24 point
body, 12–14 point references and source tags, and never bold on the reference line.

## The font-substitution problem

PowerPoint substitutes any font the opening machine lacks. Substitution changes character widths,
which pushes a two-line headline onto three lines and can overflow a text box. A deck that renders
correctly on the author's machine and breaks on the recipient's has failed.

Apply this rule:
1. **The recipient's machine governs.** For a deck that leaves your machine — emailed, presented from
   someone else's laptop, posted to a shared drive — use **Calibri**. It ships with Microsoft Office
   everywhere and satisfies the handout's requirement directly.
2. **Use Arial** when the deck must match the official template's own theme, or when the audience
   mixes Windows and macOS and Calibri coverage is uncertain.
3. **Use Gotham or Montserrat** only when you control the presenting machine and have confirmed the
   font is installed, or when you export to PDF. Brand compliance is real, but a broken layout in
   front of leadership costs more than a substituted typeface.
4. **Embed or export.** When brand typefaces matter and the file must travel, either embed fonts in
   the `.pptx` or deliver a PDF alongside it.

State which typeface you chose and why when you deliver the deck. That one sentence prevents the
recipient from "fixing" it.

## Color

The default is the **neutral palette** (`--brand neutral`, the builder's default): ink `333333`
for body text, primary `4B4B4B`, muted `767676` for source tags and slide numbers, secondary
`A6A6A6`, on white. Every *text* pair clears WCAG AA on white — `333333` at 12.63:1, `767676` at
4.54:1. The one value that does not is `A6A6A6`, the second chart series, at 2.43:1 against white:
below the 3:1 non-text threshold, so it is subject to the same rule as the warm accent below —
never the sole carrier of meaning. The builder keeps data labels on for exactly that reason. Use
this palette unless the deck must match an existing brand.

Everything below documents the **warm-accent palette** (`--brand warm-accent`; the older name
`ut` still resolves, so existing deck specs keep working). The values are verified from a
published institutional brand standard. It is here as a **worked case, not a recommendation** —
this is what happens when a real brand's signature color meets WCAG, and the same arithmetic
applies to whatever brand you are handed.

| Token | Name | Hex | RGB | PMS |
|---|---|---|---|---|
| Primary | Accent Orange | `FF8200` | 255, 130, 0 | 151 |
| Secondary | Slate Gray | `4B4B4B` | 75, 75, 75 | Cool Gray 11 |
| Background | White | `FFFFFF` | 255, 255, 255 | — |

Two constraints from the same source:
- **Black is not in the palette.** It is reserved for cases where black-and-white printing is the
  only option. Set body text in Slate Gray, not black.
- **The standard targets WCAG 2.2 Level AA.** Check contrast before shipping — which is exactly
  where it runs into trouble.

Contrast ratios computed from the published RGB values using the WCAG 2.x relative-luminance formula.
Thresholds: 4.5:1 for normal text, 3:1 for large text (18 pt regular or 14 pt bold and above) and for
meaningful non-text graphics.

| Pair | Ratio | Normal text | Large text | Non-text graphic |
|---|---|---|---|---|
| `4B4B4B` on white | 8.72:1 | Passes | Passes | Passes |
| `767676` on white | 4.54:1 | Passes | Passes | Passes |
| `FF8200` on white | 2.49:1 | **Fails** | **Fails** | **Fails** |
| White on `FF8200` | 2.49:1 | **Fails** | **Fails** | — |
| `4B4B4B` on `FF8200` | 3.51:1 | **Fails** | Passes | — |

Three consequences follow, and each contradicts a habit common in brand-compliant decks:
1. **The accent fails as text on white.** Never set a headline, body text, or a callout number
   in orange on a white background.
2. **White text on an accent fill also fails**, at the same 2.49:1. The readable combination
   on an orange fill is Slate Gray at large sizes, which reaches 3.51:1.
3. **Orange on white falls below the 3:1 non-text threshold too.** So orange alone must never be the
   sole carrier of meaning in a chart or diagram. Pair it with a direct label, a darker outline, or a
   distinct shape, so the information survives for a viewer who cannot separate the hue.

A working allocation:
- Headline: Slate Gray `4B4B4B`
- Body text and labels: Slate Gray `4B4B4B`
- Source tags and slide numbers: `767676`, which clears 4.5:1
- Emphasis fills and chart primary series: Accent Orange `FF8200`, always directly labeled and
  outlined in `4B4B4B` so meaning does not rest on hue
- Text placed on an orange fill: `4B4B4B` at 18 pt or larger
- Chart secondary series: Slate Gray and its tints

These values cover one institution-level palette. Sub-brands within a large organization typically
publish their own accent sets; check the relevant brand site before borrowing an accent color, and
re-run the contrast arithmetic on whatever you find — a sanctioned color is not an accessible one.

## Applying the tokens

`scripts/build_deck.py` encodes the tokens for the slide kinds it builds. The neutral palette is
the default; pass `--brand warm-accent` only when you must match that brand, and `--font` to
override the typeface. The builder computes contrast on three pairs — ink-on-background, muted-on-background, and
the accent used as text — and warns on stderr when one falls below its threshold.
`--brand warm-accent` warns every run, because the accent as a magnitude number is 2.49:1; that
warning is the tokens rule above speaking, and the fix is to label the value directly rather than to ignore it. Text placed on
a filled shape is picked automatically as whichever of ink/background contrasts better with the
fill.

When you build outside the script — editing a template, using the `pptx` skill directly — copy the
geometry table above rather than eyeballing positions. Consistent placement across slides is most of
what makes a deck look professional, and it costs nothing once the numbers are written down.
