import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/for-owner.html'
s = open(path, encoding='utf-8').read()
original = s

pat = re.compile(r'<section class="section reveal" style="padding-top:24px;" aria-label="Связанный кейс Табачный магазин: экономи">.*?</section>', re.S)
compact = '''<section class="section reveal" style="padding-top:24px;" aria-label="Кейсы">
  <div class="container">
    <p style="text-align:center;margin:0;">Кейс: экономия до 660 000 ₽/год, 0 простоев. <a href="cases.html" class="u-gold">Все кейсы →</a></p>
  </div>
</section>'''

s2 = pat.sub(compact, s, count=1)
if s2 != original:
    open(path, 'w', encoding='utf-8').write(s2)
    print('Updated for-owner.html')
else:
    print('No changes')
print('Done')
