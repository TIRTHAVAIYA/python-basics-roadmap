n = int(input("Enter a number which you want to find factorial: "))

if n<0:
    print("factorial is not defined for negative numbers")
if n == 0:
    print(1)

result =1
for i in range(1,n+1):
    result *=i
    
print(f"Factorial of {n} is : {result}")
