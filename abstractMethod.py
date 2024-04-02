# worldbank ---- save() loan()
# SBI       ---- save() loan()
# ICIC      ---- save() loan()


# complte abstraction ----> method defination 
#  incomplete abstaction --> class definition



from abc import ABC ,abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan(self,x):
        pass
    
    @abstractmethod
    def save(self,x):
        pass


    #  we can not create  object of abstract class but we can create objects of its child classes.
    # because the child class will have implementation for all the methods that are in the parent class
    # and hence it becomes a complete class .
    
class WorldBank(Bank):
        
    def __init__(self):
        super().__init__()
            
    def loan(self,loan_amount): 
        print("Loan amount is : ",loan_amount)
        return "World bank Loan"
        
    def save(self,amount):    
        print("Amount to be saved is :",amount)
        return "Saved through World Bank"

class SbiBank(Bank):
    def __init__(self):
        super().__init__()
        self._sbi = True

    @staticmethod
    def _check_eligibility():
        print("Checking eligibility")

    def loan(self,loan_amount):    
        self._check_eligibility()
        print("SBI Loan Amount: ",loan_amount)
        return "Loan taken from SBI"
    
    
    def save(self, x):
        return  "Not able to Save here, Please use World Bank"

# Creating Objects of different Banks
wb=WorldBank()
sb=SbiBank()

print("\n\nDetails of World Bank Account:\n")

print(wb.loan(1000))
print(wb.save(5000))

a=SbiBank
print("\n\nDetails of SBI Bank Account:\n")
print(a().loan(2000)) # Using Class variable to call the method
