import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

count = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    s = s.replace('F&F Казань', 'F&F IT')
    s = s.replace('F&amp;F Казань', 'F&amp;F IT')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        count += 1
print(f'Updated {count} files')
print('Done')
