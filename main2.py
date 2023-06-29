data = [{'obj1':{'bank':'sbi','budget':15000,'city':'pune'}},
        {'obj2':{'bank':'hdfc','budget':36000,'city':'pune'}},
        {'obj3':{'bank':'sbi','budget':75000,'city':'mumbai'}},
        {'obj4':{'bank':'sbi','budget':16000,'city':'chennai'}},
        {'obj5':{'bank':'sbi','budget':95000,'city':'banglore'}},
        {'obj2':{'bank':'hdfc','budget':36000,'city':'pune'}},
        {'obj2':{'bank':'axis','budget':45000,'city':'pune'}}]

st = {}

for i in data:
        temp = list(i.values())
        if temp[0]['bank'] in st:
            st[temp[0]['bank']] += temp[0]['budget']
        else:
                st[temp[0]['bank']] = temp[0]['budget']

print(st)





