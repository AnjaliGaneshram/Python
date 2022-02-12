#Python Dictionary to find mirror characters in a string

str1 = "abcdefghijklmnopqrstuvwxyz"

str2 = str1[::-1]

in_str = input("Enter your string: ")

pos = int(input("Enter the position: "))

list1 = []
list2 = []
list3 = []
res = []

for i in in_str[:pos]:
    list1.append(i)
for i in in_str[pos::]:
    list2.append(i)

print(list1)
print(list2)

for i in list2:
    t = str1.find(i)
    a = str2[t]
    list3.append(a)
print(list3)

res = list1+list3
print(res)

x = "".join(res)
print(x)

        
    
