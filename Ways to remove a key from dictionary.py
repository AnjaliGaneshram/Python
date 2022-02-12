#Ways to remove a key from dictionary

dict1 = {"anjali": 10, "ganeshram": 20, "shrinav": 30}

key1 = input("Enter the key to be deleted: ")
new_dict1 = {}
list1 = []
list2 = []
for key,val in dict1.items():
    if key!=key1:
        list1.append(key)
        list2.append(val)
new_dict1 = dict(zip(list1,list2))


print(new_dict1)
    


