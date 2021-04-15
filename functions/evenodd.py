def display(var):
    if var%2 == 0:
        print(var,"Is even number")
    else:
        print(var,"Is odd number")
num=input("Enter number:")
display(int(num))
