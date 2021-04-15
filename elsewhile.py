cnt=0
while cnt<3:
    print("Now we are inside while loop")
    cnt += 1
else:
    print("Now we are in else  block")
i = 0
numbers=[]
while i<6:
    print("At the top i is %d"%i)
    numbers.append(i)
    i=i+1
    print("Numbers now:",numbers)
    print("At the bottom i is %d"%i)
print("The numbers:")
for num in numbers:
    print(num)
