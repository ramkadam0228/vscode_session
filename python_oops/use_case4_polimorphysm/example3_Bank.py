class SavingAccount:
    def calculate_interest(self, balance):
        print(balance*0.04)

class FixedDepositAccount:
    def calculate_interest(self, balance):
        print(balance*0.07)

# saving=SavingAccount()
# fd=FixedDepositAccount()
# saving.calculate_interest(10000)
# fd.calculate_intreest(10000)

def process_account(account, balance):
    account.calculate_interest(balance)

process_account(SavingAccount(),10000)


# if global parameter value is used then you can use varibale to allocate to object...
#     If you want to use different parameters then dont use varible of object use class name . function name