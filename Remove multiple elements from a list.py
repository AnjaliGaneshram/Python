num = int(input("Enter the number of elements in the list"))
list1 = []
for i in range(num):
    a = int(input("Enter the element number {}:".format(i+1)))
    list1.append(a)
print(list1)
num1 = int(input("Enter the number of elements to be removed in the list: "))
list2 = []
for i in range(num1):
    b = int(input("Enter the element number {}: ".format(i+1)))
    list2.append(b)
print(list2)

for j in list2:
    for i in list1:
        if j == i:
            list1.remove(i)
            break
        else:
            continue
print(list1)

