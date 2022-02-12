#Replace duplicate Occurrence in String

str1 = input("Enter your string: ")

replace = {"Anjali":"She","Ganeshram":"He"}

temp = []

list1 = str1.split()

for key,val in enumerate(list1):
    
    if val in replace:
        if val in temp:
            list1[key]=replace[val]
        else:
            temp.append(val)
            print(temp)

otpt = " ".join(list1)
print(otpt)
        
