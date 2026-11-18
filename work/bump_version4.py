import os
root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
count = 0
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        path = os.path.join(r, f)
        s = open(path, encoding='utf-8').read()
        s2 = s.replace('?v=120', '?v=121')
        if s2 != s:
            open(path, 'w', encoding='utf-8').write(s2)
            count += 1
print('Updated', count, 'HTML files')
