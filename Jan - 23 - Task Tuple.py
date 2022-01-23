#Tuple

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

tuple1 = (1,4,5,6,7,8)
tuple2 = (5,6,7,8,9)
set1 = set(tuple1)
set2 = set(tuple2)
set3 = set1.intersection(set2)
tuple3 = tuple(set3)
print("Common Value of both tuples:", tuple3)

tupleadd = tuple1 + tuple2

tuple3 = tuple(set(tupleadd))

print("Index value of 9", tuple3.index(9))
print("Multiplication of tuples by 3", tuple3 * 3)


