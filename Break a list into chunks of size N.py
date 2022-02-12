num = int(input("Enter the number of elements in the list: "))
list1 = []
list2 = []
e = 0
for i in range(num):
    a = int(input("Enter the element number {}: ".format(i+1)))
    list1.append(a)
n = int(input("Enter the number of elements to be split inside the list: "))

b = len(list1)
c = int(b//n)

for i in range(c):
    d = list1[e:n*(i+1)]
    list2.append(d)
    e = e + n
print(list2)
        
