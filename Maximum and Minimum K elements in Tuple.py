#Maximum and Minimum K elements in Tuple

tup1 = (3,6,5,1,9)

num = 2

s_temp = set(tup1)
l_temp = list(sorted(s_temp))
tup2 = l_temp[:num]
tup3 = l_temp[-num:]

res = tup2 + tup3
print(tuple(res))
