list1 = []

num1 = int(input("Enter the number of elements in the list: "))

for i in range(num1):
    a = input("Enter the element number {}: ".format(i+1))
    list1.append(a)

num2 = input("Enter the element to be checked: ")

for i in range(num1):
    if num2 == list1[i]:
        print("The element exists in the list in positionn{}.".format(i+1))
        break
    else:
        continue
else:
    print("The element does not exists in the list.")



        
