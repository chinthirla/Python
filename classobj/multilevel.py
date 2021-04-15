class A:
    a=20
    def methodA1(self):
        print("This is method 1 for class A")
    def methodA2(self):
        print("This is method 2 for class A")
class B(A):
    b=300
    def methodB1(self):
        print("This is method 1 for class B")
    def methodB2(self):
        print("This is method 2 for class B")
class C(B):
    c=400
    def methodC1(self):
        print("This is method 1 for class C")
    def methodC2(self):
        print("This is method 2 for class C")
class D(C):
    d=9000
    def methodD1(self):
        print("This is method 1 for class D")
    def methodD2(self):
        print("This is method 2 for class D")
obj=D()
print(obj.a)
obj.methodA1()
obj.methodA2()
print(obj.b)
obj.methodB1()
obj.methodB1()
print(obj.c)
obj.methodC1()
obj.methodC1()
print(obj.d)
obj.methodD1()
obj.methodD1()


