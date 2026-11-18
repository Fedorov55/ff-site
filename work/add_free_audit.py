import re
prices_path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(prices_path, encoding='utf-8').read()

af = open('C:/Users/Eblan/AppData/Local/Temp/opencode/audit-free.html', encoding='utf-8').read()
af_sections = re.findall(r'<section[^>]*>(.*?)</section>', af, re.S)
# pick section 1 (what's included) - 1324 chars
af_sec = af_sections[1]

extra = f'<section class="section reveal">\n<div class="container">\n{af_sec}\n</div>\n</section>\n'
extra = extra.replace('../index.html', 'index.html')
extra = extra.replace('../blog.html', 'blog.html')
extra = extra.replace('../audit.html', 'audit.html')
extra = extra.replace('../contacts.html', 'contacts.html')
extra = extra.replace('../services.html', 'services.html')
extra = extra.replace('../support.html', 'support.html')
extra = extra.replace('../servers.html', 'servers.html')
# Fix h1 -> h2
extra = re.sub(r'<h1([^>]*)>', r'<h2\1>', extra)
extra = extra.replace('</h1>', '</h2>')

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, extra + marker, 1)
else:
    s = s.replace('</main>', extra + '</main>', 1)

open(prices_path, 'w', encoding='utf-8').write(s)
print('Added free audit section')
print('Done')
