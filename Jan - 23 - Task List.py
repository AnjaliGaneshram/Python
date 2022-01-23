#List

#Create an empty list (two ways)
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple

list1 = []
print(list1)
list2 = list()
print(list2)

list2 = [5,6,7,8]

list1.extend(list2)
print(list1)
list4 = [8,9,1,5,6,7,8,1]
print(list1+list4)
print(list4.count(8))
#Mean

val1 = sum(list4)/len(list4)
print("Mean:", int(val1))
print("Sum:", sum(list4))
print("Minimum value", min(list4))
print("Maximum Value", max(list4))
list4.sort()
#print(list4)
list5 = int(len(list4)//2)
print("Median:", list4[list5])
output = tuple(set(list4))
print(output)
print(type(output))




