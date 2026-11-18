import os, re, hashlib
from collections import defaultdict

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Hash div blocks containing '99,5' or 'кейс' keywords, length > 100
div_map = defaultdict(set)
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'<div[^>]*>(.*?)</div>', s, re.S):
        text = m.group(1)
        plain = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text)).strip()
        if len(plain) < 100:
            continue
        if '99,5' in plain or 'кейс' in plain.lower() or 'SLA' in plain:
            h = hashlib.md5(plain.encode()).hexdigest()
            div_map[h].add(os.path.relpath(f, root))

print('Repeated divs (>=8 pages):')
for h, pages in sorted(div_map.items(), key=lambda x: -len(x[1])):
    if len(pages) >= 8:
        # sample
        sample=None
        for f in files:
            s=open(f,encoding='utf-8',errors='replace').read()
            for m in re.finditer(r'<div[^>]*>(.*?)</div>', s, re.S):
                plain=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(1))).strip()
                if hashlib.md5(plain.encode()).hexdigest()==h and len(plain)>=100:
                    sample=plain[:200]; break
            if sample: break
        print(f'  {len(pages)} pages: {sample}')
        print(f'    {sorted(list(pages))[:4]}')
print('total unique divs:', len(div_map))
