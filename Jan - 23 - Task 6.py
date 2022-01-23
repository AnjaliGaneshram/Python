'''
Task6:

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}


#py
#ello
#en
#zoo
#Bot



print(a)
'''

a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}


b = a[1][3]
print(b[:2])
c = a[2][10]
print(c[1:])
d = a[2][40]
print(d[3:5])
e = a[40][1]
print(e[:3])
f = a[40][2]
print(f[:3])

        
