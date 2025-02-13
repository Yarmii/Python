def find_elements(matrix, k):
    count = 0  # Счетчик элементов, кратных k
    max_element = None  # Наибольший элемент, кратный k

    for row in matrix:
        for element in row:
            if element % k == 0:  # Проверяем, кратен ли элемент k
                count += 1
                if max_element is None or element > max_element:
                    max_element = element

    return count, max_element

# Пример использования
matrix = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]
k = 5  # Число, на которое должны делиться элементы

count, max_element = find_elements(matrix, k)

print(f"Число элементов, кратных {k}: {count}")
print(f"Наибольший элемент, кратный {k}: {max_element}")