#Reverse words in a given String
str1 = input("Enter the string: ")
x = str1.split(" ")
x = x[::-1]
print(x[::-1])
y = " ".join(x)

print(y)
