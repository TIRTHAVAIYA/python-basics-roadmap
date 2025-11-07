import math
n = int(input("Enter a nummber to check prime or not : "))

def is_prime(n):
    if n<=1:
        return False
    #check for factors up to sqrt(n)

    for i in range(2 , int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        return True
    

print(f"Is {n} prime? =>" , is_prime(n))
