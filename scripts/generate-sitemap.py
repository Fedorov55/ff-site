import os, re

BASE = 'https://fedorov55.github.io/ff-site'
EXCLUDE = {'404.html', 'pasahalki.html', 'room.html', 'vcard.html'}
EXCLUDE_DIRS = {'.git', 'node_modules', '.agents', 'dist', 'img', 'fonts', 'js'}

noindex_pages = set()
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    if '.git' in root_dir: continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root_dir, f)
            rel = os.path.relpath(p, '.').replace(chr(92), '/')
            s = open(p, encoding='utf-8').read()
            if 'noindex' in s:
                noindex_pages.add(rel)

urls = []
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    if '.git' in root_dir: continue
    for f in files:
        if not f.endswith('.html'): continue
        rel = os.path.relpath(os.path.join(root_dir, f), '.').replace(chr(92), '/')
        if rel in EXCLUDE or rel in noindex_pages:
            continue
        if rel.startswith('blog/'):
            url = BASE + '/blog/' + rel[5:]
        elif rel.startswith('articles/'):
            url = BASE + '/articles/' + rel[9:]
        elif rel.startswith('cases/'):
            url = BASE + '/cases/' + rel[6:]
        elif rel.startswith('geo/'):
            url = BASE + '/geo/' + rel[4:]
        elif rel.startswith('services/'):
            url = BASE + '/services/' + rel[9:]
        else:
            url = BASE + '/' + rel
        if rel == 'index.html':
            url = BASE + '/'
        urls.append(url)

urls = sorted(set(urls))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    xml += f'  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
xml += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)
print(f'Generated sitemap with {len(urls)} URLs')