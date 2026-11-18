path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/cases.html'
s = open(path, encoding='utf-8').read()
original = s

cases = [
    ('cases/case-server-kazan.html', 'Сервер под ключ в Казани', 'Казань', 'Сервер под ключ для офиса на 25 человек', 'img/case-server-turnkey.webp'),
    ('cases/case-support-kazan.html', 'Абонентка в Казани', 'Казань', 'Абонентское обслуживание офиса на 20 ПК', 'img/case-tobacco.webp'),
    ('cases/case-servers-nabchelny.html', 'Сервер в Набережных Челнах', 'Набережные Челны', 'Сервер для производства', 'img/case-server-turnkey.webp'),
    ('cases/case-security-nabchelny.html', 'ЭЦП в Набережных Челнах', 'Набережные Челны', 'Настройка ЭЦП для тендеров', 'img/case-ecp-eis.webp'),
    ('cases/case-servers-almetyevsk.html', 'Сервер в Альметьевске', 'Альметьевск', 'Сервер для нефтяной компании', 'img/case-server-turnkey.webp'),
    ('cases/case-support-almetyevsk.html', 'Абонентка в Альметьевске', 'Альметьевск', 'IT-аутсорсинг для офиса', 'img/case-tobacco.webp'),
    ('cases/case-security-nizhnekamsk.html', 'ЭЦП в Нижнекамске', 'Нижнекамск', 'Защита ПДн и ЭЦП для завода', 'img/case-ecp-eis.webp'),
    ('cases/case-support-nizhnekamsk.html', 'Абонентка в Нижнекамске', 'Нижнекамск', 'IT-аутсорсинг для промышленного офиса', 'img/case-tobacco.webp'),
    ('cases/case-support-zelendolsk.html', 'Абонентка в Зеленодольске', 'Зеленодольск', 'IT-аутсорсинг для офиса', 'img/case-tobacco.webp'),
    ('cases/case-servers-innopolis.html', 'Сервер в Иннополисе', 'Иннополис', 'Сервер для IT-компании', 'img/case-server-turnkey.webp'),
]

cards = ''
for href, title, city, desc, img in cases:
    cards += f'''<a href="{href}" class="case-card fade-up">
<div class="case-card__image">
<img src="{img}?v=123" alt="{title}" width="800" height="500" loading="lazy" decoding="async">
</div>
<div class="case-card__content">
<span class="case-card__tag">{city}</span>
<h3 class="case-card__title">{title}</h3>
<div class="case-card__result">{desc}</div>
</div>
</a>
'''

block = f'''
<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Кейсы по городам</span>
<h2 class="section__title reveal">Реальные проекты в городах Татарстана</h2>
</div>
<div class="cases__grid">
{cards}
</div>
</div>
</section>
'''

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, block + marker, 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated cases.html')
else:
    print('Marker not found')
print('Done')
