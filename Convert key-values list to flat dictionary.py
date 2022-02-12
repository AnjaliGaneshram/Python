#Convert key-values list to flat dictionary

dict1 = {"name": ['anjali','ganeshram', 'shrinav'],"age": [31,32,2]}

res = dict(zip(dict1["name"],dict1["age"]))
print(res)
