a=open('/home/Python/files/testing.txt','r')
v=list(a.read())
print(v[-2])
print(len(v))
b=open('/home/Python/files/testing.txt','r')
f=b.readlines()
c=0
for i in f:
    x=i.split()
    for j in x:
        c=c+len(j)
print(c)
