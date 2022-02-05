str1 = input("Enter the string: ")

def vowel(a):
    b = int(len(a)/2)
    if a[b]=="a" or a[b]=="e" or a[b]=="i" or a[b]=="o" or a[b]=="u":
        return "{} is a vowel".format(a[b])
    else:
        return "{} is not a vowel".format(a[b])


print(vowel(str1))
