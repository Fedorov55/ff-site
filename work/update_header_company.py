import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

dropdown_re = re.compile(r'<div class="dropdown" id="menu-company">.*?</div>', re.S)

updated = 0
for f in files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    prefix = '' if d in ('', '.') else '../'
    s = open(f, encoding='utf-8').read()
    original = s
    new_dropdown = (
        f'<div class="dropdown" id="menu-company">'
        f'<a href="{prefix}about.html" class="dropdown__link">О нас</a>'
        f'<a href="{prefix}team.html" class="dropdown__link">Команда</a>'
        f'<a href="{prefix}methodology.html" class="dropdown__link">Как мы работаем</a>'
        f'<a href="{prefix}trust.html" class="dropdown__link">Доверие и SLA</a>'
        f'<a href="{prefix}partners.html" class="dropdown__link">Партнёрам</a>'
        f'<a href="{prefix}research.html" class="dropdown__link">Исследования</a>'
        f'<a href="{prefix}status.html" class="dropdown__link">Статус</a>'
        f'</div>'
    )
    s = dropdown_re.sub(new_dropdown, s)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1
print(f'Updated {updated} files')
print('Done')
