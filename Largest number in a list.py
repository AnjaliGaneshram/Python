num = int(input("Enter the number of elements: "))
list1 = []
for i in range(num):
    a = int(input("Enter element number {}: ".format(i+1)))
    list1.append(a)
    
list1.sort()
print(list1)
print("Largest number in the list is ", max(list1))
