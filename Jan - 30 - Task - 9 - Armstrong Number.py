num = int(input("Enter your number: "))
a = []
b = []
for i in str(num):
    a.append(i)
print(a)

for i in a:
    temp = int(i)**3
    b.append(temp)
    print(b)
if sum(b)== num:
    print("Armstrong Number")
else:
    print ("Not a Armstrong Number")
    
    
    
    
    
    
