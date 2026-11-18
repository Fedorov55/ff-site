path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/articles.html'
s = open(path, encoding='utf-8').read()
original = s
# Add a card before </div> of why__grid
card = '''<a href="it-budget.html" class="why-item fade-up" style="text-decoration:none;color:inherit">
<h3 class="why-item__title">IT-бюджет 2026-2027: исследование</h3>
<p class="why-item__text">Реальные расходы малого и среднего бизнеса на IT. Шаблон для планирования.</p>
</a>
'''
s = s.replace('</div>\n</div>\n</section>', card + '</div>\n</div>\n</section>', 1)
open(path, 'w', encoding='utf-8').write(s)
print('Updated articles.html')
print('Done')
