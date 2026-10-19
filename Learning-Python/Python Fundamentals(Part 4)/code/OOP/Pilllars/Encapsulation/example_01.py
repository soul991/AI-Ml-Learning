class BankAccount:
    def __init__(self, name, balance, account_id):
        self.name = name #public
        self._balance = balance #protected
        self.__account_id = account_id #private attribute -- data mangling


user1 = BankAccount("Kabirul", 100000, 2441139)

print(user1.name, user1._balance , user1.__account_id)