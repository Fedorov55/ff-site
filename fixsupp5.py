import re
s = open('support.html', encoding='utf-8').read()

# 1. Fix calculator: add id="calculator" to the abonentka section, remove empty div
old = '<div id="calculator" style="scroll-margin-top:92px;">\n</div>'
if old in s:
    s = s.replace(old, '', 1)
    print('removed empty div')
old2 = '<section class="section section--alt reveal" id="abonentka">'
new2 = '<section class="section section--alt reveal" id="calculator" style="scroll-margin-top:96px;">'
if old2 in s:
    s = s.replace(old2, new2, 1)
    print('added id to section')

# 2. Remove "Вы находитесь в разделе" block
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:860px;margin:0 auto;padding:16px;border:1px solid var\(--border\);border-radius:12px;background:var\(--card\);text-align:center;">\s*<p style="margin:0;font-size:13px;color:var\(--text-2\);">Вы находитесь в разделе:.*?</section>\s*', '', s, flags=re.S)

# 3. Remove VPN section
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<h2[^>]*>.*?VPN и удалённый доступ.*?</section>\s*', '', s, flags=re.S)

# 4. Remove "Мы не пряchem цены..." section
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:860px;margin:0 auto;padding:24px;border:2px solid var\(--gold-light\);border-radius:16px;background:var\(--card\);">.*?Мы не пряchem цены.*?</section>\s*', '', s, flags=re.S)

# 5. Remove "Почему нам можно доверять" section
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:860px;margin:0 auto;padding:24px;border:1px solid var\(--border\);border-radius:16px;background:var\(--card\);">.*?Почему нам можно доверять.*?</section>\s*', '', s, flags=re.S)

# 6. Remove "Готовы навести порядок в IT?" section
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;text-align:center;padding:32px 24px;border:2px solid var\(--gold-light\);border-radius:16px;background:var\(--card\);">.*?Готовы навести порядок в IT\?.*?</section>\s*', '', s, flags=re.S)

# 7. Remove "Нужна смета или консультация?" section
s = re.sub(r'<section[^>]*>\s*<div class="container" style="text-align:center;">\s*<h2[^>]*>Нужна смета или консультация\?</h2>.*?</section>\s*', '', s, flags=re.S)

# 8. Remove "Полезные статьи" / "Смотрите также" link blocks
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;">\s*<h3[^>]*>Полезные статьи.*?</section>\s*', '', s, flags=re.S)
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;">\s*<h3[^>]*>Смотрите также.*?</section>\s*', '', s, flags=re.S)

# 9. Remove "Полезные статьи кластера" link block
s = re.sub(r'<section[^>]*>\s*<div class="container">\s*<div style="max-width:760px;margin:0 auto;">\s*<h3[^>]*>Полезные статьи кластера.*?</section>\s*', '', s, flags=re.S)

# 10. Add VPN link after FAQ (if not present)
if 'Удалённый доступ — на странице VPN' not in s:
    s = s.replace('</section>\n<section class="section reveal" id="reviews">', '</section>\n<p style="text-align:center;margin:16px 0;"><a href="vpn.html" style="color:var(--gold);">Удалённый доступ — на странице VPN</a></p>\n<section class="section reveal" id="reviews">', 1)

# 11. Add final CTA before </main>
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