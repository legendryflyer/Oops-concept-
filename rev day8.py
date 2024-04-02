class bank:
    country = "INDIA"
    count=0
    def __init__(self,fn,ln,acc,bal):
        self.firstName=fn
        self.lastName=ln
        self.accNo=acc
        self.balance=bal
        self.transitions=[]
        bank.count+=1
    
    def  deposit(self,amount):
        if amount>0:
            self.balance+=amount
            self.transitions.append(("Deposited",amount))
        else:
            print("Amount should be greater than zero")
            
    def withdrawal(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.transitions.append(("Withdrawn",amount))
        else:
            print("Insufficient Balance")
    
    def lastFiveTransetions(self):
        print(self.transitions[-5:])
        
    def display_account(self):
        print(f"\nAccount Holder Name : {self.firstName} {self.lastName}")
        print(f"Account Number      : {self.accNo}")
        print(f"Current Balance         : {self.balance}\n")
        for t in self.transitions:
            print(f"{t[0]:10}{' ':{5}}: {t[1]}")
    
    
    @classmethod
    def countNumberOfObjects(cls):
        print(cls.count)       
            
tavish = bank("tavish","anade",1234567,10000)   
ankit = bank("ankit","bhisikar",1234567,10000)   

tavish.deposit(5000)
tavish.withdrawal(2000)
tavish.deposit(534500)
tavish.withdrawal(3000)
tavish.deposit(500)
tavish.withdrawal(200000)
tavish.display_account()
tavish.lastFiveTransetions()
bank.countNumberOfObjects()

