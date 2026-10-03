# Successor Record — Protected Administrative Document

**Kanon source:** Blueprint §§16.8–16.10 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

> **PROTECTED DOCUMENT.** This record describes the structure of
> successor/legacy administration. It contains pointers to where
> operational information lives — never the secrets themselves.
> The filled-in successor record is PROTECTED material (§16.3):
> access-controlled, never public.

---

## 1. Purpose

If the Kreator can no longer maintain the site, an authorized successor
must be able to keep the Universe intact without guessing. This document
defines what that successor record must contain and where each piece lives.

**Objective (§16.11):** not merely "keep the website online" — **KEEP THE
UNIVERSE INTACT**: relationships, dates, family trees, versions, deaths,
burials, resurrections, Realms, visual history, archives, Museum exhibits,
Library records, posthumous material.

---

## 2. Successor record structure (§16.9)

The protected successor record must eventually explain:

| Item | Location / Status |
|------|-------------------|
| Hosting information | Cloudflare Pages project `the-manik-cryptid` — access via credential vault (see §3) |
| Domain information | PENDING KREATOR APPROVAL (no custom domain attached yet) |
| Backup instructions | `docs/BACKUP_AND_RECOVERY.md` in this repo |
| Archive structure | Blueprint transfer accumulator + `data/` JSON records + Library/Museum structure |
| Maintenance instructions | This repo's docs (`STRUCTURE.md`, `BUILD_STATUS.md`, deployment sequence in `BACKUP_AND_RECOVERY.md`) |
| Credential location | Pointer only: the Kreator's secure secret store — see `docs/CREDENTIAL_VAULT_ARCHITECTURE.md`. **Values never written here.** |
| Recovery instructions | `docs/BACKUP_AND_RECOVERY.md` §2 |
| Posthumous activation rules | §4 below — currently DORMANT |
| Kanon rules | Master lock: DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL; change log in `docs/KANON_CHANGE_LOG.md` |
| Prohibited changes | Never silently retcon (§19.6); never expose private material for immersion (§16.18); never treat hidden links as security (§15.2) |
| Contact / authority information | PENDING KREATOR APPROVAL |

---

## 3. Credential location (pointer, not secrets)

Operational credentials live in the Kreator's chosen password manager /
secure secret store — **PENDING KREATOR APPROVAL** (she has not named one yet).

- Per-category inventory: `docs/credentials/PLACEHOLDERS.md`
- Architecture: `docs/CREDENTIAL_VAULT_ARCHITECTURE.md`
- Recovery codes are stored **independently** from the website (§15.5).

A successor who needs access follows the vault — this document never
carries the values.

---

## 4. Posthumous activation rules (§16.4–16.6)

**Current status: DORMANT.** The Mausoleum is visibly represented in the
Universe while its posthumous content remains inaccessible. It must not
become an ordinary public memorial page while the Kreator is alive.

Posthumous activation is a high-consequence administrative function. It is
NOT a casual switch — the final architecture must establish:

- **WHO** can activate it — PENDING KREATOR APPROVAL
- **WHAT** evidence / authorization is required — PENDING KREATOR APPROVAL
- **WHAT** exactly becomes accessible — PENDING KREATOR APPROVAL
- **CAN** activation be reversed — PENDING KREATOR APPROVAL
- **WHAT** remains permanently private — PENDING KREATOR APPROVAL

Until those decisions are finalized: **POSTHUMOUS SYSTEM = DORMANT.**

The architecture must still allow the Kreator to *prepare* posthumous
material in advance (letters, instructions, archive indexes, historical
notes, creative explanations, Artifact histories, Realm explanations,
personal context, permissions, legacy material) without making it
publicly accessible before the appropriate time (§16.7).

---

## 5. Legacy Curator role (§16.8)

The architecture permits a future authorized person maintaining the archive:

**LEGACY CURATOR** — PENDING KREATOR APPROVAL (identity, selection, timing).

This role does **NOT** automatically possess unrestricted access.
Permissions must be deliberately defined by the Kreator:

- **WHO** may serve — PENDING KREATOR APPROVAL
- **WHAT** they may access and change — PENDING KREATOR APPROVAL
- **WHEN** their authority begins — PENDING KREATOR APPROVAL
- **HOW** authority is transferred and verified — PENDING KREATOR APPROVAL
- **WHY** (scope of their mandate: preserve, not reinvent) — PENDING KREATOR APPROVAL

---

## 6. "IF I AM GONE" archive (§16.10)

Conceptual requirement (final legal/administrative wording must be
Kreator-approved):

1. DO NOT DESTROY THE ARCHIVE.
2. DO NOT ALTER KANON WITHOUT AUTHORITY.
3. PRESERVE THE ORIGINAL ARTIFACT HISTORY.
4. PRESERVE THE FAMILY TREES.
5. PRESERVE THE SEMMATERRY™.
6. PRESERVE THE MORGUE.
7. PRESERVE THE MAUSOLEUM.
8. PRESERVE THE KREATOR'S APPROVED MATERIAL.
9. FOLLOW THE KREATOR'S SPECIFIED RELEASE RULES.
10. DO NOT TURN THE ARCHIVE INTO SOMETHING IT WAS NEVER INTENDED TO BE.

---

## 7. Data portability & platform independence (§16.12–16.13)

- Important structured data must be exportable: JSON, CSV, database
  backup, media archive, document archive. Critical for posthumous
  preservation.
- **CONTENT ≠ PLATFORM.** If the website platform is replaced, the
  Artifact genealogy and historical records must remain recoverable.
  The structured archive is the source of truth; the front end is a
  presentation of that data (§16.14–16.16).
