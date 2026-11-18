import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

moji = set('╨╤╥╙╘╒╓╫╪┘┌█▄▌▐▀■□▪▫▬▲►◄↕‼¶§▬ ')

# Find all sections with mojibake
sections = list(re.finditer(r'<section[^>]*>(.*?)</section>', s, re.S))
moji_sections = []
for m in sections:
    if any(c in m.group(1) for c in moji):
        moji_sections.append(m)

print(f'Found {len(moji_sections)} mojibake sections')

# Replace from last to first to preserve indices
for m in reversed(moji_sections):
    sec_start = m.start()
    sec_end = m.end()
    # Determine which clean section to use based on position/content
    # Section 11 (comparison) -> clean comparison table
    # Section 12 (FAQ) -> clean FAQ
    if sec_start < (len(s) // 2):
        # first mojibake section -> comparison table
        clean = '''<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Сравнение</span>
<h2 class="section__title reveal">Матрица сравнения: штатный vs аутсорсинг</h2>
</div>
<div style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:14px;">
<thead>
<tr style="border-bottom:2px solid var(--border);">
<th style="text-align:left;padding:12px 8px;color:var(--muted);">Критерий</th>
<th style="text-align:left;padding:12px 8px;">Штатный сисадмин</th>
<th style="text-align:left;padding:12px 8px;color:var(--gold-light);">F&F</th>
</tr>
</thead>
<tbody>
<tr class="u-border-bottom">
<td style="padding:12px 8px;font-weight:600;">Стоимость в год</td>
<td style="padding:12px 8px;">1,4–1,8 млн ₽</td>
<td style="padding:12px 8px;color:var(--gold-light);">от 120 000 ₽</td>
</tr>
<tr class="u-border-bottom">
<td style="padding:12px 8px;font-weight:600;">Доступность</td>
<td style="padding:12px 8px;">Зависит от человека</td>
<td style="padding:12px 8px;color:var(--gold-light);">99,5% по SLA</td>
</tr>
<tr class="u-border-bottom">
<td style="padding:12px 8px;font-weight:600;">Реакция</td>
<td style="padding:12px 8px;">Когда освободится</td>
<td style="padding:12px 8px;color:var(--gold-light);">От 15 минут</td>
</tr>
<tr class="u-border-bottom">
<td style="padding:12px 8px;font-weight:600;">Бэкапы</td>
<td style="padding:12px 8px;">Часто нет</td>
<td style="padding:12px 8px;color:var(--gold-light);">3-2-1, проверка раз в квартал</td>
</tr>
<tr class="u-border-bottom">
<td style="padding:12px 8px;font-weight:600;">Документация</td>
<td style="padding:12px 8px;">В голове у админа</td>
<td style="padding:12px 8px;color:var(--gold-light);">Схемы, пароли, регламенты</td>
</tr>
<tr>
<td style="padding:12px 8px;font-weight:600;">Замена при болезни</td>
<td style="padding:12px 8px;">Нет</td>
<td style="padding:12px 8px;color:var(--gold-light);">Команда из 4 инженеров</td>
</tr>
</tbody>
</table>
</div>
<p style="text-align:center;margin-top:16px;"><a href="compare.html" class="u-gold">Подробнее о сравнении →</a></p>
</div>
</section>'''
    else:
        clean = '''<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">FAQ</span>
<h2 class="section__title reveal">Частые вопросы о ценах</h2>
</div>
<div class="faq">
<details class="faq__item">
<summary class="faq__q">Сколько стоит абонентское обслуживание?</summary>
<p class="faq__a">От 10 000 ₽/мес или от 900 ₽ за ПК (берётся большая сумма). Точный расчёт — в калькуляторе выше.</p>
</details>
<details class="faq__item">
<summary class="faq__q">Что входит в абонентку?</summary>
<p class="faq__a">Мониторинг 24/7, выезд по Казани, реакция от 15 минут, бэкапы с проверкой восстановления, обновления, консультации.</p>
</details>
<details class="faq__item">
<summary class="faq__q">Можно ли получить бесплатный аудит?</summary>
<p class="faq__a">Да, экспресс-аудит за 15 минут — бесплатно. Полный аудит с отчётом — от 4 000 ₽.</p>
</details>
<details class="faq__item">
<summary class="faq__q">Что если сервер уже не работает?</summary>
<p class="faq__a">Звоните +7 (901) 265-52-52. Реакция от 15 минут. Мы не гадаем пароли — у нас есть реестр доступов и бэкапы.</p>
</details>
</div>
</div>
</section>'''
    s = s[:sec_start] + clean + s[sec_end:]

open(path, 'w', encoding='utf-8').write(s)
print('Replaced mojibake sections with clean content')
print('Done')
# verify
s2 = open(path, encoding='utf-8').read()
moji = [c for c in s2 if ord(c)>127 and not (0x0400<=ord(c)<=0x04FF) and c not in '—–…«»„“”' and c not in ' \xa0·→₽©×']
print('remaining mojibake:', set(moji))
print('H1 count:', len(__import__('re').findall(r'<h1[^>]*>(.*?)</h1>', s2, __import__('re').S)))
