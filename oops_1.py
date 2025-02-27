# Modeling a Bank Account

## Define a class for bank account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

    def get_balance(self):
        return self.balance

## create an account

account = BankAccount("Krish", 5000)
print(account.balance)


## Call instance method
account.deposit(100)

account.withdraw(300)

print(account.get_balance())