import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/for-owner.html'
s = open(path, encoding='utf-8').read()
original = s

compact = 'Реакция от 15 минут, 99,5% в договоре. <a href="trust.html" class="u-gold">Доверие и SLA →</a>'

redundant = [
    'Ежемесячный отчёт: что сделано, что требует внимания, план на следующий месяц. SLA 99,5% в договоре. Мониторинг 24/7 — видите всё в личном кабинете.',
    'SLA распространяется на все дни и часы. Реакция от 15 минут. Команда подменяет, SLA не прерывается.',
    'Договор со SLA 99,5%, ежемесячный отчёт, мониторинг 24/7. Видите всё в личном кабинете.',
]

# Split by script tags to avoid touching JSON-LD
parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
new_parts = []
for part in parts:
    if part.startswith('<script'):
        new_parts.append(part)
    else:
        for para in redundant:
            part = part.replace(para, compact)
        new_parts.append(part)
s = ''.join(new_parts)

if s != original:
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated for-owner.html safely')
else:
    print('No changes')
print('Done')
