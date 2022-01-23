#Dictionary:

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

dict1 = {}
print(type(dict1))

dict1 = {1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}

print(dict1[3][0][::2])

print(dict1[3][2][:-6:-1])

print(dict1.keys())

tuple1 = tuple(dict1.keys())
print(tuple1, type(tuple1))

a = dict1[2]
b = int(sum(a)/len(a))
print("Average", b)

