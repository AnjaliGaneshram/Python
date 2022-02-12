#Convert Nested Tuple to Custom Key Dictionary

tup1 = ((1, 'Gfg', 2), (3, 'best', 4))

keys = ['key', 'value', 'id']
dict1 = {}
list1 = []
for val in tup1:
    dict1 = dict(zip(keys,val))
    print(dict1)
    list1.append(dict1)
    print(list1)
