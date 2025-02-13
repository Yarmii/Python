# Практическое занятие №11. «Работа со строками» Вариант 4 2
def transform_text(text):
    lowercase_count = 0  # Счетчик строчных букв
    uppercase_count = 0  # Счетчик прописных букв

    # Подсчет строчных и прописных букв
    for char in text:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1

    # Преобразование текста
    if uppercase_count > lowercase_count:
        # Заменяем все строчные буквы на прописные
        transformed_text = text.upper()
    elif lowercase_count > uppercase_count:
        # Заменяем все прописные буквы на строчные
        transformed_text = text.lower()
    else:
        # Оставляем текст без изменений
        transformed_text = text

    return transformed_text

# Пример использования
text = "Hello World! This is a Test."
result = transform_text(text)
print(result)