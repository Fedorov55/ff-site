import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for f in files:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s)
    if m and 'Казань — Казань' in m.group(1):
        print(os.path.relpath(f, root))
        print('   ', m.group(1))
print('Done')
