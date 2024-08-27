from collections import Counter
import string
def count_word_letter(given):
    given = given.lower()
    translator = str.maketrans('', '', string.punctuation)
    sentence = given.translate(translator)
    letter_count = Counter(sentence.replace(' ', ''))
    word_count = Counter(given.split())
    return letter_count, word_count


given = """"TCS is the largest IT service company in India, 
headquartered in Mumbai, and also the largest employee base."""
letter_count, word_count = count_word_letter(given)

print("Letter counts:")
for letter, count in letter_count.items():
    print(f"'{letter}': {count}")

print("\n")

print("Word counts:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
