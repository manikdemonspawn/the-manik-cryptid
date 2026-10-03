# Kanon Change Log

**Kanon source:** Blueprint §15.13 (Transfer Block 08).
**Master lock:** DO NOT CHANGE KANON WITHOUT KREATOR APPROVAL.

Every meaningful Kanon change is recorded here with:

- **change_id** — stable identifier
- **date** — when the change was made (ISO 8601)
- **previous_value** — what it was before
- **new_value** — what it became
- **affected_object** — the Realm, Artifact, page, or system touched
- **reason** — why the change was made
- **approved_by** — who approved it
- **notes** — anything else relevant

**Rule (§15.13):** If approval was not obtained, the change is NOT
classified as Kreator-approved Kanon. **Rule (§19.6):** Do not retcon
silently — if the Kreator changes an idea, preserve the historical
record. The Universe is an archive; its evolution is part of its history.

---

## Entries

### KCL-2026-1002-001 — Kurio Shoppe spelling locked

| Field | Value |
|---|---|
| change_id | KCL-2026-1002-001 |
| date | 2026-10-02 |
| previous_value | "Kurio Shop" / "Curio Shop" (mixed display spellings across site and docs) |
| new_value | "KURIO SHOPPE" (locked Kanonikal spelling) |
| affected_object | Site-wide display text, docs, manifest, audit map, construction ribbons |
| reason | Kreator directive: public spelling is Kurio Shoppe |
| approved_by | Kreator (Manik) — direct instruction 2026-10-02 |
| notes | 49 occurrences swept. Technical paths (e.g. `realms/kurio-shop/`) intentionally unchanged — display lock only. Re-locked in blueprint §19.7. |

### KCL-2026-1002-002 — Katakombs portal moved out of Nexus masthead nav

| Field | Value |
|---|---|
| change_id | KCL-2026-1002-002 |
| date | 2026-10-02 |
| previous_value | Katakombs link present in Nexus masthead quicklinks nav |
| new_value | Katakombs entry lives at the bottom entry section only; masthead nav has no Katakombs link |
| affected_object | `index.html` (Nexus) |
| reason | Construction audit rule: bottom Katakombs placement only; masthead link was redundant and violated the audit |
| approved_by | Kreator (Manik) — via audit-fix authorization 2026-10-02 |
| notes | Audit passes with bottom placement. The Katakombs Realm page itself is unchanged. |

### KCL-2026-1003-001 — Kurio Shoppe banner v1 approved

| Field | Value |
|---|---|
| change_id | KCL-2026-1003-001 |
| date | 2026-10-03 |
| previous_value | Banner image text read "CURIO SHOP" |
| new_value | Banner image text reads "KURIO SHOPPE" (v1), wired into Kurio Shoppe page hero |
| affected_object | `assets/images/kurio-shoppe/kurio-shoppe-banner-v1.webp`; `realms/kurio-shop/index.html` hero |
| reason | Kreator identified the spelling on the banner as the photo fix needed; approved the corrected version ("Yup") |
| approved_by | Kreator (Manik) — direct approval 2026-10-03 |
| notes | Original banner preserved (source file in workspace/user/files/ and goal files dir). Per the visual lock: OLD VERSION → ARCHIVE, NEW VERSION → CURRENT. Never deleted. Parent/child artifact lineage per blueprint §9.5. |

---

## Format for future entries

```
### KCL-YYYY-MMDD-NNN — short title

| Field | Value |
|---|---|
| change_id | KCL-YYYY-MMDD-NNN |
| date | YYYY-MM-DD |
| previous_value | ... |
| new_value | ... |
| affected_object | ... |
| reason | ... |
| approved_by | ... (if not Kreator-approved, state so explicitly) |
| notes | ... |
```

Entries are append-only. Corrections to an entry are made as a NEW
entry referencing the old one — never by editing history.
