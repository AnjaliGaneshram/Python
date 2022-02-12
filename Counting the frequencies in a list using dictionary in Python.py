#Counting the frequencies in a list using dictionary in Python

list1 = [1,2,2,3,4,3,4,2,3,1,4,5]
len = len(list1)
dict1 = {}
count = 0

for i in list1:
    
    if i in dict1:
        count = list1.count(i)
        dict1[i] = count
    else:
        dict1[i] = 1
print(dict1.items())

