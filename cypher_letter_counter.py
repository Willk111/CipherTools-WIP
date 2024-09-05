from collections import Counter

# Analyze the frequency of characters in the given text to check for common patterns
text = input("Please enter your cyper for counting: ")

# Count the frequency of each character in the text
char_frequency = Counter(text.lower())

# Return the most common characters
char_frequency.most_common()

for char, freq in char_frequency.items():
    print(f"{char}: {freq}")