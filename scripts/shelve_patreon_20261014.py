#!/usr/bin/env python3
"""Shelve the 51-post Patreon catalog into data/library.json (2026-10-14).
Harvested from the public Patreon page; titles + URLs only, no post bodies.
Locked (members-only) posts are listed with their links — Patreon gates them.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (title, url, locked)
POSTS = [
    ("Appalachian Gothic: A Mother's Day Miracle | Sarah Elizabeth's View", "https://www.patreon.com/TheManikCryptid/posts/appalachian-day-167601789", False),
    ("Court of Ash and Blood: NSFW Edition Chapter 6: Blood and Roots", "https://www.patreon.com/TheManikCryptid/posts/court-of-ash-and-163405559", True),
    ("Work in progress sneak peak.", "https://www.patreon.com/TheManikCryptid/posts/work-in-progress-162064100", False),
    ("Chapter 5: Descent into Dawn", "https://www.patreon.com/TheManikCryptid/posts/chapter-5-into-161010606", True),
    ("Chapter 4: Shadows and Hunger \u2013 Part 3", "https://www.patreon.com/TheManikCryptid/posts/chapter-4-and-3-159623737", True),
    ("Chapter 4: Shadows and Hunger \u2013 Part 2", "https://www.patreon.com/TheManikCryptid/posts/chapter-4-and-2-159624034", True),
    ("Chapter 4: Shadows and Hunger \u2013 Part 1", "https://www.patreon.com/TheManikCryptid/posts/chapter-4-and-1-159624135", True),
    ("Chapter 3: The Court of Ash and Blood: NSFW Edition", "https://www.patreon.com/TheManikCryptid/posts/chapter-3-court-157973697", True),
    ("Some days", "https://www.patreon.com/TheManikCryptid/posts/some-days-158007387", False),
    ("Chapter 2: The Court of Ash and Blood: NSFW Edition", "https://www.patreon.com/TheManikCryptid/posts/chapter-2-court-157800942", True),
    ("Ch 1: The Court of Ash and Blood (NSFW Edition)", "https://www.patreon.com/TheManikCryptid/posts/ch-1-court-of-157304389", False),
    ("Patterns of Silence / S1 Fadin'", "https://www.patreon.com/TheManikCryptid/posts/fadin-158962838", True),
    ("SCP FOUNDATION/FAE: Chapter 19 \u2014 The Gilded Resonance (SEASON FINALE)", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148461318", False),
    ("SCP FOUNDATION/FAE: CHAPTER 18: THE SINGING ARCHIVE", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148461199", False),
    ("SCP FOUNDATION/ FAE: CHAPTER 17: THE IRON VEIL", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148461073", False),
    ("Court Of Ash & Blood: Book I (teens/YA)", "https://www.patreon.com/TheManikCryptid/posts/court-of-ash-i-148462099", True),
    ("SCP FOUNDATION/ FAE: CHAPTER 16: THE BLOOM REBORN", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148460916", False),
    ("SCP FOUNDATION/ FAE: CHAPTER 15: THE BREACH OF MEMORY", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148460063", False),
    ("SCP FOUNDATION/ FAE: Chapter 14: The Resonant Dead", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-148459499", False),
    ("ROOT//ANE: S1E9 THE DREAMING CIRCUITS (SEASON FINALE)", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e9-147903226", False),
    ("SCP Foundation Meets Fae: CHAPTER 13:", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-147889170", False),
    ("SCP Foundation Meets Fae: CHAPTER 12:", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-147889075", False),
    ("Lost and Broken", "https://www.patreon.com/TheManikCryptid/posts/lost-and-broken-146064758", False),
    ("ROOT//ANE: S1E8", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e8-145763404", False),
    ("The Witch House: Chapter 6", "https://www.patreon.com/TheManikCryptid/posts/witch-house-6-145763064", True),
    ("Resonance Apocalypse", "https://www.patreon.com/TheManikCryptid/posts/resonance-146027431", False),
    ("SCP FOUNDATION/FAE: CHAPTER 11", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-144712652", False),
    ("The Witch House Chapter 5", "https://www.patreon.com/TheManikCryptid/posts/witch-house-5-143215183", True),
    ("SCP FOUNDATION/FAE: CHAPTER 10", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-144712485", False),
    ("ROOT//ANE: S1E7", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e7-143715899", False),
    ("The Witch House Chapter 4", "https://www.patreon.com/TheManikCryptid/posts/witch-house-4-143211554", True),
    ("SCP Foundation/Fae: Chapter 9", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-9-143720449", False),
    ("ROOT//ANE: S1E6", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e6-143713896", False),
    ("The Witch House Chapter 3", "https://www.patreon.com/TheManikCryptid/posts/witch-house-3-142992145", True),
    ("SCP Foundation/Fae CHAPTER 8: THE UNSEEN PREDATOR", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-8-143717431", False),
    ("ROOT//ANE: S1E5", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e5-143711437", False),
    ("The Witch House Chapter 2", "https://www.patreon.com/TheManikCryptid/posts/witch-house-2-142923458", True),
    ("ROOT//ANE: S1E4", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e4-143458342", False),
    ("The Witch House Chapter 1", "https://www.patreon.com/TheManikCryptid/posts/witch-house-1-142921730", True),
    ("ROOT//ANE: S1E3", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e3-141969214", False),
    ("SCP Foundation/Fae : CHAPTER 7", "https://www.patreon.com/TheManikCryptid/posts/scp-foundation-7-142592900", False),
    ("ROOT//ANE: S1E2", "https://www.patreon.com/TheManikCryptid/posts/root-ane-s1e2-141967907", False),
    ("CHAPTER 6: THE UNRAVELING ARGUMENT", "https://www.patreon.com/TheManikCryptid/posts/chapter-6-141550331", False),
    ("S1E1 ROOT//ANE", "https://www.patreon.com/TheManikCryptid/posts/s1e1-root-ane-141810366", False),
    ("Chapter 5: The Heart of the Gilded Forest", "https://www.patreon.com/TheManikCryptid/posts/chapter-5-heart-140867119", False),
    ("The Unexpected Assistant", "https://www.patreon.com/TheManikCryptid/posts/unexpected-141308668", False),
    ("Chapter 4: The Lure of the Bloom", "https://www.patreon.com/TheManikCryptid/posts/chapter-4-lure-141135316", False),
    ("Chapter 3: The Bloom of Unreality", "https://www.patreon.com/TheManikCryptid/posts/chapter-3-bloom-140866801", False),
    ("Chapter 2 : The Echoes of the Gilded Land", "https://www.patreon.com/TheManikCryptid/posts/chapter-2-echoes-140866731", False),
    ("Chapter 1: The Allure of Lyra", "https://www.patreon.com/TheManikCryptid/posts/chapter-1-allure-140866677", False),
    ("\U0001f98f THE CONGREGATION OF SHADOWS AWAITS \U0001f98f", "https://www.patreon.com/TheManikCryptid/posts/congregation-of-140860177", False),
]

AUDIO_TITLES = {"Patterns of Silence / S1 Fadin'"}
def category_for(title):
    if title in AUDIO_TITLES or title.startswith("ROOT//ANE") or title.startswith("S1E1 ROOT"):
        return "audio"
    return "fiction"

def series_for(title):
    t = title.lower()
    if "court of ash" in t: return "Court of Ash and Blood"
    if "scp" in t: return "SCP Foundation Meets the Fae"
    if "witch house" in t: return "The Witch House"
    if "root//ane" in t or title.startswith("S1E1"): return "ROOT//ANE"
    if "mother's day miracle" in t: return "Appalachian Gothic"
    return None

p = os.path.join(ROOT, "data/library.json")
d = json.load(open(p, encoding="utf-8"))
existing_ids = {r["record_id"] for r in d["records"]}
assert "LIB-BOOK-001" in existing_ids, "book record missing!"

new_records = []
for i, (title, url, locked) in enumerate(POSTS, start=1):
    rid = f"LIB-PTRN-{i:03d}"
    series = series_for(title)
    desc = "Patreon post from The Manik Cryptid's Resurrection Artifact Universe."
    if series: desc += f" Part of {series}."
    if locked: desc += " Members-only."
    new_records.append({
        "record_id": rid,
        "title": title,
        "Kanonikal_title": None,
        "category": category_for(title),
        "realm": "library",
        "creator": "The Manik Cryptid",
        "type": "episode" if category_for(title) == "audio" else "post",
        "status": "PUBLISHED",
        "Kanon_status": "KREATOR-APPROVED",
        "archive_status": "NOT_ARCHIVED",
        "creation_date": None,
        "version": None,
        "description": desc,
        "notes": "Members-only post on Patreon; link opens the Patreon post (login/membership required)." if locked else "Public post on Patreon.",
        "source": url,
        "access": "members-only" if locked else "public",
        "media": {"audio_embed": None, "hero_image": None, "thumbnail": None, "video_embed": None},
        "related_artifacts": [],
    })

d["records"] = [r for r in d["records"]] + new_records
d["notes"] = ("Library record schema per blueprint \u00a718.2. Categories are the Kreator's taxonomy (decided 2026-10-03): Fiction, Audio, Apps, Photos, Memes. "
    "Records shelve alphabetically by title within their category. LIB-BOOK-001 is the Amazon book; LIB-PTRN-001..051 are the 51 Patreon posts harvested 2026-10-14 "
    "(36 public, 15 members-only; titles + links only, no post bodies copied). Do not fabricate the Kreator's books or stories; records are added only from real materials.")
json.dump(d, open(p, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"shelved {len(new_records)} Patreon records; total records: {len(d['records'])}")

# Modal link text: Patreon-aware
p = os.path.join(ROOT, "assets/js/library-catalog.js")
js = open(p, encoding="utf-8").read()
old = '''      a.textContent = "Buy on Amazon (affiliate link)";'''
new = '''      if (/patreon\\.com/.test(record.source || "")) {
        a.textContent = record.access === "members-only" ? "View on Patreon (members-only)" : "Read on Patreon";
      } else {
        a.textContent = "Buy on Amazon (affiliate link)";
      }'''
assert old in js
js = js.replace(old, new)
open(p, "w", encoding="utf-8").write(js)
print("catalog js: Patreon-aware link text")
