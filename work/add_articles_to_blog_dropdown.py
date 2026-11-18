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
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    p = '' if d in ('', '.') else '../'
    s = open(f, encoding='utf-8').read()
    original = s

    # Update desktop blog dropdown: add articles link after "Все статьи"
    old = f'<a href="{p}blog.html" class="dropdown__link">Все статьи</a>'
    new = f'<a href="{p}blog.html" class="dropdown__link">Все статьи</a>\n<a href="{p}articles.html" class="dropdown__link">Статьи и исследования</a>'
    if old in s:
        s = s.replace(old, new, 1)

    # Update mobile blog group: add articles link after "Все статьи"
    old_m = f'<a href="{p}blog.html" class="mobile-nav__link">Все статьи</a>'
    new_m = f'<a href="{p}blog.html" class="mobile-nav__link">Все статьи</a>\n<a href="{p}articles.html" class="mobile-nav__link">Статьи и исследования</a>'
    if old_m in s:
        s = s.replace(old_m, new_m, 1)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
