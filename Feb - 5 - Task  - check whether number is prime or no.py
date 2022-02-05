#check whether number is prime or no



def Primenumber(a):
    for i in range(2,a+1):
        if a%i==0 and i!=a:
            return "Not a prime number"
    else:
        return "Prime Number"
  
num1 = int(input("Enter the number: "))

if num1==0 or num1==1:
    print("Not a prime number")
else:
    print(Primenumber(num1))

    
