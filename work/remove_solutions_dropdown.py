import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Pattern: the whole "Решения" nav item (desktop + mobile)
pattern = re.compile(r'<div class="nav__item">\s*<button[^>]*data-nav-trigger[^>]*>Решения<svg[^>]*>.*?</svg></button>\s*<div class="dropdown" id="menu-solutions">.*?</div>\s*</div>', re.S)

updated = 0
for f in files:
    s = open(f, encoding='utf-8').read()
    original = s
    s = pattern.sub('', s)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1
print(f'Updated {updated} files')
print('Done')
