#Python – Remove Tuples of Length K

list1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
list2 = []

n = int(input("Enter the length of the tuple to be removed: "))

for i in list1:
    if len(i) == n:
        continue
    else:
        list2.append(i)

print(list2)

