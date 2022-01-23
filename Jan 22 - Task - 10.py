#Mutation
string = input("Enter the string, position, character to be changed:")
pos = int(input())
character = input()
print(string[:pos]+character+string[pos+1:])
