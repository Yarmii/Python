# 9 Дан файл, содержащий текст на русском языке. Определить,
# сколько раз встречается в нем самое короткое слово.

# Открываем файл для чтения
with open('text1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Разделяем текст на слова (учитываем знаки препинания)
words = text.split()

# Находим длину самого короткого слова
min_length = min(len(word) for word in words)

# Находим все слова с минимальной длиной
shortest_words = [word for word in words if len(word) == min_length]

# Выбираем первое самое короткое слово (если их несколько)
shortest_word = shortest_words[0]

# Подсчитываем количество вхождений самого короткого слова
count = words.count(shortest_word)

# Выводим результат
print(f"Самое короткое слово: '{shortest_word}'")
print(f"Оно встречается {count} раз(а).")