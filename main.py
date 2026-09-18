from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# first test instance for SavingsAccount subclass
savings_test1 = SavingsAccount("Alexa", 700, 100, "07654", "1234567", 0.042)
savings_test1.deposit(2000)
savings_test1.add_interest()
print(f"Interest rate: {savings_test1.get_interest_rate()}%")
savings_test1.withdraw(55)
savings_test1.print_customer_information()

# second test instance for Savings Account subclass
savings_test2 = SavingsAccount("David", 400, 50, "9876545", "1234567", 0.032)
savings_test2.withdraw(500)
savings_test2.deposit(205)
savings_test2.add_interest()
print(f"Interest rate: {savings_test2.get_interest_rate()}%")
savings_test2.print_customer_information()

checking1 = CheckingAccount("Alexa", 1000, 100, "1000200030", "071000013")
checking2 = CheckingAccount("Bob", 2500, 200, "1000200031", "071000014")
checking3 = CheckingAccount("Chris", 500, 50, "1000200032", "071000015")

checking1.withdraw(200)
checking1.print_customer_information()

checking2.transfer(300, checking3)
checking2.print_customer_information()
checking3.print_customer_information()

checking3.transfer(1000, checking1)
checking3.print_customer_information()
