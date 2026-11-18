import os, sys

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
targets = sys.argv[1:]
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for target in targets:
    cnt = 0
    refs = []
    for f in files:
        s = open(f, encoding='utf-8', errors='replace').read()
        if target in s:
            cnt += 1
            refs.append(os.path.relpath(f, root))
    print(f'{target}: referenced in {cnt} files')
    if cnt <= 10:
        for r in refs:
            print('   ', r)
