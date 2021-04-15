class A():
    a=100
    def methodA1(self):
        print("This is method 1 for class A")
    def methodA2(self):
        print("This is method 2 for class A")
class B(A):
    b=2000    
    def methodB1(self):
        print("This is method 1 for class B")
    def methodB2(self):
        print("This is method 2 for class B")
class C(A):
    c=3000
    def methodC1(self):
        print("This is method 1 for class C")
    def methodC2(self):
        print("This is method 2 for class C")
obj=C()
print(obj.a)
obj.methodA1()
obj.methodA2()
obj1=B()
print(obj1.b)
obj1.methodB1()
obj1.methodB2()
print(obj.c)
obj.methodC1()
obj.methodC2()
