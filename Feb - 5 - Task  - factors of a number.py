#factors of a number

def Factors(a):
    list1 = []
    for i in range(1,a+1):
        if a%i == 0:
            list1.append(i)
        else:
            continue
    else:
        return list1
num1 = int(input("Enter the number: "))

print(Factors(num1))
            
