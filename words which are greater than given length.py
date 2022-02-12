#words which are greater than given length
list1 = []
list2 = []
str1 = input("Enter the string: ")
n = int(input("Enter the length of the string: "))


temp = str1.split(" ")

for i in temp:
    a = len(i)
    list1.append(a)

res = list(zip(temp,list1))
print(res)
for i in range(len(res)):
    if res[i][1] > n:
           list2.append(res[i][0])

s = " ".join(list2)
print(s)       
    


