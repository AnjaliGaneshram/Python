row_n = int(input("Enter the no of rows of the matrices: "))
col_n = int(input("Enter the no of columns of the matrices: "))
row_1 = int(input("Enter the no of rows of the second matrices: "))
col_1 = int(input("Enter the no of columns of the second matrices: "))


def matrices_input(x,y):
    list1 = []
    for i in range(x):
        list2 = []
        for j in range(y):
            
            a = int(input("Enter the matrices element {}{}: ".format(i+1,j+1)))
            list2.append(a)
        list1.append(list2)
    print(list1)
    return list1

mat_1 = matrices_input(row_n,col_n)
mat_2 = matrices_input(row_1,col_1)
mat_3 = []
for i in range(row_n):
    temp = []
    for j in range(col_n):
        b = mat_1[i][j] + mat_2[i][j]
        temp.append(b)
    mat_3.append(temp)

print(mat_3)
        






        

    
