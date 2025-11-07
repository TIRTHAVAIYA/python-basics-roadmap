str = input("Enter a string : ")

def is_palindrome(s):
    cleaned_str = "".join(char for char in s.lower() if char.isalnum())
    return cleaned_str == cleaned_str[::-1]


print(f"Is '{str}' Palindrome? => {is_palindrome(str)}" )
