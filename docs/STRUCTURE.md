# Construction Structure

```text
/
├── index.html                           # Nexus / active realm thresholds
├── 404.html                             # in-world lost-path page
├── assets/
│   ├── css/
│   │   ├── site.css                    # phase 1 shared + realm skeleton
│   │   └── phase2.css                  # expanded layouts / visual-target hooks
│   └── js/site.js                      # decon, bookcase, gate, generic interactions
├── data/
│   ├── realm-manifest.json             # machine-readable realm map
│   └── artifact-schema.json            # reusable artifact metadata model
├── realms/
│   ├── museum/index.html
│   ├── library/
│   │   ├── index.html                  # decontamination threshold
│   │   ├── archive/index.html          # Vatican-scale main Library realm
│   │   └── forbidden/index.html        # adult gate skeleton, no restricted content
│   ├── morgue/index.html
│   ├── crypt/index.html
│   ├── guild-hall/index.html
│   ├── curio-shop/
│   │   ├── index.html
│   │   ├── apothecary/index.html
│   │   └── yard-sale/index.html
│   └── catacombs/index.html
├── templates/
│   ├── library-artifact.html
│   ├── museum-exhibit.html
│   ├── morgue-record.html
│   ├── curio-product.html
│   └── affiliate-find.html
└── docs/
    ├── CANON.md
    ├── STRUCTURE.md
    ├── CONTENT_MODEL.md
    ├── VISUAL_TARGET_BRIEF.md
    └── LAUNCH_CHECKLIST.md
```

## Branch strategy

- `main`: public source intentionally has no site HTML while construction is underway.
- `construction`: active build branch.

Do not republish/merge the construction site to the public branch until the creator explicitly approves launch or preview publication.

## Architecture principles

1. Realms are top-level experiential spaces, not ordinary website sections.
2. Each realm has a symbolic threshold plus a readable/accessible link.
3. Shared infrastructure stays reusable; realm identity lives in body classes, realm styling, content hierarchy, and final art.
4. Artifacts receive metadata and cross-references instead of duplicate copies wherever possible.
5. Final visual targets replace CSS construction set-pieces without requiring a new information architecture.
6. Media-heavy artifacts can live on external platforms while the Library remains the canonical catalog.
7. The Forbidden Library remains content-empty until real age assurance and direct-resource protection exist.
8. The future Mausoleum remains non-navigable and posthumous-only.

## Current practical ceiling before generated visual targets

The code can define:

- realm hierarchy;
- portal locations and semantics;
- transitions and interactions;
- page layouts;
- artifact metadata;
- exhibit scales;
- platform gateway slots;
- resurrection/death records;
- accessibility/navigation fallbacks;
- responsive behavior;
- visual placeholder geometry.

Generated visual targets are needed to settle final environmental composition, architecture, object placement, texture, lighting, portal artwork, and realm-specific aesthetic details.
