def display(z,a):
    print("Before swapping::","X=",z,"Y=",a)
    temp=0
    temp=z
    z=a
    a=temp
    print("After swapping::","X=",z,"Y=",a)
x=input("Enter X:")
y=input("Enter Y:")
display(x,y)
