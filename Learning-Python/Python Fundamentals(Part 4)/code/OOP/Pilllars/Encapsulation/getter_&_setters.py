class BankAccount:
    def __init__(self, name, balance, account_id):
        self.name = name #public
        self._balance = balance #protected
        self.__account_id = account_id #private attribute -- data mangling

    def get_account_id(self): #getter
        return(self.__account_id)

    def set_account_id(self, new_account_id):
        self.__account_id =  new_account_id


user1 = BankAccount("Kabirul", 100000, 2441139)


user1.set_account_id(2441137)
print(user1.name,",",user1._balance,",",user1.get_account_id()) 

# Still Private attributes can be print outside the Class through proper command so there really doesn't 
# exist an actual data hiding concept in Python

print(user1._BankAccount__account_id)