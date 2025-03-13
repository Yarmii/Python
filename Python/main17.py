def get_array(prompt, expected_length):
    while True:
        try:
            arr = list(map(int, input(prompt).split()))
            if len(arr) != expected_length:
                raise ValueError(f"Ожидалось {expected_length} элементов, а было введено {len(arr)}.")
            return arr
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте еще раз.")

# Ввод массивов G и H с валидацией
G = get_array("Введите 9 элементов массива G через пробел: ", 9)
H = get_array("Введите 7 элементов массива H через пробел: ", 7)

# Функция для удаления и возвращения элемента по индексу
def remove_and_return(arr, index):
    return arr.pop(index)

# Удаление седьмого элемента из массива G (индекс 6)
removed_element = remove_and_return(G, 6)
print(f"Удаленный элемент из G: {removed_element}")

# Добавление числа 22 в конец массива H
H.append(22)

# Вставка числа 55 на пятое место в массиве H (индекс 4)
H.insert(4, 55)

# Создание нового массива GH1 путем объединения G и H
GH1 = G + H

# Сортировка массива GH1 по возрастанию
GH1.sort()

# Определение позиции числа 55 в массиве GH1
position_55 = GH1.index(55)
print(f"Позиция числа 55 в массиве GH1: {position_55}")

# Формирование массива GH2 из элементов, расположенных на местах с номерами, имеющими остаток от деления на 3, равный 1
GH2 = [GH1[i] for i in range(len(GH1)) if i % 3 == 1]

# Сдвиг элементов массива GH2 на 2 влево
GH2 = GH2[2:] + GH2[:2]

# Вывод результатов
print("Массив G после удаления седьмого элемента:", G)
print("Массив H после добавления 22 и вставки 55:", H)
print("Массив GH1 после объединения и сортировки:", GH1)
print("Массив GH2 после формирования и сдвига:", GH2)