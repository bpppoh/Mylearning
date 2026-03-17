class BankAccount :
    _balance = 0
    
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self._balance = balance
        
    def deposit(self,amount) :
        if amount > 0 :
            self._balance += amount 
            print(f"ฝาก {amount} บัญชี {self.account_number} ยอด {self._balance}")
        else :
            print("จํานวนเงินต้องมากกว่า 0")
            
    def withdraw(self,amount) :
        if amount > 0 :
            self._balance -= amount
            print(f"ถอน {amount} บัญชี {self.account_number} ยอด {self._balance}")
        else :
            print("ยอดเงินไม่พอหรือจํานวนเงินไม่ถูกต้อง")
    
    def get_balance(self) :
        return self._balance 
    
class SavingsAccount(BankAccount) :
    interest_rate = 0.015
    
    def __init__(self,account_number,balance=0) :
        super().__init__(account_number,balance)
    
    def add_interest(self) :
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"เพิ่มดอกเบี้ย {interest:.2f} บัญชี {self.account_number}")
        
account = SavingsAccount("123-456-789\n")

print("Try Deposit 10,000.-")
account.deposit(10000)
print(f"Balance account : {account.get_balance()}\n")

print("Try calculate interest...")
account.add_interest()
print(f"Balance account : {account.get_balance()}\n")

print("Try withdraw...")
account.withdraw(2000)
print(f"Balance account : {account.get_balance()}\n")