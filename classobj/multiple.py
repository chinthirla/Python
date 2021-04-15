class A():
    a=100
    def mA1(self):
        print("This is method 1 for class A")
    def mA2(self):
        print("This is method 2 for class A")
class B():
    b=200
    def mB1(self):
        print("This is method 1 for class B")
    def mB2(self):
        print("This is method 2 for class B")
class C():
    c=300
    def mC1(self):
        print("This is method 1 for class C")
    def mC2(self):
        print("This is method 2 for class C")
class D(A,B,C):
    d=400
    def mD1(self):
        print("This is method 1 for class D")
    def mD2(self):
        print("This is method 2 for class D")
obj=D()
print(obj.d)
obj.mD1()
obj.mD2()
print(obj.c)
obj.mC1()
obj.mC2()
print(obj.b)
obj.mB1()
obj.mB2()
print(obj.a)
obj.mA1()
obj.mA2()


