### ENCAPULATION - PRIVATE VARIABLES....

class Account:
    def __init__(self, initial_bal):
        self.__balance = initial_bal  ## "__" means strongly-private variable
        self.__owner = "User"

    def get_balance(self):
        return self.__balance
    
    def deposit(self , amount):
        if amount >0:
            self.__balance += amount
            print(f"Deposited {amount} . New balance : {self.__balance}")

        else:
            print("Deposit amount must be positive.")


acc = Account(2000)

print(f"Accessing 'prottected' variable directly (Discouraged) : {acc._Account__owner}")

try:
    print(f"Direct access to __balance: {acc.__balance}")
except AttributeError as e:
    print({e})


acc.deposit(5132)
print(f"Current Balance via Getter method : {acc.get_balance()}")


        