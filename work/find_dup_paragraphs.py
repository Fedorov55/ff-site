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

total = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    # Remove script blocks
    s_no_script = re.sub(r'<script[^>]*>.*?</script>', '', s, flags=re.S)
    # Find all <p> tags
    paras = re.findall(r'<p[^>]*>(.*?)</p>', s_no_script, re.S)
    paras = [re.sub(r'<[^>]+>', '', p).strip() for p in paras]
    paras = [p for p in paras if len(p) > 30]
    cnt = Counter(paras)
    dups = {p: c for p, c in cnt.items() if c > 1}
    if dups:
        total += 1
        if total <= 15:
            print(f'{os.path.relpath(f, root)}: {len(dups)} duplicate paragraphs')
            for p, c in list(dups.items())[:2]:
                print(f'   x{c}: {p[:80]}')
print(f'\nTotal pages with duplicate paragraphs: {total}')
print('Done')
