#Remove all duplicates words from a given sentence
str1 = input("Enter the string: ")
temp = str1.split(" ")
s = set()

for i in temp:
    s.add(i)

x = " ".join(s)

print(x)


