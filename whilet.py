while True:
    print('Enter ypur age:')
    age=input()
    if age.isdecimal():
        break
    print("please enter a umber for your age.")
while True:
    print('select new password(letters and numbers only):')
    pwd=input()
    if pwd.isalnum():
        break
    print('password can only have numbers and letters')
