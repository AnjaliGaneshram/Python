#Append Dictionary Keys and Values ( In order ) in dictionary

dict1 = {'a': 3, 'e': 8, 'i': 4, 'o': 2, 'u': 7}
list3 = []

list1 = list(dict1.keys())
print(list1)
list2 = list(dict1.values())
print(list2)

print(list1 + list2)

