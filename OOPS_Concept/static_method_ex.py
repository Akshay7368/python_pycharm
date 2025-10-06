class BankAccount:
    def _init_(self, owner, account_number, balance=0):
        self.owner = owner
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Getter for balance (read-only access)
    def get_balance(self):
        return self.__balance

    # Protected method to update balance (used in subclasses)
    def _update_balance(self, new_balance):
        self.__balance = new_balance

    # Get masked account number
    def get_account_number(self):
        return f"{str(self.__account_number)[-4:]}"


# 🔽 Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def _init_(self, owner, account_number, balance=0, interest_rate=0.02):
        super()._init_(owner, account_number, balance)  # Call parent constructor
        self.interest_rate = interest_rate  # Public attribute for simplicity

    # Method to apply interest to balance
    def apply_interest(self):
        balance = self.get_balance()
        interest = balance * self.interest_rate
        new_balance = balance + interest
        self._update_balance(new_balance)
        print(f"Interest of ${interest:.2f} applied. New balance: ${new_balance:.2f}")


# ✅ Using the SavingsAccount
account = SavingsAccount("Alice", 123456789, 1000, 0.05)

print(f"Owner: {account.owner}")
print(f"Account Number: {account.get_account_number()}")
print(f"Initial Balance: ${account.get_balance()}")

account.deposit(500)
account.withdraw(300)
account.apply_interest()  # Applying 5% interest