(() => {
  "use strict";

  const bookcaseButton = document.querySelector("[data-bookcase-trigger]");
  const blackDoorWrap = document.querySelector("[data-black-door]");

  if (bookcaseButton && blackDoorWrap) {
    bookcaseButton.addEventListener("click", () => {
      const isHidden = blackDoorWrap.hasAttribute("hidden");
      if (isHidden) {
        blackDoorWrap.removeAttribute("hidden");
        bookcaseButton.setAttribute("aria-expanded", "true");
        blackDoorWrap.scrollIntoView({ behavior: "smooth", block: "center" });
      } else {
        blackDoorWrap.setAttribute("hidden", "");
        bookcaseButton.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Construction-only age-gate hook.
  // IMPORTANT: This is not real age verification. Do not load restricted content
  // until a proper verification/assurance provider is connected before launch.
  const ageYes = document.querySelector("[data-age-yes]");
  const ageNo = document.querySelector("[data-age-no]");
  const ageStatus = document.querySelector("[data-age-status]");

  if (ageYes && ageStatus) {
    ageYes.addEventListener("click", () => {
      ageStatus.hidden = false;
      ageStatus.textContent =
        "Construction checkpoint only. A real age-verification service will be connected before restricted material is added.";
    });
  }

  if (ageNo && ageStatus) {
    ageNo.addEventListener("click", () => {
      ageStatus.hidden = false;
      ageStatus.textContent = "Access remains closed.";
    });
  }
})();
