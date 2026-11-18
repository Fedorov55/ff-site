import re
prices_path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(prices_path, encoding='utf-8').read()

# Extract from comparison-matrix
cm = open('C:/Users/Eblan/AppData/Local/Temp/opencode/comparison-matrix.html', encoding='utf-8').read()
cm_sections = re.findall(r'<section[^>]*>(.*?)</section>', cm, re.S)

# Extract from audit-free
af = open('C:/Users/Eblan/AppData/Local/Temp/opencode/audit-free.html', encoding='utf-8').read()
af_sections = re.findall(r'<section[^>]*>(.*?)</section>', af, re.S)

extra = ''
# comparison table: find section with "Матрица" or "Штатный"
for sec in cm_sections:
    if 'Матрица' in sec or 'Штатный' in sec or 'сравнени' in sec.lower():
        extra += f'<section class="section reveal">\n<div class="container">\n{sec}\n</div>\n</section>\n'
        break

# free audit: find section with "Бесплатный" or "Проверка"
for sec in af_sections:
    if 'Бесплатный' in sec or 'Проверка' in sec or 'аудит' in sec.lower():
        extra += f'<section class="section reveal">\n<div class="container">\n{sec}\n</div>\n</section>\n'
        break

# Fix relative links: ../ -> (none, since prices.html is root)
extra = extra.replace('../index.html', 'index.html')
extra = extra.replace('../blog.html', 'blog.html')
extra = extra.replace('../audit.html', 'audit.html')
extra = extra.replace('../contacts.html', 'contacts.html')
extra = extra.replace('../services.html', 'services.html')
extra = extra.replace('../support.html', 'support.html')
extra = extra.replace('../servers.html', 'servers.html')

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, extra + marker, 1)
else:
    s = s.replace('</main>', extra + '</main>', 1)

open(prices_path, 'w', encoding='utf-8').write(s)
print('Added comparison + free audit sections')
print('Done')
