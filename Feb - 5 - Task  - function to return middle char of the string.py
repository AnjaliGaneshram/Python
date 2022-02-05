#function to return middle char of the string
str1 = input("Enter the string: ")

def middle_char(a):
    b = int(len(a)/2)
    return a[b]
print(middle_char(str1))
    

