path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services.html'
s = open(path, encoding='utf-8').read()
s = s.replace('href="mail.html"', 'href="services/mail.html"')
open(path, 'w', encoding='utf-8').write(s)
print('Done')
