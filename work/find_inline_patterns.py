import os, re
from collections import Counter

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Collect normalized inline styles
counter = Counter()
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'style="([^"]*)"', s):
        val = m.group(1).strip()
        # normalize: sort properties, remove spaces after colons/semicolons
        props = [p.strip() for p in val.split(';') if p.strip()]
        # normalize each prop
        norm_props = []
        for p in props:
            if ':' in p:
                k, v = p.split(':', 1)
                norm_props.append(f"{k.strip()}:{v.strip()}")
        norm_props.sort()
        norm = ';'.join(norm_props)
        if norm:
            counter[norm] += 1

# Show patterns with 10-30 repetitions
print('Patterns with 10-30 repetitions:')
for val, c in counter.most_common():
    if 10 <= c <= 30:
        print(f'  {c:3d} | {val}')
print()
print('Total unique patterns:', len(counter))
print('Patterns with >=10:', sum(1 for c in counter.values() if c >= 10))
print('Patterns with 10-30:', sum(1 for c in counter.values() if 10 <= c <= 30))
