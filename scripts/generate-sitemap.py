import os
from datetime import date

BASE = 'https://fedorov55.github.io/ff-site'
EXCLUDE = {'404.html'}
EXCLUDE_DIRS = {'.git', 'node_modules', '.agents', 'dist', 'img', 'fonts', 'js', 'css'}
LASTMOD = date.today().isoformat()

HIGH = {'index.html'}
MID = {'services.html', 'servers.html', 'support.html', 'cases.html', 'contacts.html',
       'prices.html', 'industries.html', 'articles.html', 'blog.html'}

noindex_pages = set()
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    if '.git' in root_dir:
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root_dir, f)
        rel = os.path.relpath(p, '.').replace(os.sep, '/')
        try:
            s = open(p, encoding='utf-8').read()
        except Exception:
            continue
        if 'noindex' in s:
            noindex_pages.add(rel)

urls = []
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    if '.git' in root_dir:
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        rel = os.path.relpath(os.path.join(root_dir, f), '.').replace(os.sep, '/')
        if rel in EXCLUDE or rel in noindex_pages:
            continue
        if rel == 'index.html':
            url = BASE + '/'
            prio = '1.0'
        else:
            url = BASE + '/' + rel
            if rel in MID:
                prio = '0.9'
            else:
                prio = '0.8'
        urls.append((url, prio))

urls = sorted(set(urls))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url, prio in urls:
    xml += '  <url>\n'
    xml += f'    <loc>{url}</loc>\n'
    xml += f'    <lastmod>{LASTMOD}</lastmod>\n'
    xml += '    <changefreq>weekly</changefreq>\n'
    xml += f'    <priority>{prio}</priority>\n'
    xml += '  </url>\n'
xml += '</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml)
print(f'Generated sitemap with {len(urls)} URLs')
