import json
from collections import Counter
recs=json.load(open('C:/Users/Eblan/Downloads/records_classified.json',encoding='utf-8'))
debits=[r for r in recs if r['is_debit']]
own=[r for r in debits if 'КОДЫЛЕВ' in r['corr_name']]
c=Counter((r['corr_name'], r['account']) for r in own)
for k,v in c.items():
    print(v, k)
