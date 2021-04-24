class myclass():
    pass
    def __init__(mysilly,name,age):
        mysilly.name=name
        mysilly.age=int(age)
    def myfunc(abc):
        print("My name is:"+abc.name)
#        print("My age is:"+bc.age)

myobj=myclass("vijay",28)
myobj.myfunc()
myobj.age=30
print(myobj.age)
