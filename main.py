from BankAccount import BankAccount
from SavingsAccount import SavingsAccount

# first test instance for SavingsAccount subclass
savings_test1 = SavingsAccount("Alexa", 700, 100, "07654", "1234567", 0.042)
savings_test1.deposit(2000)
savings_test1.add_interest()
savings_test1.get_interest_rate()
savings_test1.withdraw(55)
savings_test1.print_customer_information()

# second test instance for Savings Account subclass
savings_test2 = SavingsAccount("David", 400, 50, "9876545", "1234567", 0.032)
savings_test2.withdraw(500)
savings_test2.deposit(205)
savings_test2.add_interest()
savings_test2.get_interest_rate()
savings_test2.print_customer_information()