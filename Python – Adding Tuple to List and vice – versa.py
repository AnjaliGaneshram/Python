#Python – Adding Tuple to List and vice – versa
#+= is an operator to add list and tuple
list1 = [1,3,5]

tup1 = (6,8)

list1+= tup1

print(list1)

tup1 = tup1 + tuple(list1)

print(tup1)
