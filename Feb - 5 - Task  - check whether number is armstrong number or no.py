#check whether number is armstrong number or no
def Armstrong(a):
    b = str(a)
    c=0
    for i in b:
        c = c + (int(i)**3)
        print(c)
    if c==a:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
num1 = int(input("Enter the number: "))
print(Armstrong(num1))
