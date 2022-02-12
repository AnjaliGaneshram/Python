#find uncommon words from two Strings

str1 =input("Enter the string: ")
str2 = input("Enter the second string: ")
uncommon = []
for i in str1.split():
    if i not in str2:
        uncommon.append(i)
for j in str2.split():
    if j not in str1:
        uncommon.append(j)
uc=" ".join(uncommon)

print(uc)
