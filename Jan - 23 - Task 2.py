'''Task2


a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

Extract
#science
#computer
'''
a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]

b = a[4][3]

print(b.split("_"))
c = b.split("_")
print(c)
e = c[0].lower()

print(c[1], e)



