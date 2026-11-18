import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

for target in ['faq.html', 'map.html']:
    cnt = 0
    for f in files:
        s = open(f, encoding='utf-8').read()
        if target in s:
            cnt += 1
    print(f'{target}: referenced in {cnt} files')
print('Done')
