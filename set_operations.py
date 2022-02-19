import statistics as stat

def set_input():
    set2 = set()
    num = int(input("Enter the number of elements for your second set: "))
    while num == 0:
        num = int(input("Number of elements for your second set can't be zero: "))
    for i in range(num):
        temp = int(input("Enter your element number {}: ".format(i+1)))
        set2.add(temp)
    return set2

def back_option(a):
    bc = int(input("Enter number 1 to return to set operations: "))
    while bc!=1:
        bc = int(input("Enter number 1 to return to set operations: "))
    return set_ops(a)

def set_add(a):
    print("Your set: ", a)
    temp = int(input("Enter the number to be added to the set: "))
    a.add(temp)    
    return a
def set_clear(a):
    print("Your set: ", a)
    print("Your set before clearing: ", a)
    return a.clear()
def set_copy(a):
    print("Your set: ", a)
    set2 = ()
    print("The empty set before copying: ", set2)
    set2 = a.copy()
    return set2
def set_difference(a):
    print("Your set: ", a)
    set2 = set_input()
    set3 = a.difference(set2)
    return set3
def set_discard(a):
    print("Your set: ", a)
    b = int(input("Enter the element to be removed in the set: "))
    while b not in a:
        b = int(input("Enter the element already exists in the set: "))
    a.discard(b)
    return a
def set_intersection(a):
    print("Your set: ", a)
    set2 = set_input()
    set3 = a.intersection(set2)
    return set3
def set_disjoint(a):
    print("Your set: ", a)
    set2 = set_input()
    x = a.isdisjoint(set2)
    return x
def set_subset(a):
    print("Your set: ", a)
    set2 = set_input()
    x = a.issubset(set2)
    return x
def set_superset(a):
    print("Your set: ", a)
    set2 = set_input()
    x = a.issuperset(set2)
    return x
def set_symmetric(a):
    print("Your set: ", a)
    set2 = set_input()
    set3 = a.symmetric_difference(set2)
    return set3
def set_union(a):
    print("Your set: ", a)
    set2 = set_input()
    set3 = a.union(set2)
    return set3
def set_update(a):
    print("Your set: ", a)
    set2 = set_input()
    a.update(set2)
    return a
def set_sum(a):
    print("Your set: ", a)
    set2 = sum(a)
    return set2
def set_mean(a):
    print("Your set: ", a)
    set2 = int(sum(a)/len(a))
    return set2
def set_median(a):
    print("Your set: ", a)
    set2 = stat.median(a)
    return set2
    
    
    
    
    
    
    
        


def operations():
    print("SET OPERATONS:")
    set1 = set()
    num = int(input("Enter the number of elements to be present in the set: "))
    while num==0:
        num = int(input("Number of elements can't be zero: "))
    for i in range(num):
        temp = int(input("Enter your element number {}:".format(i+1)))
        set1.add(temp)
    return set_ops(set1)
def set_ops(set1):
    print("Your set: ", set1)
    print("Operations available in the Set Data Structure: ")
    print("Enter 0 to return to Data Structure Calculator: ")
    print("1. Add\n2. Clear\n3. Copy\n4. Difference\n5. Discard or Remove\n6. Intersection\n7. Check if Disjoint\n8. Check if subset\n9. Check if superset\n10. Symmetric differenct\n11. Union\n12. Update\n13. Sum\n14. Mean\n15. Median")
    set_option = int(input("Enter your option: "))
    while set_option not in range(16):
        set_option = int(input("Enter your option: "))
    if set_option == 0:
        import Main_Program as main
        main.main()
    if set_option == 1:
        res = set_add(set1)
        print("The final set after adding the element: ", res)
        back_option(set1)
    if set_option == 2:
        res = set_clear(set1)
        print("The set after using clear function: ", res)
        back_option(set1)
    if set_option ==3:
        res = set_copy(set1)
        print("The final set after copying: ", res)
        back_option(set1)
    if set_option == 4:
        res = set_difference(set1)
        print("The difference of both the sets: ", res)
        back_option(set1)
    if set_option == 5:
        res = set_discard(set1)
        print("The final set after discarding the element: ", res)
        back_option(set1)
    if set_option ==6:
        res = set_intersection(set1)
        if res!=set():
            print("The final set contains similar elements in both sets: ", res)
        else:
            print("Both sets have no similar elements.")
            
        back_option(set1)
    if set_option == 7:
        res = set_disjoint(set1)
        if res == True:
            print("There are no elements common in both sets hence both sets are disjoint sets.")
        else:
            print("Both sets are not disjoint")
        back_option(set1)
    if set_option == 8:
        res = set_subset(set1)
        if res == True:
            print("The elements in first set are present in second set. Set1 is subset of Set2")
        else:
            print("Not all elements in first set are present in the second set.")
        back_option(set1)
    if set_option == 9:
        res = set_superset(set1)
        if res == True:
            print("The first set contains all elements of the second set. Set1 is superset of Set2")
        else:
            print("Set1 is not superset of Set2. Not all elements in second set is present in first set")
        back_option(set1)
    if set_option == 10:
        res = set_symmetric(set1)
        print("The final set after excluding the common elements of both sets: ", res)
        back_option(set1)
    if set_option ==11:
        res = set_union(set1)
        print("Union of the two sets : ", res)
        back_option(set1)
    if set_option == 12:
        res = set_update(set1)
        print("The first set after updating the second set element: ", res)
        back_option(set1)
    if set_option == 13:
        res = set_sum(set1)
        print("The sum of the given set: ", res)
        back_option(set1)
    if set_option == 14:
        res = set_mean(set1)
        print("The mean of the given set: ", res)
        back_option(set1)
    if set_option == 15:
        res = set_median(set1)
        print("The median of the given set: ", res)
        back_option(set1)
    
    
        
        
    
    
    
        
