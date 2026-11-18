import os

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
service_pages = [
    'support.html', 'servers.html', 'infrastructure.html', 'security.html',
    'audit.html', 'visit.html', 'vpn.html', 'services.html',
]

for rel in service_pages:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print(f'MISSING: {rel}')
        continue
    d = os.path.dirname(rel)
    prefix = '' if d in ('', '.') else '../'
    s = open(path, encoding='utf-8').read()
    original = s

    block = f'''
<section class="section reveal u-pt-0">
<div class="container">
<div class="u-max-760">
<h3 class="u-title-16">Решения</h3>
<div class="u-flex" style="flex-wrap:wrap;gap:8px;">
<a href="{prefix}hub-office.html" class="btn btn--ghost btn--sm">Офис под ключ</a>
<a href="{prefix}office-move.html" class="btn btn--ghost btn--sm">Переезд офиса</a>
<a href="{prefix}pain-server-down.html" class="btn btn--ghost btn--sm">Сервер упал</a>
<a href="{prefix}pain-1c-slow.html" class="btn btn--ghost btn--sm">1С тормозит</a>
<a href="{prefix}pain-no-backup.html" class="btn btn--ghost btn--sm">Бэкап не работает</a>
<a href="{prefix}pain-admin-left.html" class="btn btn--ghost btn--sm">Сисадмин уволился</a>
</div>
</div>
</div>
</section>
'''

    marker = '<section class="section reveal u-pt-0" aria-label="Смотрите также">'
    if marker in s:
        s = s.replace(marker, block + marker, 1)
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}')
    else:
        print(f'Marker not found in {rel}')
print('Done')
