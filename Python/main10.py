# Практическое занятие №10. «Обработка двумерных массивов» Вариант 9 1
def swap_blocks(matrix, n):
    # Меняем блоки крест-накрест
    for i in range(n):
        for j in range(n):
            # Меняем верхний левый и нижний правый блоки
            matrix[i][j], matrix[i + n][j + n] = matrix[i + n][j + n], matrix[i][j]
            # Меняем верхний правый и нижний левый блоки
            matrix[i][j + n], matrix[i + n][j] = matrix[i + n][j], matrix[i][j + n]

# Пример использования
n = 2  
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

swap_blocks(matrix, n)
for row in matrix:
    print(row)