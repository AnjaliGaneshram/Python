num1, num2 = int(input("Enter the position of the elements to be swapped: ")), int(input())

list1 = [10,20,30,40,50]

print(list1)

temp = list1[num1-1]
list1[num1-1] = list1[num2-1]
list1[num2-1] = temp

print(list1)
