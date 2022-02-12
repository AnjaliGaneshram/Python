list1 = [0,1]

num = int(input("Enter the number: "))

for i in range(2,num+1):
    a = list1[i-1] + list1[i - 2]
    list1.append(a)
print(list1)
for i in list1:
    if num == i:
        print("The given number is Fibonacci number.")
        break
    else:
        continue
else:
    print("The given number is not a Fibonacci number.")
    
