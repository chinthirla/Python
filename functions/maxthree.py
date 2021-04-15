def max(x,y,z):
    if x>y and x>z:
        print(x,"is Greater value")
    elif y>x and y>z:
        print(y,"Is Greater value")
    elif x==y==z:
        print("All three values are equal")
    else:
        print(z,"is greater value")
var1=int(input("Enter var1:"))
var2=int(input("Enter var2:"))
var3=int(input("Enter var3:"))
max(var1,var2,var3)
