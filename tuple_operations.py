def back_option(a):
    bc = int(input("Enter numer 1 to return to tuple operations: "))
    while bc!=1:
        bc = int(input("Enter numer 1 to return to tuple operations: "))
        
    return tup_ops(a)

def tup_add(a):
    list1 = list(a)
    print("Your tuple: ", a)
    b = int(input("Enter the element to be added: "))
    list1.append(b)
    a = tuple(list1)
    return a
def tup_remove(a):
    list1 = list(a)
    print("Your tuple: ", a)
    b = int(input("Enter the element to be removed: "))
    while b not in a:
        if len(a) == 0:
            print("Tuple is empty. Please add elements in the tuple to perform this operation.")
            tup_ops(a)
        else:
            b = int(input("Enter the element exist in the tuple: "))
    for i in list1:
        if b==i:
            list1.remove(i)
    a = tuple(list1)
    return a
def tup_count(a):
    
    print("Your tuple: ", a)
    x = int(input("Enter the value to be counted in the tuple: "))
    while x not in a:
        if len(a) == 0:
            print("Tuple is empty. Please add elements in the tuple to perform this operation.")
            tup_ops(a)
        else:
            x = int(input("Enter the element exist in the tuple: "))
    b = a.count(x)
    return b
def tup_sum(a):
    list1 = []
    print("Your tuple: ", a)
    sum1 = sum(a)
    min1 = min(a)
    max1 = max(a)
    list1.append(sum1)
    list1.append(min1)
    list1.append(max1)
    return list1

def tup_mean(a):
    print("Your tuple: ",a)
    mean = int(sum(a)/len(a))
    return mean  
    

def tup_ops(tup1):
    print("Your tuple: ", tup1)
    print("List of operations available in Tuple Data Structure: ")
    print("Enter 0 to return to Data Structure Calculator: ")    
    print("1. Add\n2. Remove\n3. Count\n4. Sum, Min, Max\n5. Mean")
    tup_option = int(input("Enter your option: "))
    while tup_option not in range(6):
        tup_option = int(input("Enter your option: "))
    if tup_option == 0:
        import Main_Program as main
        main.main()
    elif tup_option ==1:
        res = tup_add(tup1)
        print("The final tuple: ", res)
        back_option(res)
    elif tup_option == 2:
        res = tup_remove(tup1)
        print("The tuple after the val removed: ",res)
        back_option(res)
    elif tup_option == 3:
        res = tup_count(tup1)
        print("The count of the given element in the tuple: ", res)
        back_option(tup1)
    elif tup_option == 4:
        res = tup_sum(tup1)
        print("The sum of the tuple: ", res[0])
        print("The lowest number in the tuple: ", res[1])
        print("The highest number in the tuple: ", res[2])
        back_option(tup1)
    elif tup_option == 5:
        res = tup_mean(tup1)
        print("The mean of the tuple: ", res)
        back_option(tup1)
def operations():
    print("Tuple Operations: \n")
    num = int(input("Enter the number of elements in the tuple: "))
    list1 = []
    while num == 0:
        num = int(input("Number of elements can't be zero: "))
    for i in range(num):
        temp = int(input("Enter the element number {}: ".format(i+1)))
        list1.append(temp)
    tup1 = tuple(list1)
    return tup_ops(tup1)
        
    
