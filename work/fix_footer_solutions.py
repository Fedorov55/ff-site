import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
files = []
for r, ds, fs in os.walk(root):
    if '.git' in r or 'node_modules' in r or '.agents' in r:
        continue
    for f in fs:
        if f.endswith('.html'):
            files.append(os.path.join(r, f))

# Pattern: footer column with "Решения" title and 5 links
# We'll replace the whole div containing footer__title "Решения"
pat = re.compile(r'<div>\s*<div class="footer__title">Решения</div>.*?</div>\s*(?=<div>)', re.S)

new_col = '''<div>
<div class="footer__title">Ресурсы</div>
<a href="{prefix}blog.html" class="footer__link">Блог</a>
<a href="{prefix}faq.html" class="footer__link">FAQ</a>
<a href="{prefix}cases.html" class="footer__link">Кейсы</a>
<a href="{prefix}research.html" class="footer__link">Исследования</a>
<a href="{prefix}status.html" class="footer__link">Статус</a>
</div>
'''

updated = 0
for f in files:
    rel = os.path.relpath(f, root).replace('\\', '/')
    d = os.path.dirname(rel)
    prefix = '' if d in ('', '.') else '../'
    s = open(f, encoding='utf-8').read()
    original = s
    s = pat.sub(new_col.format(prefix=prefix), s, count=1)
    if s != original:
        open(f, 'w', encoding='utf-8').write(s)
        updated += 1
print(f'Updated {updated} files')
print('Done')
