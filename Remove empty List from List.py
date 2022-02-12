num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
for i in range(num):
    a = input("Enter the element number{}: ".format(i+1))
    list1.append(a)
print(list1)
list2 = list1.copy()
for i in list2:
    print(i)
    if i == '[]':
        
        list1.remove(i)
        print(list1)
        
    else:
        pass
else:
    print(list1)
'''
for i in range(num+1):
    print(list1[i])
    b = list1[i]
    if b == "[]":
        list1.remove(b)
        pass
    else:
        pass
else:
    print(list1)
'''
