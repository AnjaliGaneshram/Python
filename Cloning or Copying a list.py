num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
for i in range(num):
    a = input("Enter the element number {}: ".format(i+1))
    list1.append(a)

print(list1)

list2 = list1.copy()
print(list2)
list1[0] = 5

print(list1, list2)
