import re
s = open('support.html', encoding='utf-8').read()

# Get all sections
sections = list(re.finditer(r'<section[^>]*>.*?</section>', s, re.S))

# Identify sections to remove by their content
to_remove = []
for m in sections:
    seg = m.group(0)
    text = ' '.join(re.sub(r'<[^>]+>', '', seg).split())
    # Remove if contains these keywords (specific sections)
    if 'Вы находитесь в разделе' in seg:
        to_remove.append(m)
    elif 'VPN и удалённый доступ' in seg and len(text) < 250:
        to_remove.append(m)
    elif 'Мы не пряchem цены' in seg:
        to_remove.append(m)
    elif 'Почему нам можно доверять' in seg:
        to_remove.append(m)
    elif 'Готовы навести порядок в IT?' in seg:
        to_remove.append(m)
    elif 'Нужна смета или консультация?' in seg:
        to_remove.append(m)
    elif 'Полезные статьи' in seg or 'Смотрите также' in seg or 'Полезные статьи кластера' in seg:
        to_remove.append(m)
    elif 'Один человек в отпуске' in seg:
        to_remove.append(m)

# Remove from end to start
for m in reversed(to_remove):
    s = s[:m.start()] + s[m.end():]
    # remove trailing whitespace/newline
    s = s.rstrip('\n') + '\n' if s.endswith('\n') else s

# Fix calculator id
old = '<div id="calculator" style="scroll-margin-top:92px;">\n</div>'
if old in s:
    s = s.replace(old, '', 1)
old2 = '<section class="section section--alt reveal" id="abonentka">'
new2 = '<section class="section section--alt reveal" id="calculator" style="scroll-margin-top:96px;">'
if old2 in s:
    s = s.replace(old2, new2, 1)

# Add VPN link after FAQ (if not present)
if 'Удалённый доступ — на странице VPN' not in s:
    # find FAQ section end
    faq_match = re.search(r'(<section[^>]*>.*?Частые вопросы.*?</section>)', s, re.S)
    if faq_match:
        s = s.replace(faq_match.group(0), faq_match.group(0) + '\n<p style="text-align:center;margin:16px 0;"><a href="vpn.html" style="color:var(--gold);">Удалённый доступ — на странице VPN</a></p>\n', 1)

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
print('removed', len(to_remove), 'sections')
print('done')