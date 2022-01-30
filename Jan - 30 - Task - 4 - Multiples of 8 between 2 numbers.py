result = list()
num1 = int(input("Enter your starting range:"))
num2 = int(input("Enter your ending range: "))
for i in range(num1,num2+1):
    if i%8==0:
        result.append(i)
else:
    print(result)
        
