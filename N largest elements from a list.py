num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
for i in range(num):
    a = int(input("Enter the element number {}.".format(i+1)))
    list1.append(a)

print(list1)
n = int(input("Enter the number: "))
list1.sort()
list2 = list1[::-1]
print(list2[n-1])
