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

    # Desktop: replace "Услуги" dropdown with direct link
    services_dropdown_re = re.compile(r'<div class="nav__item"><button class="nav__trigger"[^>]*>Услуги<svg.*?</svg></button>\s*<div class="dropdown" id="menu-services">.*?</div>\s*</div>', re.S)
    new_services_link = f'<a href="{p}services.html" class="nav__direct">Услуги</a>'
    s = services_dropdown_re.sub(new_services_link, s, count=1)

    # Desktop: add "Авария" link before "Контакты" (if not already)
    contacts_root = '<a href="contacts.html" class="nav__direct">Контакты</a>'
    contacts_sub = f'<a href="{p}contacts.html" class="nav__direct">Контакты</a>'
    incident_link = f'<a href="{p}incident.html" class="u-incident mobile-nav__link nav__direct">Авария</a>' if False else f'<a href="{p}incident.html" class="nav__direct" style="color:var(--danger);">Авария</a>'
    # Actually use a cleaner approach: add after "Кейсы" direct link
    cases_root = '<a href="cases.html" class="nav__direct">Кейсы</a>'
    cases_sub = f'<a href="{p}cases.html" class="nav__direct">Кейсы</a>'
    if cases_root in s and 'incident.html' not in s.split(cases_root)[1][:80] if cases_root in s else True:
        s = s.replace(cases_root, cases_root + '\n' + f'<a href="{p}incident.html" class="nav__direct" style="color:var(--danger);font-weight:700;">Авария</a>', 1)
    elif cases_sub in s and 'incident.html' not in s.split(cases_sub)[1][:80] if cases_sub in s else True:
        s = s.replace(cases_sub, cases_sub + '\n' + f'<a href="{p}incident.html" class="nav__direct" style="color:var(--danger);font-weight:700;">Авария</a>', 1)

    # Mobile: replace "Услуги" group with direct link
    mobile_services_re = re.compile(r'<details class="mobile-nav__group">\s*<summary>Услуги</summary>.*?</details>', re.S)
    new_mobile_services = f'<a href="{p}services.html" class="mobile-nav__link">Услуги</a>'
    s = mobile_services_re.sub(new_mobile_services, s, count=1)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
