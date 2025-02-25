# 14 Имеется упорядоченный файл. Вставить в него заданное
# число таким образом, чтобы упорядоченность сохранилась.
# Функция для вставки числа в упорядоченный список
def insert_into_sorted_list(sorted_list, number):
    # Находим позицию для вставки
    for i in range(len(sorted_list)):
        if sorted_list[i] > number:
            sorted_list.insert(i, number)
            return
    # Если число больше всех элементов, добавляем в конец
    sorted_list.append(number)

# Открываем файл для чтения
with open('sorted_numbers.txt', 'r', encoding='utf-8') as file:
    # Читаем числа из файла и преобразуем их в список целых чисел
    numbers = [int(line.strip()) for line in file]

# Запрашиваем у пользователя число для вставки
new_number = int(input("Введите число для вставки: "))

# Вставляем число в список
insert_into_sorted_list(numbers, new_number)

# Открываем файл для записи
with open('sorted_numbers.txt', 'w', encoding='utf-8') as file:
    # Записываем обновленный список чисел в файл
    for number in numbers:
        file.write(f"{number}\n")

print(f"Число {new_number} успешно вставлено в файл.")