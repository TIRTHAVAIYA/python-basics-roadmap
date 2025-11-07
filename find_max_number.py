num1 = float(input("Enter the 1st number : "))
num2 = float(input("Enter the 2nd number : "))
num3 = float(input("Enter the 3rd number : "))

#method 1 using built-in max() function
maximum = max(num1 , num2 , num3)
print(f"maximun among entered number is : {maximum}")

#using conditional statements

if num1>=num2 and num2>=num3 :
    max_no = num1
elif num2>=num1 and num1>=num3 :
    max_no=num2
else:
    max_no=num3

print(f"Maximum among given 3 number (using if/else) {max_no}: ")