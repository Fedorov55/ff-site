import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

patterns = [
    'color:var(--gold);',
    'margin:0 4px;',
    'text-align:center;',
    'color:var(--text);',
    'display:none;',
]
for pat in patterns:
    cnt = 0
    for f in files:
        s = open(f, encoding='utf-8', errors='replace').read()
        cnt += s.count(f'style="{pat}"')
    print(f'{pat}: {cnt} remaining exact matches')
