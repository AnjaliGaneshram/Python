#Python – Closest Pair to Kth index element in Tuple

list1 = [(1,23), (5,13), (9,43)]

tup1 = (6,12)

k = 2
min_dif = 100
res = []

for key,val in enumerate(list1):

    dif = abs(tup1[k-1]  - val[k-1])
    if dif<min_dif:
        min_dif = dif
        res = val
print(res)
    
    
