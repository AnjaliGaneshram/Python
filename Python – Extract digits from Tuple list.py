#Python – Extract digits from Tuple list

list1 = [(15, 3), (3, 9)]
list2 = []

for val in list1:
    for ele in val:
        a = str(ele)
        b = len(a)
        if b > 1:
            for i in range(b):
                x = int(a[i])
                list2.append(x)         
        else:
            list2.append(ele)

set1 = set(list2)

print(set1)
