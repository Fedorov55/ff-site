import json
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
targets=['Абдулгалимов','Файзуллин','Имангалиев','ПАРДОН','ШАНС']
for r in debits:
    if any(t.lower() in r['corr_name'].lower() for t in targets):
        print(r['date'], '|', r['corr_name'], '|', r['content'], '|', r['amount'])
