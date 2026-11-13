#!/usr/bin/env python3
"""Generate sitemap.xml from all HTML files in the project."""
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://fedorov55.github.io/ff-site"
EXCLUDE = {'404.html', 'pasahalki.html', 'room.html', 'vcard.html'}

PRIORITY = {
    'index.html': '1.0',
}
HIGH_PRIORITY = {'support.html', 'servers.html', 'services.html', 'cases.html', 'index.html'}
MID_PRIORITY = {'for-owner.html', 'for-it-director.html', 'for-accountant.html',
                'infrastructure.html', 'security.html', 'audit.html', 'vpn.html',
                'team.html', 'about.html', 'contacts.html', 'blog.html'}

def priority_for(rel):
    name = os.path.basename(rel)
    if name in PRIORITY:
        return PRIORITY[name]
    if name in HIGH_PRIORITY:
        return '0.9'
    if name in MID_PRIORITY:
        return '0.8'
    if name.startswith('cases/'):
        return '0.7'
    if name.startswith('blog/') or name.startswith('articles/'):
        return '0.6'
    if name.startswith('geo/') or name.startswith('services/') or name.startswith('industries/'):
        return '0.7'
    return '0.5'

def main():
    urls = []
    for r, ds, fs in os.walk(ROOT):
        if '.git' in r or 'node_modules' in r or '.agents' in r:
            continue
        for f in fs:
            if not f.endswith('.html'):
                continue
            rel = os.path.relpath(os.path.join(r, f), ROOT).replace('\\', '/')
            name = os.path.basename(rel)
            if name in EXCLUDE:
                continue
            if '.agents' in rel:
                continue
            mtime = os.path.getmtime(os.path.join(r, f))
            lastmod = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%Y-%m-%d')
            prio = priority_for(rel)
            urls.append((rel, lastmod, prio))

    urls.sort(key=lambda x: x[0])

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel, lastmod, prio in urls:
        lines.append('  <url>')
        lines.append(f'    <loc>{BASE_URL}/{rel}</loc>')
        lines.append(f'    <lastmod>{lastmod}</lastmod>')
        lines.append(f'    <priority>{prio}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')

    out = os.path.join(ROOT, 'sitemap.xml')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
    print(f'Generated {len(urls)} URLs -> {out}')

if __name__ == '__main__':
    main()