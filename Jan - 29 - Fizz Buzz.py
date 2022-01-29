'''
#Fizz buzz
#Get one number from user
#5
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number
'''
n = int(input("Enter the number: "))
if n%3==0 and n%5 == 0:
    print("Fizzbuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print("Invalid Number")
