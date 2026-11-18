import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services.html'
s = open(path, encoding='utf-8').read()
original = s

pat = re.compile(r'<section class="section reveal u-pt-0">\s*<div class="container">\s*<div class="section__head fade-up reveal">\s*<span class="section__label reveal">Кейсы</span>.*?</section>', re.S)
compact = '''<section class="section reveal u-pt-0">
<div class="container">
<p style="text-align:center;margin:0;">Кейс: экономия до 660 000 ₽/год, 0 простоев. <a href="cases.html" class="u-gold">Все кейсы →</a></p>
</div>
</section>'''

s2 = pat.sub(compact, s, count=1)
if s2 != original:
    open(path, 'w', encoding='utf-8').write(s2)
    print('Updated services.html')
else:
    print('No changes')
print('Done')
