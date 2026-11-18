path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/vybor-podryadchika.html'
s = open(path, encoding='utf-8').read()
original = s

block = '''
<section class="section reveal u-pt-0">
<div class="container">
<div style="max-width:760px;margin:0 auto;text-align:center;padding:32px 24px;border:2px solid var(--gold-light);border-radius:16px;background:var(--card);">
<h2 style="font-size:24px;font-weight:700;margin:0 0 12px;color:var(--gold-light);">Мини-курс: как выбрать IT-подрядчика</h2>
<p style="font-size:15px;color:var(--text-2);line-height:1.7;margin:0 0 20px;">4 письма за 6 дней: 12 вопросов, красные флаги, что смотреть в договоре, как проверить подрядчика. Скачайте бесплатно.</p>
<a href="files/course.pdf" class="btn btn--primary" download>Скачать мини-курс PDF</a>
</div>
</div>
</section>
'''

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, block + marker, 1)
else:
    s = s.replace('</main>', block + '</main>', 1)

open(path, 'w', encoding='utf-8').write(s)
print('Updated vybor-podryadchika.html')
print('Done')
