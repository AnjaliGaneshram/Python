 #Sets

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

set1 = set()
set2 = set()
print(type(set1), type(set2))

set1input = {7,8,9,1,2,3,4,5,0}
set2input = {4,5,6,0}

set1.update(set1input)
print("Set1:", set1)
set2.update(set2input)
print("Set2:", set2)

print("set2 is subset of set1:", set2.issubset(set1))

print("Does both sets have unique elements:", set1.isdisjoint(set2))

set1.remove(8)
print(set1)
#set2.remove(8)
print(set2)

set1.discard(0)
set2.discard(0)
print(set1, set2)

set3 = set1.union(set2)
print(set3)




