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

total_dup = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    # extract sentences (split by . ! ?)
    text = re.sub(r'<[^>]+>', ' ', s)
    text = ' '.join(text.split())
    sentences = re.split(r'[.!?]\s+', text)
    sentences = [st.strip() for st in sentences if len(st.strip()) > 30]
    cnt = Counter(sentences)
    dups = {st: c for st, c in cnt.items() if c > 1}
    if dups:
        total_dup += 1
        if total_dup <= 10:
            print(f'{os.path.relpath(f, root)}: {len(dups)} duplicated sentences')
            for st, c in list(dups.items())[:3]:
                print(f'   x{c}: {st[:80]}')
print(f'\nTotal pages with internal duplicates: {total_dup}')
print('Done')
