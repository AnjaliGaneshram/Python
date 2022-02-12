#Python dictionary with keys having multiple inputs

dict1 = {}
'''
x,y,z = 10,20,30

dict1[x,y,z] = x+y+z

x,y,z = 1,2,3

dict1[x,y,z] = x+y+z
print(dict1)
'''

n = int(input("Enter the number of elements in the dictionary: "))

for i in range(n):
    a = input("Enter the key value:")
    b = int(input("Enter the value: "))
    dict1[a] = b

print(dict1)
