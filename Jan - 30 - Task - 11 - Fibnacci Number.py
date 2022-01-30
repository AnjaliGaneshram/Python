num = int(input("Enter the number: "))

list1 = [0,1]
for i in range(num+1):
    a = list1[i] + list1[i+1]
    list1.append(a)
print(list1[num])
    
    
    
    
    
