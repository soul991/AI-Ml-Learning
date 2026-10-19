# Create a BankAccount class with attributes account_number, owner_name and balance.
# Add methods to deposit, withdraw and check balance

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def money_deposit(self, deposit_amount):
        if(deposit_amount<=0):
            print("Invalid Ammount to deposit!")
        else:
            self.balance+=deposit_amount
            print("Deposited sucessfully!")
            print(f"Your Current Balance is {self.balance}INR")
            print("Thank You!")

    def money_withdraw(self, withdraw_amount):
        if(withdraw_amount<=0):
            print("Invalid Ammount to withdraw!")
        elif(withdraw_amount>self.balance):
                print("Insufficient Balance!")
        else:
            self.balance-=withdraw_amount
            print("Withdrawn sucessfully!")
            print(f"Your Current Balance is {self.balance}INR")
            print("Thank You!")

    def check_balance(self):
        print(f"Your current balance is {self.balance}INR")
        print("Thank You!")


user1 = BankAccount("R2216", "Rahul", 69_000)
user2 = BankAccount("P3628", "Mohul", 59_000)
user3 = BankAccount("D6733", "Meghnad", 79_000)




a = input("Enter your Bank Account Number: ")

print("Which operation you want to perform:\n" \
"1. To Deposit money enter 1\n" \
"2. To Withdraw money enter 2\n" \
"3. To Check Balance enter 3")
b = int(input("Enter your choice: "))

if(a==user1.account_number):
    if(b==1):
        x = int(input("Enter the ammount you want to deposit: "))
        user1.money_deposit(x)
    elif(b==2):
        y = int(input("Enter the ammount you want to withdraw: "))
        user1.money_withdraw(y)
    elif(b==3):
        user1.check_balance()
    else:
        print("Please enter a valid option!")

elif(a==user2.account_number):
    if(b==1):
        x = int(input("Enter the ammount you want to deposit: "))
        user2.money_deposit(x)
    elif(b==2):
        y = int(input("Enter the ammount you want to withdraw: "))
        user2.money_withdraw(y)
    elif(b==3):
        user2.check_balance()
    else:
        print("Please enter a valid option!")

elif(a==user3.account_number):
    if(b==1):
        x = int(input("Enter the ammount you want to deposit: "))
        user3.money_deposit(x)
    elif(b==2):
        y = int(input("Enter the ammount you want to withdraw: "))
        user3.money_withdraw(y)
    elif(b==3):
        user3.check_balance()
    else:
        print("Please enter a valid option!")

else:
    print("Invalid Bank Acoount Number!")