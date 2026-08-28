(() => {
  "use strict";

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const scrollBehavior = reducedMotion ? "auto" : "smooth";

  // LIBRARY: construction-mode decontamination sequence.
  const deconStart = document.querySelector("[data-decon-start]");
  const deconStatus = document.querySelector("[data-decon-status]");
  const deconSteps = [...document.querySelectorAll("[data-decon-step]")];
  const archiveEntry = document.querySelector("[data-archive-entry]");

  if (deconStart && deconStatus && deconSteps.length && archiveEntry) {
    deconStart.addEventListener("click", async () => {
      deconStart.disabled = true;
      const messages = [
        "Stage 1: exterior contaminants isolated.",
        "Stage 2: preservation-safe intake confirmed.",
        "Stage 3: archive seal released."
      ];

      for (let i = 0; i < deconSteps.length; i += 1) {
        deconStatus.textContent = messages[i] || "Preservation cycle continuing.";
        deconSteps[i].dataset.complete = "true";
        await new Promise(resolve => setTimeout(resolve, reducedMotion ? 0 : 650));
      }

      deconStatus.textContent = "Decontamination complete. The Library may be entered.";
      archiveEntry.hidden = false;
      archiveEntry.scrollIntoView({ behavior: scrollBehavior, block: "center" });
    });
  }

  // LIBRARY: hidden bookcase and black-door reveal.
  const bookcaseButton = document.querySelector("[data-bookcase-trigger]");
  const blackDoorWrap = document.querySelector("[data-black-door]");

  if (bookcaseButton && blackDoorWrap) {
    bookcaseButton.addEventListener("click", () => {
      const isHidden = blackDoorWrap.hasAttribute("hidden");
      if (isHidden) {
        blackDoorWrap.removeAttribute("hidden");
        bookcaseButton.setAttribute("aria-expanded", "true");
        bookcaseButton.textContent = "The bookcase is open";
        blackDoorWrap.scrollIntoView({ behavior: scrollBehavior, block: "center" });
      } else {
        blackDoorWrap.setAttribute("hidden", "");
        bookcaseButton.setAttribute("aria-expanded", "false");
        bookcaseButton.textContent = "Pull the suspicious volume";
      }
    });
  }

  // FORBIDDEN LIBRARY: construction-only gate.
  // This deliberately does NOT unlock restricted material and MUST be replaced
  // by real age assurance / access control before adult content is loaded.
  const ageYes = document.querySelector("[data-age-yes]");
  const ageNo = document.querySelector("[data-age-no]");
  const ageStatus = document.querySelector("[data-age-status]");
  const restrictedShelves = document.querySelector("[data-restricted-shelves]");

  if (ageYes && ageStatus) {
    ageYes.addEventListener("click", () => {
      ageStatus.hidden = false;
      ageStatus.textContent = "Construction checkpoint only. No adult collection has been unlocked. Real verification must replace this control before launch.";
      if (restrictedShelves) restrictedShelves.setAttribute("aria-hidden", "true");
    });
  }

  if (ageNo && ageStatus) {
    ageNo.addEventListener("click", () => {
      ageStatus.hidden = false;
      ageStatus.textContent = "Access remains closed.";
      if (restrictedShelves) restrictedShelves.setAttribute("aria-hidden", "true");
    });
  }

  // Generic construction detail toggles for artifact cards and realm notes.
  document.querySelectorAll("[data-toggle-target]").forEach(button => {
    const id = button.getAttribute("data-toggle-target");
    const target = id ? document.getElementById(id) : null;
    if (!target) return;

    button.addEventListener("click", () => {
      const willOpen = target.hasAttribute("hidden");
      target.toggleAttribute("hidden", !willOpen);
      button.setAttribute("aria-expanded", String(willOpen));
      if (willOpen) target.scrollIntoView({ behavior: scrollBehavior, block: "nearest" });
    });
  });
})();
