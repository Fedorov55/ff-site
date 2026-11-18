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
    if m:
        title = m.group(1)
        # check for any city repeated
        cities = ['Казань', 'Казани', 'Казань,', 'Казани,']
        for city in cities:
            if title.count(city) > 1:
                print(os.path.relpath(f, root))
                print('   ', title)
                break
print('Done')
