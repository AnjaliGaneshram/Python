num = int(input("Enter the number of elements in the list: "))
a = 0
list1 = []
list2 = []
for i in range(num):
    b = int(input("Enter the element number {}.".format(i+1)))
    list1.append(b)
    a = a + b
    list2.append(a)
print(list1)
print(list2)
    
