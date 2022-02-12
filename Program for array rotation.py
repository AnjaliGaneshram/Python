num1 = int(input("Enter then number of elements in the array: "))
n = int(input("Enter the number of elements to be split: "))
list1 = []
temp = []
list2 = []
for i in range(num1):
    a = int(input("Enter the elements: "))
    list1.append(a)
for i in range(num1):
    if i < n:
        b = list1[i]
        temp.append(b)
    else:
        c =list1[i]
        list2.append(c)
    
list1 = list2 + temp
print(list1)
    
    

    
