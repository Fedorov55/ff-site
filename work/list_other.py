import json
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
skip={'АО "ТБанк"','КОДЫЛЕВ АЛЕКСЕЙ','ИНДИВИДУАЛЬНЫЙ ПРЕДПРИНИМАТЕЛЬ КОДЫЛЕВ АЛЕКСЕЙ ВЛАДИМИРОВИЧ'}
out=[]
for r in debits:
    if r['corr_name'] not in skip:
        out.append(r['date'] + ' | ' + r['corr_name'] + ' | ' + r['content'] + ' | ' + str(r['amount']))
open('C:/Users/Eblan/Downloads/debits_other.txt','w',encoding='utf-8').write('\n'.join(out))
print('lines', len(out))
