# Bundeling data and method that work on that data into one unit (usually a class) while restricting direct access to some of the data.


class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = Bankaccount(1000)

account.deposit(500)
print(account.get_balance()) 
