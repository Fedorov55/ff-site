s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/index.html',encoding='utf-8').read()
i=s.find('<nav class="nav"')
j=s.find('</nav>', i)
print(s[i:j+6])
print('---')
# mobile
i2=s.find('mobile-nav__inner')
j2=s.find('</div>', s.find('mobile-nav__footer', i2))
print(s[i2:j2+20])
