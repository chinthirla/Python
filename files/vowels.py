a=open('/home/Python/files/testing.txt')
b=a.read()
#print(b)
v="aeiouAEIOU"
d={}.fromkeys(v,0)
for i in b:
    if i in d:
        d[i]=d[i]+1
print(d)
