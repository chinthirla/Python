subnames=[]
while True:
    print("Enter subnames"+str(len(subnames)+1)+"(or enter nothing to stop.):")
    name=input()
    if name=='':
        break
    subnames=subnames+[name]
print('The subject names are:')
for name in subnames:
    print(''+name)
