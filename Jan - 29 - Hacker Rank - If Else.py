#Hacker-Rank - If Else Program

'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

num = int(input("Enter the number: "))
if num%2!=0:
    print("Weird")
elif num>=2 and num<=5:
    print("Not weird")
elif num>=6 and num<=20:
    print("Weird")
elif num>20:
    print("Not Weird")
''' This program is to identify the given number is "Weird" or "Not Weird" based on the conditions given in the Task section.'''
