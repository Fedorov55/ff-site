import re
s = open('index.html', encoding='utf-8').read()

def remove_section_by_keyword(text, keyword):
    """Remove a single section containing the keyword."""
    for m in re.finditer(r'<section[^>]*>.*?</section>', text, re.S):
        if keyword in m.group(0):
            return text[:m.start()] + text[m.end():]
    return text

# Remove "Вы находитесь в разделе"
s = remove_section_by_keyword(s, 'Вы находитесь в разделе')
# Remove "Смотрите также" link block
s = remove_section_by_keyword(s, 'Смотрите также')
# Remove "Полезные статьи" link block
s = remove_section_by_keyword(s, 'Полезные статьи')
# Remove "Нужна смета или консультация?" orphan CTA
s = remove_section_by_keyword(s, 'Нужна смета или консультация?')
# Remove "Бэкапы не восстанавливаются?" orphan
s = remove_section_by_keyword(s, 'Бэкапы не восстанавливаются')

# Remove "Мы не пряchem цены" and "Почему нам можно доверять" sections
s1 = remove_section_by_keyword(s, 'Мы не пряchem цены')
s2 = remove_section_by_keyword(s1, 'Почему нам можно доверять')

# Insert price block where the first removed section was
# Find position between "Что берём на себя" and "Три работы с цифрой"
price_block = '''<section class="section reveal" style="padding-top:24px;">
<div class="container">
<div style="max-width:860px;margin:0 auto;padding:24px;border:1px solid var(--border);border-radius:16px;background:var(--card);">
<h2 style="font-size:22px;font-weight:700;margin:0 0 12px;color:var(--text);">Цена в договоре, доступы ваши</h2>
<p style="font-size:15px;color:var(--text-2);line-height:1.7;margin:0 0 16px;">Абонентка от 10 000 ₽/мес. Сервер для офиса 10–15 человек от 200 000 ₽. Настройка от 4 000 ₽.</p>
<p style="font-size:15px;color:var(--text-2);line-height:1.7;margin:0 0 16px;">Новая работа отдельной строкой. Сюрприз в акте не считается сметой.</p>
<p style="font-size:15px;color:var(--text-2);line-height:1.7;margin:0;">При уходе отдаём пароли, схемы и паспорт линий. Это занимает 3–5 рабочих дней и фиксируется в акте.</p>
</div>
</div>
</section>
'''
# Insert before "Три работы с цифрой" section
tri_marker = '<section'  # we'll find the one containing "Три работы с цифрой"
for m in re.finditer(r'<section[^>]*>.*?</section>', s2, re.S):
    if 'Три работы с цифрой' in m.group(0):
        s2 = s2[:m.start()] + price_block + s2[m.start():]
        break

open('index.html', 'w', encoding='utf-8').write(s2)
print('done')