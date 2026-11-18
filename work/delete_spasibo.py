import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# Update references
all_files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            all_files.append(os.path.join(r, f))

for f in all_files:
    s = open(f, encoding='utf-8').read()
    original = s
    s = s.replace('spasibo.html', 'index.html')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Update _redirects
redirects_path = os.path.join(root, '_redirects')
s = open(redirects_path, encoding='utf-8').read()
line = '/spasibo.html /index.html 301\n'
if line not in s:
    s += line
open(redirects_path, 'w', encoding='utf-8').write(s)

# Delete file
p = os.path.join(root, 'spasibo.html')
if os.path.exists(p):
    os.remove(p)
    print('Deleted spasibo.html')
print('Done')
