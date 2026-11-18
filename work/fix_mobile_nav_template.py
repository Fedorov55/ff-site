p='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/work/update_mobile_nav.py'
s=open(p,encoding='utf-8').read()
# Remove research from О компании group: the line after partners in that group
# We'll remove the specific line that appears in the О компании group context.
# Since there are two research lines, remove only the second occurrence.
idx = s.find('Исследования</a>\n<a href="{p}status.html"')
if idx >= 0:
    s = s[:idx] + 'Статус</a>\n' + s[idx+len('Исследования</a>\n<a href="{p}status.html"'):]
    # fix: we removed too much, need reconstruct
# Simpler: just do targeted string replacements
s = open(p,encoding='utf-8').read()
# Remove research line from О компании group (the one followed by status)
s = s.replace('<a href="{p}research.html" class="mobile-nav__link">Исследования</a>\n<a href="{p}status.html" class="mobile-nav__link">Статус</a>',
              '<a href="{p}status.html" class="mobile-nav__link">Статус</a>')
# Remove comparison-matrix from Блог group
s = s.replace('<a href="{p}comparison-matrix.html" class="mobile-nav__link">Матрица сравнения</a>\n', '')
open(p,'w',encoding='utf-8').write(s)
print('done')
# verify
s2=open(p,encoding='utf-8').read()
print('research count in template:', s2.count('Исследования</a>'))
print('comparison-matrix count in template:', s2.count('Матрица сравнения</a>'))
