class A():
    a=100
    def methoda1(self):
        print("This is method1 for class A")
    def methoda2(self):
        print("This is method2 for class A")
class B(A):
    b=200
    def methodb1(self):
        print("This is methodb1 for class B")
    def methodb2(self):
        print("This is methodb2 for class B")
objb=B()
objb.methodb1()
print(objb.b)
objb.methodb2()
print(objb.a)
objb.methoda1()
objb.methoda2()
