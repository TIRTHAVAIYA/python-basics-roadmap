str = input("Enter a string : ")

seen = set()
result = ""

for char in str:
    if char not in seen:
        result += char
        seen.add(char)

print(f"Original : '{str}")
print(f"Without Duplicates : '{result}")
