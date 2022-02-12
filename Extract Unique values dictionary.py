#Extract Unique values dictionary
dict1 = {'anjali':[1,2,3],'ganeshram': [2,4,6],'shrinav':[3,6,9]}
temp = []
for val in dict1.values():
    for ele in val:
        if ele not in temp:
            temp.append(ele)

print(temp)
        

    
