import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Pattern: mobile-nav__inner block up to the closing </nav> of mobile nav
pat = re.compile(r'<div class="mobile-nav__inner" aria-label="Основная навигация">.*?</div>\s*(?=<div class="u-sticky-footer mobile-nav__footer")', re.S)

updated = 0
for f in files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    p = '' if d in ('', '.') else '../'
    s = open(f, encoding='utf-8').read()
    original = s
    new_nav = f'''<div class="mobile-nav__inner" aria-label="Основная навигация">
<a href="{p}index.html" class="mobile-nav__link">Главная</a>
<details class="mobile-nav__group">
<summary>Услуги</summary>
<div class="mobile-nav__group-links">
<a href="{p}support.html" class="mobile-nav__link">Абонентское обслуживание</a>
<a href="{p}servers.html" class="mobile-nav__link">Серверы под ключ</a>
<a href="{p}infrastructure.html" class="mobile-nav__link">Инфраструктура и сети</a>
<a href="{p}security.html" class="mobile-nav__link">Безопасность</a>
<a href="{p}audit.html" class="mobile-nav__link">IT-аудит</a>
<a href="{p}visit.html" class="mobile-nav__link">Разовый выезд</a>
<a href="{p}vpn.html" class="mobile-nav__link">VPN и удалённый доступ</a>
<a href="{p}pbx.html" class="mobile-nav__link">Телефония</a>
<a href="{p}printers.html" class="mobile-nav__link">Принтеры</a>
<a href="{p}mail.html" class="mobile-nav__link">Почта</a>
<a href="{p}services.html" class="mobile-nav__link">Все услуги и цены</a>
</div>
</details>
<details class="mobile-nav__group">
<summary>Цены</summary>
<div class="mobile-nav__group-links">
<a href="{p}services.html#calculator" class="mobile-nav__link">Калькуляторы</a>
<a href="{p}quiz.html" class="mobile-nav__link">Квиз</a>
<a href="{p}support-prices.html" class="mobile-nav__link">Тарифы</a>
<a href="{p}servers-tco.html" class="mobile-nav__link">TCO сервера</a>
<a href="{p}audit-free.html" class="mobile-nav__link">Бесплатный аудит</a>
</div>
</details>
<details class="mobile-nav__group">
<summary>Блог</summary>
<div class="mobile-nav__group-links">
<a href="{p}blog.html" class="mobile-nav__link">Все статьи</a>
<a href="{p}research.html" class="mobile-nav__link">Исследования</a>
<a href="{p}glossary.html" class="mobile-nav__link">Глоссарий</a>
<a href="{p}it-budget.html" class="mobile-nav__link">IT-бюджет 2026</a>
<a href="{p}demo.html" class="mobile-nav__link">Интерактивное демо</a>
<a href="{p}course.html" class="mobile-nav__link">Мини-курс</a>
<a href="{p}status.html" class="mobile-nav__link">Статус</a>
</div>
</details>
<details class="mobile-nav__group">
<summary>О компании</summary>
<div class="mobile-nav__group-links">
<a href="{p}about.html" class="mobile-nav__link">О нас</a>
<a href="{p}team.html" class="mobile-nav__link">Команда</a>
<a href="{p}methodology.html" class="mobile-nav__link">Как мы работаем</a>
<a href="{p}trust.html" class="mobile-nav__link">Доверие и SLA</a>
<a href="{p}partners.html" class="mobile-nav__link">Партнёрам</a>
<a href="{p}status.html" class="mobile-nav__link">Статус</a>
</div>
</details>
<a href="{p}cases.html" class="mobile-nav__link">Кейсы</a>
<a href="{p}incident.html" class="u-incident-link mobile-nav__link">Авария</a>
<a href="{p}contacts.html" class="mobile-nav__link">Контакты</a>
</div>'''
    s2 = pat.sub(new_nav, s, count=1)
    if s2 != s:
        open(f, 'w', encoding='utf-8').write(s2)
        updated += 1
print(f'Updated {updated} files')
print('Done')
