def display(var):
    var=str(var)
    var=''.join(reversed(var))
    var=int(var)
    print("given number is",num,',after reversing the number is',var)
num=int(input("Enter num:"))
display(num)
