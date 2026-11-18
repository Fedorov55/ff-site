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
    # Update references to 152fz-prep.html
    s = s.replace('152fz-prep.html', 'services/152fz.html')
    # Fix font paths in services/152fz.html (already done by regex, but check)
    if 'services/152fz.html' in f:
        s = s.replace('../fonts/', '../fonts/')  # no-op
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)

# Fix font paths in services/152fz.html
path = os.path.join(root, 'services/152fz.html')
s = open(path, encoding='utf-8').read()
s = s.replace('fonts/inter-v20-cyrillic_latin-700.woff2', '../fonts/inter-v20-cyrillic_latin-700.woff2')
s = s.replace('fonts/jetbrains-mono-v24-cyrillic_latin-700.woff2', '../fonts/jetbrains-mono-v24-cyrillic_latin-700.woff2')
open(path, 'w', encoding='utf-8').write(s)
print('Fixed font paths')

# Fix blog/152fz.html and blog/fines-2026.html relative links to services/152fz.html
for f in ['blog/152fz.html', 'blog/fines-2026.html']:
    path = os.path.join(root, f)
    s = open(path, encoding='utf-8').read()
    s = s.replace('services/152fz.html', '../services/152fz.html')
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed', f)

print('Done')
