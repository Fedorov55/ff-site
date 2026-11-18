import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

# Fix vpn.html stray >
path = os.path.join(root, 'vpn.html')
s = open(path, encoding='utf-8').read()
s = s.replace('>\n<h2 class="u-title-16">Смотрите также</h2>', '\n<h2 class="u-title-16">Смотрите также</h2>')
open(path, 'w', encoding='utf-8').write(s)
print('Fixed vpn.html')

# Fix cases.html corrupted img tag
path = os.path.join(root, 'cases.html')
s = open(path, encoding='utf-8').read()
s = s.replace('<img case-cardbp?v=123"', '<img src="img/case-ecp-eis.webp?v=123"')
open(path, 'w', encoding='utf-8').write(s)
print('Fixed cases.html')
print('Done')
