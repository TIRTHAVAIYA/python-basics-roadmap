str = input("Enter a string : ")

frequency = {}

for char in str:
    frequency[char] = frequency.get(char , 0)+1  ## .get ->gets thr current count or 0 if the char is not in the dict yet!!   

print(f"string : '{str}")
print(f"Frequency: {frequency}")    