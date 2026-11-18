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
    # Remove from desktop dropdown
    s = re.sub(r'<a href="(?:\.\./)?it-budget\.html" class="dropdown__link">IT-бюджет 2026-2027</a>\n?', '', s)
    # Remove from mobile nav
    s = re.sub(r'<a href="(?:\.\./)?it-budget\.html" class="mobile-nav__link">IT-бюджет 2026-2027</a>\n?', '', s)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1
print(f'Updated {updated} files')
print('Done')
