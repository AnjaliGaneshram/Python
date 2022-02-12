list1 = []
n = int(input("Enter the number of elements in the list: "))

for i in range(n):
    a = int(input("Enter the element number {}: ".format(i+1)))
    list1.append(a)
list2 = list1.reverse()
j = 0
b = 0
c = 0
i = 0
for i in range(n):
     j = j + 1
     if j < n:
         if list1[i] > list1[j]:
             b = b+1
         else:
             c = c+1
     else:
         if b!=0 and c!=0:
            print("The list is not montonic")
         elif b==0:
            print("Monotonic decreasing")
         else:
            print("Monotonic increasing")
   
    
         
    
