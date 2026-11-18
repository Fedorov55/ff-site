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

    # Update "О компании" dropdown: remove Исследования
    old_company = re.compile(r'<div class="dropdown" id="menu-company">.*?</div>', re.S)
    new_company = (
        f'<div class="dropdown" id="menu-company">'
        f'<a href="{p}about.html" class="dropdown__link">О нас</a>'
        f'<a href="{p}team.html" class="dropdown__link">Команда</a>'
        f'<a href="{p}methodology.html" class="dropdown__link">Как мы работаем</a>'
        f'<a href="{p}trust.html" class="dropdown__link">Доверие и SLA</a>'
        f'<a href="{p}partners.html" class="dropdown__link">Партнёрам</a>'
        f'<a href="{p}status.html" class="dropdown__link">Статус</a>'
        f'</div>'
    )
    s = old_company.sub(new_company, s)

    # Update "Блог" dropdown: remove Матрица сравнения
    old_blog = re.compile(r'<div class="dropdown" id="menu-blog">.*?</div>', re.S)
    new_blog = (
        f'<div class="dropdown" id="menu-blog">'
        f'<a href="{p}blog.html" class="dropdown__link">Все статьи</a>'
        f'<a href="{p}research.html" class="dropdown__link">Исследования</a>'
        f'<a href="{p}glossary.html" class="dropdown__link">Глоссарий</a>'
        f'<a href="{p}it-budget.html" class="dropdown__link">IT-бюджет 2026</a>'
        f'<a href="{p}demo.html" class="dropdown__link">Интерактивное демо</a>'
        f'<a href="{p}course.html" class="dropdown__link">Мини-курс</a>'
        f'<a href="{p}status.html" class="dropdown__link">Статус</a>'
        f'</div>'
    )
    s = old_blog.sub(new_blog, s)

    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
