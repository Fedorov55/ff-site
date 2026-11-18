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

    # Replace direct Blog link with Blog dropdown
    old_blog = '<a href="blog.html" class="nav__direct">Блог</a>'
    new_blog = (
        f'<div class="nav__item"><button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="menu-blog" data-nav-trigger>Блог<svg viewBox="0 0 20 20" aria-hidden="true"><path d="m5 7 5 5 5-5"/></svg></button>'
        f'<div class="dropdown" id="menu-blog">'
        f'<a href="{p}blog.html" class="dropdown__link">Все статьи</a>'
        f'<a href="{p}research.html" class="dropdown__link">Исследования</a>'
        f'<a href="{p}glossary.html" class="dropdown__link">Глоссарий</a>'
        f'<a href="{p}comparison-matrix.html" class="dropdown__link">Матрица сравнения</a>'
        f'<a href="{p}it-budget.html" class="dropdown__link">IT-бюджет 2026</a>'
        f'<a href="{p}demo.html" class="dropdown__link">Интерактивное демо</a>'
        f'<a href="{p}course.html" class="dropdown__link">Мини-курс</a>'
        f'<a href="{p}status.html" class="dropdown__link">Статус</a>'
        f'</div></div>'
    )
    # adjust hrefs for subdir
    if d not in ('', '.'):
        old_blog_sub = f'<a href="{p}blog.html" class="nav__direct">Блог</a>'
        # but original uses blog.html without prefix in root? In subdir files, blog.html should be ../blog.html
        # Actually, in subdir files, the link is ../blog.html. Let's handle both.
        pass

    # Try replacing root-style first, then subdir-style
    if old_blog in s:
        s = s.replace(old_blog, new_blog, 1)
    else:
        old_blog2 = f'<a href="{p}blog.html" class="nav__direct">Блог</a>'
        if old_blog2 in s:
            s = s.replace(old_blog2, new_blog, 1)

    # Add "Цены" dropdown before "Контакты" direct link
    # Find contacts direct link
    contacts_pattern_root = '<a href="contacts.html" class="nav__direct">Контакты</a>'
    contacts_pattern_sub = f'<a href="{p}contacts.html" class="nav__direct">Контакты</a>'
    prices_dropdown = (
        f'<div class="nav__item"><button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="menu-prices" data-nav-trigger>Цены<svg viewBox="0 0 20 20" aria-hidden="true"><path d="m5 7 5 5 5-5"/></svg></button>'
        f'<div class="dropdown" id="menu-prices">'
        f'<a href="{p}comparison-matrix.html" class="dropdown__link">Матрица сравнения</a>'
        f'<a href="{p}services.html#calculator" class="dropdown__link">Калькуляторы</a>'
        f'<a href="{p}quiz.html" class="dropdown__link">Квиз</a>'
        f'<a href="{p}support-prices.html" class="dropdown__link">Тарифы</a>'
        f'<a href="{p}servers-tco.html" class="dropdown__link">TCO сервера</a>'
        f'<a href="{p}audit-free.html" class="dropdown__link">Бесплатный аудит</a>'
        f'</div></div>'
    )
    if contacts_pattern_root in s:
        s = s.replace(contacts_pattern_root, prices_dropdown + contacts_pattern_root, 1)
    elif contacts_pattern_sub in s:
        s = s.replace(contacts_pattern_sub, prices_dropdown + contacts_pattern_sub, 1)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
