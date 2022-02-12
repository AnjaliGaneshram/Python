num1 = int(input("Enter the number of elements in the list: "))
list1 = []
temp = 0
for i in range(num1):
    a = int(input("Enter the element number {}:".format(i+1)))
    list1.append(a)
    
print(list1)

temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)
