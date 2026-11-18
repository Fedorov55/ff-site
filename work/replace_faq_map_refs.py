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
    original = s
    s = s.replace('faq.html', 'blog.html')
    s = s.replace('map.html', 'index.html')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
print('Done')
