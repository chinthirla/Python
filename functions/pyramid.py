def display(x):
    for i in range(x,0,-1):
        for j in range(i):
            print('*',end='')
        print('\n')
num=int(input("Enter num:"))
num=num+1
display(num)

def display2(y):
    for i in range(y):
        for j in range(i):
            print(' ',end='')
        for k in range(i,y):
            print('*',end='')
        print('\n')

n=int(input("Enter num:"))
n=n+1
display2(n)
