# Credential Placeholders — Inventory

**Kanon source:** Blueprint §15.8 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

> This file contains NO real credentials — only placeholders marking
> where each credential belongs once it becomes available.
> **NEVER replace a placeholder with a fake credential that looks real**
> (§15.8). Real secrets go into the Kreator's chosen password manager /
> secure secret store (see `docs/CREDENTIAL_VAULT_ARCHITECTURE.md`),
> never into this repository.

Every entry below is **PENDING KREATOR APPROVAL** until the Kreator
supplies or confirms the real credential in the secure store.

---

| # | Category  | Placeholder | Status |
|---|-----------|-------------|--------|
| 1 | DOMAIN | `[DOMAIN_CREDENTIAL_PENDING]` — registrar login, DNS access, transfer authorization | PENDING KREATOR APPROVAL |
| 2 | HOSTING | `[HOSTING_CREDENTIAL_PENDING]` — Cloudflare account access, Pages project deployment | PENDING KREATOR APPROVAL |
| 3 | WEBSITE | `[WEBSITE_CREDENTIAL_PENDING]` — site admin accounts, management access | PENDING KREATOR APPROVAL |
| 4 | DATABASE | `[DATABASE_CREDENTIAL_PENDING]` — host, user, password, keys (no database exists yet) | PENDING KREATOR APPROVAL |
| 5 | STORAGE | `[STORAGE_CREDENTIAL_PENDING]` — media storage, backup storage, asset repository | PENDING KREATOR APPROVAL |
| 6 | EMAIL | `[EMAIL_CREDENTIAL_PENDING]` — domain email, transactional email, administrator email | PENDING KREATOR APPROVAL |
| 7 | APIs | `[API_KEY_PENDING]` — API keys, OAuth credentials, webhooks, service integrations | PENDING KREATOR APPROVAL |
| 8 | COMMERCE | `[COMMERCE_CREDENTIAL_PENDING]` — payment provider, affiliate systems, store systems | PENDING KREATOR APPROVAL |
| 9 | ANALYTICS | `[ANALYTICS_CREDENTIAL_PENDING]` — analytics property, tracking IDs, access | PENDING KREATOR APPROVAL |
| 10 | RECOVERY | `[RECOVERY_CODES_PENDING]` — backup credentials, recovery codes, emergency access. Stored INDEPENDENTLY from the website (§15.5) — never as the sole copy inside site storage | PENDING KREATOR APPROVAL |

---

## Rules for this file

1. Placeholders are inventory markers, not secrets. They are safe to
   commit because they contain no credential material.
2. When the Kreator provisions a real credential, the real value goes
   into the secure secret store — this file's entry is then marked
   `PROVISIONED IN SECURE STORE` (the value itself is never written here).
3. If a category turns out not to apply (e.g. no database is ever
   created), its entry is marked `NOT APPLICABLE` with date and reason —
   never deleted, per the archive principle (OLD ≠ DELETED).
