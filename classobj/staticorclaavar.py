class myclass():
    i="Python"
    j="Developer"
    def __init__(self):
        print(myclass.i)
        print(myclass.j)
x1=myclass()
print(x1.i)
print(x1.j)
x1.__init__()
