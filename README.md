# The Manik Cryptid — Resurrection Artifact Universe

## Current state

**Construction branch only. Not approved for public launch.**

The public `main` branch intentionally contains no website HTML while reconstruction is underway. Active website development happens on the `construction` branch.

## What this repository is becoming

This is not a conventional author website. The site is structured as a universe of distinct realms connected by a fairy-forest Nexus. Each realm has its own symbolic threshold, atmosphere, display logic, and future visual identity.

Current top-level realm skeletons, in Kanon order:

1. Library — decontamination chamber, massive archive, hidden Forbidden Library;
2. Museum — Stonehenge threshold;
3. Krypt — coffin/sarcophagus threshold, memory and afterlife threads;
4. Guildhall — castle door, capabilities and worktables;
5. Morgue — clinical doors, gurneys, toe tags, ghost-resurrection logic;
6. Kurio Shop — round storefront door, Manik-made goods, and affiliate Yard Sale out back;
7. Forge — top-level realm, UNDER KONSTRUCTION; purpose/content deliberately deferred;
8. Apothecary — top-level realm, physically upstairs in the Kurio Shop, UNDER KONSTRUCTION.

The Forbidden Library lives inside the Library. The Katakombs are the legalese-only infrastructure realm, entered through a separate portal at the bottom of the Nexus rather than counted among the eight primary realms.

The future Mausoleum is posthumous-only and has no active Nexus portal.

## Construction systems already built

- image-ready Nexus hotspot layer independent of final art;
- accessible plain Realm Index fallback;
- interactive Library decontamination sequence;
- hidden-bookcase / black-door interaction hooks;
- construction-only Forbidden Library gate with no adult content loaded;
- reusable artifact schema and Kanonikal artifact registry;
- reusable artifact-registry renderer for future books, apps, audio, products, museum pieces, Morgue records, and other artifacts;
- content templates for major artifact types;
- final-art CSS hooks so approved images can be integrated without rebuilding markup;
- reduced-motion behavior and keyboard-focus support;
- launch and cultural-verification safeguards.

## Construction references

- `docs/CANON.md` — world and realm rules;
- `docs/STRUCTURE.md` — repository/site structure;
- `docs/CONTENT_MODEL.md` — how artifacts scale without breaking the architecture;
- `docs/BUILD_STATUS.md` — code-first build status and known blockers;
- `docs/VISUAL_TARGET_BRIEF.md` — art-direction requirements after the code ceiling;
- `docs/ART_ASSET_CONTRACT.md` — how approved visual targets plug into the site;
- `docs/LAUNCH_CHECKLIST.md` — gates before anything becomes public;
- `data/realm-manifest.json` — machine-readable realm map;
- `data/artifact-schema.json` — reusable artifact metadata shape;
- `data/artifacts.json` — Kanonikal artifact registry;
- `assets/images/README.md` — visual asset staging and versioning rules;
- `templates/` — construction templates for future content;
- `registry-preview.html` — internal construction test of the artifact renderer;
- `realm-index.html` — non-visual accessible navigation fallback.

## Important locks

- Do not merge to `main` without explicit creator approval.
- Do not load adult/restricted content before real access control exists.
- Do not fabricate Cherokee, Blackfoot, Elder Futhark, or other culturally specific writing.
- Do not expose the posthumous Mausoleum as an active living-site portal.
- Do not treat a genuine outside-issued Credential, a Universe-issued Sertifikate, and an artifact-specific COA as the same document type.
- Approved visual targets become lore-bearing artifacts and are not silently discarded when later versions exist.
