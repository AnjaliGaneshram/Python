num1 = int(input("Enter the starting number of the range: "))
num2 = int(input("Enter the ending number of the range: "))
list1 = []
for i in range(num1, num2+1):
    if i%2 == 0:
        a = i
        list1.append(a)
    else:
        continue
print("The even numbers in the range: ", list1)
    
