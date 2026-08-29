# Construction Structure

The `construction` branch is the only active build. The public `main` branch remains untouched and unpublished.

```text
/
├── index.html                           # Nexus: eight primary portals + bottom Katakombs portal
├── realm-index.html                      # accessible fallback for the same eight primary realms
├── 404.html                              # in-world lost-path page
├── assets/
│   ├── css/
│   │   ├── site.css                      # shared + realm skeleton styles
│   │   ├── phase2.css                    # expanded layouts / visual-target hooks
│   │   └── stage.css                     # Nexus hotspot positions
│   └── js/site.js                        # decontamination, bookcase, gate, generic interactions
├── data/
│   ├── realm-manifest.json               # Kanonikal machine-readable realm map
│   └── artifact-schema.json              # reusable artifact metadata model
├── realms/
│   ├── library/index.html                # primary realm; contains Forbidden Library
│   ├── library/archive/index.html        # main Library collection space
│   ├── library/forbidden/index.html      # restricted gate skeleton, no adult content
│   ├── museum/index.html                 # primary realm; permanent Sertifikate exhibit
│   ├── krypt/index.html                  # primary realm
│   ├── guildhall/index.html              # primary realm
│   ├── morgue/index.html                 # primary realm
│   ├── kurio-shop/index.html             # primary realm; Apothecary physically upstairs
│   ├── kurio-shop/yard-sale/index.html   # subordinate affiliate space
│   ├── forge/index.html                  # primary realm; UNDER KONSTRUCTION
│   ├── apothecary/index.html             # primary destination; upstairs; UNDER KONSTRUCTION
│   └── katakombs/index.html              # bottom portal; legalese-only infrastructure
├── templates/                            # reusable artifact templates
└── docs/                                 # Kanon, structure, status, launch, and art rules
```

## Navigation topology

The Nexus shows eight primary portals near the top of the page, in Kanon order: Library, Museum, Krypt, Guildhall, Morgue, Kurio Shop, Forge, Apothecary. The Apothecary has a direct top-level destination for accessibility and orientation, while its in-world location remains upstairs inside the Kurio Shop behind a rope marked **UNDER KONSTRUCTION**.

The Katakombs has a real portal entry at the bottom of the Nexus. It is an infrastructure realm for legalese, policies, permissions, administration, and site machinery—not an additional primary creative realm. The accessible Realm Index describes this distinction and does not list Katakombs among the eight primary cards.

The Forbidden Library remains a subrealm inside the Library and is not a Nexus portal. The future Mausoleum remains non-navigable and posthumous-only.

## Branch strategy

- `main`: public source intentionally has no site HTML while construction is underway.
- `construction`: active build branch.

Do not republish or merge the construction site to the public branch until the creator explicitly approves launch or preview publication.

## Architecture principles

1. Primary realms are experiential spaces with symbolic thresholds and readable HTML links.
2. Katakombs is a real bottom-of-Nexus infrastructure portal, not a ninth primary realm.
3. The Forbidden Library stays inside the Library.
4. Shared infrastructure stays reusable; realm identity lives in body classes, styling, hierarchy, and future art.
5. Artifacts receive metadata and cross-references instead of duplicate copies wherever possible.
6. The Forbidden Library remains content-empty until real age assurance and direct-resource protection exist.
7. The future Mausoleum remains non-navigable and posthumous-only.
8. Retired spelling/path stubs may preserve history, but they never appear in active navigation or source-of-truth manifests.

## Current practical ceiling before generated visual targets

The code can define realm hierarchy, portal locations, transitions, layouts, artifact metadata, accessibility fallbacks, responsive behavior, and visual placeholder geometry. Generated visual targets are still needed for final environmental composition, architecture, object placement, texture, lighting, portal artwork, and realm-specific aesthetic details.
