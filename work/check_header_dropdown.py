import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

old_pattern = re.compile(r'<div class="dropdown" id="menu-company">.*?</div>', re.S)
count = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    if 'menu-company' in s:
        count += 1
print('Pages with menu-company dropdown:', count)
print('Total pages:', len(files))
