class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.__accountNumber = acc_no
        self.__accountHolder = holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            self.__balance = value
        else:
            self.__balance = "no neg"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("no neg deposits.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            self.__balance = "Insufficient funds"

    def display(self):
        print("Account number:", self.__accountNumber, "Account holder name:", self.__accountHolder)
        print("Balance:", self.__balance)


ac = BankAccount("12345", "Alice", 1000)
ac.display()

ac.deposit(500)
ac.withdraw(200)
print("Balance:",ac.balance)
ac.balance = 1500

