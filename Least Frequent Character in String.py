string = input("Enter your string: ")
str1 = string.lower()
list1 = []
list2 = []
list3 = []
for i in str1:
    if i not in list1:
        list1.append(i)
print(list1)

for i in list1:
    x = str1.count(i)
    list2.append(x)
print(list2)

list3 = list(zip(list1,list2))
print(list3)
list2.sort()
print(list2)
y = list2[0]
for i in range(len(list3)):
    if list3[i][1] == y:
        print(list3[i][0])
        

    



    
