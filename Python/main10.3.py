def compute_square_sums(matrix, N, M):
    # Шаг 1: Вычисление сумм для горизонтальных полос
    horizontal_sums = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        # Вычисляем сумму для первого прямоугольника в строке
        horizontal_sums[i][0] = sum(matrix[i][0:M])
        # Вычисляем суммы для остальных прямоугольников с использованием скользящего окна
        for j in range(1, N - M + 1):
            horizontal_sums[i][j] = horizontal_sums[i][j - 1] - matrix[i][j - 1] + matrix[i][j + M - 1]

    # Шаг 2: Вычисление сумм для квадратов M x M
    square_sums = [[0] * (N - M + 1) for _ in range(N - M + 1)]
    # Вычисляем сумму для первого квадрата
    for j in range(N - M + 1):
        square_sums[0][j] = sum(horizontal_sums[i][j] for i in range(M))
    # Вычисляем суммы для остальных квадратов с использованием скользящего окна
    for i in range(1, N - M + 1):
        for j in range(N - M + 1):
            square_sums[i][j] = square_sums[i - 1][j] - horizontal_sums[i - 1][j] + horizontal_sums[i + M - 1][j]

    return square_sums

# Пример использования
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
N = 4  # Размер матрицы
M = 2  # Размер квадрата

result = compute_square_sums(matrix, N, M)
for row in result:
    print(row)