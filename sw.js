/* Service Worker for F&F site — offline cache of static assets */
const CACHE_NAME = 'ff-cache-v14';
const __swBase = self.location.pathname.replace(/sw\.js$/, '') || '/';
const PRECACHE_URLS = [
  __swBase,
  __swBase + 'index.html',
  __swBase + 'css/style.css',
  __swBase + 'css/critical.css',
  __swBase + 'css/components.css',
  __swBase + 'css/tokens.css',
  __swBase + 'js/script.js',
  __swBase + 'js/search.js',
  __swBase + 'js/search-worker.js',
  __swBase + 'js/calculator.js',
  __swBase + 'search-index.json',
  __swBase + 'manifest.json',
  __swBase + 'img/favicon-32.webp',
  __swBase + 'img/logo-44.webp',
];

// Install: precache static assets
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(PRECACHE_URLS).catch(function(err) {
        console.warn('Precache partial failure:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(k){ return k !== CACHE_NAME; })
            .map(function(k){ return caches.delete(k); })
      );
    })
  );
  self.clients.claim();
});

// Fetch: cache-first for static assets, network-first for HTML
self.addEventListener('fetch', function(event) {
  let url = new URL(event.request.url);
  // Only handle same-origin requests
  if (url.origin !== location.origin) return;
  // Skip non-GET
  if (event.request.method !== 'GET') return;

  let isHTML = event.request.headers.get('accept') && event.request.headers.get('accept').indexOf('text/html') !== -1;
  let isStatic = /\.(css|js|woff2|webp|png|jpg|jpeg|svg|json|ico)$/i.test(url.pathname);

  if (isStatic) {
    // Cache-first for static assets
    event.respondWith(
      caches.match(event.request).then(function(cached) {
        if (cached) return cached;
        return fetch(event.request).then(function(response) {
          if (response && response.status === 200) {
            let clone = response.clone();
            caches.open(CACHE_NAME).then(function(cache) {
              cache.put(event.request, clone);
            });
          }
          return response;
        }).catch(function() {
          return new Response('', { status: 503, statusText: 'Offline' });
        });
      })
    );
  } else if (isHTML) {
    // Network-first for HTML (fresh content, fallback to cache)
    event.respondWith(
      fetch(event.request).then(function(response) {
        if (response && response.status === 200) {
          let clone = response.clone();
          caches.open(CACHE_NAME).then(function(cache) {
            cache.put(event.request, clone);
          });
        }
        return response;
      }).catch(function() {
        return caches.match(event.request).then(function(cached) {
          return cached || caches.match(__swBase + 'index.html');
        });
      })
    );
  }
});
