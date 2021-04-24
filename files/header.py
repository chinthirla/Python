a=open('/home/Python/files/testing.txt','r')
v=a.readlines()
for i in v:
    x=i.split(',')
    print(x[0],'\n------------------')
    for j in range(1,len(x)):
        print(x[j])
