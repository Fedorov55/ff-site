path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

# Find the mojibake section (contains ╨)
import re
moji = '╨'
i = s.find(moji)
sec_start = s.rfind('<section', 0, i)
sec_end = s.find('</section>', i) + len('</section>')

clean_section = '''<section class="section reveal">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Аудит</span>
<h2 class="section__title reveal">Бесплатный IT-аудит</h2>
<p class="section__subtitle reveal">Проверка инфраструктуры, доступов, бэкапов. Бесплатно.</p>
</div>
<div class="u-max-760">
<h3 style="font-size:16px;font-weight:700;margin:0 0 8px;">Что входит в бесплатный аудит</h3>
<ul style="color:var(--text-2);font-size:14px;line-height:1.8;margin:0 0 16px;">
<li>Проверка доступов и паролей (реестр, кто имеет доступ)</li>
<li>Проверка бэкапов (есть ли, проверяются ли восстановлением)</li>
<li>Проверка обновлений (ОС, ПО, антивирус)</li>
<li>Проверка ЭЦП и КриптоПро (сертификаты, токены)</li>
<li>Проверка 152-ФЗ (обработка ПДн, согласия, шифрование)</li>
</ul>
<p style="color:var(--text-2);font-size:14px;line-height:1.7;margin:0 0 16px;">Экспресс-аудит за 15 минут — бесплатно. Полный аудит с отчётом — от 4 000 ₽.</p>
<div style="text-align:center;margin-top:16px;">
<a href="audit.html" class="btn btn--ghost btn--sm">Подробнее об аудите →</a>
<a href="contacts.html" class="btn btn--primary btn--sm">Записаться на аудит</a>
</div>
</div>
</div>
</section>'''

s = s[:sec_start] + clean_section + s[sec_end:]
open(path, 'w', encoding='utf-8').write(s)
print('Replaced mojibake section with clean free audit section')
print('Done')
