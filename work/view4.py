import json
from collections import Counter
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
tb=[r for r in debits if r['corr_name']=='АО "ТБанк"']
c=Counter()
for r in tb:
    # normalize content: take first phrase
    txt=r['content']
    key=txt.split('Дата операции')[0].strip()
    # shorten
    if 'эквайринга' in key: key='Комиссия за операции по терминалам эквайринга'
    elif 'пополнение по операции СБП' in key: key='Плата за пополнение по операции СБП'
    elif 'внешний банковский перевод' in key: key='Комиссия за внешний банковский перевод'
    else: key=key[:80]
    c[key]+=1
for k,v in c.items():
    print(v, k)
