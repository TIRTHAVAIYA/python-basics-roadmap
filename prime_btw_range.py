
import math

lower_bound = int(input("Enter lower bound : "))
upper_bound = int(input("Enter upper bound : "))

def is_prime(n):
    if n<=1:
        return False
    #check for factors up to sqrt(n)

    for i in range(2 , int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        return True
    
def print_primes():
    primes = [n for n in range(lower_bound , upper_bound) 
              if is_prime(n)]
    print(primes)    


print(f"Primes between {lower_bound} to {upper_bound} : ")   
print_primes() 