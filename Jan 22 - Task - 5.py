string1 = input("enter the first string:")
string2 = input("enter the second string:")
str_1 = len(string1)//2
str_2 = len(string2)//2
print(string1[str_1], "+", string2[str_2])
sum = ord(string1[str_1]) + ord(string2[str_2])
print(sum)
