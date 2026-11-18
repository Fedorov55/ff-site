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

# Extract 120-char window around '99,5' or '99.5'
contexts = Counter()
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'.{0,60}99[,.]5.{0,60}', s):
        ctx = m.group(0)
        # normalize whitespace
        ctx = ' '.join(ctx.split())
        contexts[ctx] += 1

for ctx, c in contexts.most_common(15):
    print(f'{c:3d} | {ctx}')
