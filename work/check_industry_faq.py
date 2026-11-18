import re, os
root='C:/Users/Eblan/Documents/Проект по умолчанию/ff-site'
f='industry-clinics.html'
s=open(os.path.join(root,f),encoding='utf-8').read()
print('FAQPage in html:', 'FAQPage' in s)
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    if 'FAQPage' in m.group(1):
        print('schema found:', m.group(1)[:200])
