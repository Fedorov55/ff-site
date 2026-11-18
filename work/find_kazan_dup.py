import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Find titles with duplicate Kazan
for f in files:
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s)
    if m:
        title = m.group(1)
        if title.count('Казань') > 1:
            print(os.path.relpath(f, root))
            print('   ', title)
print('Done')
