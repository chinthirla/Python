def display(var):
    for i in range(0,var,2):
        print(i)
var=int(input("Enter number to disaply even numbers:"))
display(var)
x=int(input("Enter value:"))
l=[]
for i in range(2,10000,2):
    l.append(i)
    if len(l)==x:
        break
print(l)
for j in l:
    print(j)
