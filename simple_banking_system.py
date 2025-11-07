class BankingAccount:
    def __init__(self, acc_holder , initial_bal=0):
        self.holder = acc_holder
        self.__balance = initial_bal
        print(f"Account created for {self.holder} with initial balance : {self.__balance:.2f}")


    def get_balance(self):
        return f"{self.holder}'s current balance: {self.__balance:.2f}"


    def deposit(self , amount):
        if amount>0:
            self.__balance += amount
            return f"Deposit of {amount:.2f} successful. \n New balance : {self.__balance:.2f}"
        else:
            return "Deposit amount must be positive"
        
    def withdraw(self , amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"Withdrawal of {amount:.2f} successful . \n New balance : {self.__balance:.2f}"
            else:
                return "Withdrawal Failed : Insufficient funds."
        else:
            return "Withdrawal amount must be positive" 


account = BankingAccount("Tirth Avaiya" , 61000)        

print("\n --- TRANSACTIONS ---")
print(account.deposit(5550.265))
print(account.withdraw(500))
print(account.get_balance())
print(account.withdraw(1000000))


       