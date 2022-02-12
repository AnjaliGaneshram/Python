#Python program to create a list of tuples from given list having number and its cube in each tuple

list1 = [2,4,6]
tup1, tup2, tup3 = (),(),()

res = []
for i in list1:
    list2 = []
    list2.append(i)
    list2.append(i**3)
    tup1 = tuple(list2)
    res.append(tup1)


print(res)
