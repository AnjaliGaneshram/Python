#function to check a string is palindrom or not

str1 = input("Enter the string: ")

def Palindrome(a):
    if a == a[::-1]:
        return "It's a palindrome"
    else:
        return "Not a palindrome"

print(Palindrome(str1))
