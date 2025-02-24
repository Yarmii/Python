#Практическое занятие №2. «Составление программ линейной структуры»Вариант 9

import math
def formula_y(t, m, k):
    # Вычисление y согласно формуле
    y = ((1 + t)**(2 * k) - abs(3 * m))**t + (t + k + 5 * m) / (t * k * m + 1)
    return y
# Ввод значений t, m и k
t = float(input("Введите значение t: "))
m = float(input("Введите значение m: "))
k = float(input("Введите значение k: "))
# Вычисление и вывод результата
result = formula_y(t, m, k)
print(f"Результат y: {result}")