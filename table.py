n = int(input("Enter a number , which you want multiplication table : "))

print(f"Multiplication table of {n} : ")

for i in range(1,11):
    result = n*i
    print(f"{n} x {i} = {result}")