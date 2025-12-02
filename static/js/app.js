if ("serviceworker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceworker
      .register("static/js/serviceworker.js")
      .then((res) => console.log("service worker registered"))
      .catch((err) => console.log("service worker not registered", err));
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var btn = document.getElementById("menu-toggle");
  var nav = document.getElementById("main-nav");
  if (!btn || !nav) return;

  function closeNav() {
    nav.classList.remove("open");
  }

  function openNav() {
    nav.classList.add("open");
  }

  btn.addEventListener("click", function (e) {
    e.stopPropagation();
    if (expanded) closeNav();
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
});
