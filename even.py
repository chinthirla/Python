def even(start, n):
 for i in range(1,n):
    for j in range(start,10):
        if j % 2 == 0:
         return(j)
num1 = int(input("Enter number:"))
num2 = int(input("Enter end number:"))
print(even(num1, num2))
