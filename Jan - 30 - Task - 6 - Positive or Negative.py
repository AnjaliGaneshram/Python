list1 = [-1, -7,8,10,20,21,17,28,-3,0,0,]
positive = []
negative = []
zero = []

for i in list1:
    if i == 0:
        zero.append(i)
    elif i < 0:
        negative.append(i)
    else:
        positive.append(i)
else:
    print("Positive Numbers: ",positive)
    print("Count of positive numbers: ", len(positive))
    print("Negative Numbers: ", negative)
    print("Count of negative numbers: ", len(negative))
    print("Zeroes: ", zero)
    print("Count of Zeroes: ", len(zero))
    
        
