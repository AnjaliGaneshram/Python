#list_operations
import statistics as stat


def back_option(list1):
    bo = int(input("Enter 1 to return to List Operations page: "))
    while bo != 1:
        bo = int(input("Enter 1 to return to List Operations page: "))
    return list_ops(list1)

def list_add(a):
    num = int(input("Enter the number to be added in the list: "))
    a.append(num)
    return a
def list_clear(a):
    print("Your list: ", a)
    print("List after clearing the data's: ")
    b = a.clear()
    return b
def list_copy(a):
    print("Your list: ", a)
    list2 = []
    print("This is the list before copying your list: ", list2)
    list2 = a.copy()
    return list2
def list_count(a):
    print("Your list: ", a)
    x = int(input("Enter the element to be counted: "))
    while x not in a:
        x = int(input("Enter the element exists in the list: "))        
    y = a.count(x)
    return y
def list_extend(a):
    print("Your list: ", a)
    list2 = []
    num = int(input("Enter the number of elements of the second list: "))
    while num == 0:
        num = int(input("Number cannot be zero: "))
    for i in range(num):
        temp = int(input("Enter the element number {}: ".format(i+1)))
        list2.append(temp)
    a.extend(list2)
    return a
def list_insert(a):
    print("Your list: ", a)
    ele = int(input("Enter the element to be inserted: "))
    pos = int(input("Enter the position of the list the element should be inserted: "))
    while pos not in range(len(a)):
        pos = int(input("Enter the position of the list the element should be inserted: "))        
    a.insert(pos,ele)
    return a
def list_pop(a):
    print("Your list: ", a)
    x = int(input("Enter the position of list to be removed: "))
    while x not in range(len(a)):
        x = int(input("Enter the position of list to be removed: "))            
    a.pop(x)
    return a
def list_remove(a):
    print("Your list: ", a)
    x = int(input("Enter the value of the list to be removed: "))
    while x not in a:
        x = int(input("Enter the value of the list to be removed: "))
    a.remove(x)
    return a
def list_sort(a):
    print("Your list: ", a)
    x = int(input("Enter 1 to sort the list in ascending order or 2 in descending order: "))
    list2 = [1,2]
    while x not in list2:
        x = int(input("Enter either 1 or 2 to sort the list: "))
    if x==1:
        a = sorted(a)
        return a
    else:
        a = sorted(a, reverse = True)
        return a
        
def list_reverse(a):
    print("Your list: ", a)
    list2 = a[::-1]
    return list2
def list_arith_ops(a):
    print("Your list: ", a)     
    sum1 = sum(a)
    min1 = min(a)
    max1 = max(a)
    x = []
    x.append(sum1)
    x.append(min1)
    x.append(max1)
    return x
def list_mean(a):
    print("Your list: ", a)
    mean = int(sum(a)/len(a))
    return mean
def list_find(a):
    print("Your list: ", a)
    ele = int(input("Enter the value to find in the list: "))
    while ele not in a:
        ele = int(input("The given value not found in the list. Enter the value exist in the list to find it's position: "))
    for i in range(len(a)):
        if ele==a[i]:
            return i
def list_length(a):
    print("Your list: ", a)
    
    x = len(a)
    return x

def list_median(a):
    print("Your list: ", a)
    median = stat.median(a)
    return median  


def list_ops(list1):
    print("Your list: ", list1)
    print("Operations available in the List data structure: ")
    print("Enter 0 to return to Data Structure Calculator:")
    print("1. Add\n2. Clear\n3. Copy\n4. Count or Frequency\n5. Extend\n6. Insert\n7. Pop\n8. Remove\n9. Sort\n10. Reverse\n11. Sum, Min, Max\n12. Mean\n13. Find\n14. Length\n15. Median\n")
    list_option = int(input("Enter your option: "))
    while list_option not in range(16):
        list_option = int(input("Enter correct number to do list operations: "))
    if list_option == 0:
        import Main_Program as main
        main.main()
    elif list_option == 1:
        res = list_add(list1)
        print("The final list after adding the elements: ", res)
        back_option(list1)
        
    elif list_option == 2:
        res = list_clear(list1)
        print("The final list after clearing the elements: ", res)
        back_option(list1)
    elif list_option == 3:
        res = list_copy(list1)
        print("The final list after copying the first list", res)
        back_option(list1)
    elif list_option == 4:
        res = list_count(list1)
        print("The count of the given element in the list: ", res)
        back_option(list1)
    elif list_option == 5:
        res = list_extend(list1)
        print("The extended list is: ", res)
        back_option(list1)

    elif list_option == 6:
        res = list_insert(list1)
        print("The list after inserting the element: ", res)
        back_option(list1)
    elif list_option == 7:
        res = list_pop(list1)
        print("The list after removing the element using index: ", res)
        back_option(list1)
    elif list_option == 8:
        res = list_remove(list1)
        print("The list after removing the element using value: ", res)
        back_option(list1)
    elif list_option == 9:
        list1 = list_sort(list1)
        print("The list after sorting: ", list1)
        back_option(list1)
    elif list_option == 10:
        list1 = list_reverse(list1)
        print("The list after reversing the elements: ", list1)
        back_option(list1)
    elif list_option == 11:
        res = list_arith_ops(list1)
        
        print("Sum of the list: ", res[0])
        print("Low number of the list: ",res[1])
        print("Highest number of the list: ", res[2])
        back_option(list1)
    elif list_option == 12:
        res = list_mean(list1)
        print("The mean of the list: ", res)
        back_option(list1)
    elif list_option == 13:
        res = list_find(list1)
        print("The position of the given element in the list: ", res)
        back_option(list1)
    elif list_option == 14:
        res = list_length(list1)
        print("The length of the list: ", res)
        back_option(list1)
    elif list_option == 15:
        res = list_median(list1)
        print("The median of the list: ", res)
        back_option(list1)
def operations():
    print("List Operations:\n")
    list1 = []
    num = int(input("Enter the number of elements in the list: "))
    while num == 0:
        num = int(input("Your input can not be zero: "))
    for i in range(num):
        temp = int(input("Enter the element number {}:".format(i+1)))
        list1.append(temp)
    return list_ops(list1)
        
        
        
        
        
            
        
        
            

        

    
    
