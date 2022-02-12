num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
d = 0

for i in range(num):
    a = int(input("Enter the element number {}:".format(i+1)))
    list1.append(a)

for b in list1:
    c = str(b)
    for j in c:
        d = d+int(j)
    else:
        list2.append(d)
        d=0


print(list1)
print(list2)
    
    
    
