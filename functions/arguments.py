def multi_args(a,*x):
    print("Formal arg is:",a)
    for i in x:
        print("The no_keywarded arg is:",i)
    return
multi_args(10,20,'Vijay','kumar')
def varlen(*y):
    print("The output is")
    for i in y:
        print(y)
    print("Length of arg is:",len(y))
    return;
print("Calling with single value")
varlen(55)
print("Calling with multiple values")
varlen(50,'Django',60,'Narayana',70,'Python',80)
