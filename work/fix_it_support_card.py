import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

# Find the broken card
pat = re.compile(r'<a href="services/it-support.html" class="service-card fade-up">.*?</a>', re.S)
m = pat.search(s)
if m:
    print('Found broken card:', m.group(0)[:300])
    # Replace with correct card
    correct = '''<a href="services/it-support.html" class="service-card fade-up">
<div class="service-card__icon">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
<path d="M4 7h16M4 12h16M4 17h10"/></svg>
</div>
<h3 class="service-card__title">IT-обслуживание офиса</h3>
<p class="service-card__text">Абонентский сисадмин, мониторинг, бэкапы.</p>
<div class="service-card__price">от 10 000 ₽/мес</div>
</a>'''
    s = pat.sub(correct, s, count=1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Fixed')
else:
    print('Pattern not found')
print('Done')
