# 9 Записать в файл / последовательного доступа N натуральных
# чисел. Получить в другом файле последовательного доступа все числа файла /, кроме чисел, кратных К. Вывести полученный файл
# на печать.

# Функция для чтения чисел из файла и записи чисел, не кратных K, в другой файл
def filter_numbers_not_divisible_by_K(input_filename, output_filename, K):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            number = int(line.strip())  # Читаем число из файла
            if number % K != 0:  # Проверяем, не кратно ли оно K
                output_file.write(f"{number}\n")  # Записываем в новый файл

# Функция для вывода содержимого файла на печать
def print_file_contents(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Основная программа
if __name__ == "__main__":
    input_filename = "number.txt"  # Имя входного файла
    output_filename = "filtered_numbers.txt"  # Имя выходного файла
    K = int(input("Введите число K: "))  # Вводим K

    # Фильтруем числа, не кратные K, и записываем в другой файл
    filter_numbers_not_divisible_by_K(input_filename, output_filename, K)

    # Выводим полученный файл на печать
    print(f"Содержимое файла с числами, не кратными {K}:")
    print_file_contents(output_filename)
    