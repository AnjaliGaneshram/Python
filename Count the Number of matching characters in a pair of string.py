#Count the Number of matching characters in a pair of string
def match(a,b):
    j = 0
    count = 0
    list1 = []
    for i in a:
        t = a.find(i)
        if b.find(i)!=-1 and j==t:
            count = count + 1
            list1.append(i)
        j = j+1
    print(list1, count)
    return count
    





str1 = input("Enter your first string: ")
str2 = input("Enter you second string: ")

match(str1,str2)
