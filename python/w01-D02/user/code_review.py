# !<-----------   BankAccount
class BankAccount:
    all_accounts = []

    # !<------------------Constructor----------------->
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    # ! deposit method

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount is: {amount}$")
        return self

    # ! Withdraw Method
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging 5$")
            # print(f"Balance : {self.balance}$ ")
        else:
            self.balance -= amount
            print(f"We will di withdrawing {amount} for account")

    # ! display_account_info method

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # ! yield_interest method
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # !Ninja Bonus
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}\n, Interest rate: {account.int_rate}")


# !------------------ User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
        self.savingaccount = BankAccount(0.01, 750)

    def make_deposit(self, amount, acc="main"):
        if acc == "main":
            self.account.deposit(amount)
        elif acc == "saving":
            self.savingaccount.deposit(amount)
        return self

    def make_withdrawal(self, amount, acc="main"):
        if acc == "main":
            self.account.withdraw(amount)
        elif acc == "saving":
            self.savingaccount.withdraw(amount)
        return self

    def display_user_balance(self, acc="main"):
        if acc == "main":
            print(self.account.balance)
        elif acc == "saving":
            print(self.savingaccount.balance)
        return self


user1 = User("Mouadh", "mouadhjenouiz@gmail.com")

user1.make_deposit(1000).make_withdrawal(150).display_user_balance()
user1.make_deposit(500, "saving").make_withdrawal(300, "saving").display_user_balance(
    "saving"
)
