#Join Tuples if similar initial element

list1 = [(3,4), (3,6), (4,5), (4,8), (7,9), (7,12)]
list2 = []
list3 = []
dict1 = {}

for tup in list1:
    temp = tup[0]
    list2.append(temp)


set1 = set(list2)



for val in set1:
    
    tup1 = (val,)
    tup2 = ()
    for tup in list1:
        print(tup[0])
        if val == tup[0]:
            
            tup2 = (tup[1],)
            tup1 = tup1 + tup2
            print(tup1)
    else:
        list3.append(tup1)

print(list3)
        

    
