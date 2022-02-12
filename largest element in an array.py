arr= (2,3,4,1,9)

temp = arr[0]

for i in arr:
    if temp < i:
        temp = i
    else:
        continue
else:
    print(temp)
