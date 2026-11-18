import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
compact = 'Кейс: экономия до 660 000 ₽/год, 0 простоев. <a href="cases.html" class="u-gold">Все кейсы →</a>'

# Repeated testimonial quote on support.html and compare.html
testimonial = '«Перешли с штатного админа. Экономия 660 тысяч в год. Бэкапы проверяют каждые 3 месяца. Спокойно.» — Ольга, руководитель офиса (Казань)'
# variations
variants = [
    '«Перешли с штатного админа. Экономия 660 тысяч в год. Бэкапы проверяют каждые 3 месяца. Спокойно.» — Ольга, руководитель офиса (Казань)',
    '«Перешли с штатного админа на абонентку. Экономия 40%. Бэкапы проверяют каждые 3 месяца. Ни одного простоя за 2 года.» — Дмитрий, собственник бизнеса (Казань, 30 ПК + 2 сервера)',
]

targets = ['support.html', 'compare.html']

for rel in targets:
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    original = s
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    new_parts = []
    for part in parts:
        if part.startswith('<script'):
            new_parts.append(part)
            continue
        for v in variants:
            part = part.replace(v, compact)
        new_parts.append(part)
    s = ''.join(new_parts)
    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}')
    else:
        print(f'No changes {rel}')
print('Done')
