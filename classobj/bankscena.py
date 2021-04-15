class bankaccount:
    def __init__(self,bal=10000):
        self.bal=bal
    def deposite(self,value):
        self.bal=self.bal+value
        print('This current balance is:',self.bal)
    def withdraw(self,value):
        self.bal=self.bal-value
        print('The current balance is:',self.bal)
class savingsaccount(bankaccount):
    def __init__(self,bal=10000):
        self.bal=bal
        def deposite(self,value):
            self.bal=self.bal+(value*1.03)
            print('The current balance is:',self.bal)
class currentaccount(bankaccount):
    def __init__(self,bal=10000):
        self.bal=bal
    def withdraw(self,value):
        if value>1000:
            print('You can withdraw less than 1000 only')
        else:
            self.bal=self.bal-value
            print("Your current account is:",self.bal)
SA=savingsaccount()
CA=currentaccount()
while True:
    print('1.Savings Account')
    print('2.Current Account')
    MOption=int(input("PLease select the account type:"))
    if MOption==1:
        print('1.Withdraw')
        print('2.Deposite')
        SOption=int(input('please select any operation type:'))
        if SOption==1:
            value=int(input('please enter amount to withdraw from savings account:'))
            SA.withdraw(value)
        elif SOption==2:
            value=int(input('Please enter amount to deposite in savings accoutn:'))
            SA.deposite(value)
        else:
            print('you entered',SOption,'its invalid operation')
    elif MOption==2:
        print('1.Withdraw')
        print('2.Deposute')
        SOption=int(input("Please selecr any operation type:"))
        if SOption==1:
            value=int(input('Please enter amount you want to withdraw from your current account:'))
            CA.withdraw(value)
        elif SOption==2:
            value=int(input('PLease enter aount you want to deposite into your current account:'))
            CA.deposite(value)
        else:
            print('you entered',SOption,'it is invalid operation')
    else:
         print('you entered',MOption,'it is invalid account type')
    break


