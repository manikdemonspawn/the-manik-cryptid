# Credential Vault Architecture — The Manik Cryptid

**Kanon source:** Blueprint §§15.1–15.11 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

This document specifies WHERE credentials live, HOW they are classified,
and WHAT the rules are. It contains NO credentials — only their architecture.

> **Critical Kreator requirement (§15):** The Kreator may not currently
> have access to the credentials. Nothing in this architecture requires
> her to produce them again merely to continue architectural work.
> This document preserves a clear location for credentials to be
> securely stored once they become available.

---

## 1. The Krypt → Secure Vault concept (§15.3)

The Kreator asked: *"Lock the credentials in a hidden yet accessible folder."*

Implementation interpretation:

```
KRYPT                      ← Universe concept (protected/guarded location)
└── SECURE VAULT           ← administrative concept (protected area)
    ├── WEBSITE ADMIN
    ├── HOSTING
    ├── DOMAIN
    ├── DATABASE
    ├── EMAIL
    ├── API KEYS
    ├── STORAGE
    ├── ANALYTICS
    ├── PAYMENT / COMMERCE
    └── RECOVERY
```

- The **visual structure** may resemble a hidden archive (storytelling skin).
- The **actual secrets** must live in a secure credential-management
  system (security skeleton). Skin vs. skeleton — never confuse them (§16.17).

### HIDDEN ≠ SECURE (§15.2)

A folder named `SECRET`, `PRIVATE`, `DO NOT OPEN`, `KRYPT`, or
`CREDENTIALS` provides **zero security by itself**. Real storage requires:

- authentication
- authorization
- encryption where appropriate
- access restrictions
- backup / recovery
- auditability where available

---

## 2. Credential categories (§15.4)

| Category   | Covers |
|------------|--------|
| DOMAIN     | domain registrar, DNS, domain transfer authorization |
| HOSTING    | hosting provider, deployment credentials, server access |
| WEBSITE    | CMS/admin, administrator accounts, site management |
| DATABASE   | database host, user, password, keys |
| STORAGE    | media storage, backup storage, asset repository |
| EMAIL      | domain email, transactional email, administrator email |
| APIs       | API keys, OAuth credentials, webhooks, service integrations |
| COMMERCE   | payment provider, affiliate systems, store systems |
| ANALYTICS  | analytics property, tracking IDs, access credentials |
| RECOVERY   | backup credentials, recovery codes, emergency access |

Per-category placeholder inventory: `docs/credentials/PLACEHOLDERS.md`.

---

## 3. Where secrets actually live (§15.6)

**Preferred architecture:**

```
PASSWORD MANAGER / SECURE SECRET STORE
↓
Website / service credentials
```

**Forbidden architecture:**

```
Website
↓
Plaintext credential file
```

The Kreator's chosen password manager / secret store is
**PENDING KREATOR APPROVAL**. Until she names one, secrets are not
collected anywhere — only placeholders exist.

### Rules

- **§15.1 — NEVER in public content.** No passwords, API keys, access
  tokens, database credentials, private keys, session secrets, webhook
  secrets, or admin credentials in: public webpages, source files in
  this public repository, CSS, JavaScript, HTML, public JSON, public
  images, downloadable PDFs, public Library records, browser-visible
  configuration, client-side environment variables, screenshots, or
  public documentation.
- **§15.5 — Recovery codes** must NOT be stored inside the website
  itself as the sole recovery mechanism. Maintain independent recovery
  storage. If the site is compromised, the attacker must not obtain
  the recovery information.
- **§15.8 — Placeholders, never fakes.** Until credentials are
  available, use clearly-marked placeholders such as
  `[DOMAIN_CREDENTIAL_PENDING]`. NEVER insert fake credentials that
  resemble real ones — this prevents accidental deployment of
  placeholder secrets.
- **§16.18 — Private data is NEVER decorative lore.** Passwords, API
  keys, private addresses, recovery codes, authentication tokens,
  private financial/medical/legal information must never be exposed
  merely because it makes the experience more immersive.

---

## 4. Public config vs. private config (§15.7)

If the technical stack supports environment variables, secrets are
injected through the deployment environment:

- **PUBLIC CONFIG** = safe, browser-visible settings
  (e.g. site name, public URLs, feature flags).
- **PRIVATE CONFIG** = server-side environment secrets
  (e.g. API keys, tokens, database passwords).

**Never** place private secrets into variables that get bundled into
client-side JavaScript. The current build is a fully static site
(Cloudflare Pages); there is no server-side runtime, so private config
does not exist yet — this separation is specified now so a future
dynamic layer inherits it.

---

## 5. Access tiers (§15.9)

| Tier | Scope |
|------|-------|
| Visitor | PUBLIC — public site content only |
| Editor | CONTENT MANAGEMENT — draft/publish content, no Kanon authority |
| KREATOR | FULL KANON AUTHORITY — Kanon, Realm relationships, Artifact identity/genealogy, public/private status, posthumous rules, visual identity, final approval |
| Admin / Technical | TECHNICAL MAINTENANCE — deployment, backups, infrastructure; no Kanon authority |
| Protected / Posthumous | SPECIAL ACCESS — posthumous and sealed material under Kreator-defined rules |

Exact role names may change during implementation. The underlying
separation must remain.

### Kreator authority (§15.10)

The Kreator has final authority over: Kanon, Realm relationships,
Artifact identity, Artifact genealogy, public/private status,
posthumous rules, visual identity, final approval.

Demon may recommend technical solutions. Demon must not silently
change Kanon. **Master rule: DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.**

---

## 6. Admin interface (§15.11) — future scope

The current site is static; there is no admin interface. When one
exists, it must eventually allow authorized users to manage: Realms,
Artifacts, Library records, Museum exhibits, SERTIFIKATES, family
relationships, lifecycle status, images, documents, archive records,
Shoppe items, Yard Sale items, and access permissions.

It must **NOT** expose credentials unnecessarily. Admin design is
**PENDING KREATOR APPROVAL**.

---

## 7. Audit history (§15.12)

Where technically feasible, record important changes:

- Artifact created / edited
- Kanon status changed
- Realm relationship changed
- Artifact buried / resurrected
- Museum exhibit published
- Protected record accessed
- Posthumous status changed

The purpose is historical accountability. Kanon changes specifically
are recorded in `docs/KANON_CHANGE_LOG.md`.

---

## 8. Draft vs. published (§15.14)

Content must support at least **DRAFT** and **PUBLISHED**, with
potential additional states: PENDING APPROVAL, ARCHIVED, RETIRED,
PRIVATE, POSTHUMOUS.

Core principle: **not everything created in the admin system is
automatically public.** (Applies when an admin/content system exists;
the current static build publishes only what is committed.)

---

## 9. Private content and protected media (§15.15–15.16)

- **Private ≠ "hidden link."** If a private file exists at a
  predictable public URL, it may still be accessible. Private files
  require authorization **at the data/resource layer** — never rely on
  "the page isn't linked."
- **Protected media:** photographs, documents, and media that are
  protected must not sit in a public asset directory merely because
  the page displaying them is private. The underlying file must also
  be protected.

Current state: the construction build contains no private or protected
material — everything in this repository is public by construction.
These rules govern future protected material.

---

## 10. Pending Kreator decisions (this document)

- [ ] Chosen password manager / secure secret store — PENDING KREATOR APPROVAL
- [ ] Actual backup destinations — PENDING KREATOR APPROVAL
- [ ] Admin interface design and role names — PENDING KREATOR APPROVAL
- [ ] Posthumous activation mechanism (WHO/WHAT/HOW) — PENDING KREATOR APPROVAL
- [ ] Legacy Curator identity and permissions — PENDING KREATOR APPROVAL
