# Design tokens

Read at stage 5. Every value below carries its provenance. Two sources supply them: the official
Microsoft assertion-evidence template, and the University of Tennessee System brand guidelines.
`scripts/build_deck.py` encodes all of them; copy the geometry table when building outside the
script.

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
| UT System brand guidelines | Primary **Goudy Old Style** (serif); supporting **Gotham** (sans-serif); sanctioned free alternative for presentations by non-designers: **Montserrat** |

UT's brand page states that its office licenses Gotham and Goudy Old Style, and that open-source
alternatives "are encouraged to be used by non-designers for presentations, letters and other
materials utilizing the UT System brand," naming Montserrat as the preferred alternative to Gotham.

Point sizes come from the handout and hold regardless of typeface: 28 point headline, 18–24 point
body, 12–14 point references and source tags, and never bold on the reference line.

## The font-substitution problem

PowerPoint substitutes any font the opening machine lacks. Substitution changes character widths,
which pushes a two-line headline onto three lines and can overflow a text box. A deck that renders
correctly on the author's machine and breaks on the Controller's has failed.

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

Verified from the UT System brand guidelines.

| Token | Name | Hex | RGB | PMS |
|---|---|---|---|---|
| Primary | Tennessee Orange | `FF8200` | 255, 130, 0 | 151 |
| Secondary | Smoky Mountain Gray | `4B4B4B` | 75, 75, 75 | Cool Gray 11 |
| Background | White | `FFFFFF` | 255, 255, 255 | — |

Two constraints from the same source:
- **Black is not in the palette.** UT reserves it for cases where black-and-white printing is the
  only option. Set body text in Smoky Mountain Gray, not black.
- **UT targets WCAG 2.2 Level AA.** Check contrast before shipping.

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

Three consequences follow, and each contradicts a habit common in UT decks:
1. **Tennessee Orange fails as text on white.** Never set a headline, body text, or a callout number
   in orange on a white background.
2. **White text on a Tennessee Orange fill also fails**, at the same 2.49:1. The readable combination
   on an orange fill is Smoky Mountain Gray at large sizes, which reaches 3.51:1.
3. **Orange on white falls below the 3:1 non-text threshold too.** So orange alone must never be the
   sole carrier of meaning in a chart or diagram. Pair it with a direct label, a darker outline, or a
   distinct shape, so the information survives for a viewer who cannot separate the hue.

A working allocation:
- Headline: Smoky Mountain Gray `4B4B4B`
- Body text and labels: Smoky Mountain Gray `4B4B4B`
- Source tags and slide numbers: `767676`, which clears 4.5:1
- Emphasis fills and chart primary series: Tennessee Orange `FF8200`, always directly labeled and
  outlined in `4B4B4B` so meaning does not rest on hue
- Text placed on an orange fill: `4B4B4B` at 18 pt or larger
- Chart secondary series: Smoky Mountain Gray and its tints

Colors marked "sanctioned" here cover the UT System palette only. Campus and institute brands (UTK,
UTIA, UTHSC, UTFI) publish their own accent sets; check the relevant brand site before borrowing an
accent color.

## Applying the tokens

`scripts/build_deck.py` encodes every value on this page. Pass `--brand ut` for the UT palette,
`--brand neutral` for grayscale, and `--font` to override the typeface. The builder computes contrast
and warns when a chosen combination falls below AA.

When you build outside the script — editing a template, using the `pptx` skill directly — copy the
geometry table above rather than eyeballing positions. Consistent placement across slides is most of
what makes a deck look professional, and it costs nothing once the numbers are written down.
