# Backup and Recovery

**Kanon source:** Blueprint §§15.17–15.20 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

---

## 1. What gets backed up (§15.17)

Independent backups must cover:

- [ ] git repository (code + committed content) — currently GitHub `manikdemonspawn/the-manik-cryptid`
- [ ] structured records — `data/*.json` (Realm manifest, future Artifact/Library/Museum records)
- [ ] images — `assets/images/**`
- [ ] documents — `docs/**` and content documents
- [ ] configuration — build/deploy config (Cloudflare Pages settings, `_headers`, `_redirects`, etc.)
- [ ] approved content — all Kreator-approved public material
- [ ] relevant code — CSS/JS/templates

**Credentials are NOT dumped into ordinary site backups** (§15.17).
Secrets and recovery material use separate encrypted secret/recovery
mechanisms (see `docs/CREDENTIAL_VAULT_ARCHITECTURE.md`).

### Backup destinations — PENDING KREATOR APPROVAL

Actual backup destinations (where the copies live) are not yet chosen.
Candidates must be independent of the live site: if Cloudflare Pages
is the host, backups must not live only on Cloudflare Pages.

- [ ] Primary backup destination — PENDING KREATOR APPROVAL
- [ ] Secondary / off-site copy — PENDING KREATOR APPROVAL
- [ ] Backup schedule / retention — PENDING KREATOR APPROVAL

---

## 2. Restore procedure (§15.18)

A backup is not proven useful merely because it exists. The build must
eventually include a recovery test confirming the system can actually
restore:

```
SITE + STRUCTURED ARCHIVE + MEDIA + CONFIG
```

**Restore outline:**

1. **Verify** — confirm which backup snapshot to restore (date, commit hash).
2. **Stage** — restore to a non-production environment first (never
   restore untested snapshots directly over production).
3. **Check** — run the construction audit (`python3 scripts/site_audit.py`);
   confirm pages render, JSON parses, links resolve, noindex intact on
   construction builds.
4. **Secrets** — re-inject private config from the secure secret store
   (never from the site backup itself).
5. **Deploy** — follow the deployment safety sequence (§4 below).
6. **Record** — log the restore in the Kanon change log if any Kanon
   state was affected.

**Recovery test status:** NOT YET PERFORMED — scheduled as launch work
(blueprint §20.1, §21.8). Do not claim backups are verified until a
real restore test passes.

---

## 3. Version control (§15.19)

- Website code uses git; meaningful changes are committed in logical
  chunks so any experimental change can be reverted without destroying
  the only working version.
- Kanon data has historical preservation via `docs/KANON_CHANGE_LOG.md`
  and the blueprint transfer accumulator
  (`~/workspace/gremmy-blueprint/BLUEPRINT-TRANSFERS.md`, outside this repo).
- Working branch: `construction`. Production branch: `main`.
  Never commit experimental work directly to `main`.

---

## 4. Deployment safety sequence (§15.20)

Before deploying a major change:

```
DEVELOPMENT
↓
TEST            (audit: python3 scripts/site_audit.py)
↓
REVIEW          (Kreator review for Kanon-affecting changes)
↓
BACKUP          (snapshot current production state)
↓
DEPLOY
↓
VERIFY          (live check: pages load, links work, no secrets exposed)
```

Do not make irreversible production changes casually.

---

## 5. Current posture (2026-10-03)

- Code is version-controlled (git, `construction` branch).
- No automated backup destinations are configured yet — PENDING KREATOR APPROVAL.
- No restore test has been performed — launch-gated.
- Deployment is via Cloudflare Pages automatic builds from the
  `construction` branch (preview) and `main` (production).
