import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/for-owner.html'
s = open(path, encoding='utf-8').read()
original = s

# Compact replacement
compact = 'Реакция от 15 минут, 99,5% в договоре. <a href="trust.html" class="u-gold">Доверие и SLA →</a>'

# Replace redundant SLA paragraphs (exact matches)
redundant = [
    'Ежемесячный отчёт: что сделано, что требует внимания, план на следующий месяц. SLA 99,5% в договоре. Мониторинг 24/7 — видите всё в личном кабинете.',
    'SLA распространяется на все дни и часы. Реакция от 15 минут. Команда подменяет, SLA не прерывается.',
    'Договор со SLA 99,5%, ежемесячный отчёт, мониторинг 24/7. Видите всё в личном кабинете.',
]
for para in redundant:
    # replace in <p> tags
    s = s.replace(f'<p>{para}</p>', f'<p>{compact}</p>')
    s = s.replace(f'<p class="u-text-2-sm">{para}</p>', f'<p class="u-text-2-sm">{compact}</p>')
    # also inline (no p wrapper)
    s = s.replace(para, compact)

if s != original:
    open(path, 'w', encoding='utf-8').write(s)
    print('Updated for-owner.html')
    print('Replacements made:', sum(1 for p in redundant if p in original))
else:
    print('No changes')
print('Done')
