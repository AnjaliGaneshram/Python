num = int(input("Enter the number:"))
a = 0
b = 0
for i in range(1,num+1):
    a = i**2
    b = b + a
    
    
print("Sum of {} number of natural numbers: ".format(num),b)
