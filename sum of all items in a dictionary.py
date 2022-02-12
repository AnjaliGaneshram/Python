#sum of all items in a dictionary


dict1 = {'anjali': [1,2,3], 'ganeshram': [2,3,4], 'shrinav': [4,5,6]}

res = 0
for val in dict1.values():
    res = res + sum(val)
    
print(res)


