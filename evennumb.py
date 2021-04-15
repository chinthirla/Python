target=int(input("Enter target number:"))
var=1
while var<target:
    if var % 2 != 0:
        var+=1
        continue
    print('This number='+str(var))
    var+=1
print("Displayed all even number before",var)

