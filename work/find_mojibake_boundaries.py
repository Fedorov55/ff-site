s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
import re
# find first mojibake char
moji = '╨'
i = s.find(moji)
print('first mojibake at:', i)
# find the section start before it
sec_start = s.rfind('<section', 0, i)
print('section start:', sec_start)
sec_end = s.find('</section>', i)
print('section end:', sec_end)
print('section preview:', repr(s[sec_start:sec_start+100]))
print('...')
print('section tail:', repr(s[sec_end-50:sec_end+50]))
# show full section length
print('section length:', sec_end - sec_start)
