#Find the size of a Tuple in Python - return the value in bytes
import sys
tup1 = ("a", 2, "b", 12, "c", 36)

print("The size of tuple is ", tup1.__sizeof__())#without garbage value

print("The size of tuple is ", sys.getsizeof(tup1))#add garbage value


    
