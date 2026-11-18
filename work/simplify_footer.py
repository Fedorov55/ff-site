import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

footer_re = re.compile(r'<footer class="footer">.*?</footer>', re.S)

updated = 0
for f in files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    prefix = '' if d in ('', '.') else '../'
    s = open(f, encoding='utf-8').read()
    original = s

    new_footer = f'''<footer class="footer">
<div class="container">
<div class="footer__grid" style="grid-template-columns: 1fr 1fr; gap: 24px;">
<div>
<div class="footer__brand gold">F&amp;F</div>
<p class="u-fs-13 footer__desc">Казань, Республика Татарстан</p>
</div>
<div>
<div class="footer__title">Контакты</div>
<a href="tel:+79012655252" class="footer__link">+7 (901) 265-52-52</a>
<a href="mailto:FathFed@yandex.ru" class="footer__link">FathFed@yandex.ru</a>
<a href="{prefix}services.html#estimate" class="u-mt-8 btn btn--primary btn--sm">Получить смету</a>
</div>
</div>
<div class="footer__bottom">
<div>© 2026 F&amp;F. Все права защищены.</div>
<div>
<a href="{prefix}privacy.html" class="footer__link">Политика конфиденциальности</a> ·
<a href="{prefix}terms.html" class="footer__link">Условия использования</a> ·
<a href="{prefix}cookie.html" class="footer__link">Cookie</a>
</div>
</div>
</div>
</footer>'''

    s = footer_re.sub(new_footer, s, count=1)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1

print(f'Updated {updated} files')
print('Done')
