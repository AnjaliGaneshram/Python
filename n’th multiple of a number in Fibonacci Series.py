num = int(input("Enter the number: "))
n = int(input("Enter the multiple number: "))
list1 = [0,1]

x = num**n
a = 0
b = 0
for i in range(2, x+1):
    a = list1[i-1] + list1[i-2]
    list1.append(a)
print(list1)
for i in list1:
    print(i)
    if i == 0 or i == 1:
        continue
    
    elif i%num==0:
        b = b+1
        if b==n:
            print(i)
            break
        else:
            continue
    else:
        continue
else:
    print("End of the program")
'''
i = 2
b=0
while 1==1:
    a = list1[i-1] + list1[i-2]
    list1.append(a)
    i=i+1
    if a%num==0:
        b=b+1
        if b==n:
            print(a)
            break
        else:
            continue
    else:
        continue
else:
    print("End of the program")
    
'''
    
    
