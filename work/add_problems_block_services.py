path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services.html'
s = open(path, encoding='utf-8').read()
original = s

block = '''
<section class="section reveal u-pt-0">
<div class="container">
<div class="section__head fade-up reveal">
<span class="section__label reveal">Проблемы</span>
<h2 class="section__title reveal">Что ломается и как решаем</h2>
</div>
<div class="u-flex" style="flex-wrap:wrap;gap:8px;">
<a href="pain-1c-slow.html" class="btn btn--ghost btn--sm">1С тормозит</a>
<a href="pain-server-down.html" class="btn btn--ghost btn--sm">Сервер упал в субботу</a>
<a href="pain-admin-left.html" class="btn btn--ghost btn--sm">Сисадмин уволился</a>
<a href="pain-no-backup.html" class="btn btn--ghost btn--sm">Бэкап не работает</a>
<a href="pain-no-internet.html" class="btn btn--ghost btn--sm">Нет интернета</a>
<a href="pain-new-employee.html" class="btn btn--ghost btn--sm">Новый сотрудник без места</a>
<a href="pain-astra.html" class="btn btn--ghost btn--sm">Переход на Astra Linux</a>
</div>
</div>
</section>
'''

marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
if marker in s:
    s = s.replace(marker, block + marker, 1)
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated services.html')
else:
    print('Marker not found')
print('Done')
