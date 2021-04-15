while True:
    name=input("Enter Name:")
    if name != 'Narayana':
        continue
    print("Hello", name,",please enter your password..")
    pwd=input("Enter password:")
    if pwd == 'Durgasoft':
        print("you entered correct details")
        print("Congratulations",name)
        break
print("Thank You",name)
