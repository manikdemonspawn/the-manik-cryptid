(() => {
  "use strict";

  const script = document.currentScript;
  if (!script) return;

  const dataUrl = new URL("../../data/library.json", script.src);

  const searchInput = document.querySelector("[data-catalog-search]");
  const shelvesEl = document.querySelector("[data-catalog-shelves]");
  const statusEl = document.querySelector("[data-catalog-status]");
  if (!shelvesEl) return;

  const PER_ROW = 8;

  // Object shape per category; unknown future categories fall back to books.
  const SHAPES = {
    fiction: "book",
    audio: "disc",
    apps: "app",
    photos: "photo",
    memes: "meme"
  };
  const shapeFor = categoryId => SHAPES[categoryId] || "book";

  const make = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  };

  // Deterministic per-record variation so shelves look hand-filled and stable.
  const hash = value => {
    const str = String(value || "");
    let h = 0;
    for (let i = 0; i < str.length; i += 1) h = (h * 31 + str.charCodeAt(i)) | 0;
    return Math.abs(h);
  };

  const BOOK_HUES = ["#5a3f28", "#6b2737", "#2f4a38", "#2a3a5c", "#4a2c4f", "#41362a"];
  const BOOK_HEIGHTS = [150, 165, 175, 190, 205];
  const BOOK_WIDTHS = [30, 34, 38, 44];

  // Library shelving order: alphabetical by title, ignoring leading articles.
  const sortKey = title =>
    String(title || "")
      .replace(/^(the|a|an)\s+/i, "")
      .toLocaleLowerCase();

  const recordMatches = (record, categoryName, query) => {
    const q = query.toLocaleLowerCase();
    return [record.title, record.Kanonikal_title, record.creator, categoryName, record.description]
      .some(value => typeof value === "string" && value.toLocaleLowerCase().includes(q));
  };

  // ---- Object builders: one visual per category shape.
  // Each returns its top-level element; renderShelves tags it with the record id.

  const buildBook = record => {
    const h = hash(record.record_id);
    // Fiction shelves hold books and scrolls; the mix is stable per record.
    if (h % 4 === 3) return buildScroll(record, h);
    const btn = make("button", "shelf-object obj-book");
    btn.type = "button";
    btn.style.setProperty("--obj-h", `${BOOK_HEIGHTS[h % BOOK_HEIGHTS.length]}px`);
    btn.style.setProperty("--obj-w", `${BOOK_WIDTHS[h % BOOK_WIDTHS.length]}px`);
    btn.style.setProperty("--obj-bg", BOOK_HUES[h % BOOK_HUES.length]);
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-spine-title", record.title || "Untitled"));
    return btn;
  };

  const buildScroll = (record, h) => {
    const btn = make("button", "shelf-object obj-scroll");
    btn.type = "button";
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-scroll-ribbon", ""));
    return withCaption(btn, record);
  };

  const withCaption = (btn, record) => {
    const wrap = make("span", "obj-with-caption");
    wrap.appendChild(btn);
    wrap.appendChild(make("span", "obj-caption", record.title || "Untitled"));
    return wrap;
  };

  const buildDisc = record => {
    const h = hash(record.record_id);
    // Audio shelves hold CDs and vinyl records; the mix is stable per record.
    if (h % 3 === 2) return buildVinyl(record, h);
    const btn = make("button", "shelf-object obj-disc");
    btn.type = "button";
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-disc-hole", ""));
    return withCaption(btn, record);
  };

  const buildVinyl = (record, h) => {
    const btn = make("button", "shelf-object obj-vinyl");
    btn.type = "button";
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    const label = make("span", "obj-vinyl-label", "");
    label.style.setProperty("--obj-bg", BOOK_HUES[h % BOOK_HUES.length]);
    btn.appendChild(label);
    btn.appendChild(make("span", "obj-disc-hole", ""));
    return withCaption(btn, record);
  };

  const buildApp = record => {
    // Apps sit on the shelf as floppy disks — software you can hold.
    const btn = make("button", "shelf-object obj-floppy");
    btn.type = "button";
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-floppy-shutter", ""));
    btn.appendChild(make("span", "obj-floppy-label", ""));
    return withCaption(btn, record);
  };

  const buildPhoto = record => {
    const h = hash(record.record_id);
    const btn = make("button", "shelf-object obj-photo");
    btn.type = "button";
    btn.style.setProperty("--obj-w", h % 2 === 0 ? "96px" : "72px");
    btn.style.setProperty("--obj-h", h % 2 === 0 ? "72px" : "96px");
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-photo-print", ""));
    return withCaption(btn, record);
  };

  const buildMeme = record => {
    const h = hash(record.record_id);
    const btn = make("button", "shelf-object obj-meme");
    btn.type = "button";
    btn.style.setProperty("--obj-tilt", `${(h % 5) - 2}deg`);
    btn.setAttribute("aria-label", `Open record: ${record.title || "Untitled record"}`);
    btn.appendChild(make("span", "obj-meme-text", String(record.title || "Untitled").slice(0, 24)));
    return btn;
  };

  const BUILDERS = { book: buildBook, disc: buildDisc, app: buildApp, photo: buildPhoto, meme: buildMeme };

  // ---- Record detail modal ----

  const modal = make("div", "catalog-modal");
  modal.setAttribute("hidden", "");
  modal.setAttribute("role", "dialog");
  modal.setAttribute("aria-modal", "true");
  modal.setAttribute("aria-label", "Artifact record");
  const modalCard = make("div", "catalog-modal-card");
  const modalClose = make("button", "catalog-modal-close", "×");
  modalClose.type = "button";
  modalClose.setAttribute("aria-label", "Close record");
  const modalBody = make("div", "catalog-modal-body");
  modalCard.appendChild(modalClose);
  modalCard.appendChild(modalBody);
  modal.appendChild(modalCard);
  document.body.appendChild(modal);

  let lastFocus = null;
  const closeModal = () => {
    modal.setAttribute("hidden", "");
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  };
  modalClose.addEventListener("click", closeModal);
  modal.addEventListener("click", event => {
    if (event.target === modal) closeModal();
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && !modal.hasAttribute("hidden")) closeModal();
  });

  const fieldRow = (label, value) => {
    if (value == null || value === "") return null;
    const row = make("p", "catalog-modal-field");
    row.appendChild(make("strong", "", `${label}: `));
    row.appendChild(document.createTextNode(String(value)));
    return row;
  };

  const openRecord = (record, categoryName) => {
    lastFocus = document.activeElement;
    modalBody.replaceChildren();
    modalBody.appendChild(make("h3", "catalog-modal-title", record.title || "Untitled record"));
    const coverSrc = record.media && (record.media.hero_image || record.media.thumbnail);
    if (coverSrc) {
      const coverImg = document.createElement("img");
      coverImg.src = coverSrc;
      coverImg.alt = "Cover art: " + (record.title || "artifact");
      coverImg.className = "catalog-modal-cover";
      modalBody.appendChild(coverImg);
    }
    const rows = [
      fieldRow("Category", categoryName),
      fieldRow("Kanonikal title", record.Kanonikal_title),
      fieldRow("Creator", record.creator),
      fieldRow("Kanon status", record.Kanon_status),
      fieldRow("Status", record.status),
      fieldRow("Created", record.creation_date),
      fieldRow("Version", record.version),
      fieldRow("Description", record.description),
      fieldRow("Notes", record.notes)
    ];
    for (const row of rows) if (row) modalBody.appendChild(row);
    if (record.source) {
      const srcRow = make("p", "catalog-modal-field");
      srcRow.appendChild(make("strong", "", "Get it: "));
      const a = document.createElement("a");
      a.href = record.source;
      if (/patreon\.com/.test(record.source || "")) {
        a.textContent = record.access === "members-only" ? "View on Patreon (members-only)" : "Read on Patreon";
      } else {
        a.textContent = "Buy on Amazon (affiliate link)";
      }
      a.setAttribute("rel", "sponsored noopener");
      a.setAttribute("target", "_blank");
      srcRow.appendChild(a);
      modalBody.appendChild(srcRow);
    }
    modal.removeAttribute("hidden");
    modalClose.focus();
  };

  // ---- Shelf rendering ----

  const renderShelves = (categories, recordsByCategory, recordById) => {
    shelvesEl.replaceChildren();
    for (const category of categories) {
      const section = make("section", "catalog-shelf");
      section.setAttribute("aria-label", `${category.name} shelves`);
      section.appendChild(make("h3", "catalog-shelf-title", category.name));
      if (category.description) {
        section.appendChild(make("p", "catalog-shelf-desc", category.description));
      }

      const builder = BUILDERS[shapeFor(category.id)] || BUILDERS.book;
      const records = (recordsByCategory.get(category.id) || [])
        .slice()
        .sort((a, b) => sortKey(a.title).localeCompare(sortKey(b.title)));

      const bookcase = make("div", "bookshelf");
      const chunks = [];
      for (let i = 0; i < records.length; i += PER_ROW) chunks.push(records.slice(i, i + PER_ROW));
      if (chunks.length === 0) chunks.push([]);

      for (const chunk of chunks) {
        const row = make("div", "shelf-row");
        if (chunk.length === 0) {
          row.appendChild(
            make("p", "shelf-plaque", "Awaiting artifacts — the Kreator has not filed any here yet.")
          );
        } else {
          for (const record of chunk) {
            const obj = builder(record);
            obj.dataset.recordId = record.record_id;
            const clickable = obj.classList.contains("shelf-object")
              ? obj
              : obj.querySelector(".shelf-object");
            if (clickable) {
              clickable.addEventListener("click", () => {
                const full = recordById.get(record.record_id);
                if (full) openRecord(full, category.name);
              });
            }
            row.appendChild(obj);
          }
        }
        bookcase.appendChild(row);
        bookcase.appendChild(make("div", "shelf-plank"));
      }

      section.appendChild(bookcase);
      shelvesEl.appendChild(section);
    }
  };

  const applySearch = (recordById, categoryNames) => {
    const query = searchInput ? searchInput.value.trim() : "";
    let matches = 0;
    const tops = shelvesEl.querySelectorAll(".shelf-row > [data-record-id]");
    for (const top of tops) {
      const record = recordById.get(top.dataset.recordId);
      const categoryName = record ? categoryNames.get(record.category) || "" : "";
      top.classList.remove("is-dim", "is-match");
      if (query.length === 0) continue;
      if (record && recordMatches(record, categoryName, query)) {
        top.classList.add("is-match");
        matches += 1;
      } else {
        top.classList.add("is-dim");
      }
    }
    if (statusEl) {
      statusEl.textContent =
        query.length === 0
          ? ""
          : matches === 0
            ? `No matches on the shelves for “${query}”.`
            : `${matches} match${matches === 1 ? "" : "es"} on the shelves for “${query}”.`;
    }
  };

  fetch(dataUrl.href)
    .then(response => {
      if (!response.ok) throw new Error(`Catalog data failed to load (${response.status}).`);
      return response.json();
    })
    .then(data => {
      const categories = Array.isArray(data.categories) ? data.categories : [];
      const categoryNames = new Map(categories.map(c => [c.id, c.name]));
      // PLACEHOLDER records are never shelved.
      const records = (Array.isArray(data.records) ? data.records : []).filter(
        record => record && record.status !== "PLACEHOLDER"
      );
      const recordById = new Map(records.map(r => [r.record_id, r]));
      const recordsByCategory = new Map();
      for (const record of records) {
        if (!record.category || !categoryNames.has(record.category)) continue;
        if (!recordsByCategory.has(record.category)) recordsByCategory.set(record.category, []);
        recordsByCategory.get(record.category).push(record);
      }

      renderShelves(categories, recordsByCategory, recordById);

      if (searchInput) {
        searchInput.addEventListener("input", () => applySearch(recordById, categoryNames));
        searchInput.addEventListener("keydown", event => {
          if (event.key === "Escape") {
            searchInput.value = "";
            applySearch(recordById, categoryNames);
          }
        });
      }
    })
    .catch(() => {
      shelvesEl.replaceChildren(
        make("p", "catalog-empty", "The catalog could not be loaded. The shelves will return.")
      );
    });
})();
