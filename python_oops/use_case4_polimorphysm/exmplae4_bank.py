class SavingAccount:
    def __init__(self, balance) -> None:
        self.balance=balance
    def calculate_interest(self):
        print(self.balance*0.04)

class FixedDepositAccount:
    def __init__(self, balance) -> None:
        self.balance=balance
    def calculate_interest(self):
        print(self.balance*0.07)

saving=SavingAccount(10000)
fd=FixedDepositAccount(10000)
saving.calculate_interest()
fd.calculate_interest()

# def process_account(account, balance):
#     account.calculate_interest(balance)

# process_account(SavingAccount(),10000)


# if global parameter value is used then you can use varibale to allocate to object...
#     If you want to use different parameters then dont use varible of object use class name . function name