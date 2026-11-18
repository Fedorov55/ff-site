import os, re

root = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
compact = 'Штатный сисадмин обходится в 1,4 млн ₽/год. <a href="compare.html" class="u-gold">Сравнить с штатным →</a>'

replacements = {
    'index.html': [
        'Штатный сисадмин обходится в 1,4 млн ₽ в год. Абонентка F&F — от 10 000 ₽/мес, реакция от 15 минут в договоре.',
    ],
    'for-owner.html': [
        'Штатный стоит 1,4 млн ₽/год с налогами. Абонентка F&F — от 120 000 ₽/год. Команда из 4 инженеров вместо одного.',
    ],
    'services.html': [
        'Штатный один: отпуск, больничный, один навык. У нас несколько инженеров, реакция от 15 минут и 99,5% в договоре. Стоимость в 8–12 раз ниже.',
    ],
    'support.html': [
        'Штатный один: отпуск, больничный, один навык. У нас несколько инженеров, реакция от 15 минут и 99,5% в договоре. Стоимость в 8–12 раз ниже.',
    ],
}

for rel, paras in replacements.items():
    path = os.path.join(root, rel)
    s = open(path, encoding='utf-8').read()
    original = s
    parts = re.split(r'(<script[^>]*>.*?</script>)', s, flags=re.S)
    new_parts = []
    for part in parts:
        if part.startswith('<script'):
            new_parts.append(part)
            continue
        for para in paras:
            part = part.replace(para, compact)
        new_parts.append(part)
    s = ''.join(new_parts)
    if s != original:
        open(path, 'w', encoding='utf-8').write(s)
        print(f'Updated {rel}')
    else:
        print(f'No changes {rel}')
print('Done')
