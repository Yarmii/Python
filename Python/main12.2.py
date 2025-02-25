# Вариант 16 2 
text = "Это пример текста на русском языке. Согласные буквы нужно найти."
consonants = set("бвгджзйклмнпрстфхцчшщ")
consonant_count = {letter: 0 for letter in consonants}
words = text.lower().split()

for word in words:
   
    unique_consonants_in_word = set(word) & consonants
    for consonant in unique_consonants_in_word:
        consonant_count[consonant] += 1
result = sorted([letter for letter, count in consonant_count.items() if count == 1])
print("Согласные буквы, входящие только в одно слово:")
print(result)