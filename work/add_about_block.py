path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s = open(path, encoding='utf-8').read()
original = s

block = '''
<section class="section reveal u-pt-0">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">О компании</h3>
<div class="u-flex" style="flex-wrap:wrap;gap:8px;">
<a href="team.html" class="btn btn--ghost btn--sm">Команда</a>
<a href="methodology.html" class="btn btn--ghost btn--sm">Как мы работаем</a>
<a href="trust.html" class="btn btn--ghost btn--sm">Доверие и SLA</a>
<a href="partners.html" class="btn btn--ghost btn--sm">Партнёрам</a>
<a href="research.html" class="btn btn--ghost btn--sm">Исследования</a>
<a href="status.html" class="btn btn--ghost btn--sm">Статус</a>
</div>
</div>
</div>
</section>
'''

if '</main>' in s:
    s = s.replace('</main>', block + '</main>', 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated about.html')
else:
    print('No </main> found')
print('Done')
