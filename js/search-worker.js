'use strict';

// Levenshtein distance for fuzzy matching
function levenshtein(a, b) {
  if (a === b) return 0;
  if (!a.length) return b.length;
  if (!b.length) return a.length;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    let cur = [i];
    for (let j = 1; j <= b.length; j++) {
      let cost = a[i - 1] === b[j - 1] ? 0 : 1;
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
    }
    prev = cur;
  }
  return prev[b.length];
}

// Normalize text for search
function normalize(text) {
  return (text || '').toLowerCase().replace(/ё/g, 'е').replace(/[^а-яa-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
}

// Tokenize
function tokenize(text) {
  return normalize(text).split(' ').filter(function (w) { return w.length > 1; });
}

// Score a page against query tokens
function scorePage(page, queryTokens) {
  let title = normalize(page.t);
  let desc = normalize(page.d);
  let h1 = normalize(page.h);
  let text = normalize(page.x);
  let full = title + ' ' + h1 + ' ' + desc + ' ' + text;
  let score = 0;
  let matched = 0;
  for (let i = 0; i < queryTokens.length; i++) {
    let q = queryTokens[i];
    let found = false;
    if (title.indexOf(q) !== -1) { score += 10; found = true; }
    if (h1.indexOf(q) !== -1) { score += 8; found = true; }
    if (desc.indexOf(q) !== -1) { score += 5; found = true; }
    if (text.indexOf(q) !== -1) { score += 2; found = true; }
    if (!found && q.length >= 4) {
      let words = full.split(' ');
      for (let w = 0; w < words.length; w++) {
        if (words[w].length >= 3 && levenshtein(q, words[w]) <= 2) {
          score += 1; found = true; break;
        }
      }
    }
    if (found) matched++;
  }
  if (matched === queryTokens.length && queryTokens.length > 1) score += 5;
  return score;
}

// Worker message handler
self.onmessage = function (e) {
  let msg = e.data;
  if (msg.type === 'search') {
    let index = msg.index;
    let query = msg.query;
    let tokens = tokenize(query);
    if (!tokens.length) {
      self.postMessage({ type: 'results', results: [] });
      return;
    }
    let results = [];
    for (let i = 0; i < index.length; i++) {
      let sc = scorePage(index[i], tokens);
      if (sc > 0) results.push({ page: index[i], score: sc });
    }
    results.sort(function (a, b) { return b.score - a.score; });
    self.postMessage({ type: 'results', results: results.slice(0, 12), query: query });
  }
};