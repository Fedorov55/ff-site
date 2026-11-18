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
    for attr in ['title', 'og:title', 'h1']:
        # find all occurrences of brand variants
        for v in ['F&F Казань', 'F&amp;F Казань', 'F&F IT', 'F&amp;F IT']:
            if v in s:
                variants[v] += 1
print('Brand variants across all HTML:')
for v, c in variants.most_common():
    print(f'  {c:3d} | {v}')
print('Total pages:', len(files))
print('Done')
