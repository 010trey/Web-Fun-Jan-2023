class BankAccount:
    def __init__(self, balance, int_rate=0.335): 
        self.int_rate = int_rate
        self.balance=balance
        
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount+5
        else:
            print("Insufficient funds")
    def display_account_info(self):
        print(f"Balance: {self.balance} - Interest_rate: {self.int_rate}")
    def yield_interest(self):
        self.balance +=self.balance*self.int_rate
        
acc = BankAccount(5000)
acc.display_account_info()
acc.deposit(1000)
acc.display_account_info()
acc.withdraw(3000)
acc.display_account_info()
acc.withdraw(3000)
