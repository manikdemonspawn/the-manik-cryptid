# Content Model

The website should grow by adding artifacts to established realms, not by inventing a new top-level realm every time a new project appears.

## Artifact identity

Every meaningful item should eventually have:

- unique ID / slug;
- title;
- canonical realm;
- optional collection / shelf / district;
- artifact type;
- status;
- dates where relevant;
- public-safe summary;
- provenance / why it matters;
- media references;
- platform destinations;
- cross-references rather than duplicate copies.

See `data/artifact-schema.json`.

## Death and resurrection

### Morgue

A dead project records a `death_date` and status `deceased`.

A resurrected project retains its original `death_date`, adds `resurrection_date`, and changes status to `resurrected`.

The death record is never erased.

### Library

A resurrected work that belongs in the Library may visually wander the archive like a zombie. The underlying metadata still carries death and resurrection dates.

## Museum display hierarchy

`museum_scale` determines visual treatment:

- `ceremonial`: major certificates / credentials in oversized formal frames;
- `hearth`: foundational people, images, events, and core identity material at over-the-fireplace scale;
- `normal`: ordinary important exhibits;
- `not-applicable`: item is not a Museum display.

## External media and distribution

The Library is the canonical catalog even when the actual media is hosted elsewhere.

One artifact can have multiple platform destinations, such as:

- YouTube;
- Spotify;
- Patreon;
- Google Play;
- Apple App Store;
- alternate software storefronts;
- direct distribution;
- future platforms.

Alternative distribution does not require open-source licensing. Licensing, payment, and platform rules are handled per artifact when that product exists.

## Curio Shop

### Main floor

Cryptid-made products only.

### Apothecary

Digital knowledge / instructions are the default product. Free shelf cards can provide synopsis, meaning, context, and partial materials. Paid full products can contain the full guide and sourcing information.

### Yard sale

Affiliate items remain visually and semantically distinct from Cryptid-made goods. The affiliate disclosure appears before the visitor begins browsing the yard-sale tables.

## Restricted content

The Forbidden Library contains the mature collection architecture.

No explicit/adult material should be loaded until real age assurance and direct-access protection are implemented. Public surfaces should not leak explicit previews.

Restricted material can be sexual or nonsexual. Erotica is one shelf, not the definition of the whole Forbidden Library.

## Cultural material

- Keep Cherokee and Blackfoot material distinct.
- Verify writing, language, and symbols before publishing.
- Do not fabricate pseudo-Indigenous glyphs.
- Dreamcatcher use is treated as a personal-practice detail and is not mislabeled as Cherokee or Blackfoot.
- Elder Futhark uses sound-based transliteration with readable translation beneath it.
- Norse belief material is separated from modern extremist/political branding.
