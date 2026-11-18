path = 'C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/services/mail.html'
s = open(path, encoding='utf-8').read()
s = s.replace('fonts/inter-v20-cyrillic_latin-700.woff2', '../fonts/inter-v20-cyrillic_latin-700.woff2')
s = s.replace('fonts/jetbrains-mono-v24-cyrillic_latin-700.woff2', '../fonts/jetbrains-mono-v24-cyrillic_latin-700.woff2')
s = s.replace('href="rss.xml"', 'href="../rss.xml"')
open(path, 'w', encoding='utf-8').write(s)
print('Done')
