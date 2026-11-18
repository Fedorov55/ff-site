import re
path='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/about.html'
s=open(path,encoding='utf-8').read()
original=s
# Remove the empty section
pat=re.compile(r'<section class="section reveal" aria-label="5 лет на рынке.*?</section>', re.S)
m=pat.search(s)
if m:
    s=s[:m.start()]+s[m.end():]
    open(path,'w',encoding='utf-8').write(s)
    print('Removed empty section')
else:
    print('Not found')
print('Done')
