#even length words in a string

str1 = input("Enter your string: ")
a = str1.split(" ")
for i in a:
    if int(len(i))%2==0:
        print(i)
    else:
        continue
