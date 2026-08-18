(function () {
  const target = document.querySelector("header");

  fetch("center-header.html")
    .then((r) => r.text())
    .then((html) => {
      if (!target) {
        console.warn("center.js: <header> element not found.");
        return;
      }
      target.innerHTML = html;
    })
    .catch((err) =>
      console.error("center.js: failed to load center-header.html", err),
    );
})();

(function () {
  const target = document.querySelector("footer");

  fetch("center-footer.html")
    .then((r) => r.text())
    .then((html) => {
      if (!target) {
        console.warn("center.js: <header> element not found.");
        return;
      }
      target.innerHTML = html;
    })
    .catch((err) =>
      console.error("center.js: failed to load center-footer.html", err),
    );
})();
