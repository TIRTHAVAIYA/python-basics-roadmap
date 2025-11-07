#method 1 using arithmetic

a=10
b=15
print(f"before swap(arithmetic): a={a} , b={b}")
a=a+b  # a=15
b=a-b  # b=0
a=a-b  # a=15

print(f"after swap(arithmetic): a={a} , b={b}")

#method 2 using tuple

x=10
y=20

print(f"before swap(tuple): x={x} , y={y}")

x,y=y,x    #single line swap

print(f"after swap(tuple): x={x} , y={y}")
