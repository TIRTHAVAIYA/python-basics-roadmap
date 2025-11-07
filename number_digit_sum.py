n = input("Enter a number : ")


def sum_digits(n):
    return sum(int(digit) for digit in str(n))

print("Sum of digit : " , sum_digits(n))