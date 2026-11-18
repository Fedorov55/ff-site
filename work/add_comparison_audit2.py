import re
prices_path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(prices_path, encoding='utf-8').read()

cm = open('C:/Users/Eblan/AppData/Local/Temp/opencode/comparison-matrix.html', encoding='utf-8').read()
cm_sections = re.findall(r'<section[^>]*>(.*?)</section>', cm, re.S)
# pick the longest section (likely the comparison table)
cm_sec = max(cm_sections, key=len)

af = open('C:/Users/Eblan/AppData/Local/Temp/opencode/audit-free.html', encoding='utf-8').read()
af_sections = re.findall(r'<section[^>]*>(.*?)</section>', af, re.S)
# pick the longest section (likely the free audit content)
af_sec = max(af_sections, key=len)

extra = ''
extra += f'<section class="section reveal">\n<div class="container">\n{cm_sec}\n</div>\n</section>\n'
extra += f'<section class="section reveal">\n<div class="container">\n{af_sec}\n</div>\n</section>\n'

# Fix relative links
extra = extra.replace('../index.html', 'index.html')
extra = extra.replace('../blog.html', 'blog.html')
extra = extra.replace('../audit.html', 'audit.html')
extra = extra.replace('../contacts.html', 'contacts.html')
extra = extra.replace('../services.html', 'services.html')
extra = extra.replace('../support.html', 'support.html')
extra = extra.replace('../servers.html', 'servers.html')

# Fix any h1 in extra to h2
extra = re.sub(r'<h1([^>]*)>', r'<h2\1>', extra)
extra = extra.replace('</h1>', '</h2>')

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, extra + marker, 1)
else:
    s = s.replace('</main>', extra + '</main>', 1)

open(prices_path, 'w', encoding='utf-8').write(s)
print('Added comparison + free audit sections (longest)')
print('Done')
