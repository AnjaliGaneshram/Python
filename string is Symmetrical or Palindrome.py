#string is Symmetrical or Palindrome


str1 = input("Enter the string: ")

a = int(len(str1)/2)
b = len(str1)
if str1[:a] == str1[a:b]:
    print('Symmetrical')
else:
    print("Non-Symmetrical")
    

if str1== str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
