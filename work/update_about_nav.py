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

    # Desktop: replace "О компании" dropdown with direct link
    company_dropdown_re = re.compile(r'<div class="nav__item"><button class="nav__trigger"[^>]*>О компании<svg.*?</svg></button>\s*<div class="dropdown" id="menu-company">.*?</div>\s*</div>', re.S)
    new_link = f'<a href="{p}about.html" class="nav__direct">О компании</a>'
    s = company_dropdown_re.sub(new_link, s, count=1)

    # Mobile: replace "О компании" group with direct link
    mobile_company_re = re.compile(r'<details class="mobile-nav__group">\s*<summary>О компании</summary>.*?</details>', re.S)
    new_mobile = f'<a href="{p}about.html" class="mobile-nav__link">О компании</a>'
    s = mobile_company_re.sub(new_mobile, s, count=1)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
