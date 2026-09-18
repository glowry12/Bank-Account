from BankAccount import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_numer, routing_number, transfer_limit=500):
        super().__init__(customer_name, current_balance, minimum_balance, account_numer, routing_number)
        self._transfer_limit = transfer_limit
        self.__max_transfers = 3
        self.__transfers_made = 0

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > self._transfer_limit:
            print(f"Transfer amount exceeds the transfer limit of {self._transfer_limit:.2f}.")
        elif self.__transfers_made >= self.__max_transfers:
            print("Transfer limit reached for this account.")
        elif amount > self.current_balance:
            print("Insufficient balance.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer will put account under the minimum.")
        else:
            self.current_balance -= amount
            recipient_account.deposit(amount)
            self.__transfers_made += 1
