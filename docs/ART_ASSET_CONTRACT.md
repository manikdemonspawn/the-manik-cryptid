# Final Visual Asset Contract

This document defines how approved visual targets plug into the construction build without changing realm architecture.

## Rule

Code and interaction structure come first. Approved visual targets come afterward and become both implementation references and lore-bearing artifacts.

## Nexus master image

- Purpose: one large environmental image representing the full Fairy Forest Nexus.
- Must show the eight primary realm thresholds in a coherent impossible landscape:
  - Library / decontamination entrance;
  - Museum / Stonehenge;
  - Krypt / coffin or sarcophagus threshold, protected vault, guarded memory, and afterlife-thread language;
  - Guildhall / castle door;
  - Morgue / clinical doors and gurney language;
  - Kurio Shop / round storybook storefront;
  - Forge / construction threshold, details deferred;
  - Apothecary / upstairs room inside the Kurio Shop, visibly under construction.
- The Katakombs / cellar-door legalese infrastructure portal sits at the bottom of the Nexus and may be represented as a separate descent, not as a ninth primary realm.
- No active Mausoleum while the creator is alive.
- Must leave visual breathing room around portal areas so accessible HTML hotspots can sit over the image.
- Cultural-influence zones remain visually distinct. Do not fabricate Cherokee or Blackfoot writing or symbols.
- Norse writing must not be fabricated. Verified Elder Futhark transliterations can be added later as separate text layers.
- Avoid embedded labels in the master art whenever possible. HTML provides accessible names.

Recommended working shape: wide landscape, minimum 16:9. Preserve a higher-resolution master for future crops.

Expected path after approval:
`assets/images/nexus/nexus-master.*`

## Realm master images

Each realm gets at least one Kanonikal environment view showing what a visitor should plausibly see after crossing its threshold.

Expected paths:
- `assets/images/realms/museum/museum-master.*`
- `assets/images/realms/library/library-master.*`
- `assets/images/realms/forbidden-library/forbidden-library-master.*`
- `assets/images/realms/morgue/morgue-master.*`
- `assets/images/realms/krypt/krypt-master.*`
- `assets/images/realms/guildhall/guildhall-master.*`
- `assets/images/realms/kurio-shop/kurio-shop-master.*`
- `assets/images/realms/forge/forge-master.*`
- `assets/images/realms/apothecary/apothecary-master.*`
- `assets/images/realms/yard-sale/yard-sale-master.*`
- `assets/images/realms/katakombs/katakombs-master.*`

The posthumous Mausoleum gets no active site master until activation is appropriate. Concept/lore art may be archived separately if explicitly approved.

## Portal crops

The full Nexus image may later need cropped portal assets for responsive layouts and loading performance. Portal crops do not replace the Kanonikal Nexus master.

Expected paths:
`assets/images/portals/<realm-id>.*`

## Approved visuals become lore

When the creator approves a visual target, preserve it. Later visual revisions do not silently erase earlier approved depictions. Earlier versions can become maps, archival renderings, development-era depictions, museum artifacts, or other lore-bearing records.

## Accessibility

- Meaningful environmental images receive concise alt text in HTML.
- Decorative crops use empty alt text.
- Do not rely on text baked into images for navigation or warnings.
- Realm links remain real HTML links even when laid over artwork.
- Reduced-motion users must be able to navigate without animations.

## Optimization

Keep high-resolution masters outside the performance-critical path when needed. Production copies can be resized/compressed while Kanonikal masters are retained separately.
