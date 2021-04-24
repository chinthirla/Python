def sum_of_args(*x):
    sum=0
    for i in range(0,len(x)):
        sum=sum+x[i]
    return sum

print(sum_of_args(2,20,30))
