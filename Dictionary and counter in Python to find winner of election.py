#Dictionary and counter in Python to find winner of election
from collections import Counter

arr = ["A","B","C","D","B","C","E"]
'''
listkey = []
listvalues = []
for i in arr:
    if i in listkey:
        pass
    else:
        listkey.append(i)
else:
    for i in listkey:
        a = arr.count(i)
        listvalues.append(a)
'''
dict1 = Counter(arr)
print(dict1)
print(sorted(dict1))
res = sorted(dict1,key = dict1.get,reverse=True)

print(res[0])
        
