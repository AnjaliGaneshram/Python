#Remove all duplicates from a given string

def remove_dup(a):
    s = set(a)
    t = ""
    for i in a:
        if i in t:
            pass
        else:
            t = t + i
    return t

str1 = input("Enter the string: ")

print(remove_dup(str1))
