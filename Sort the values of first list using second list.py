list1 = ['a','d','e','w','t']
list2 = [7,4,8,2,0]
a = int(len(list2))
for i in range(a):
    for j in range(a):
        if list2[i] < list2[j]:
            temp = list2[i]
            list2[i] = list2[j]
            list2[j] = temp
            temp1 = list1[i]
            list1[i] = list1[j]
            list1[j] = temp1
        else:
            continue
else:
    print(list2)
    print(list1)
    
            
