def display(var):
    if var % 5 == 0:
        print(var,"Is divisible by 5")
    else:
        print(var,"Is not divisible by 5")
num=int(input("Enter number:"))
display(num)
