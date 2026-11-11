s = open('index.html', encoding='utf-8').read()
# Remove emoji from H2
s = s.replace('📋 Как мы работаем', 'Как мы работаем')
# Add team line to process section
# Find the process section and add team line before its closing
old_marker = '</div>\n</div>\n</section>\n<section class="section reveal" id="reviews">'
team_line = '''<div style="text-align:center;margin-top:28px;">
<p style="font-size:15px;color:var(--text-2);margin-bottom:8px;">Четыре инженера в Казани.</p>
<a href="team.html" class="btn btn--ghost">Команда F&F</a>
</div>
'''
if old_marker in s:
    s = s.replace(old_marker, team_line + '</div>\n</div>\n</section>\n<section class="section reveal" id="reviews">', 1)
    print('team line added')
open('index.html', 'w', encoding='utf-8').write(s)
print('done')