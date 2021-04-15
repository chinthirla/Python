def mul_key(a,**x):
    print("The formal arg is:",a)
    for i in x:
        print("Another keyworded arg is: %s:%s"%(i,x[i]))
mul_key(a=10,b=20,c='Pyhton',d='Lower')
def mul_k(a,**x):
    print("The formal arg is:",a)
    for i in x:
        print("Another keywarded sarg is:%s: %s"%(i,x[i]))
dict={"arg1":1,"arg2":2,"arg3":"Sai"}
print("keys is:",dict.keys())
mul_k(a=10,**dict)
