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

    # Desktop: add Хаб before Контакты
    contacts_root = '<a href="contacts.html" class="nav__direct">Контакты</a>'
    contacts_sub = f'<a href="{p}contacts.html" class="nav__direct">Контакты</a>'
    hub_link = f'<a href="{p}hub.html" class="nav__direct">Хаб</a>'
    if contacts_root in s:
        s = s.replace(contacts_root, hub_link + '\n' + contacts_root, 1)
    elif contacts_sub in s:
        s = s.replace(contacts_sub, hub_link + '\n' + contacts_sub, 1)

    # Mobile: add Хаб before Контакты
    mobile_root = '<a href="contacts.html" class="mobile-nav__link">Контакты</a>'
    mobile_sub = f'<a href="{p}contacts.html" class="mobile-nav__link">Контакты</a>'
    hub_mobile = f'<a href="{p}hub.html" class="mobile-nav__link">Хаб</a>'
    if mobile_root in s:
        s = s.replace(mobile_root, hub_mobile + '\n' + mobile_root, 1)
    elif mobile_sub in s:
        s = s.replace(mobile_sub, hub_mobile + '\n' + mobile_sub, 1)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
