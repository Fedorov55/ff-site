import re
s = open('index.html', encoding='utf-8').read()

# Remove "Вы находитесь в разделе" section
def remove_vy(m):
    if 'Вы находитесь в разделе' in m.group(0):
        return ''
    return m.group(0)
s = re.sub(r'<section[^>]*>.*?</section>\s*', remove_vy, s, flags=re.S)

# Merge "Мы не пряchem цены" and "Почему нам можно доверять" into price block
def find_section(text, keyword):
    for m in re.finditer(r'<section[^>]*>.*?</section>', text, re.S):
        if keyword in m.group(0):
            return m
    return None

m1 = find_section(s, 'Мы не пряchem цены')
m2 = find_section(s, 'Почему нам можно доверять')

if m1 and m2:
    start = m1.start()
    end = m2.end()
    new_price = '''<section class="section reveal" style="padding-top:24px;">
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
    s = s[:start] + new_price + s[end:]
    print('price block merged')

open('index.html', 'w', encoding='utf-8').write(s)
print('done')