class Account:    
    def __init__(self, owner, account_number, amount):
        self._owner = owner
        self._account_number = account_number
        self._balance = amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def __str__(self):
        return f"{self._owner}, {self._account_number}, balance: {self._balance}"