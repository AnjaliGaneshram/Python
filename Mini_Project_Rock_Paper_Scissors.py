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
    
    if any((e=='rock',e=='paper',e=='scissor')):
        return e
    else:
        e = input("Invalid choice, Your choice can only be rock, paper or scissor: ")
        f = valid(e.lower())
        
        return f

    
list2 = []
list1 = ["rock","paper","scissor"]
try:
    n = int(input("Number of games you want to play: "))
except:
    n = int(input("Enter only numbers: "))
while n == 0:
    n = int(input("Enter the valid number: "))

j = 0
k=0
l =0

tie = 0
for i in range(n):
    print("Game {}:".format(i+1))
    a = input("\nEnter your choice(Choices can only be rock,paper or scissor): ")
    a.lower()
    f = valid(a)
    b = random.choice(list1)
    print("\nYour choice: ", f)
    print("\nSystem's choice: ",b)
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
        print("\nUser Wins:", j)
    elif c=="False":
        k = k+1
        print("\nSystem Wins: ", k)
    else:
        l = l + 1
        print("\nTie: ",l,"\n")
        
      

x = list2.count("tie")
y = list2.count("True")
z = list2.count("False")


print("\nTotal No of games played: ",n)
print("\nUser wins: ", y)
print("\nSystem wins: ", z)
print("\nTie match: ",x,"\n")

if y>z:
    if y>x:
        print("USER WINS!!!")
    else:
        print("USER WINS!!! TIED MATCHES: {}".format(x))

elif z>y:
    
    if z>x:
        print("SYSTEM WINS")
    else:
        print("SYSTEM WINS!!! TIED MATCHES: {}".format(x))


    
        
    
