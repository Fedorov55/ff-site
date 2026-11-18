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

variants = Counter()
for f in files:
    s = open(f, encoding='utf-8').read()
    # title
    m = re.search(r'<title>(.*?)</title>', s)
    if m:
        t = m.group(1)
        # normalize brand mentions
        for v in ['F&F Казань', 'F&amp;F Казань', 'F&F IT', 'F&amp;F IT', 'F&F']:
            if v in t:
                variants[v] += 1
print('Brand variants in <title>:')
for v, c in variants.most_common():
    print(f'  {c:3d} | {v}')
print('Total pages:', len(files))
print('Done')
