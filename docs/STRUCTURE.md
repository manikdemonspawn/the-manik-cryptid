# Construction Structure

```text
/
├── index.html                         # Nexus / realm thresholds
├── assets/
│   ├── css/site.css                  # shared + realm visual skeleton
│   └── js/site.js                    # interaction hooks
├── realms/
│   ├── museum/index.html
│   ├── library/
│   │   ├── index.html                # decontamination threshold
│   │   ├── archive/index.html        # main Library realm
│   │   └── forbidden/index.html      # adult gate skeleton, no restricted content
│   ├── morgue/index.html
│   ├── crypt/index.html
│   ├── guild-hall/index.html
│   ├── curio-shop/
│   │   ├── index.html
│   │   ├── apothecary/index.html
│   │   └── yard-sale/index.html
│   └── catacombs/index.html
└── docs/
    ├── CANON.md
    └── STRUCTURE.md
```

## Branch strategy

- `main`: public source intentionally has no site HTML while construction is underway.
- `construction`: active build branch.

Do not republish/merge the construction site to the public branch until the creator explicitly approves launch or preview publication.

## Future hooks

- final portal artwork can replace CSS-built placeholders;
- realm-specific font packages can be added later;
- Library collection pages can scale independently;
- app/audio exhibits can point to outside platforms;
- real age verification can replace the construction-only gate hook;
- Morgue metadata can eventually move into JSON/data files for sorting;
- posthumous Mausoleum stays unexposed until activation is explicitly appropriate.
