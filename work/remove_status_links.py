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
    # Remove status link from "О компании" dropdown (desktop)
    s = s.replace('<a href="status.html" class="dropdown__link">Статус</a>', '')
    s = s.replace('<a href="../status.html" class="dropdown__link">Статус</a>', '')
    # Remove status link from "Ресурсы" dropdown (desktop)
    s = s.replace('<a href="status.html" class="dropdown__link">Статус</a>', '')
    s = s.replace('<a href="../status.html" class="dropdown__link">Статус</a>', '')
    # Remove status link from mobile "О компании" group
    s = s.replace('<a href="status.html" class="mobile-nav__link">Статус</a>\n', '')
    s = s.replace('<a href="../status.html" class="mobile-nav__link">Статус</a>\n', '')
    # Remove status link from mobile "Ресурсы" group
    s = s.replace('<a href="status.html" class="mobile-nav__link">Статус</a>\n', '')
    s = s.replace('<a href="../status.html" class="mobile-nav__link">Статус</a>\n', '')
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
