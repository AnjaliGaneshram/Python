num = int(input("Enter the number: "))
b = 0

for i in range(1,num+1):
    a = i**3
    b = b + a
print("Sum of the cube of the {} numbers: ".format(num), b)
