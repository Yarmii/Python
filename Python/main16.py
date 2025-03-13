# Дан файл, содержащий текст, включающий в себя русские и
# английские слова. Определить, каких букв в тексте больше: рус­
# # ских или латинских.

def count_letters(text):
    """
    Подсчитывает количество русских и латинских букв в тексте.
    Возвращает кортеж (количество русских букв, количество латинских букв).
    """
    russian_count = 0
    latin_count = 0

    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':  # Русские буквы
            russian_count += 1
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':  # Латинские буквы
            latin_count += 1

    return russian_count, latin_count

def main():
    # Чтение файла
    file_path = input("Введите путь к файлу: ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не найден.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return

    # Подсчет букв
    russian_count, latin_count = count_letters(text)

    # Вывод результата
    print(f"Количество русских букв: {russian_count}")
    print(f"Количество латинских букв: {latin_count}")

    if russian_count > latin_count:
        print("Русских букв больше.")
    elif latin_count > russian_count:
        print("Латинских букв больше.")
    else:
        print("Количество русских и латинских букв одинаково.")

# Запуск программы
if __name__ == "__main__":
    main()