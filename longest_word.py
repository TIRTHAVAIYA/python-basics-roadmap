sentence = input("Enter a sentence : ")

words = sentence.split()

longest_word = max(words , key=len)
print(f"Sentence : '{sentence}")
print(f"Longest Word : '{longest_word}")
