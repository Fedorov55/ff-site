import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/compare.html'
s = open(path, encoding='utf-8').read()
original = s

# Replace the entire "Кейсы перехода" section
pat = re.compile(r'<section id="кейсы" class="section reveal">.*?</section>', re.S)
compact = '''<section id="кейсы" class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Результаты</span>
<h2 class="section__title reveal">Кейсы перехода со штатного на аутсорсинг</h2>
</div>
<p style="text-align:center;margin-top:16px;">Кейс: экономия до 660 000 ₽/год, 0 простоев. <a href="cases.html" class="u-gold">Все кейсы →</a></p>
</div>
</section>'''

s2 = pat.sub(compact, s, count=1)
if s2 != original:
    open(path, 'w', encoding='utf-8').write(s2)
    print('Updated compare.html')
else:
    print('No changes')
print('Done')
