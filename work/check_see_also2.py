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

patterns = Counter()
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'Смотрите также.*?</section>', s, re.S)
    if m:
        links = re.findall(r'href="([^"]+)"', m.group(0))
        key = tuple(sorted(set(links)))
        patterns[key] += 1

print('Unique "Смотрите также" link sets:', len(patterns))
for k, c in patterns.most_common(15):
    print(f'  {c:3d} pages: {k}')
print()
print('Pages with "Смотрите также":', sum(patterns.values()))
print('Pages without:', len(files) - sum(patterns.values()))
