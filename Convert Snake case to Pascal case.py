#Convert Snake case to Pascal case

str1 = input("Enter the string in snake case format: ")

a = str1.replace("_"," ")

b = a.title()

c = b.replace(" ","")
print(c)
