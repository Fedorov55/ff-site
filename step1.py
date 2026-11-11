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

open('support.html', 'w', encoding='utf-8').write(s)
print('done')