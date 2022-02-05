#function multiply three different integers and return a int

x,y,z = int(input("Enter the three numbers: ")),int(input()), int(input())

def multiplication(a,b,c):
    d = a*b*c
    return int(d)
print(multiplication(x,y,z))
