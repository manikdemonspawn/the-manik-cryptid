# Content Classification — Public / Private / Protected / Posthumous

**Kanon source:** Blueprint §§16.1–16.4, 16.14–16.20 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

The site contains different classes of information. They must not all
have the same visibility.

---

## The four classes

### PUBLIC (§16.1)

May include: approved stories, approved artwork, public Realms, Museum
exhibits, public Library records, public Shoppe material, approved
creator information, public SERTIFIKATES, public Artifact records.

**Only Kreator-approved public material belongs here.**

### PRIVATE (§16.2)

May include: personal documents, private drafts, restricted artwork,
private photographs, unpublished work, sensitive archive material,
credentials / credential references, administrative material.

**Private ≠ "hidden link."** Private means access-controlled at the
data/resource layer. If a private file exists at a predictable public
URL, it may still be accessible — authorization is required, not obscurity.

### PROTECTED (§16.3)

Material requiring stronger access controls. Potential examples:
Krypt records, sensitive archive material, posthumous instructions,
successor instructions, credential/recovery references, legally
sensitive records, deeply personal material.

Exact contents remain Kreator-controlled.

### POSTHUMOUS (§16.4)

Intended for release/access after the Kreator's death according to
rules established by the Kreator. Requires an explicit activation
mechanism — not a casual switch. Until activation rules are finalized:
**DORMANT** (see `docs/SUCCESSOR.md` §4).

---

## Rules

- **Creative secrets ≠ security secrets (§16.19).** A creative secret
  ("something exists here, but visitors haven't discovered it") is not
  a security mechanism ("only authorized users may access this").
  Never solve a security requirement with creative secrecy.
- **Security vs. storytelling (§16.17).** The Krypt, secure vault,
  sealed archive, and restricted collection can be story skin — the
  technical implementation must be real. Skin vs. skeleton.
- **Private data is never decorative lore (§16.18).** Passwords, API
  keys, private addresses, recovery codes, authentication tokens,
  private financial/medical/legal information are NEVER exposed for
  immersion.
- **Public presentation is not the source of truth (§16.14–16.16).**
  Conceptually two layers: PUBLIC EXPERIENCE (approved material) and
  MASTER ARCHIVE (deeper source/history). The structured archive is the
  source of truth; the front end presents it.

---

## Current posture (2026-10-03)

This is a **static public site** (HTML/CSS/JS + JSON on Cloudflare
Pages). There is no backend, no auth layer, no private storage.

**Therefore: everything in this repository is PUBLIC by construction.**

This classification document is the architecture for when protected
material exists. Until access-controlled storage exists:

- Do not commit private, protected, or posthumous material to this repo.
- Do not "protect" material by unlinking it — unlinked public files are
  still public (§15.15).
- Protected media rule (§15.16): when protected media exists, the
  underlying file must be protected — not just the page displaying it.
