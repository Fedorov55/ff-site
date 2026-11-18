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
    if 'https://ff-it.ru/apple-touch-icon-180.webp' in s:
        s = s.replace('https://ff-it.ru/apple-touch-icon-180.webp', 'apple-touch-icon-180.webp')
        open(f, 'w', encoding='utf-8').write(s)
        count += 1
print(f'Updated {count} files')
print('Done')
