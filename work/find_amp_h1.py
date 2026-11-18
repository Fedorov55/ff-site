import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

found = []
for f in files:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<h1[^>]*>(.*?)</h1>', s, re.S):
        if '&amp;' in m.group(1):
            found.append((os.path.relpath(f, root), m.group(1).strip()[:80]))
            break

print('Pages with &amp; in H1:', len(found))
for f, h1 in found:
    print(f'  {f}: {h1}')
print('Done')
