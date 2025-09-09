class Account:
    def __init__(self, owner, balance) -> None:
        self.ower=owner
        self.__balance= balance

    def get_balance(self):
        print(self.__balance)
    def __chkbalance__(self):
        print(self.__balance)


acc=Account('Mahesh',5000)
acc.get_balance()  #--> Works
# acc.__balance  # Use case of private variable
acc._Account__balance  #--> This works
acc.__chkbalance__()
# __balance is a private variable
# but we are using inside the class so it will works
# acc.__balnace  
# outside the class we are trying to access balance
# it is a private variable will give error