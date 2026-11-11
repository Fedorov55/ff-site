import re
s = open('support.html', encoding='utf-8').read()

# Remove "Вы находитесь в разделе" blocks
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:860px;margin:0 auto;padding:16px;border:1px solid var\(--border\);border-radius:12px;background:var\(--card\);text-align:center;">\s*<p style="margin:0;font-size:13px;color:var\(--text-2\);">Вы находитесь в разделе:.*?</section>\s*', '', s, flags=re.S)

# Remove "VPN и удалённый доступ" section
s = re.sub(r'<section[^>]*>.*?VPN и удалённый доступ.*?</section>\s*', '', s, flags=re.S)

# Remove "Мы не прячем цены..." section
s = re.sub(r'<section[^>]*>.*?Мы не пряchem цены и не держим вас заложником.*?</section>\s*', '', s, flags=re.S)

# Remove "Почему нам можно доверять" section
s = re.sub(r'<section[^>]*>.*?Почему нам можно доверять.*?</section>\s*', '', s, flags=re.S)

# Remove "Готовы навести порядок в IT?" section
s = re.sub(r'<section[^>]*>.*?Готовы навести порядок в IT\?.*?</section>\s*', '', s, flags=re.S)

# Remove "Нужна смета или консультация?" section
s = re.sub(r'<section[^>]*>.*?Нужна смета или консультация\?.*?</section>\s*', '', s, flags=re.S)

# Remove orphan CTA sections (no heading, < 120 chars, contains buttons)
def remove_orphan(m):
    seg = m.group(1)
    text = ' '.join(re.sub(r'<[^>]+>', '', seg).split())
    if ('Рассчитать' in text or 'Позвонить' in text) and len(text) < 120 and '<h' not in seg:
        return ''
    return m.group(0)
s = re.sub(r'<section[^>]*>(.*?)</section>\s*', remove_orphan, s, flags=re.S)

# Remove "Полезные статьи" / "Смотрите также" link blocks
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;">\s*<h3[^>]*>Полезные статьи.*?</section>\s*', '', s, flags=re.S)
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;">\s*<h3[^>]*>Смотрите также.*?</section>\s*', '', s, flags=re.S)

# Add VPN link after FAQ (if not present)
if 'Удалённый доступ — на странице VPN' not in s:
    s = s.replace('</section>\n<section class="section reveal" id="reviews">', '</section>\n<p style="text-align:center;margin:16px 0;"><a href="vpn.html" style="color:var(--gold);">Удалённый доступ — на странице VPN</a></p>\n<section class="section reveal" id="reviews">', 1)

# Add final CTA before </main>
final_cta = '''
<section class="section section--end">
  <div class="container">
    <div class="end-cta">
      <h2>Посчитать абонентку под ваш офис</h2>
      <p>Число компьютеров, сервер и принтеры. Итог не ниже 10 000 ₽ в месяц.</p>
      <div class="double-cta">
        <a class="btn btn--primary" href="#calculator">Рассчитать абонентку</a>
        <a class="btn btn--ghost" href="tel:+79012655252">Позвонить +7 (901) 265-52-52</a>
      </div>
    </div>
  </div>
</section>
'''
if 'section--end' not in s:
    s = s.replace('</main>', final_cta + '\n</main>', 1)

open('support.html', 'w', encoding='utf-8').write(s)
print('done')