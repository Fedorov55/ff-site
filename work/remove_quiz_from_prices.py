import re
path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html'
s = open(path, encoding='utf-8').read()
original = s

# Find section containing "IT-инфраструктура для офиса на 20–50 человек" (the quiz)
pat = re.compile(r'<section[^>]*>(?:(?!</section>).)*?IT-инфраструктура для офиса на 20–50 человек(?:(?!</section>).)*?</section>', re.S)
m = pat.search(s)
if m:
    s = s[:m.start()] + s[m.end():]
    open(path, 'w', encoding='utf-8').write(s)
    print('Removed quiz section')
else:
    print('Quiz section not found')
print('Done')
