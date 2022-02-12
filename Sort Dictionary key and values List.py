#Sort Dictionary key and values List
dict1 = {}

dict1 = {'c': [3], 'b': [12, 10], 'a': [19, 4]}



for key,value in dict1.items():
    x = sorted(value)
    dict1[key] = x

print(sorted(dict1.items()))
