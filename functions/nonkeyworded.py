def multi_arg(a,*x):
    print("Formal arg is:",a)
    for i in x:
        print("The non_keywarded arg is:",i)
    return
def multi_arg2(a,x,c,v,b):
    print("Formal arg is:",a)
    print("nonkeywarded arg is:",x)
    print("nonkeywarded arg is:",c)
    print("nonkeywarded arg is:",v)
    print("nonkeywarded arg is:",b)
tup1=(100,'py','sai')
tup2=(30,'vijay','kumar','li')
multi_arg(10,*tup1)
multi_arg2(10,*tup2)
