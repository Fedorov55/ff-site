import re
s = open('support.html', encoding='utf-8').read()

# Remove "Мы не прячем цены..." section
m = re.search(r'<section[^>]*>.*?Мы не пряchem цены и не держим вас заложником.*?</section>\s*', s, re.S)
if m:
    s = s.replace(m.group(0), '', 1)
    print('removed price/trust block 1')
else:
    print('block 1 not found')

# Remove "Почему нам можно доверять" section
m = re.search(r'<section[^>]*>.*?Почему нам можно доверять.*?</section>\s*', s, re.S)
if m:
    s = s.replace(m.group(0), '', 1)
    print('removed trust block 2')
else:
    print('block 2 not found')

open('support.html', 'w', encoding='utf-8').write(s)
print('done')