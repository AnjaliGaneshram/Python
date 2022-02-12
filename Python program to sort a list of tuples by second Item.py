#Python program to sort a list of tuples by second Item
list1 = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
list2 = []
res_list = []

for val in list1:
    list2.append(val[1])

print(list2)

sorted_list = sorted(list2)

print(sorted_list)

for i in sorted_list:
    for val in list1:
        if i == val[1]:
            res_list.append(val)

print(res_list)
    
