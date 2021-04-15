spam=0
if spam<=5:
    print("Hello ,World.")
    spam = spam + 1

while spam<5:
    print("Hi Vijay")
    spam = spam + 1
num=1
while num<5:
    print("The count is:",num)
    num += 1
print("Thank You")
var=int(input("Enter start num:"))
var2=int(input("Enter end num:"))
while var<=var2:
    print("Sqare of number",var,"is:",var**2)
    var += 1
num=int(input("Enter number for sum:"))
sum = 0
i = 1
while i<=num:
    sum = sum + i
    i +=1 
print("The sum is:", sum)
v = 1
target = int(input("Enter number for even:"))
while v<target:
    if v%2 != 0:
        v += 1
        continue
    print("This number is:",v)
    v += 1
print("Displayed all even number befoe",v)
