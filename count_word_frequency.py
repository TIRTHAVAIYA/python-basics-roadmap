import os
import string

def count_word_frequency(filename):
    word_freq = {}
    try:
        
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, filename)

        with open(file_path, 'r') as file:
            text = file.read().lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            words = text.split()

            for word in words:
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
            return word_freq
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

print(count_word_frequency('sample.txt'))
