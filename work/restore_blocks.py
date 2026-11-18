path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html'
s = open(path, encoding='utf-8').read()
original = s

team_block = '''<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Команда</span>
<h2 class="section__title reveal">Четыре человека из Казани</h2>
<p class="section__subtitle reveal">Булат, Эмиль, Диляра, Руслан — инженеры, которые отвечают за ваш офис.</p>
</div>
<div class="team__grid" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;">
<div class="team-card" style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;">
<h3 style="font-size:18px;font-weight:800;margin:0 0 4px;color:var(--text);">Булат</h3>
<p style="font-size:13px;color:var(--text-2);margin:0;">Технический директор</p>
</div>
<div class="team-card" style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;">
<h3 style="font-size:18px;font-weight:800;margin:0 0 4px;color:var(--text);">Эмиль</h3>
<p style="font-size:13px;color:var(--text-2);margin:0;">Главный инженер</p>
</div>
<div class="team-card" style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;">
<h3 style="font-size:18px;font-weight:800;margin:0 0 4px;color:var(--text);">Диляра</h3>
<p style="font-size:13px;color:var(--text-2);margin:0;">Специалист первой линии</p>
</div>
<div class="team-card" style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;">
<h3 style="font-size:18px;font-weight:800;margin:0 0 4px;color:var(--text);">Руслан</h3>
<p style="font-size:13px;color:var(--text-2);margin:0;">Выезды и монтаж</p>
</div>
</div>
<p style="text-align:center;margin-top:16px;"><a href="team.html" class="u-gold">Вся команда →</a></p>
</div>
</section>
'''

calc_block = '''<section class="section reveal u-pt-0">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Калькулятор</span>
<h2 class="section__title reveal">Рассчитать стоимость IT-поддержки</h2>
<p class="section__subtitle reveal">Соберите контур за 3 шага. Без звонка.</p>
</div>
<div style="text-align:center;">
<a href="services.html#calculator" class="btn btn--primary">Рассчитать стоимость</a>
</div>
</section>
'''

# Insert before "Смотрите также" section
marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, team_block + calc_block + marker, 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Inserted team and calculator blocks before "Смотрите также"')
else:
    print('Marker not found')
print('Done')
