'''Task1:

Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]


5
56
222
50000
put
5555
7777
666
89
on
333
3333
'''
Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]

print(Li1[3])
print(Li1[4][1])
print(Li1[4][4][1])
print(Li1[4][4][3][2][1])
print(Li1[4][4][3][2][3][3:6])
print(Li1[4][4][3][0])
print(Li1[4][4][3][4])
print(Li1[4][4][6])
print(Li1[4][-3])
string = str((Li1[4][4][3][2][2]))
print(string[4:])
print(Li1[4][4][2])
print(Li1[4][4][3][1])