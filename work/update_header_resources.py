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

    # Update desktop "Блог" dropdown -> "Ресурсы"
    old_blog = re.compile(r'<div class="dropdown" id="menu-blog">.*?</div>', re.S)
    new_resources = (
        f'<div class="dropdown" id="menu-resources">'
        f'<a href="{p}blog.html" class="dropdown__link">Блог</a>'
        f'<a href="{p}articles.html" class="dropdown__link">Статьи</a>'
        f'<a href="{p}research.html" class="dropdown__link">Исследования</a>'
        f'<a href="{p}it-budget.html" class="dropdown__link">IT-бюджет 2026-2027</a>'
        f'</div>'
    )
    # Also update the trigger button text from "Блог" to "Ресурсы"
    s = s.replace('<button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="menu-blog" data-nav-trigger>Блог<svg', '<button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="menu-resources" data-nav-trigger>Ресурсы<svg')
    s = old_blog.sub(new_resources, s)

    # Update mobile "Блог" group -> "Ресурсы"
    mobile_blog_re = re.compile(r'<details class="mobile-nav__group">\s*<summary>Блог</summary>.*?</details>', re.S)
    new_mobile = f'''<details class="mobile-nav__group">
<summary>Ресурсы</summary>
<div class="mobile-nav__group-links">
<a href="{p}blog.html" class="mobile-nav__link">Блог</a>
<a href="{p}articles.html" class="mobile-nav__link">Статьи</a>
<a href="{p}research.html" class="mobile-nav__link">Исследования</a>
<a href="{p}it-budget.html" class="mobile-nav__link">IT-бюджет 2026-2027</a>
</div>
</details>'''
    s = mobile_blog_re.sub(new_mobile, s)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
