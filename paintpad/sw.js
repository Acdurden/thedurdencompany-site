// Paint Pad offline support.
// On first visit this saves the whole app (page, icons, font) on the iPad.
// Everything is served from this site; nothing comes from anywhere else.
// After that the app opens and works with no connection at all.
// Bump VERSION whenever any file in this folder changes, so iPads pick up the update.
const VERSION = 'paintpad-v3';
const CORE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './apple-touch-icon.png',
  './icon-192.png',
  './icon-512.png',
  './fonts/fredoka-latin-400-normal.woff2',
  './fonts/fredoka-latin-500-normal.woff2',
  './fonts/fredoka-latin-600-normal.woff2',
  './fonts/fredoka-latin-700-normal.woff2'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(VERSION)
      .then((c) => c.addAll(CORE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Try the network for a few seconds, then fall back to the saved copy.
function networkFirst(request, fallbackUrl) {
  return new Promise((resolve) => {
    let done = false;
    const useCache = () => {
      if (done) return;
      done = true;
      caches.match(request, { ignoreSearch: true })
        .then((hit) => hit || caches.match(fallbackUrl))
        .then((hit) => resolve(hit || new Response('Offline', { status: 503 })));
    };
    const timer = setTimeout(useCache, 3000);
    fetch(request).then((res) => {
      if (done) return;
      clearTimeout(timer);
      done = true;
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(fallbackUrl || request, copy));
      }
      resolve(res);
    }).catch(() => { clearTimeout(timer); useCache(); });
  });
}

// Use the saved copy right away; refresh it in the background when online.
function cacheFirst(request) {
  return caches.match(request).then((hit) => {
    const refresh = fetch(request).then((res) => {
      if (res && (res.ok || res.type === 'opaque')) {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(request, copy));
      }
      return res;
    }).catch(() => hit);
    return hit || refresh;
  });
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (req.mode === 'navigate') {
    event.respondWith(networkFirst(req, './index.html'));
  } else if (url.origin === self.location.origin) {
    event.respondWith(cacheFirst(req));
  }
});
