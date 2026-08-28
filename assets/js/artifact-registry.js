(() => {
  "use strict";

  const script = document.currentScript;
  if (!script) return;

  const dataUrl = new URL("../../data/artifacts.json", script.src);
  const siteRoot = new URL("../../", script.src);

  const make = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  };

  const formatDate = value => value || "Not recorded";

  const safeSiteAssetUrl = value => {
    if (!value || typeof value !== "string") return null;
    try {
      return new URL(value.replace(/^\/+/, ""), siteRoot).href;
    } catch {
      return null;
    }
  };

  const renderMedia = artifact => {
    const hero = artifact.media && artifact.media.hero_image;
    const src = safeSiteAssetUrl(hero);
    if (!src) return null;

    const figure = make("figure", "registry-media");
    const image = make("img", "registry-image");
    image.src = src;
    image.alt = artifact.title ? `${artifact.title} artifact image` : "Artifact image";
    image.loading = "lazy";
    image.decoding = "async";
    figure.appendChild(image);
    return figure;
  };

  const renderArtifact = artifact => {
    const card = make("article", "registry-artifact");
    card.dataset.status = artifact.status || "active";
    card.dataset.realm = artifact.realm || "";

    const media = renderMedia(artifact);
    if (media) card.appendChild(media);

    const title = make("h3", "registry-title", artifact.title || "Untitled artifact");
    card.appendChild(title);

    const meta = make("div", "registry-meta");
    meta.appendChild(make("span", "registry-chip", artifact.artifact_type || "artifact"));
    meta.appendChild(make("span", "registry-chip", artifact.status || "active"));
    if (artifact.museum_scale && artifact.museum_scale !== "not-applicable") {
      meta.appendChild(make("span", "registry-chip", artifact.museum_scale));
    }
    if (artifact.restricted) meta.appendChild(make("span", "registry-chip", "restricted"));
    card.appendChild(meta);

    if (artifact.summary) card.appendChild(make("p", "registry-summary", artifact.summary));

    if (artifact.status === "deceased" || artifact.status === "resurrected") {
      const dates = make("dl", "registry-dates");
      dates.appendChild(make("dt", "", "Died"));
      dates.appendChild(make("dd", "", formatDate(artifact.death_date)));
      if (artifact.status === "resurrected") {
        dates.appendChild(make("dt", "", "Resurrected"));
        dates.appendChild(make("dd", "", formatDate(artifact.resurrection_date)));
      }
      card.appendChild(dates);
    }

    if (artifact.provenance) {
      const details = make("details", "registry-provenance");
      details.appendChild(make("summary", "", "Provenance"));
      details.appendChild(make("p", "", artifact.provenance));
      card.appendChild(details);
    }

    if (Array.isArray(artifact.platforms) && artifact.platforms.length) {
      const platformRow = make("div", "registry-platforms");
      artifact.platforms.forEach(platform => {
        if (!platform || !platform.url) return;
        const link = make("a", "registry-platform", platform.label || "Open");
        link.href = platform.url;
        link.rel = "noopener noreferrer";
        link.target = "_blank";
        platformRow.appendChild(link);
      });
      if (platformRow.childElementCount) card.appendChild(platformRow);
    }

    return card;
  };

  const renderCollection = (host, artifacts) => {
    const realm = host.dataset.realm || "";
    const collection = host.dataset.collection || "";
    const status = host.dataset.status || "";

    const matches = artifacts.filter(item => {
      if (realm && item.realm !== realm) return false;
      if (collection && item.collection !== collection) return false;
      if (status && item.status !== status) return false;
      return true;
    });

    host.replaceChildren();

    if (!matches.length) {
      host.appendChild(make("p", "registry-empty", "Collection wired. No artifacts have been loaded here yet."));
      return;
    }

    matches.forEach(item => host.appendChild(renderArtifact(item)));
  };

  const hosts = [...document.querySelectorAll("[data-artifact-registry]")];
  if (!hosts.length) return;

  fetch(dataUrl)
    .then(response => {
      if (!response.ok) throw new Error(`Artifact registry failed: ${response.status}`);
      return response.json();
    })
    .then(payload => {
      const artifacts = Array.isArray(payload.artifacts) ? payload.artifacts : [];
      hosts.forEach(host => renderCollection(host, artifacts));
    })
    .catch(() => {
      hosts.forEach(host => {
        host.replaceChildren(make("p", "registry-empty", "Artifact registry unavailable in this preview. The static realm structure still works."));
      });
    });
})();
