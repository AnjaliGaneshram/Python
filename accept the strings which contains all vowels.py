#accept the strings which contains all vowels

str1 = input("Enter the string: ")

str1.lower

list1 = [str1.count('a'),str1.count('e'),str1.count('i'),str1.count('o'),str1.count('u')]

print(list1)

list2 = ['a','e','i','o','u']

dic1 = zip(list2, list1)

d = list(dic1)
print(d)
if list1.count(0)>0:
    print("Not agreed")
temp = []

for i in range(len(d)):
    if d[i][1]==0:
        temp.append(d[i][0])
print(temp)




    
