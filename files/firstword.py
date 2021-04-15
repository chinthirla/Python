a=open('/home/Python/files/testing.txt','r')
v=a.readlines()
for i in v:
    k=i.split()
    print(k[0])
for i in open('/home/Python/files/testing.txt','r').readlines():
    print(i.split()[1])
b=open('/home/Python/files/testing.txt','r')
z=b.readlines()
x=v[0]
y=x.split()
print("Second word is:",y[2])
print(open('/home/Python/files/testing.txt','r').readlines()[-1].split()[-1])
j=open('/home/Python/files/testing.txt','r')
l=j.readlines()
for i in l:
    print(i[-2])

