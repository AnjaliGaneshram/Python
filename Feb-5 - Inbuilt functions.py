#abs()

num1 = -90.34

print(abs(num1))

num2 = 54.76
#all() and any()
if all((num1==num2, num1<0)):
    print("True")
if any((num1==num2, num1<0)):
    print("False")


#bin()
print(bin(int(num1)))
#callable()
def function():
    a=10
    return a
print(callable(function))
#chr()
print(chr(109))
#complex()
print(complex(num1,num2))
#divmod()
print(divmod(9,3))
#enumerate()
list1 = [10,20,30,40,50]
print(dict(enumerate(list1)))
#eval()
x = str(num1!=num2)
y = eval(x)
print(y)
#exec()
m = "d = 114\nprint(int(d/4))"
exec(m)

#filter()

list2 = [10,34,56,20,35]

def Divisible(x):
    if x%5 == 0:
        return True
    else:
        return False

divbyfive = filter(Divisible, list2)

print(list(divbyfive))
#hex()
print(hex(int(num2)))
#iter() & next()
z = iter((10,20,30))

print(next(z))
print(next(z))
print(next(z))
#oct()
print(oct(int(num2)))
#ord()
print(ord("y"))
#pow()
print(pow(3,4))
#reversed

list3 = reversed(list2)
print(list(list3))
#round
print(round(num2,1))
#slice
list4 = slice(0,-1,2)
print(list2[list4])
#sorted
list5 = sorted(list2)
print(list(list5))
#zip
list6 = zip(list2,list5)
print(list(list6))



    
