import os
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
    if 'apple-touch-icon' in s:
        import re
        m = re.search(r'apple-touch-icon[^>]*href="([^"]*)"', s)
        if m:
            print(os.path.relpath(f, root), '->', m.group(1))
            break
print('Done')
# count
cnt = sum(1 for f in files if 'apple-touch-icon' in open(f,encoding='utf-8').read())
print('files with apple-touch-icon:', cnt)
# show unique hrefs
hrefs = set()
for f in files:
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'apple-touch-icon[^>]*href="([^"]*)"', s):
        hrefs.add(m.group(1))
print('unique hrefs:', hrefs)
