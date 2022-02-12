num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
for i in range(num):
    a = int(input("Enter the element number {}: ".format(i+1)))
    list1.append(a)
for i in list1:
    b = list1.count(i)
    
    if b>1 and list2.count(i)==0:
        list2.append(i)
        
    else:
        continue
else:
    print(list2)
