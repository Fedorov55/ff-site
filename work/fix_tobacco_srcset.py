path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/cases.html'
s = open(path, encoding='utf-8').read()
original = s
# Fix tobacco srcset
s = s.replace('srcset="img/case-tobacco.webp?v=123 400w, img/case-tobacco.webp?v=123 800w"', 'srcset="img/case-tobacco.webp?v=123"')
open(path, 'w', encoding='utf-8').write(s)
print('Updated' if s != original else 'No change')
print('Done')
