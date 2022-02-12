num1 = int(input("Enter the starting interval: "))
num2 = int(input("Enter the ending interval: "))
list1 = []
for i in range(num1, num2+1):
    if i==0 or i==1:
        continue
    else:
        prime = True
        for j in range(1,i+1):
                if i%j==0 and j!=i and j!=1:
                    prime = False
                    break
        if prime == True:
             list1.append(i)
             
            
     
            
print(list1)
