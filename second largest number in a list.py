num = int(input("Enter the number of elements: "))
list2 = []
list1 = []
for i in range(num):
    a = int(input("Enter element number {}: ".format(i+1)))
    list1.append(a)
list1.sort()
list2 = list1[::-1]
print("Second largest number in the list is ", list2[1])

