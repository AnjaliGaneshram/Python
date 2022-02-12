
x = "ABCDCDC"

y = "CDC"

#print(count_substring(x,y))

a = len(x)
n = len(y)
list1 = []
for i in range(a+1-n):
    
    b = x[i:n]
    list1.append(b)
    n = n+1

res = list1.count(y)

print(res)
