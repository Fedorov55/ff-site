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

c = Counter()
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'<h[23][^>]*>([^<]*SLA[^<]*)</h[23]>', s, re.I):
        c[m.group(1).strip()] += 1

for heading, n in c.most_common(20):
    print(f'{n:3d} | {heading}')
print('Total unique SLA headings:', len(c))
