#Check if a Substring is Present in a Given String

str1 = input("Enter the string: ")
a = str1.lower()

substr1 = input("Enter the substring: ")


if a.find(substr1) ==-1:
    print("Substring is not found in the string")
else:
    print("Substring found in the string")
