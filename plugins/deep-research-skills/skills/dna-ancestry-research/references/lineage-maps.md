# Lineage maps — the four maps, the spec recipes, and the honesty rules

The bundled renderer (`scripts/lineage_maps.py`) draws what a JSON spec says onto simplified
public-domain outlines, or lays out an ahnentafel pedigree. It knows nothing about ancestry: the
sources, dates and uncertainty come from the spec, and every map carries them in its footer.

## Contents
- [§1 Which maps, and what each may claim](#1-which-maps-and-what-each-may-claim)
- [§2 Map spec recipes](#2-map-spec-recipes)
- [§3 Pedigree chart and ahnentafel](#3-pedigree-chart-and-ahnentafel)
- [§4 Honesty rules](#4-honesty-rules)
- [§5 Redaction and sharing](#5-redaction-and-sharing)
- [§6 Data, licence and interchange](#6-data-licence-and-interchange)

## §1 Which maps, and what each may claim

| Map | Layer | Draws | May claim | Must say |
|---|---|---|---|---|
| Deep-ancestry routes | Y-DNA and mtDNA | one schematic route per line through dated, sourced waypoints | the sequence of dated nodes from the ladder (`haplogroups-and-deep-ancestry.md` §5) | "schematic lines between named places, not travelled paths"; each waypoint's age and source; the confidence grade; where the chip's resolution ends |
| Composition shading | autosomal | the vendor's regions shaded by the vendor's own numbers | resemblance to reference panels at the stated confidence and version | vendor, version, confidence slider; "not descent" |
| Ancestor places | genealogy | one point per documented person or event, grouped by line | where the records place named people | the evidence grade of each link; living people redacted |
| Pedigree chart | genealogy | the ahnentafel to N generations | the proven, supported and hypothesised links, visually distinct | the numbering rule; dashed boxes are unproven or unknown |

Keep them separate. A route and a percentage on the same canvas invite the reader to connect a
thousands-of-years lineage to a centuries-scale similarity score, and the two have nothing to do
with each other.

## §2 Map spec recipes

Run: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/lineage_maps.py" map spec.json -o out.svg`.
Named extents: `world`, `atlantic`, `europe`, `ireland-britain`, or a box
`[minlon, minlat, maxlon, maxlat]`. The world and Atlantic extents use the 1:110m outlines; the Europe
and Ireland–Britain extents, and any custom box inside the Europe extent, use the finer 1:50m file.
A box such as `[-16, 28, 62, 62]` (Ireland to the steppe and the Near East) suits most European
deep-ancestry routes better than the Atlantic extent. `width` and `height` size the map panel; the
footer — legend, the numbered waypoint key, wrapped notes and the attribution — is laid out below it
and the canvas grows to fit, so long notes never overlap the legend. Waypoints are drawn as numbered
markers with their names and dates in the key, which keeps a crowded coastline legible; a waypoint
with no label and no `when` only bends the line. Country names are Natural Earth `ADMIN` names or
ISO-A3 codes, case-insensitive; a name the data does not contain is reported in the footer rather
than silently dropped. Shaded countries carry their value at the polygon's centre, and the six-band
legend (0–1, 1–5, 5–10, 10–25, 25–50, 50–100 %) is added automatically — the bands are finer below
25% because that is where composition sub-labels live.

**Deep-ancestry routes** (dates and places illustrative — fill from the ladder):
```json
{
  "title": "Deep ancestry — paternal and maternal lines",
  "subtitle": "schematic routes between dated nodes; ages from the cited clocks",
  "extent": [-16, 28, 62, 62],
  "routes": [
    {"label": "Y-DNA: M269 > P312 > L21 (terminal marker on chip)", "color": "#b5452c",
     "waypoints": [
       {"lon": 40.0, "lat": 48.0, "label": "steppe", "when": "M269 TMRCA ~6,400 ybp (YFull)"},
       {"lon": 10.0, "lat": 50.0, "label": "central Europe", "when": "P312 ~4,500 ybp (YFull)"},
       {"lon": -1.8, "lat": 51.2, "label": "Wessex", "when": "Beaker arrival ~2450 BCE (Olalde 2018)"},
       {"lon": -6.2, "lat": 55.3, "label": "Rathlin", "when": "L21 present ~2000 BCE (Cassidy 2016)"}]},
    {"label": "mtDNA: T1 — diffuse European presence, two entry routes", "color": "#2a5d8f", "dash": "6 4",
     "waypoints": [
       {"lon": 38.0, "lat": 36.0, "label": "Near East", "when": "T1 ~21 ka (Pala 2012)"},
       {"lon": 21.0, "lat": 45.5, "label": "Starčevo-Criş", "when": "Early Neolithic T1a"},
       {"lon": 11.7, "lat": 51.3, "label": "Karsdorf (LBK)", "when": "~7,000 ybp"}]}
  ],
  "legend": [{"color": "#b5452c", "label": "paternal line (Y-DNA)"}, {"color": "#2a5d8f", "label": "maternal line (mtDNA)"}],
  "notes": ["Ages: YFull tree (date read), Pala et al. 2012; ancient samples: Haak 2015, Olalde 2018, Cassidy 2016.",
            "Chip resolution ends at the terminal marker shown; deeper nodes need sequencing.",
            "Coordinates are plotting approximations, not sourced locations."]
}
```
Use `"dash"` to distinguish a diffuse or hypothesised leg from a sampled one.

**Composition shading** (the vendor's numbers, with version):
```json
{
  "title": "Ancestry composition — vendor X, version N, 50% confidence",
  "extent": [-12, 35, 30, 62],
  "shade": [{"country": "Ireland", "value": 62, "label": "British & Irish 62%"},
            {"country": "GBR", "value": 62},
            {"country": "France", "value": 9, "label": "French & German 9%"},
            {"country": "Germany", "value": 9}],
  "notes": ["Shading repeats the vendor's regional figure on every country the region covers; it is resemblance to the vendor's reference panel, not descent.",
            "Vendor X, Ancestry Composition version N, read <date>."]
}
```
A vendor region that spans several countries is shaded on each of them at the same value, and
the note says so; do not invent a per-country split the vendor did not make.

**Ancestor places** (points grouped by line; redacted copy for sharing):
```json
{
  "title": "Documented ancestors by place",
  "extent": "ireland-britain",
  "points": [{"lon": -8.47, "lat": 51.90, "label": "#4 (paternal grandfather)", "sub": "b. 1890s, civil register", "group": "paternal"},
             {"lon": -8.60, "lat": 53.70, "label": "#5", "sub": "m. 1920s, parish register", "group": "paternal"},
             {"lon": -9.05, "lat": 53.27, "label": "#7", "sub": "bapt. 1890s, parish register", "group": "maternal"}],
  "legend": [{"color": "#2a5d8f", "label": "paternal"}, {"color": "#b5452c", "label": "maternal"}],
  "notes": ["Each point is a record-supported event; evidence grades in the report's ahnentafel table."]
}
```
Points in the same `group` share a colour; use the ahnentafel number as the label on any copy
that leaves the machine and keep names in the private copy only.

## §3 Pedigree chart and ahnentafel

Run: `python3 "${CLAUDE_PLUGIN_ROOT}/skills/dna-ancestry-research/scripts/lineage_maps.py" pedigree persons.json -o pedigree.svg --generations 5 --redact`.
Input is a JSON object keyed by ahnentafel number: person 1 is the subject, and person n has
father 2n and mother 2n+1, so even numbers are men and odd numbers women apart from person 1
[canon attribution — Eytzinger's 1590 numbering]. Five generations are persons 1–31. Missing
numbers draw as dashed "unknown" boxes, which is the right way to show an unproven link: leave the
number empty rather than filling it with a guess.
```json
{"1": {"name": "Subject", "birth": "1980", "place": "Boston"},
 "2": {"name": "Father", "birth": "1950", "place": "Boston"},
 "3": {"name": "Mother", "birth": "1952", "death": "2015", "place": "Cork"},
 "6": {"name": "Maternal grandfather", "birth": "1920", "death": "1990", "place": "Cork"}}
```

## §4 Honesty rules

1. **Routes are schematic.** The renderer's footer says so automatically; the spec's `notes`
   must add the sources and the clock for every waypoint's date.
2. **Nothing on a map that is not in the ladder or the report.** A waypoint without a source row
   is removed, not decorated.
3. **Resolution ends where the data ends.** The route stops at the terminal marker the data
   supports; a dashed leg may continue to a sequencing-based node only when such a result exists.
4. **One number per shaded region, the vendor's own, with its version**, repeated on every
   country the region spans.
5. **Dates with their uncertainty.** "~2,000 ybp (YFull TMRCA; CI not shown)" beats "0 CE".
6. **No ethnonyms as waypoints.** "Beaker-associated", "Yamnaya horizon" and "Early Neolithic"
   are archaeological labels tied to dated samples; "Celts", "Vikings" and the like are not
   waypoints unless the ladder has a cited sample for them.

## §5 Redaction and sharing

`--redact` replaces the name, dates and place of anyone with no death date and a birth within the
last hundred years with "living". It is the default for any copy leaving the machine. On the
ancestor-places map, label points by ahnentafel number and keep the named version private.
Because every file this skill produces describes relatives who did not consent, the private
directory — not a repository, not a shared drive — is where the un-redacted versions live.

## §6 Data, licence and interchange

- **Outlines:** Natural Earth Admin 0 country polygons, 1:110m and 1:50m, simplified and stored
  as compact JSON in `assets/`. Natural Earth is public domain; no permission or credit is
  required, and the suggested credit "Made with Natural Earth" is in every footer [licence file
  read]. Natural Earth's own carve-outs — a newspaper's world base map, a European agency's
  rivers and lakes, a vendor's North American roads — are not in these files; adding European
  rivers to a map would bring one in [snippet-only — licence file].
- **Projection:** equirectangular with the standard parallel at the extent's mid-latitude. Fine
  for these extents; a world map at the poles is distorted, and the routes are schematic anyway.
- **Format:** SVG, viewable in any browser; convert with `rsvg-convert` or `cairosvg` when a PNG
  is needed. Keep the spec JSON beside the SVG so the map can be re-drawn when a source changes.
- **Interchange:** if a tree is to leave this skill, emit GEDCOM 7 directly from the ahnentafel
  (the specification is Apache-2.0 and ships grammar and validation files) rather than through a
  bundled parser library whose licence or supported version does not fit [snippet-only]; read the
  minimal file skeleton from the specification, not from memory.
