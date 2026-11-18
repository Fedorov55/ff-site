import re
s=open('C:/Users/Eblan/Documents/Проект по умолчанию/ff-site/prices.html',encoding='utf-8').read()
# find from 'Что делать' to 'Смотрите также'
start=s.find('Что делать')
end=s.find('Смотрите также')
print('start:', start, 'end:', end)
print(repr(s[start:end][:200]))
print('...')
print(repr(s[end-100:end+50]))
