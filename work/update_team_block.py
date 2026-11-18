import re

path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html'
s = open(path, encoding='utf-8').read()
original = s

# Extract team cards from team.html
team_html = open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/team.html', encoding='utf-8').read()
m = re.search(r'<div class="team__grid">(.*?)</div>\s*</div>\s*</section>', team_html, re.S)
team_cards = m.group(1).strip() if m else ''
# fallback: extract from team-card fade-up
if not team_cards:
    cards = re.findall(r'<div class="team-card fade-up">.*?</div>\s*</div>\s*</div>', team_html, re.S)
    team_cards = '\n'.join(cards)

# Replace the team__grid block on index.html
pat = re.compile(r'<div class="team__grid" style="display:grid;grid-template-columns:repeat\(4,minmax\(0,1fr\)\);gap:18px;">.*?</div>\s*</div>\s*</section>', re.S)
new_block = f'''<div class="team__grid">
{team_cards}
</div>
</div>
</section>'''
s2 = pat.sub(new_block, s, count=1)

# Add link to team.html
s2 = s2.replace('</div>\n</section>\n', '</div>\n<p style="text-align:center;margin-top:16px;"><a href="team.html" class="u-gold">Вся команда →</a></p>\n</div>\n</section>\n', 1) if 'Вся команда' not in s2 else s2

if s2 != original:
    open(path, 'w', encoding='utf-8').write(s2)
    print('Updated index.html team block')
else:
    print('No changes')
print('Done')
