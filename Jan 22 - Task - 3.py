string1 = input("Enter the name and percentage:(name float value):")
string2 = input("Enter the name and percentage:(name float value):")
string3 = input("Enter the name and percentage:(name float value):")

str_1 = string1.split()
str_2 = string2.split()
str_3 = string3.split()

sum = float(str_1[1]) + float(str_2[1]) + float(str_3[1])

print("Sum value = {:.5f}".format(sum))
