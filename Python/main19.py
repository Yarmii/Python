class StringCleaner:
    def __init__(self, input_string):
        self.input_string = input_string

    def remove_extra_spaces(self):
        # Разделяем строку на слова и возвращаем очищенную строку
        words = self.input_string.split()
        cleaned_string = ' '.join(words)
        return cleaned_string

def main():
    input_string = input("Введите строку: ")  # Запрашиваем ввод у пользователя
    cleaner = StringCleaner(input_string)      # Создаем экземпляр класса
    result = cleaner.remove_extra_spaces()      # Удаляем лишние пробелы
    print(f"Результат: '{result}'")             # Выводим результат

if __name__ == "__main__":
    main()  # Запускаем программу