import string

sentence = input("Enter a sentence : ").lower()

# replace punctuation with a space , then split
for char in string.punctuation:
    sentence = sentence.replace(char , "")

words = sentence.split()
word_frequency = {}

# list of word count
for word in words:
    word_frequency[word] = word_frequency.get(word,0)+1

print(f"\n Word Frequencies: \n{word_frequency}")    