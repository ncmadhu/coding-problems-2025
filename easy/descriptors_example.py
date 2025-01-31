class NonNegative:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        instance.__dict__[self.name] = value

class BankAccount:
    balance = NonNegative('balance')
    def __init__(self, init_balance =0):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

def demo():
    account = BankAccount(100)
    print(account.balance)  # Output: 100

    account.deposit(50)
    print(account.balance)  # Output: 150

    account.withdraw(30)
    print(account.balance)

    try:
        account.balance = -50
    except ValueError as e:
        print(e)

    try:
        account.withdraw(200)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    demo()

