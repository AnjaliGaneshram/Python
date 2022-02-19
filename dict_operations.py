# Dictionary Operations
def back_option(a):
    bo = int(input("Enter 1 to return to dictionary operation page: "))
    while bo !=1:
        bo = int(input("Enter 1 to return to dictionary operation page: "))
    return dict_ops(a)
def dict_add(a):
    print("Your dictionary: ", a)
    temp_key = int(input("Enter the key to be added: "))
    temp_val = int(input("Enter the value to be added: "))
    a[temp_key] = temp_val
    return a
def dict_clear(a):
    print("Your dictionary: ", a)
    return a.clear()
def dict_copy(a):
    print("Your dictionary: ", a)
    b = {}
    print("Empty dictionary before copying your dictionary: ", b)
    b = a.copy()
    return b
def dict_find(a):
    print("Your dictionary: ", a)
    temp_key = int(input("Enter the key of the dictionary to find its value: "))
    while temp_key not in a.keys():
        temp_key = int(input("Enter the key of the dictionary already exists in the dictionary: "))
    return a.get(temp_key)
def dict_remove(a):
    print("Your dictionary: ", a)
    temp_key = int(input("Enter the key of the dictionary to be removed: "))
    while temp_key not in a.keys():
        temp_key = int(input("Enter the key of the dictionary already exists in the dictionary: "))
    a.pop(temp_key)
    return a
def dict_update(a):
    print("Your dictionary: ", a)
    temp_key = int(input("Enter the key of the dictionary for which the value should be updated: "))
    while temp_key not in a.keys():
        temp_key = int(input("Enter the key of the dictionary exists in the dictionary: "))
    temp_val = int(input("Enter the value to be updated"))
    a[temp_key] = temp_val
    return a
def dict_sum(a):
    print("Your dictionary: ", a)
    list1 = []
    sum1 = sum(a.values())
    min1 = min(a.values())
    max1 = max(a.values())
    list1.append(sum1)
    list1.append(min1)
    list1.append(max1)
    return list1
def dict_mean(a):
    print("Your dictionary: ", a)
    mean = int(sum(a.values())/len(a))
    return mean
def dict_sort_values(a):
    print("Your dictionary: ", a)
    b = sorted(a.items(), key = lambda kv: (kv[1], kv[0]))
    return b
def dict_sort_keys(a):
    print("Your dictionary: ", a)
    b = sorted(a.items())
    return b




def dict_ops(dict1):
    
    print("List of operations available in Dictionary Data Structure: ")
    print("Enter 0 to return to Data Structure Calculator: ")
    print("1. Add\n2. Clear\n3. Copy\n4. Find\n5. Remove\n6. Update\n7. Sum of the Dictionary Values\n8. Mean of the Dictionary Values\n9. Sorting the Dictionary Values\n10. Sorting the Dictionary Keys")
    dict_option = int(input("Enter your option: "))
    while dict_option not in range(11):
            dict_option = int(input("Enter option between 1 to 10: "))
    if dict_option == 0:
        import Main_Program as main
        main.main()
    elif dict_option == 1:
        res = dict_add(dict1)
        print("The dictionary after adding the element: ", res)
        back_option(dict1)
    elif dict_option == 2:
        res = dict_clear(dict1)
        print("The dictionary after clearing the elements: ", res)
        back_option(dict1)
    elif dict_option == 3:
        res = dict_copy(dict1)
        print("The dictionary after copying the elements: ", res)
        back_option(dict1)
    elif dict_option == 4:
        res = dict_find(dict1)
        print("The value of the given key in the dictionary: ", res)
        back_option(dict1)
    elif dict_option == 5:
        res = dict_remove(dict1)
        print("The dictionary after removing the given key value: ", res)
        back_option(dict1)
    elif dict_option == 6:
        res = dict_update(dict1)
        print("The dictionary after updating the given key value: ", res)
        back_option(dict1)
    elif dict_option == 7:
        res = dict_sum(dict1)
        print("The sum of the values in the dictionary: ", res[0])
        print("The lowest value in the dictionary: ", res[1])
        print("The highest value in the dictionary: ", res[2])
        back_option(dict1)
    elif dict_option == 8:
        res = dict_mean(dict1)
        print("Mean of the dictionary values: ", res)
        back_option(dict1)
    elif dict_option == 9:
        res = dict_sort_values(dict1)
        print("The dictionary after sorting the values: ", res)
        back_option(dict1)
    elif dict_option == 10:
        res = dict_sort_keys(dict1)
        print("The dictionary after sorting the keys: ", res)
        back_option(dict1)
    return "Thank you for using Data Structure Calculator"
        
def operations():
    print("Dictionary Operations: ")
    dict1 = {}
    num = int(input("Enter the number of key values in the dictionary: "))
    while num == 0:
        num = int(input("Number of key values can't be zero: "))
    for i in range(num):
        key_1 = int(input("Enter the key for the element number {}: ".format(i+1)))
        value_1 = int(input("Enter the value for the element number {}: ".format(i+1)))
        dict1[key_1] = value_1
    print("Your dictionary: ",dict1)
    return dict_ops(dict1)      
        
        
        
        

