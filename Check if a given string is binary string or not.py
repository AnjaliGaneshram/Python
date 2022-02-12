#Check if a given string is binary string or not
str1 = input("Enter the string: ")

s = set(str1)

a = {'0','1'}

if s==a or s == {'0'} or s == {'1'}:
    print("The given string is binary")
else:
    print("Not binary")
