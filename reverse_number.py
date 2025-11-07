n = int(input("Enter a number which you want to reverse: "))

original_number = n
reversed_number = 0

sign = -1 if n<0 else 1
n= abs(n)

while n>0:
    digit = n%10
    reversed_number = reversed_number*10+digit
    n //=10
final_result = reversed_number * sign
print(f"Reverse of {original_number} is {final_result}")