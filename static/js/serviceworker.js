// Improved service worker: fixed activate logic, runtime caching for API, navigation fallback
const PRECACHE = "catalogue-assets-v1";
const RUNTIME = "runtime-cache";

const PRECACHE_URLS = [
  "/",
  "/static/css/style.css",
  "/static/js/app.js",
  "/static/images/F1.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(PRECACHE)
      .then((cache) => cache.addAll(PRECACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== PRECACHE && key !== RUNTIME) {
            return caches.delete(key);
          }
        })
      )
    )
  );
  self.clients.claim();
});

// Utility to put a response clone into runtime cache
function cacheRuntimeResponse(request, response) {
  if (!response || response.status !== 200 || response.type === "opaque")
    return;
  const copy = response.clone();
  caches.open(RUNTIME).then((cache) => cache.put(request, copy));
}

self.addEventListener("fetch", (event) => {
  const request = event.request;

  // Always try network first for API requests, fallback to cache
  if (request.url.includes("/api/")) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          cacheRuntimeResponse(request, response);
          return response;
        })
        .catch(() => caches.match(request))
    );
    return;
  }

  // For navigation requests, respond with cached / or network
  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then((response) => response)
        .catch(() => caches.match("/"))
    );
    return;
  }

  // For other requests, try cache first then network
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;
      return fetch(request)
        .then((response) => {
          cacheRuntimeResponse(request, response);
          return response;
        })
        .catch(() => {
          // nothing else to do
        });
    })
  );
});
