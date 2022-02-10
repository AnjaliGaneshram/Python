import random
def rock(c,d):
    if d == "paper":
        return "False"
    else:
        return "True"
def paper(c,d):
    if d == "scissor":
        return "False"
    else:
        return "True"
def scissor(c,d):
    if d == "rock":
        return "False"
    else:
        return "True"
def valid(e):
    if any((a=='rock',a=='paper',a=='scissor')):
        return e
    else:
        e = input("Invalid choice, Your choice can only be rock, paper or scissor: ")
        return e
list2 = []
list1 = ["rock","paper","scissor"]

n = int(input("Number of games you want to play: "))
j = 0
k=0
l =0
if n == 0:
    print("Game Over")
tie = 0
for i in range(n):
    a = input("Enter your choice: ")
    a.lower()
    f = valid(a)
    b = random.choice(list1)
    print("Your choice: ", f)
    print("System's choice: ",b)
    if f==b:
        c = "tie"
        list2.append(c)
        
    elif f == "rock":
        c = rock(a,b)
        list2.append(c)
        
            
    elif f == "paper":
        c = paper(a,b)
        list2.append(c)
        
    else:
        c = scissor(a,b)
        list2.append(c)
    if c=="True":
        j = j +1
        print("User Wins:", j)
    elif c=="False":
        k = k+1
        print("System Wins: ", k)
    else:
        l = l + 1
        print("Tie: ",l)
        
      

x = list2.count("tie")
y = list2.count("True")
z = list2.count("False")


print("Total No of games played: ",n)
print("User wins: ", y)
print("System wins: ", z)
print("Tie match: ",x)

if y>x and y>z:
    print("CONGRATS! USER WINS")
elif z>y and z>x:
    print("SYSTEM WINS. TRY AGAIN!")
elif x>y and y>z:
    print("CONGRATS! USER WINS")
else:
    print("SYSTEM WINS. TRY AGAIN")



    
        
    
