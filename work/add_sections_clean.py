import re

prices_path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(prices_path, encoding='utf-8').read()

# Read comparison-matrix with BOM handling
cm = open('C:/Users/Eblan/AppData/Local/Temp/opencode/comparison-matrix.html', encoding='utf-8-sig').read()
cm_sections = re.findall(r'<section[^>]*>(.*?)</section>', cm, re.S)

# Read audit-free with BOM handling
af = open('C:/Users/Eblan/AppData/Local/Temp/opencode/audit-free.html', encoding='utf-8-sig').read()
af_sections = re.findall(r'<section[^>]*>(.*?)</section>', af, re.S)

extra = ''

# Comparison table: find section with "Матрица" or "Штатный" or longest
cm_sec = None
for sec in cm_sections:
    if 'Матрица' in sec or 'Штатный' in sec or 'сравнени' in sec.lower():
        cm_sec = sec
        break
if not cm_sec:
    cm_sec = max(cm_sections, key=len)
extra += f'<section class="section reveal">\n<div class="container">\n{cm_sec}\n</div>\n</section>\n'

# Free audit: find section with "Бесплатный" or "Проверка" or longest
af_sec = None
for sec in af_sections:
    if 'Бесплатный' in sec or 'Проверка' in sec:
        af_sec = sec
        break
if not af_sec:
    af_sec = max(af_sections, key=len)
extra += f'<section class="section reveal">\n<div class="container">\n{af_sec}\n</div>\n</section>\n'

# Cloud comparison from articles/server-vs-cloud.html
sv = open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/articles/server-vs-cloud.html', encoding='utf-8').read()
sv_sections = re.findall(r'<section[^>]*>(.*?)</section>', sv, re.S)
sv_sec = None
for sec in sv_sections:
    if 'облако' in sec.lower() or 'сервер' in sec.lower():
        sv_sec = sec
        break
if sv_sec:
    extra += f'<section class="section reveal">\n<div class="container">\n{sv_sec}\n</div>\n</section>\n'

# Fix relative links
extra = extra.replace('../index.html', 'index.html')
extra = extra.replace('../blog.html', 'blog.html')
extra = extra.replace('../audit.html', 'audit.html')
extra = extra.replace('../contacts.html', 'contacts.html')
extra = extra.replace('../services.html', 'services.html')
extra = extra.replace('../support.html', 'support.html')
extra = extra.replace('../servers.html', 'servers.html')

# Fix h1 -> h2 in extra
extra = re.sub(r'<h1([^>]*)>', r'<h2\1>', extra)
extra = extra.replace('</h1>', '</h2>')

# Insert before "Смотрите также"
marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, extra + marker, 1)
else:
    s = s.replace('</main>', extra + '</main>', 1)

open(prices_path, 'w', encoding='utf-8').write(s)
print('Added comparison + free audit + cloud comparison sections')
print('Done')
