# Exercise 1
class BankAccount:
    """Bank Account protected by pin number."""

    def __init__(self):
        """Initial account balance is 0 and pin is 'pin'"""
        self.pin = 'pin'
        self._balance = 0

    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance"""
        if self.pin == pin:
            self._balance = self._balance + amount
            return self._balance
        else:
            print('Pin Is Wrong')

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount"""
        if self.pin == pin:
            self._balance = self._balance - amount
            return self._balance
        else:
            print("pin is wrong")

    def get_balance(self, pin):
        """Return account balance"""
        if self.pin == pin:
            return self._balance
        else:
            "Pin is not correct"

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin"""
        if self.pin == oldpin:
            self.pin = newpin
            print('The old pin is = ' + oldpin)
            print('New PIN is= ' + self.pin)
        else:
            print("Pin is Wrong")


# Exercise 3
class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self._interestRate = 0.06

    def interest(self):
        self._balance = self._balance + (self._balance * self._interestRate)
        return self._balance


# Exercise 4
class FeeSavingsAccount(SavingsAccount):

    def __init__(self):
        super().__init__()
        self.fee = 1

    def withdraw(self, pin, amount):
        if self.pin == pin:
            self._balance = self._balance - (amount + self.fee)
            return self._balance
        else:
            return "Wrong Pin"


my_bank = BankAccount()
savings_account = SavingsAccount()
fee_account = FeeSavingsAccount()

print(savings_account.interest())
print(my_bank.deposit(pin='pin', amount=12))
print(my_bank.withdraw('pin', 2))
print(fee_account.deposit(pin='pin', amount=12))
print(fee_account.withdraw('pin', 2))
print(my_bank.change_pin('pin', 'test'))
