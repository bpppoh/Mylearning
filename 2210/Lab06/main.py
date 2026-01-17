import text_utils

word = input("Raw text: ")
print(f"1. Cleaned: {text_utils.clean_text(word)}")
print(f"2. Word count: {text_utils.count_words(word)}")
print(f"3. Vowel count: {text_utils.count_vowels(word)}")
print(f"4. Highlighted: {text_utils.highlight(word)}")