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

counter = Counter()
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'style="([^"]*)"', s):
        val = m.group(1).strip()
        if val:
            counter[val] += 1

print('Top 30 exact inline styles:')
for val, c in counter.most_common(30):
    print(f'  {c:3d} | {val}')
print()
print('Total unique exact styles:', len(counter))
print('Styles with >=10:', sum(1 for c in counter.values() if c >= 10))
