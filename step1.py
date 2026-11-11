s = open('index.html', encoding='utf-8').read()

# Fix hero lead
old_lead = '<p class="hero__lead" style="font-size:18px;color:#B6BFCF;max-width:62ch;">Штатный сисадмин обходится в 1,4 млн ₽ в год. Абонентка F&F — от 10 000 ₽/мес. Реакция от 15 минут, 99,5% по договору.</p>'
new_lead = '<p class="hero__lead" style="font-size:18px;color:#B6BFCF;max-width:62ch;">Штатный сисадмин обходится в 1,4 млн ₽ в год. Абонентка F&F — от 10 000 ₽/мес, реакция от 15 минут в договоре.</p>'
assert old_lead in s
s = s.replace(old_lead, new_lead, 1)

# Remove hero bullet list
old_bullets = '''<ul class="hero__features">
<li>
<span aria-hidden="true" style="background:var(--gold-soft);color:var(--gold-light);">•</span> Реакция от 15 минут — зафиксирована в договоре, а не «в рабочее время»</li>
<li>
<span aria-hidden="true" style="background:var(--gold-soft);color:var(--gold-light);">•</span> Бэкап с обязательной проверкой восстановления — раз в квартал, не «бэкап есть»</li>
<li>
<span aria-hidden="true" style="background:var(--gold-soft);color:var(--gold-light);">•</span> Передача дел без заложников — доступы, схемы, документация при уходе</li>
</ul>'''
if old_bullets in s:
    s = s.replace(old_bullets, '', 1)

# Fix hero buttons
old_buttons = '''<div class="hero__buttons">
<a href="services.html#estimate" class="btn btn--primary">Получить расчёт стоимости за 15 минут</a>
<a href="#quiz" class="btn btn--ghost">Проверить инфраструктуру бесплатно</a>
</div>
<p style="font-size:13px;color:var(--text-2);margin-top:8px;">Без обязательств. Ответим в течение 15 минут.</p>'''
new_buttons = '''<div class="hero__buttons">
<a href="services.html#estimate" class="btn btn--primary">Рассчитать стоимость</a>
<a href="#quiz" class="btn btn--ghost">Проверить инфраструктуру</a>
</div>
<p style="font-size:13px;color:var(--text-2);margin-top:8px;">Смета до старта. Без обязательств.</p>'''
if old_buttons in s:
    s = s.replace(old_buttons, new_buttons, 1)

open('index.html', 'w', encoding='utf-8').write(s)
print('done')