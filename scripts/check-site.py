#!/usr/bin/env python3
"""Basic CI checks for the F&F static site."""
import os
import re
import json
import sys
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []

def main():
    html_files = []
    for r, ds, fs in os.walk(ROOT):
        if '.git' in r or 'node_modules' in r or '.agents' in r:
            continue
        for f in fs:
            if f.endswith('.html'):
                html_files.append(os.path.join(r, f))

    # 1. Broken internal links
    existing = set(os.path.relpath(f, ROOT).replace('\\', '/') for f in html_files)
    broken = 0
    for f in html_files:
        rel = os.path.relpath(f, ROOT).replace('\\', '/')
        s = open(f, encoding='utf-8', errors='replace').read()
        d = os.path.dirname(rel)
        for m in re.finditer(r'href="([^"#]+)(?:#[^"]*)?"', s):
            href = m.group(1)
            if href.startswith(('http', 'mailto', 'tel', 'javascript', 'data:', '#')) or href == '':
                continue
            pp = href.split('?')[0]
            target = pp.lstrip('/') if pp.startswith('/') else os.path.normpath(os.path.join(d, pp)).replace('\\', '/')
            if target == '.' or target in existing or os.path.exists(target):
                continue
            broken += 1
            if broken <= 10:
                print(f'BROKEN LINK: {rel} -> {href}')
    if broken:
        ERRORS.append(f'broken links: {broken}')

    # 2. Empty sections
    empty = 0
    for f in html_files:
        s = open(f, encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
            text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            text = ' '.join(text.split())
            if len(text) < 20:
                empty += 1
    if empty:
        ERRORS.append(f'empty sections: {empty}')

    # 3. Placeholders / TODOs (excluding verification meta tags)
    bad_strings = ['YOUR_FORM_ID', 'TODO', 'FIXME', '00000000']
    placeholder_count = 0
    for f in html_files:
        s = open(f, encoding='utf-8', errors='replace').read()
        # Remove verification meta tags from check
        s_clean = re.sub(r'<meta name="(yandex|google)-site-verification" content="[^"]*"', '', s)
        for bs in bad_strings:
            if bs in s_clean:
                placeholder_count += 1
                print(f'PLACEHOLDER FOUND: {os.path.relpath(f, ROOT)} contains "{bs}"')
                break
    if placeholder_count:
        ERRORS.append(f'placeholders/TODOs: {placeholder_count} files')

    # 4. JS syntax
    for jsf in ['script.js', 'calculator.js']:
        path = os.path.join(ROOT, jsf)
        if os.path.exists(path):
            r = subprocess.run(['node', '--check', jsf], capture_output=True, text=True, cwd=ROOT)
            if r.returncode != 0:
                ERRORS.append(f'{jsf}: syntax error')

    # 5. CSS/JS version consistency
    versions = set()
    for f in html_files:
        s = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\?v=(\d+)', s):
            versions.add(m.group(1))
    if len(versions) > 1:
        ERRORS.append(f'multiple versions: {versions}')

    # 6. One H1 per page
    h1_issues = 0
    for f in html_files:
        s = open(f, encoding='utf-8').read()
        if len(re.findall(r'<h1\b', s)) != 1:
            h1_issues += 1
    if h1_issues:
        ERRORS.append(f'H1 count issues: {h1_issues}')

    # 7. Bad schema
    bad_schema = 0
    for f in html_files:
        s = open(f, encoding='utf-8').read()
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m.group(1))
            except:
                bad_schema += 1
    if bad_schema:
        ERRORS.append(f'bad JSON-LD: {bad_schema}')

    # 8. _headers exists
    if not os.path.exists(os.path.join(ROOT, '_headers')):
        ERRORS.append('_headers missing')

    print(f'Checked {len(html_files)} HTML files')
    if ERRORS:
        print(f'\n{len(ERRORS)} ERRORS:')
        for e in ERRORS:
            print(f'  - {e}')
        sys.exit(1)
    else:
        print('All checks passed!')

if __name__ == '__main__':
    main()