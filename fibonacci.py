n = int(input("Enter a number which you want to print fibonacci series: "))

if n<=0:
    print("please enter positive integer")
   

print(f"Fibonacci series upto {n} : ")

a,b=0,1
count  = 0
while count<n:
    print(a)
    a,b=b,a+b
    count+=1
    

