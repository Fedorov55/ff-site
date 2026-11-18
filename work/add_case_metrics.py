import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'

metrics = {
    'cases/case-server-kazan.html': [
        ('Экономия', '660 000 ₽/год'),
        ('Простои', '0 за 6 мес.'),
        ('Реакция', '15 мин'),
        ('Абонентка', '42 000 ₽/мес'),
    ],
    'cases/case-support-kazan.html': [
        ('Экономия', '800 000 ₽/год'),
        ('Простои', '0 за 2 года'),
        ('Реакция', '15 мин'),
        ('Абонентка', 'от 25 000 ₽/мес'),
    ],
    'cases/case-servers-nabchelny.html': [
        ('Ускорение 1С', 'в 5 раз'),
        ('Простои', '0 за 6 мес.'),
        ('Отчёт', '30 сек (было 10 мин)'),
        ('Сервер', 'от 200 000 ₽'),
    ],
    'cases/case-security-nabchelny.html': [
        ('Рабочих мест', '5'),
        ('Время настройки', '1 день'),
        ('Ошибки ЭЦП', '0'),
        ('ЭЦП', 'от 1 200 ₽'),
    ],
    'cases/case-servers-almetyevsk.html': [
        ('Сервер', 'от 200 000 ₽'),
        ('Простои', '0 за 6 мес.'),
        ('Реакция', '15 мин'),
        ('Абонентка', 'от 25 000 ₽/мес'),
    ],
    'cases/case-support-almetyevsk.html': [
        ('Экономия', 'до 1,4 млн ₽/год'),
        ('Простои', '0'),
        ('Реакция', '15 мин'),
        ('Абонентка', 'от 15 000 ₽/мес'),
    ],
    'cases/case-security-nizhnekamsk.html': [
        ('Штрафы', '0'),
        ('Защита ПДн', 'настроена'),
        ('ЭЦП', 'работает без сбоев'),
        ('Аудит ИБ', 'проведён'),
    ],
    'cases/case-support-nizhnekamsk.html': [
        ('Экономия', 'до 1,4 млн ₽/год'),
        ('Простои', '0'),
        ('Реакция', '15 мин'),
        ('Абонентка', 'от 25 000 ₽/мес'),
    ],
    'cases/case-support-zelendolsk.html': [
        ('Экономия', 'до 1,4 млн ₽/год'),
        ('Простои', '0'),
        ('Реакция', '15 мин'),
        ('Абонентка', 'от 10 000 ₽/мес'),
    ],
    'cases/case-servers-innopolis.html': [
        ('Сервер', 'от 200 000 ₽'),
        ('Простои', '0'),
        ('Виртуализация', 'Proxmox'),
        ('Абонентка', 'от 30 000 ₽/мес'),
    ],
}

for case_path, metric_list in metrics.items():
    full_path = os.path.join(root, case_path)
    if not os.path.exists(full_path):
        print(f'MISSING: {case_path}')
        continue
    s = open(full_path, encoding='utf-8').read()
    original = s

    # Build metrics block
    metrics_html = '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:24px 0;">\n'
    for label, value in metric_list:
        metrics_html += f'<div style="background:var(--card);border:1px solid var(--border);border-radius:var(--radius-sm);padding:16px;text-align:center;"><div style="font-size:12px;color:var(--muted);margin-bottom:4px;">{label}</div><div style="font-size:18px;font-weight:800;color:var(--gold-light);">{value}</div></div>\n'
    metrics_html += '</div>\n'

    # Insert after "Что изменилось" paragraph
    s = re.sub(
        r'(<h2>Что изменилось</h2>\s*<p>.*?</p>)',
        f'\\1\n{metrics_html}',
        s,
        count=1,
        flags=re.S
    )

    if s != original:
        open(full_path, 'w', encoding='utf-8').write(s)
        print(f'Updated {case_path}')
    else:
        print(f'No changes {case_path}')

print('Done')
