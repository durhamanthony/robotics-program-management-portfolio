(function () {
  document.querySelectorAll("[data-go-back]").forEach((button) => {
    button.addEventListener("click", () => {
      const fallback = button.dataset.fallback || "index.html";
      if (window.history.length > 1 && document.referrer) {
        window.history.back();
      } else {
        window.location.href = fallback;
      }
    });
  });

  const search = document.getElementById("artifact-search");
  if (search) {
    const items = [...document.querySelectorAll(".artifact-item")];
    search.addEventListener("input", () => {
      const value = search.value.toLowerCase().trim();
      items.forEach((item) => {
        item.hidden = Boolean(value && !item.dataset.search.includes(value));
      });
    });
  }

  const buttons = [...document.querySelectorAll("[data-tab-target]")];
  const panels = [...document.querySelectorAll(".dashboard-panel")];
  if (!buttons.length || !panels.length) return;

  function activate(id, updateHash) {
    if (!panels.some((panel) => panel.id === id)) id = "overview";
    buttons.forEach((button) => {
      const active = button.dataset.tabTarget === id;
      button.classList.toggle("active", active);
      button.setAttribute("aria-selected", String(active));
    });
    panels.forEach((panel) => panel.classList.toggle("active", panel.id === id));
    if (updateHash) history.replaceState(null, "", `#${id}`);
  }

  buttons.forEach((button) => {
    button.setAttribute("role", "tab");
    button.addEventListener("click", () => activate(button.dataset.tabTarget, true));
  });
  activate(location.hash.slice(1) || "overview", false);
})();
