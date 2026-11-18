import os, re, hashlib

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Hash full <section> blocks (normalized)
from collections import defaultdict
sec_map = defaultdict(set)
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
        text = m.group(1)
        plain = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text)).strip()
        if len(plain) < 60:
            continue
        h = hashlib.md5(plain.encode()).hexdigest()
        sec_map[h].add(os.path.relpath(f, root))

# Show sections appearing on >=8 pages
print('Repeated sections (>=8 pages):')
for h, pages in sorted(sec_map.items(), key=lambda x: -len(x[1])):
    if len(pages) >= 8:
        # get sample text
        sample = None
        for f in files:
            s = open(f, encoding='utf-8', errors='replace').read()
            for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
                plain = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(1))).strip()
                if hashlib.md5(plain.encode()).hexdigest() == h:
                    sample = plain[:180]
                    break
            if sample: break
        print(f'  {len(pages)} pages: {sample}')
        print(f'    example pages: {sorted(list(pages))[:5]}')
print('Total unique sections:', len(sec_map))
