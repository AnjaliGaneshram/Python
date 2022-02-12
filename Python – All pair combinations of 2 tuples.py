#Python – All pair combinations of 2 tuples

tup1 = (3,4,5,6)
tup2 = (1,2)
temp_tup = ()
res_tup = ()
list1 = []

for i in tup1:    
    for j in tup2:
        temp_tup = (i,)
        x = (j,)
        temp_tup = temp_tup + tuple(x)
        list1.append(temp_tup)
        temp_tup = ()

for i in tup2:    
    for j in tup1:
        temp_tup = (i,)
        x = (j,)
        temp_tup = temp_tup + tuple(x)
        list1.append(temp_tup)
        temp_tup = ()
        

print(list1)
