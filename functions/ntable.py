def display(n):
   # i=0
   # while i<=n:
    #    i+=1
    #    print('%d'%n,'*','%d'%i,'=',n*i)
    #  i=i+1
    for i in range(1,11):
        print(n,'*',i,'=',i*n)
var=int(input("Enter number which table you want :"))
display(var)
