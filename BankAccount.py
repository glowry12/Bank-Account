class BankAccount:

    bank_name = "The Bank" # class attribute

    def __init__(self, customer_name, current_balance, minimum_balance, account_numer, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_numer = account_numer # protected
        self.__routing_number = routing_number # private

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
        else:
            print("Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self.current_balance:
            print("Insufficient balance.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Withdrawal will put account under the minimum.")
        else:
            self.current_balance -= amount

    def print_customer_information(self):
        print(f"\nBank name: {self.bank_name}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current balance: {self.current_balance:.2f} ")
        print(f"Minimum balance: {self.minimum_balance:.2f}\n")