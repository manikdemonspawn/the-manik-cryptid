# Content Model

The Manik Cryptid’s Resurrection Artifact Universe should grow by adding artifacts to established realms, not by inventing a new top-level realm every time a new project appears. The eight primary realms are Library, Museum, Krypt, Guildhall, Morgue, Kurio Shop, Forge, and Apothecary. The Katakombs is infrastructure, reached through the bottom Nexus portal.

## Artifact identity

Every meaningful item should eventually have:

- unique ID / slug;
- title;
- Kanonikal realm;
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

### Krypt

The Krypt is the protected vault of memory, guarded truth, honored dead, afterlife belief threads, and restricted/offline-only records.

Krypt entries may be public summaries, protected indexes, or offline-only references. The public site should never expose sensitive underlying material simply because a Krypt record exists.

## Museum display hierarchy

`museum_scale` determines visual treatment:

- `ceremonial`: major certificates / credentials in oversized formal frames;
- `hearth`: foundational people, images, events, and core identity material at over-the-fireplace scale;
- `normal`: ordinary important exhibits;
- `not-applicable`: item is not a Museum display.

## External media and distribution

The Library is the Kanonikal catalog even when the actual media is hosted elsewhere.

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

## Kurio Shop

### Main floor

Cryptid-made products only.

### Apothecary

The Apothecary is physically upstairs inside the Kurio Shop, behind a rope at the bottom of the stairs marked **UNDER KONSTRUCTION**. Its final purpose, products, and content are deliberately deferred; do not infer a product model from the placeholder.

### Yard sale

Affiliate items remain visually and semantically distinct from Manik-made goods. The affiliate disclosure appears before the visitor begins browsing the yard-sale tables.

## Document classes

- **Credential:** a genuine outside-issued credential.
- **Sertifikate:** a Universe-issued ceremonial, comedic, lore, or internal document.
- **COA:** a Certificate of Authenticity tied to one specific artifact.

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
