#Maximum frequency character in String
string = input("Enter your string: ")
str1 = string.lower()
list1 = []
list2 = []
list3 = []
dict1 = {}
for i in str1:
    if i not in list1:
        list1.append(i)
print(list1)

for i in list1:
    x = str1.count(i)
    list2.append(x)
print(list2)

dict1 = dict(zip(list1,list2))

otpt = min(dict1, key = dict1.get)

print(otpt)


