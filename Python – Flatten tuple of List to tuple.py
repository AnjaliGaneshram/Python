#Python – Flatten tuple of List to tuple
tup1 = ([5], [6], [3], [8])
'''
res = tuple(sum(tup1,[]))

print(res)
'''

tup2 = ()

for val in tup1:
    tup2 = tup2 + tuple(val)

print(tup2)
