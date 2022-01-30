num = int(input("Enter the number: "))


for i in range(1,num+1):
    
    if num%i==0 and i!=num and i!=1:
        print("Not a prime number")
        break
    elif num==1:
        print("Not a prime number")
        break
else:
    print("Prime Number")
