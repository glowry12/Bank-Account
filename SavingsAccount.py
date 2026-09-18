from BankAccount import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate * 100

    def add_interest (self):
        interest = self.interest_rate * self.current_balance
        self.current_balance += interest
