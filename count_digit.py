n = int(input("Enter a number : "))

if n==0:
    count = 1
else:
    n = abs(n)
    count=0
    while n>0:
        n//=10
        count+=1

print(f"Number of Digit in input number : {count}")