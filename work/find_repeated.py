import os, re, hashlib

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Find sections containing '99,5%'
blocks = {}
for f in files:
    s = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S):
        text = m.group(1)
        plain = re.sub(r'<[^>]+>', ' ', text)
        plain = ' '.join(plain.split())
        if '99,5%' in plain or '99.5%' in plain:
            h = hashlib.md5(plain.encode()).hexdigest()[:12]
            blocks.setdefault(h, []).append((os.path.relpath(f, root), plain[:120]))

for h, lst in blocks.items():
    if len(lst) >= 3:
        print('=== BLOCK (', len(lst), 'pages ) ===')
        print(lst[0][1])
        print('pages:', [x[0] for x in lst[:8]])
        print()
