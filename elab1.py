a=[1,2,3]
b=[3,2,1]
c=a+b
a+=b
print(id(a))
print(id(c))
print(a)
print(c)
g=[3,2,1]
print(id(sorted(g)))
print(g)
print(id(g.sort()))
print(g)
