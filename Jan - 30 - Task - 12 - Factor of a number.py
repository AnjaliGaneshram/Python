num = int(input("Enter your number: "))
list1 = list()
for i in range(1, num+1):
    if num%i==0:
        a = i
        list1.append(a)
    else:
        continue
print("Multiple of {} are: ".format(num),list1)
