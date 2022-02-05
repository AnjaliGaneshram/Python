#Fibnacci series

def Fibnacci_series(a):
    list1=[0,1]
    for i in range(2,a):
        b = list1[i-1] + list1[i-2]
        list1.append(b)
    else:
        return list1[a-1]
num1 = int(input("Enter the number: "))
print(Fibnacci_series(num1))
