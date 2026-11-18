import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

updated = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    # Remove status link from dropdown (desktop)
    s = re.sub(r'<a href="(?:\.\./)?index\.html" class="dropdown__link">Статус</a>', '', s)
    # Remove status link from mobile nav
    s = re.sub(r'<a href="(?:\.\./)?index\.html" class="mobile-nav__link">Статус</a>\n?', '', s)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
