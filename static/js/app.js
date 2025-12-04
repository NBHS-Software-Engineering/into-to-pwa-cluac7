// Register service worker correctly and provide basic UI handlers (menu, search, offline banner)
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker
      .register("/static/js/serviceworker.js")
      .then((res) => console.log("service worker registered"))
      .catch((err) => console.log("service worker not registered", err));
  });
}

// Utility: debounce
function debounce(fn, wait) {
  let t;
  return function (...args) {
    clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), wait);
  };
}

document.addEventListener("DOMContentLoaded", function () {
  var btn = document.getElementById("menu-toggle");
  var nav = document.getElementById("main-nav");
  if (btn && nav) {
    function closeNav() {
      nav.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    }

    function openNav() {
      nav.classList.add("open");
      btn.setAttribute("aria-expanded", "true");
      // move focus to first link for keyboard users
      const firstLink = nav.querySelector("a");
      if (firstLink) firstLink.focus();
    }

    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      if (nav.classList.contains("open")) closeNav();
      else openNav();
    });

    document.addEventListener("click", function (e) {
      if (
        !nav.contains(e.target) &&
        !btn.contains(e.target) &&
        nav.classList.contains("open")
      ) {
        closeNav();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        closeNav();
        btn.focus();
      }
    });
  }

  // Offline/online status banner
  const statusEl = document.getElementById("status");
  function updateStatus() {
    const lastSync = localStorage.getItem("last_sync");
    if (!navigator.onLine) {
      statusEl.textContent = lastSync
        ? `Offline — showing cached data (last sync: ${lastSync})`
        : "Offline — showing cached data";
      statusEl.classList.add("visible");
    } else {
      statusEl.textContent = lastSync
        ? `Online — last sync: ${lastSync}`
        : "Online";
      statusEl.classList.remove("visible");
    }
  }

  window.addEventListener("online", updateStatus);
  window.addEventListener("offline", updateStatus);
  updateStatus();

  // Search: debounced, fetch HTML fragment from server and replace .container or #content
  const searchInput = document.getElementById("search-input");
  // prefer the grid container if present, otherwise fall back to the main content area
  const container =
    document.querySelector(".container") || document.getElementById("content");
  if (searchInput && container) {
    const doSearch = debounce(function () {
      const q = searchInput.value.trim();
      const url = `/api/search?q=${encodeURIComponent(q)}`;
      fetch(url)
        .then((res) => {
          if (!res.ok) throw new Error("Network response was not ok");
          return res.text();
        })
        .then((html) => {
          // If we replaced the entire #content, ensure it's wrapped in a container class
          if (container.id === "content") {
            container.innerHTML = `<div class="container">${html}</div>`;
          } else {
            container.innerHTML = html;
          }
          // update last sync time
          const now = new Date().toLocaleString();
          localStorage.setItem("last_sync", now);
          updateStatus();
        })
        .catch((err) => {
          console.log("Search fetch failed", err);
        });
    }, 300);

    searchInput.addEventListener("input", doSearch);
  }
});
